# Africa Calibration Guide for the ANDE Phase 1 Rubric

## Purpose

The ANDE Phase 1 scoring rubric (`references/rubrica-scoring.md`) is calibrated primarily against Latin American and developing-economy benchmarks. When applied to Sub-Saharan African ecosystems (Nairobi, Lagos, Kigali, Accra, Dakar, Addis Ababa, Kampala, Dar es Salaam, Johannesburg, Cape Town, Lusaka, Abidjan), the rubric produces scores that are systematically biased because the reference economies, data sources, and continental distributions differ.

This guide specifies the data and the process required to produce an **Africa-calibrated** companion rubric (`references/rubrica-scoring-africa.md`) that can be applied alongside or in place of the LATAM rubric for African diagnostics. It does not reproduce the rubric itself — that is the deliverable of the calibration exercise.

---

## Why calibration matters

Stam and co-authors (2025) construct the Africa Entrepreneurial Ecosystem Index across 54 African countries on 7 dimensions and 20 indicators.¹ Three findings from that work establish why a continent-specific rubric is needed:

1. **Continental distributions differ from LATAM.** Support (0.14 AEEI mean) and Finance (0.14) are the weakest dimensions across Africa, with extreme skew in VC distribution — a few countries capture most activity while most have negligible formal venture flow. Governance (0.56) and Culture (0.41) are the highest. LATAM does not exhibit comparable asymmetry, so rubric bands anchored on LATAM medians compress or saturate when applied to African ecosystems.

2. **Data sources are different.** LATAM rubric references rely on LAVCA, GEM, Latinobarómetro, World Values Survey, CONACYT/ANUIES/SNIES, Doing Business / B-READY with LATAM coverage. African equivalents are Partech Africa, Briter Bridges, Afrilabs, Afrobarometer, African Economic Outlook, and national statistical authorities with variable coverage. Proxies also differ: Stam et al. use LinkedIn users per capita and Afrilabs hubs per capita as African-context proxies that have no LATAM analogue.

3. **Structural overperformance on specific indicators.** Africa overperforms LATAM on mobile-money penetration, pay-as-you-go energy and solar, certain mobile-first digital services, and M-PESA-style financial inclusion. The LATAM rubric under-credits these.

The maturity-level classification (Naciente / Emergente / En Desarrollo / Autosostenible) is likely robust to calibration choice because it keys on structural criteria. The **absolute score is not robust** — an Africa-calibrated rubric will produce scores that differ by 3-10 points per domain for most African ecosystems.

---

## Deliverables of a calibration exercise

A complete calibration produces the following artifacts:

1. **`references/rubrica-scoring-africa.md`** — 30-indicator rubric with Africa-anchored bands, analogous in structure to the existing LATAM rubric.
2. **`references/countries/[country].md`** — updated country files for the top 15-20 African ecosystems with national indicators, referencing African regional data sources.
3. **`references/africa-benchmarks.md`** — reference document with continental percentiles for each indicator (P10, P25, P50, P75, P90) computed across the African universe.
4. **`references/peer-cities-africa.md`** — short profiles of peer cities (Lagos, Nairobi, Cape Town, Johannesburg, Accra, Addis Ababa, Kigali, Dakar, Dar es Salaam, Kampala, Lusaka, Abidjan, Tunis, Cairo, Casablanca) with absolute counts on the 30 indicators for comparative benchmarking.
5. **Update to `references/workflows/diagnostico.md`** — add a decision step that selects between LATAM and African rubric based on the country of the ecosystem being diagnosed.
6. **Validation pack** — recomputed scores for 3-5 African ecosystems already diagnosed under the LATAM rubric, side-by-side comparison, and explanatory notes.

---

## Data required

### 1. Continental ecosystem data (for benchmark bands)

| Data | Source | Access | Notes |
|---|---|---|---|
| VC flows by country (annual, 5y history) | Partech Africa Tech Venture Capital Report | Free PDF, annual | Gold standard for African VC totals |
| Deal-level funding by country | Africa: The Big Deal | Free newsletter, paid dataset | Deal-by-deal granular coverage |
| Accelerator and incubator counts | Briter Bridges, Afrilabs Directory, AfriLabs network map | Free / paid | Afrilabs is the gold standard for hub density |
| Startup directories | Disrupt Africa (annual reports), StartupBlink, Crunchbase Africa, Briter | Free / paid | Cross-reference for M1 counts |
| Corporate tech presence | Press monitoring, job boards, corporate announcements | Manual | No single source; requires scraping / curation |
| Interpersonal trust and entrepreneurship perception | Afrobarometer (Round 9 and prior) | Free | Replaces WVS/Latinobarómetro for C5 |
| TEA and entrepreneurship attitudes | GEM Africa (subset of countries) | Paid / partial free | Coverage is incomplete for Africa |
| Patents | Regional IP offices (KIPI, CIPC, ARIPO, OAPI) + WIPO | Free for aggregates | ARIPO and OAPI aggregate for member states |
| Research publications | SCImago, Scopus, Web of Science | Paid for granular, free for country totals | Aggregate by institution and city |
| Internet penetration | DataReportal, ITU, GSMA Intelligence, AfTerFibre | Free / paid | Mobile-first bias must be handled |
| Internet speed | Ookla Speedtest Global Index | Free | Fixed and mobile medians by country |
| R&D intensity | UNESCO Institute for Statistics, African Union STISA | Free | GERD as % of GDP, by country |
| Incorporation days | World Bank B-READY (successor to Doing Business) | Free | Africa coverage adequate |
| Tax regimes and startup acts | Regional tax authority publications; Startup Act trackers (i4Policy, GIZ, ANDE) | Free | Track which countries have enacted Startup Acts |

