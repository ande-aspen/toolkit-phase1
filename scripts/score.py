#!/usr/bin/env python3
"""
score.py — Cálculo determinista y validación de scoring ANDE Fase 1.

Uso:
    python3 scripts/score.py "output/[ciudad]_[pais] - indicators.csv" [más CSVs...]

Lee el CSV de 30 indicadores y calcula, sin errores aritméticos:
  - Score por dominio (promedio de indicadores con score; N/D se excluye, no cuenta como 0)
  - Score global (promedio simple de los 7 dominios)
  - Score ajustado por cuello de botella (media geométrica de los 7 dominios)
  - Rango de incertidumbre (global excluyendo indicadores estimados + % estimado)
  - Nivel de madurez propuesto por score (la validación estructural es del analista)
  - Cuello de botella y patrón Condición-Resultado (aproximación por dominios del toolkit)
  - Semáforos por dominio

Y valida:
  - Que estén los 30 indicadores esperados
  - Que los scores sean numéricos y estén en 0-100
  - La convención de IDs H2/H3 (los CSVs pre-julio 2026 usan la convención antigua)

No modifica archivos. El score oficial del reporte debe coincidir con esta salida.
"""

import csv
import math
import re
import sys
import unicodedata

DOMAIN_ORDER = ["P", "F", "C", "S", "H", "M", "I"]
DOMAIN_NAMES = {
    "P": "Política y Regulación",
    "F": "Financiamiento",
    "C": "Cultura",
    "S": "Servicios de Apoyo",
    "H": "Capital Humano",
    "M": "Mercados",
    "I": "I+D e Innovación",
}
EXPECTED_IDS = (
    [f"P{i}" for i in range(1, 4)] + [f"F{i}" for i in range(1, 7)]
    + [f"C{i}" for i in range(1, 6)] + [f"S{i}" for i in range(1, 6)]
    + [f"H{i}" for i in range(1, 6)] + [f"M{i}" for i in range(1, 4)]
    + [f"I{i}" for i in range(1, 4)]
)
CONDITION_DOMAINS = ["P", "S", "H", "I"]
OUTCOME_DOMAINS = ["F", "C", "M"]

MATURITY = [(25, "Naciente"), (45, "Emergente"), (65, "En Desarrollo"), (100, "Autosostenible")]


def strip_accents(s):
    return "".join(c for c in unicodedata.normalize("NFD", s) if unicodedata.category(c) != "Mn")


def maturity_level(score):
    for cap, name in MATURITY:
        if score <= cap:
            return name
    return "Autosostenible"


def semaforo(score, is_lowest):
    if score >= 60:
        return "🟢 Bien desarrollado"
    if score >= 40:
        return "🟡 En desarrollo"
    return "🔴 Cuello de botella" if is_lowest else "🔴 Atención prioritaria"


def is_estimated(row):
    blob = " ".join([row.get("value", ""), row.get("score", ""), row.get("notes", "")]).lower()
    return "(est" in blob or "est.)" in blob


def parse_score(raw):
    if raw is None:
        return None
    m = re.search(r"\d+(?:\.\d+)?", raw.replace(",", ""))
    return float(m.group()) if m else None


