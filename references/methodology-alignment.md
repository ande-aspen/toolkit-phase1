# Methodology Alignment — Toolkit V3.7 (Second Edition, January 2026)

This file records how the operational documents in this repo align with the canonical methodology, `drive/METODOLOGIA_EN.md` (converted from the final draft "ENG FInal draft - Toolkit_V3.7"). Read it when scoring, when comparing new outputs against pre-July-2026 outputs, or when a document seems to contradict the methodology.

---

## 1. Indicator ID convention (aligned 2026-07-06)

The official Annex B.1 defines **H2 = Tech bootcamps and training programs** and **H3 = Annual STEM graduates**. Earlier versions of this repo had them swapped. All templates, rubrics, guides and country files now follow the official convention.

**Historical caveat:** every `output/*indicators.csv` generated **before July 2026** (all 13 diagnosed cities: the 10 Mexican cities, Villahermosa, Colombo, Nairobi) uses the old convention — in those files H2 = STEM graduates and H3 = bootcamps. When reading historical CSVs, map by `indicator_name`, never by ID alone. New diagnostics must use the official convention.

## 2. Deliberate deviations from the official methodology

These are conscious operational choices of this toolkit. They are kept because they improve rigor or comparability across our diagnostics; each report's methodology note should not claim to follow the official text on these points without qualification.

| # | Topic | Official methodology (V3.7) | This toolkit | Rationale |
|---|-------|------------------------------|--------------|-----------|
| 1 | Scoring scale | Relative internal profile for a single ecosystem; Stam & Van de Ven average-deviation method (mean = 1) for multi-ecosystem comparisons | Absolute 0-100 rubric with LATAM-calibrated bands (`rubrica-scoring.md`) | Comparable scores across cities and over time; enables maturity thresholds |
| 2 | Population adjustment | Suggested per 100,000 inhabitants for count indicators | Per 1,000,000 inhabitants, applied only to cities <1M (S1-S4, C1-C2, M1-M2, I1-I2) | Bands were calibrated on per-million densities |
| 3 | Maturity classification | Structural characteristics + Cukier & Kon generations (no numeric thresholds) | Numeric thresholds on global score (0-25 Nascent, 26-45 Emerging, 46-65 Developing, 66-100 Self-Sustaining), justified narratively with generations | Reproducibility; the report's maturity paragraph must still validate against structural criteria (Gen 2+ evidence) |
| 4 | Condition-Outcome pattern | Indicator-level: only F1, F2, F5, M1 are outcome indicators (Annex B); all Culture indicators are conditions | Domain-level approximation: Condition = avg(P, S, H, I), Outcome = avg(F, C, M) | Simplicity; flag in the report that it is a domain-level approximation of the official condition-outcome distinction |
| 5 | Activity ("vigencia") windows | Annex B.1: meetups ≥1 event in 6 months; online communities active in last 30 days; accelerators with open calls in last 12 months | Stricter windows (`references/workflows/diagnostico.md`, Criterios de Vigencia): meetups ≥1 event/3 months and ≥3/year; accelerators ≥1 cohort in 24 months; funds/angels ≥1 documented deal in 24 months | Web-verifiable evidence standards; reduces overcounting of zombie actors |

## 3. Terminology by language (per V3.7)

| Concept | Spanish reports | English reports |
|---------|-----------------|-----------------|
| Growth-stage companies | PEC (Pequeñas Empresas en Crecimiento) | SGBs (Small and Growing Businesses) |
| Support organizations | Organizaciones de Apoyo | ESOs (Entrepreneurial Support Organizations) |
| Ecosystem connectors | Articuladores | Connectors |
| Maturity levels | Naciente / Emergente / En Desarrollo / Autosostenible | Nascent / Emerging / Developing / Self-Sustaining |
| Interventions (Table 4.3) | Construir / Fortalecer / Escalar / Mantener / Esperar | Build / Strengthen / Scale / Maintain / Wait |

## 4. Citing the methodology

- Official suggested citation: **ANDE. (2025). *Entrepreneurship Ecosystem Diagnosis Model* (2nd ed.). Aspen Network of Development Entrepreneurs.** (Edition published January 2026.)
- Table 4.3 (interventions by domain and maturity) kept its number in V3.7 and is safe to cite. Tables 4.8-4.12 of earlier drafts were renumbered to 4.9-4.13 in V3.7 — do not cite chapter-4 table numbers above 4.3 from memory; verify in `drive/METODOLOGIA_EN.md`.
- Chapter 5 now includes a dedicated role section "Corporations and Large Enterprises" (Table 5.6); "Entrepreneurs and SGBs" is Table 5.7.