### 2. City-level adjustments (for Tier-1 African ecosystems)

Minimum dataset per city:
- Metro population (UN Habitat, national census)
- Metro share of national VC (Partech, Briter — often inferred 80-90% for capital cities)
- University-by-institution STEM graduates (national CUE/CHE/NUC equivalents)
- Published research output by institution (SCImago)
- Bootcamp enrollment data (Moringa, AkiraChix, ALX, Zindua, Sand Technologies, Decagon, Gebeya, etc.)
- Coworking census (Afrilabs + Coworker + manual)
- Accelerator census (Briter + Afrilabs)
- Internet speed and penetration with metro adjustment (Ookla, national regulator)
- Research institution headquarters (CGIAR, African academies, international institutes)

### 3. Validation data

- 3-5 African ecosystems already diagnosed under the LATAM rubric (Nairobi, Lagos, if available Accra or Cape Town)
- ANDE Phase 2 consultation notes where available
- External rankings for triangulation (StartupBlink Africa, AEEI, GIZ country diagnostics, i4Policy Startup Act tracker)

---

## Step-by-step calibration process

### Phase 0 — Scoping (2 weeks)

1. Confirm scope: which African countries / cities does the rubric need to cover? Recommendation: start with the 15 cities listed in Deliverable #4.
2. Assign ownership: designate a lead author, a statistical reviewer, and a regional advisory panel (3-5 practitioners from different African sub-regions: West, East, Central, Southern, North).
3. Set calibration reference year and data freeze date. Recommend using the most recent complete year's Partech and AEEI data.
4. Define what "success" means: target is a rubric where a typical African top-tier ecosystem scores in the 60-80 range (not saturating top bands), a mid-tier scores in 40-60, and an emerging scores in 20-40, preserving the ANDE maturity bands.

### Phase 1 — Continental benchmark construction (4-6 weeks)

For each of the 30 ANDE indicators:

1. **Identify the African data source.** Some indicators will be straightforward (P1 via B-READY, H5 via DataReportal, S5 via Ookla). Others require aggregation (F3 VC count requires cross-referencing Partech + Briter + firm websites).
2. **Compute the African continental distribution** (54 countries where possible, 15 focus cities where indicator is city-level). Produce percentiles: P10, P25, P50, P75, P90.
3. **Compare to LATAM rubric bands.** Document where bands need to move up, down, or stay. For example, F1 LATAM top band is >USD 500M over 3 years; Africa's Stam et al. range suggests the top band should be >USD 300M for country-level and >USD 200M for city-level, given the thinner distribution.
4. **Handle data gaps.** For indicators where African data is sparse (F4 angel counts, C4 online communities, C1 meetups), use proxy indicators per Stam et al. (INS-2): Afrilabs hubs per capita, LinkedIn users per capita, Afrobarometer trust, GSMA mobile-money penetration.
5. **Document methodology and sources per indicator** in the rubric file.

### Phase 2 — City-level tier definitions (2-3 weeks)

1. Classify African ecosystems into tiers based on AEEI rank and city-level ecosystem density:
   - **Tier 1 (frontier):** Cape Town, Johannesburg, Lagos, Nairobi, Cairo (scoring band 65-80 target)
   - **Tier 2 (consolidating):** Accra, Kigali, Addis Ababa, Dakar, Casablanca, Tunis, Abidjan, Dar es Salaam, Kampala (band 45-65 target)
   - **Tier 3 (emerging):** Lusaka, Kinshasa, Maputo, Harare, Yaoundé, Kampala, Bamako, Antananarivo (band 25-45 target)
   - **Tier 4 (incipient):** Rest (band <25 target)
2. For each tier, define the "typical" profile on each of the 30 indicators as a reference.
3. Use this as a sanity check on Phase 1 band definitions — if applying the new bands to Tier 1 cities produces scores outside the 65-80 range, revisit.

