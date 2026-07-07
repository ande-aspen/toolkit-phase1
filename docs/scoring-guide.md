# Internal Scoring Guide — ANDE Phase 1 Diagnostic

Internal document explaining step by step how scores are assigned in the entrepreneurial ecosystem diagnostic under the ANDE methodology.

> **Note:** the current procedure also includes three aggregate metrics not covered by this guide — bottleneck-adjusted score (geometric mean), estimation uncertainty range, and structural maturity validation. The authoritative source for all calculations is the "Cálculos" section of `references/workflows/diagnostico.md`, and `scripts/score.py` computes all of them automatically.

---

## 1. General Principles

- **Scale:** Each indicator is scored from 0 to 100.
- **Domain score:** Simple average of the indicators within the domain.
- **Global score:** Simple average of the 7 domains (not of the 30 individual indicators). This prevents domains with more indicators from carrying disproportionate weight.
- **No data, no score:** If there is no verifiable data, record `N/A`. Estimates are allowed with explicit justification, marked as `(est.)`.

---

## 2. Diagnostic Structure

| Domain | Code | Indicators | Predominant Type |
|--------|------|------------|------------------|
| Policy & Regulation | P | P1, P2, P3 | Mixed (quant + qual) |
| Support Services | S | S1, S2, S3, S4, S5 | Count + absolute |
| Human Capital | H | H1, H2, H3, H4, H5 | Absolute |
| R&D & Innovation | I | I1, I2, I3 | Mixed |
| Finance | F | F1, F2, F3, F4, F5, F6 | Absolute + qual |
| Culture | C | C1, C2, C3, C4, C5 | Mixed + qual |
| Markets | M | M1, M2, M3 | Mixed + qual |

**Total:** 30 indicators, 7 domains.

---

## 3. Benchmark Types

Each indicator uses one of three benchmark types, which determines how the raw data is interpreted before assigning the score.

### 3.1 Absolute

The data is compared directly against fixed ranges, with no adjustment. Used when the indicator is internationally comparable or when the resource does not scale with population.

**Examples:** P1 (days to incorporate a business), F1 (total investment in USD), H5 (% internet access), S5 (internet speed in Mbps).

```
Raw data → Look up in range table → Score
```

### 3.2 Mixed (absolute or population-adjusted)

For cities with fewer than 1 million inhabitants, the data is adjusted before consulting the rubric. For cities of 1M or more, the absolute value is used.

**Applies to:** S1, S2, S3, S4, C1, C2, M1, M2, I1, I2.

```
If population < 1,000,000:
    Adjusted value = (Absolute value / Population) x 1,000,000
    Use adjusted value in the range table

If population >= 1,000,000:
    Use absolute value in the range table
```

**Worked example:**
- City with 400,000 inhabitants and 6 active accelerators (S1)
- Adjusted value = (6 / 400,000) x 1,000,000 = 15 per million
- Per S1 rubric: 15 per million → Score 80-100

### 3.3 Qualitative

The data is evaluated using descriptive criteria, not numeric thresholds. The evaluator reads the description for each range and assigns the one that best fits the observed reality.

**Applies to:** P2, P3, C3, C4, C5, M3.

```
Qualitative data → Read descriptive criteria → Choose the best-fitting range → Score
```

---

## 4. Scoring Process Step by Step

### Step 1: Collect data

For each indicator, document:

| Field | Description |
|-------|-------------|
| `value` | Raw data (number, descriptive text, or `N/A`) |
| `source` | Where the data comes from (URL, report, database) |
| `notes` | Relevant observations (data age, coverage, limitations) |

### Step 2: Adjust for population (if applicable)

Only for mixed-type indicators and only if the population is under 1 million.

### Step 3: Consult the rubric

Open `references/rubrica-scoring.md` and find the indicator. Compare the value (adjusted or absolute) against the table ranges. Assign a score within the corresponding range.

**Within a range, the evaluator chooses the exact point:**

| Position in range | When to use |
|-------------------|-------------|
| Upper end | Solid data, positive trend, multiple sources confirm |
| Midpoint | Standard data, no additional signals |
| Lower end | Single source, data older than 1 year, contradictory signals |

### Step 4: Flag estimates

If the data is not direct, add `(est.)` to the score and document the reasoning in `notes`. Situations requiring this flag:

- National data prorated to local level
- Data inferred from indirect sources
- Data older than 2 years
- Combination of partial data from multiple sources

### Step 5: Calculate domain scores

```
Domain score = Sum of indicator scores in the domain / Number of indicators in the domain
```

If an indicator is `N/A`, it is excluded from the average (not counted as zero).

### Step 6: Calculate global score

```
Global score = Sum of 7 domain scores / 7
```

---

## 5. Maturity Levels

