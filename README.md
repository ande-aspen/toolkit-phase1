# Ecosystem Expert Agent

Agente experto en ecosistemas emprendedores para Claude Code. Construido sobre la metodología ANDE (Entrepreneurial Ecosystem Diagnostic Toolkit, 2ª ed.) y una base de conocimiento creciente.

No hay skills ni comandos: se pide la tarea en lenguaje natural y el agente sigue el workflow correspondiente de `references/workflows/`.

## Tareas

| Tarea | Ejemplo de petición |
|-------|---------------------|
| Diagnóstico ANDE Fase 1 | "Diagnostica Hermosillo, Sonora, México, 950,000 habitantes" |
| Research de ecosistema | "Investiga el ecosistema de Mérida" |
| Re-diagnóstico (v2) | "Actualiza el diagnóstico de La Paz" |
| Ingesta a la base de conocimiento | "Agrega este paper a la base" (+ PDF/URL) |
| Consulta a la base de conocimiento | "¿Qué dice la literatura sobre efectividad de aceleradoras en LatAm?" |
| Reporte personalizado | "Hazme un policy brief sobre financiamiento en ciudades intermedias" |
| Comparativo | "Compara los ecosistemas del norte de México" |
| Consolidado multi-ciudad | "Consolida los 10 diagnósticos de México en un reporte" |

## Quick Start

**Diagnosticar un ecosistema:**
```
"Investiga y diagnostica Hermosillo, Sonora, México, 950,000 habitantes"
→ research en input/ → CSV + reporte de 8 secciones + radar en output/
```

**Verificar el scoring de un CSV:**
```
python3 scripts/score.py "output/[ciudad]_[pais] - indicators.csv"
```

## Estructura

```
ande-toolkit/
├── CLAUDE.md              ← Cerebro del agente: identidad, flujos de trabajo, recursos
├── references/            ← Recursos del diagnóstico
│   ├── workflows/         ← Proceso detallado de cada tarea (1 archivo por tarea)
│   ├── rubrica-scoring.md ← Benchmarks para los 30 indicadores
│   ├── reporte-template.md← Las 8 secciones del reporte
│   └── countries/         ← Indicadores nacionales por país
├── knowledge/             ← Base de conocimiento creciente (papers, índice)
├── drive/                 ← Metodología ANDE (METODOLOGIA_EN.md = canónica, V3.7)
├── guides/                ← Humanización (ES/EN) y calibración África
├── docs/                  ← Guías de scoring y template CSV
├── scripts/               ← score.py: cálculo determinista y validación de CSVs
├── input/                 ← Documentos de research por ciudad
└── output/                ← Entregables generados
```