### Phase 3 — Population adjustment and mobile-first premium (1-2 weeks)

1. **Population thresholds.** Adjust the population-adjustment rule. ANDE currently applies per-capita adjustment to ecosystems <1M. In Africa, metro-level data integrity varies; recommendation is to apply per-capita adjustment to any metro <3M (catches Kigali, Accra, Kampala) and use absolute counts only for Lagos, Cairo, Kinshasa, Johannesburg, Nairobi.
2. **Mobile-first premium.** Introduce an adjustment to S5 and H5 for mobile-money penetration (GSMA Intelligence data). Ecosystems where mobile-money covers >50% of adults get an additive adjustment to H5 (e.g., +5 points) to reflect effective financial inclusion that the traditional "internet access" indicator misses. Specify the rule precisely.
3. **Cross-border structuring premium/discount.** Kenyan, Nigerian, and South African startups commonly redomicile to Mauritius, Delaware, or UK. Introduce a note (not a scoring adjustment) that flags this structural feature when F1 totals are reported.

### Phase 4 — Cultural indicators reboot (2 weeks)

C5 requires specific treatment. Afrobarometer replaces WVS/Latinobarómetro. The GEM "good career" signal coexists with low interpersonal trust in SSA in ways the LATAM rubric does not anticipate. New C5 rubric should:
1. Use Afrobarometer trust variables as the primary signal.
2. Use GEM "good career" as secondary signal where available (~25 African countries covered).
3. Distinguish necessity-driven TEA from aspirational TEA per GEM methodology; give aspirational TEA positive weight and necessity-driven TEA neutral weight.
4. Introduce an "aspirational premium" for ecosystems that are national/regional cultural centers for tech entrepreneurship (Nairobi, Lagos, Kigali, Cape Town, Accra).

### Phase 5 — Peer-review and validation (3-4 weeks)

1. Present draft rubric to the regional advisory panel. Collect written feedback.
2. Re-score 3-5 African ecosystems already diagnosed under the LATAM rubric. Produce side-by-side comparison.
3. Check that:
   - Maturity classifications remain stable (e.g., Nairobi stays Self-Sustaining)
   - Score deltas are defensible and directionally consistent (Finance scores compress for most ecosystems; Culture scores shift based on Afrobarometer)
   - No ecosystem moves by more than one maturity band as a result of recalibration
4. If validation exposes issues, iterate Phase 1-4.

### Phase 6 — Publication and integration (2 weeks)

1. Publish `references/rubrica-scoring-africa.md` and the supporting reference files.
2. Update `references/workflows/diagnostico.md` with the country-based rubric selection logic:
   - If country is in Africa → use `rubrica-scoring-africa.md`
   - If country is in LATAM or elsewhere → use `rubrica-scoring.md`
   - Document the selection in the report header
3. Re-run diagnostics for Nairobi and any other African cities in the pipeline.
4. Update the `references/countries/` files for African countries with the new benchmarks.

---

## Indicator-by-indicator priorities

Ranked by the size of the expected calibration gap:

### High priority (largest LATAM→Africa shifts expected)
- **F1, F2, F3, F4, F5** — all Finance indicators. Continental skew means LATAM top bands saturate for Tier 1 African ecosystems.
- **C5** — LATAM reference frames (WVS, Latinobarómetro) do not apply.
- **I1** — R&D intensity is structurally lower; bands need compression.
- **H5** — LATAM internet penetration range does not map to African distribution.

### Medium priority
- **S5** — Ookla anchor needs African median replacement.
- **H4** — LinkedIn penetration differs; proxy multiplier should change.
- **M1, M2** — Absolute counts saturate for Tier 1 cities; per-capita or AEEI-normalized bands improve discrimination.
- **P3** — Program-counting rules work but examples need African references (Senegal Startup Act, Tunisia Startup Act, Ghana Startup Act, Kenya Startup Bill).

### Low priority (small calibration gap expected)
- **P1** — B-READY gives comparable global anchors; minor adjustment only.
- **P2** — Rubric is qualitative; African examples need updating but structure holds.
- **S1, S2, S3, S4** — Afrilabs hub density provides a direct African benchmark; bands shift but logic holds.
- **H1, H2, H3** — University and bootcamp counting is structurally similar; African examples need updating.
- **C1, C2, C3, C4** — Counting logic holds; African examples need updating.
- **I2, I3** — Continental distributions differ but rubric band logic holds; Nairobi's CGIAR density is an outlier either way.

---

## Worked example — F1 band recalibration (illustrative)

**LATAM rubric F1 bands:**
| Score | Band | Reference cities |
|---|---|---|
| 90-100 | >USD 500M (3y) | São Paulo, CDMX, Bogotá, Buenos Aires |
| 70-89 | USD 100M-500M | Medellín, Monterrey, Santiago, Lima |
| 50-69 | USD 30M-100M | Guadalajara, Barranquilla, San José CR |