def analyze(path):
    warnings = []
    rows = {}
    with open(path, newline="", encoding="utf-8-sig") as f:
        reader = csv.DictReader(f)
        cols = [c.strip() for c in (reader.fieldnames or [])]
        for needed in ("indicator_id", "score"):
            if needed not in cols:
                warnings.append(f"Columna faltante: '{needed}' (encontradas: {cols})")
        for r in reader:
            iid = (r.get("indicator_id") or "").strip().upper()
            if re.fullmatch(r"[PFCSHMI]\d", iid):
                if iid in rows:
                    warnings.append(f"{iid}: fila duplicada, se usa la primera")
                    continue
                rows[iid] = {k: (v or "").strip() for k, v in r.items() if k}

    missing = [i for i in EXPECTED_IDS if i not in rows]
    extra = [i for i in rows if i not in EXPECTED_IDS]
    if missing:
        warnings.append(f"Indicadores faltantes ({len(missing)}): {', '.join(missing)}")
    if extra:
        warnings.append(f"IDs inesperados: {', '.join(extra)}")

    # Convención H2/H3 (oficial desde jul 2026: H2 = bootcamps, H3 = STEM)
    h2_name = strip_accents(rows.get("H2", {}).get("indicator_name", "").lower())
    if "stem" in h2_name or "graduad" in h2_name or "graduate" in h2_name:
        warnings.append(
            "H2/H3 en convención ANTIGUA (H2=STEM): CSV pre-julio 2026. "
            "Mapear por indicator_name, no por ID, al comparar con CSVs nuevos."
        )

    scores, estimated = {}, set()
    for iid, r in rows.items():
        s = parse_score(r.get("score", ""))
        if s is None:
            warnings.append(f"{iid}: sin score numérico (valor: '{r.get('score','')}') — excluido del promedio")
            continue
        if not (0 <= s <= 100):
            warnings.append(f"{iid}: score {s} fuera de rango 0-100 — excluido")
            continue
        scores[iid] = s
        if is_estimated(r):
            estimated.add(iid)

    def domain_avgs(score_map):
        out = {}
        for d in DOMAIN_ORDER:
            vals = [v for i, v in score_map.items() if i.startswith(d)]
            if vals:
                out[d] = sum(vals) / len(vals)
        return out

    domains = domain_avgs(scores)
    if len(domains) < 7:
        warnings.append(f"Solo {len(domains)}/7 dominios con datos — el global usa los disponibles")

    dvals = list(domains.values())
    global_arith = sum(dvals) / len(dvals) if dvals else float("nan")
    global_geom = math.exp(sum(math.log(max(v, 1)) for v in dvals) / len(dvals)) if dvals else float("nan")

    no_est = {i: v for i, v in scores.items() if i not in estimated}
    dom_no_est = domain_avgs(no_est)
    global_no_est = (sum(dom_no_est.values()) / len(dom_no_est)) if dom_no_est else float("nan")
    pct_est = 100 * len(estimated) / len(scores) if scores else 0

    bottleneck = min(domains, key=domains.get) if domains else None
    ordered = sorted(domains.items(), key=lambda kv: kv[1])
    second_gap = (ordered[1][1] - ordered[0][1]) if len(ordered) > 1 else None

    cond = [domains[d] for d in CONDITION_DOMAINS if d in domains]
    outc = [domains[d] for d in OUTCOME_DOMAINS if d in domains]
    cond_avg = sum(cond) / len(cond) if cond else float("nan")
    outc_avg = sum(outc) / len(outc) if outc else float("nan")
    if cond_avg >= 50 and outc_avg >= 50:
        cr = "Ecosistema efectivo"
    elif cond_avg >= 50:
        cr = "Problema de conexión"
    elif outc_avg >= 50:
        cr = "Sistema frágil"
    else:
        cr = "Ecosistema incipiente"

    print(f"\n{'='*72}\n{path}\n{'='*72}")
    print(f"{'Dominio':28} {'Score':>6}  Semáforo")
    for d in DOMAIN_ORDER:
        if d in domains:
            print(f"{DOMAIN_NAMES[d]:28} {domains[d]:6.1f}  {semaforo(domains[d], d == bottleneck)}")
    print(f"\nScore global (aritmético):   {global_arith:.1f}  → redondeado {round(global_arith)}")
    print(f"Ajustado cuello de botella:  {global_geom:.1f}  (media geométrica)")
    gap = global_arith - global_geom
    if gap > 8:
        print(f"  ⚠ Brecha {gap:.1f} pts: los dominios fuertes enmascaran la severidad del cuello de botella")
    print(f"Sin estimados:               {global_no_est:.1f}  ({len(estimated)}/{len(scores)} indicadores estimados = {pct_est:.0f}%)")
    if pct_est > 30:
        print("  ⚠ >30% estimado: score sensible a research adicional (precedente La Paz v1→v2: +21 pts)")
    print(f"Madurez propuesta por score: {maturity_level(round(global_arith))}"
          f"  (validar contra los 4 marcadores estructurales — references/workflows/diagnostico.md)")
    if bottleneck:
        bn = f"Cuello de botella:           {DOMAIN_NAMES[bottleneck]} ({domains[bottleneck]:.1f})"
        if second_gap is not None and second_gap < 5:
            bn += f" — {DOMAIN_NAMES[ordered[1][0]]} ({ordered[1][1]:.1f}) también crítico (dif. {second_gap:.1f})"
        print(bn)
    print(f"Patrón C-R:                  {cr}  (Condición {cond_avg:.1f} / Resultado {outc_avg:.1f})"
          f"  [aproximación por dominios — ver methodology-alignment.md]")
    if warnings:
        print("\nADVERTENCIAS:")
        for w in warnings:
            print(f"  ⚠ {w}")
    else:
        print("\nSin advertencias — CSV válido.")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)
    for p in sys.argv[1:]:
        analyze(p)
