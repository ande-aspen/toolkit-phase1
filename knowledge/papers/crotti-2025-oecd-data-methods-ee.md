# Data and Methods for Entrepreneurial Ecosystem Diagnostics

## Metadata
- **Autor(es):** Roberto Crotti, Jonathan Potter, Pablo Shah, Erik Stam
- **Año:** 2025
- **Publisher:** OECD SME and Entrepreneurship Papers
- **Tipo:** academic
- **Idioma:** en
- **URL:** https://doi.org/10.1787/5173f4a2-en
- **Fecha de ingesta:** 2026-02-12

## Clasificación
- **Dominios ANDE:** P, S, H, I, F, C, M
- **Temas:** Measurement & Diagnostics, Ecosystem Frameworks & Theory
- **Regiones:** Global (OECD, 38 economies)
- **Tags:** #indicators, #normalization, #geometric-mean, #bottleneck, #composite-index, #missing-data, #OECD-benchmark

## Resumen
Methodological companion to the OECD Entrepreneurial Ecosystem Diagnostics Report (pilot edition, 38 OECD economies). Defines 29 indicators across 10 ecosystem elements with specific data sources, tests internal consistency (Cronbach's alpha), establishes a clipped min-max normalization method, and uses geometric mean aggregation to penalize bottlenecks. Provides country-level benchmark scores including Mexico and LatAm countries.

## Insights Clave

### INS-1: 29 indicators across 10 elements with reliability assessment
> The framework uses 29 indicators grouped into 10 elements: Institutions (4), Culture (3), Networks (2), Infrastructure (3), Markets (2), Finance (4), Knowledge (3), Talent (4), Leadership (1), Intermediate Services (3). Internal consistency varies widely: Knowledge (alpha=0.82) and Talent (0.81) are high; Finance (0.28) and Networks (0.18) are limited due to data heterogeneity. Perceived entrepreneurial capabilities is negatively correlated with all other talent indicators.

**Ubicación:** Section 2B (full indicator list)
**Relevancia:** Direct benchmark for ANDE's 30 indicators. The reliability scores reveal which elements have coherent indicator sets vs. which combine fundamentally different constructs. The negative correlation of perceived capabilities with education metrics is a caution for interpreting self-reported entrepreneurial confidence.

### INS-2: Clipped min-max normalization method
> Scores normalized using clipped min-max: min = mean - 2*stdev, max = mean + 2*stdev, anchored to 2020-2023 values. Values below min get 0, above max get 100. This method outperforms z-scores (weak to outliers, hard to communicate) and winsorized min-max (forces at least one country to 0 and one to 100). Inverted indicators use reversed formula.

**Ubicación:** Section 2C
**Relevancia:** Provides a validated normalization approach for cross-country ecosystem comparison. The 2-standard-deviation clipping reduces outlier distortion while maintaining distribution properties.

### INS-3: Geometric mean aggregation penalizes bottlenecks
> Indicators within each element are aggregated using geometric mean, which does not allow full compensability — a very low score on one indicator cannot be fully offset by high scores on others. This aligns with the ecosystem concept that an incomplete ecosystem hinders entrepreneurship even if other conditions are strong. The 10 elements are NOT combined into a single index; the authors argue a single score would be "an overly simplified depiction."

**Ubicación:** Section 2D
**Relevancia:** Validates the ANDE bottleneck identification approach. The mathematical rationale for geometric mean (vs. arithmetic mean) provides theoretical backing for prioritizing the weakest domain in ecosystem diagnostics.

### INS-4: Mexico scores near bottom of OECD on most elements
> Mexico benchmark scores (2020-2023): Institutions 4.6 (one of lowest OECD), Culture 28.3, Infrastructure 5.3 (near bottom), Markets 25.1. Colombia and Costa Rica similarly low. Chile somewhat better but severe weaknesses in Infrastructure (17.3) and Knowledge (18.1). Finance data unavailable for all four LatAm countries. For LatAm broadly: bank credit access "significantly more difficult than in other OECD countries."

**Ubicación:** Section 2F (country scores table)
**Relevancia:** Essential benchmarks for scoring Mexican and LatAm ecosystems against OECD peers. The near-zero scores on Institutions and Infrastructure for Mexico quantify the structural gap that local ecosystems operate within.

### INS-5: Output indicators — elements predict productive entrepreneurship better than general firm creation
> Eight output indicators tracked separately (not aggregated): birth rate of employer enterprises, medium/high-growth enterprises, equity-based young firms per million population, unicorns per million, enterprise churn, survival rates, job-creation expectations. All element scores positively correlated with equity-based young firms per capita, but correlations with general employer enterprise birth rates are weaker. Knowledge element most strongly correlated with enterprise birth rates.

**Ubicación:** Section 2G
**Relevancia:** Confirms that ecosystem conditions predict quality of entrepreneurship (productive, equity-backed) more than quantity. When evaluating ecosystem health, equity-based startup creation is a better signal than total business formation.

### INS-6: Cross-element correlations reveal development clusters
> About 40% of pairwise element correlations exceed 60%. Infrastructure-Knowledge and Institutions-Talent correlations exceed 80%. Intermediate Services-Leadership and Intermediate Services-Networks exceed 70%. Over time (2016-2023), Talent and Infrastructure show most variance (improving), while Finance and Knowledge are most stable. Ecosystems develop elements in clusters, not independently.

**Ubicación:** Section 2I
**Relevancia:** When diagnosing an ecosystem, expect correlated strengths and weaknesses. A strong Infrastructure score with weak Knowledge is unusual and worth investigating. The cluster pattern (Talent-with-Institutions, Services-with-Leadership) informs which domain improvements are likely to co-occur.

## Conexiones
- **Relacionado con:** oecd-2025-ee-diagnostics.md (companion report using this methodology), wurth-2023-ee-mechanisms.md (also uses composite index logic and bottleneck concept)
- **Refuerza:** The geometric mean / bottleneck logic directly supports Wurth et al.'s multiplicative index finding (6E). The element clusters align with Wurth's three interdependency clusters (6B).
- **Contradice o matiza:** The low Cronbach's alpha for Finance (0.28) and Networks (0.18) suggests these elements may combine heterogeneous constructs that do not form coherent latent variables — a methodological limitation acknowledged by the authors.