**Africa-calibrated F1 bands (proposed direction, would require Phase 1 computation to finalize):**
| Score | Band | Reference cities |
|---|---|---|
| 90-100 | >USD 1.5B (3y) | Lagos, Nairobi, Cape Town (frontier within Africa) |
| 70-89 | USD 500M-1.5B | Johannesburg, Cairo, Accra |
| 50-69 | USD 150M-500M | Kigali, Dakar, Tunis, Addis Ababa |
| 30-49 | USD 30M-150M | Dar es Salaam, Kampala, Lusaka, Casablanca |
| 10-29 | USD 5M-30M | Secondary African ecosystems |

Under this re-calibration, Nairobi's USD 2.5-3.0B cumulative (2023-2025) still scores 90-100 but is now near band minimum rather than well above it — reflecting that Nairobi is frontier within Africa but not a structural outlier. The LATAM rubric would score 95+ and overstate Nairobi's relative position among its African peers.

This is illustrative only; the actual recalibration must be done with the full Partech + AEEI + Briter dataset in Phase 1.

---

## Governance and maintenance

1. **Annual refresh.** Partech Africa publishes annual data; AEEI updates periodically; Ookla and DataReportal refresh quarterly. Annual rubric review with minor band adjustments keeps benchmarks current.
2. **Full re-calibration every 3-5 years.** Continental distributions shift meaningfully over 3-5 year windows. A full rebuild prevents drift.
3. **Regional advisory panel.** Maintain a rotating panel of 5-7 African ecosystem practitioners from different sub-regions to sanity-check rubric output.
4. **Change log.** Track every band change with rationale and date. Retire old versions rather than overwriting.
5. **Cross-reference with LATAM rubric.** Publish a concordance table so ecosystems can be compared across regions if needed, with explicit warnings about the limits of cross-region comparison.

---

## Rough effort and dependencies

| Phase | Effort | Skill required | Can run in parallel? |
|---|---|---|---|
| Phase 0 Scoping | 2 weeks | Project lead | No |
| Phase 1 Continental benchmarks | 4-6 weeks | Data analyst + domain expert | No |
| Phase 2 City tiers | 2-3 weeks | Ecosystem analyst | With Phase 1 |
| Phase 3 Population & mobile adjustments | 1-2 weeks | Statistical reviewer | With Phase 2 |
| Phase 4 Cultural reboot | 2 weeks | Regional specialist | With Phase 1 |
| Phase 5 Peer review & validation | 3-4 weeks | Advisory panel + lead | No |
| Phase 6 Publication | 2 weeks | Project lead | No |

Total: **16-21 weeks** for a first version. Annual refresh: 3-4 weeks.

---

## What this guide does not do

- It does not replace the ANDE Phase 1 methodology. The framework, the 7 domains, the 30 indicators, the Condition-Outcome pattern, the maturity bands, and the Table 4.3 intervention logic all stay intact.
- It does not prescribe the final Africa rubric. That is the deliverable of the calibration exercise, not an input to it.
- It does not cover North Africa specifically. Morocco, Tunisia, Egypt, Algeria have ecosystem characteristics closer to MENA than SSA. A separate MENA calibration (or a MENA section within the African rubric) may be warranted.
- It does not address French-speaking vs. English-speaking Africa differences in data availability. OHADA countries have harmonized business law that affects P1/P2 scoring; this should be flagged in the country files but does not require rubric-level treatment.

---

## References

¹ Stam, E., Nkontwana, P., McDonald, R., Murenzi, R., Aboah Addo, K., Bayuo, B., Baah, B., Riezebos, S. & Gelissen, T. (2025). *Measuring National Entrepreneurial Ecosystems in Africa*. SSRN Working Paper 5254687. See `knowledge/papers/stam-ssrn-africa-ecosystem-index.md` for indexed insights.
² ANDE (2025). *Model for the Diagnosis of Entrepreneurship Ecosystems*, Second Edition.
³ Partech Africa (annual). *Africa Tech Venture Capital Report*.
⁴ Afrobarometer. Round 9 (2022-2023) survey data. https://www.afrobarometer.org
⁵ Briter Bridges. *Africa Investment Report* (annual).
⁶ Disrupt Africa. *Annual African Tech Startups Funding Report*.
⁷ AfriLabs. *Innovation Hub Directory*. https://afrilabs.com
⁸ i4Policy, GIZ, ANDE. *African Startup Act tracker* (various).
⁹ UNESCO Institute for Statistics. *Science, Technology and Innovation statistics*.
¹⁰ GSMA Intelligence. *Mobile Economy Sub-Saharan Africa* (annual).