The global score maps to an ecosystem maturity level:

| Global Score | Level | Description |
|--------------|-------|-------------|
| 0-25 | Nascent | Basic elements absent or incipient. Few support organizations, no capital flow, limited talent. |
| 26-45 | Emerging | Some elements present but disconnected. First support organizations, sporadic investment activity, university base under development. |
| 46-65 | Developing | Most elements present with gaps. Visible capital flow, active support organizations, gaps in specific domains. |
| 66-100 | Self-sustaining | Functional ecosystem with feedback loops. Reinvestment from exits, circulating talent, steady deal flow. |

---

## 6. Rules for Ambiguous Cases

### Round up when:

- There is evidence of a recent positive trend (e.g., accelerator launched 6 months ago)
- Indirect signals are consistent even though the exact data point is unavailable
- The ecosystem is small and absolute values are low but proportionally reasonable

### Round down when:

- The source is unverifiable or older than 2 years
- The data is national-level but the local reality may differ
- There are contradictory signals (e.g., "active" accelerator with no social media activity in 12+ months)
- The value relies on a single source without corroboration

### Flag as estimate when:

- National data is prorated to local level
- Data is inferred from indirect sources
- Data is older than 2 years without an update
- Partial data from multiple sources is combined

---

## 7. Worked Example: Scoring a Domain

**Domain: Support Services (S) — Fictitious city, 500,000 inhabitants**

| ID | Indicator | Raw data | Adjustment | Value used | Rubric range | Score |
|----|-----------|----------|------------|------------|--------------|-------|
| S1 | Active accelerators | 3 | (3/500K)x1M = 6 | 6 per million | 4-7 → 60-79 | 68 |
| S2 | Active incubators | 2 | (2/500K)x1M = 4 | 4 per million | 3-5 → 60-79 | 62 |
| S3 | Coworking spaces | 5 | (5/500K)x1M = 10 | 10 per million | 8-14 → 60-79 | 65 |
| S4 | Registered mentors | 8 | (8/500K)x1M = 16 | 16 per million | 10-19 → 40-59 | 45 |
| S5 | Internet speed | 72 Mbps | Not applicable (absolute) | 72 Mbps | 40-79 → 50-69 | 58 |

```
Score S = (68 + 62 + 65 + 45 + 58) / 5 = 59.6 → 60
```

---

## 8. Regional Calibration Notes

The rubric ranges are calibrated for ecosystems in Latin America and developing economies. Key considerations:

- **LATAM:** Ranges apply directly. Reference: regional VC ~USD 4.5B in 2024 (LAVCA), average internet penetration ~77%, days to incorporate a business ~11 days post-reforms.
- **US/Europe:** Finance (F) and Tech Talent (H4) ranges need upward adjustment. An "average" US ecosystem exceeds the LATAM scale maximum on several indicators.
- **Asia/Africa:** Evaluate case by case. Internet and patent data may need recalibration.

---

## 9. Quick Reference: All 30 Indicators

| ID | Indicator | Type | Adj. <1M |
|----|-----------|------|----------|
| P1 | Days to incorporate a business | Absolute | No |
| P2 | Startup tax regime | Qualitative | No |
| P3 | Active public support programs | Count | No |
| S1 | Active accelerators | Mixed | Yes |
| S2 | Active incubators | Mixed | Yes |
| S3 | Coworking spaces | Mixed | Yes |
| S4 | Registered mentors | Mixed | Yes |
| S5 | Internet speed (Mbps) | Absolute | No |
| H1 | Universities with entrepreneurship programs | Absolute | No |
| H2 | Active tech bootcamps | Absolute | No |
| H3 | Annual STEM graduates | Absolute | No |
| H4 | Available tech talent | Absolute | No |
| H5 | Internet access (%) | Absolute | No |
| I1 | Patents granted (5 years) | Mixed | Yes |
| I2 | Research centers | Mixed | Yes |
| I3 | Indexed scientific publications (3 years) | Absolute | No |
| F1 | Total startup investment (3 years, USD) | Absolute | No |
| F2 | Annual investment rounds | Absolute | No |
| F3 | VCs with local presence | Absolute | No |
| F4 | Active angel investors | Absolute | No |
| F5 | Documented exits (5 years) | Absolute | No |
| F6 | Public seed capital programs | Qualitative | No |
| C1 | Active meetups | Mixed | Yes |
| C2 | Annual entrepreneurship events | Mixed | Yes |
| C3 | Specialized media | Qualitative | No |
| C4 | Online communities | Qualitative | No |
| C5 | Social trust / entrepreneurship perception | Qualitative | No |
| M1 | Active startups | Mixed | Yes |
| M2 | Tech corporates | Mixed | Yes |
| M3 | Specialization sectors | Qualitative | No |
