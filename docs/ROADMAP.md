# Roadmap and decision gates

## Phase 0 - partnership and feasibility (6 months)

Form the multidisciplinary team and paid patient/public panel; select regions; map data availability; define intended use and prohibited uses; run formal sample-size scenarios; agree the outcome rubric; prepare ethics, DPIA, and data applications.

**Gate:** no extraction until approvals, roles, minimum event counts, and secure environment are confirmed.

## Phase 1 - data and protocol (6-12 months)

Freeze protocol/SAP, common data model, code lists, availability timestamps, linkage plan, and adjudication study. Build federated or centrally hosted extraction tests with synthetic fixtures.

**Gate:** outcome validity, temporal ordering, missingness, and cross-region comparability pass prespecified checks.

## Phase 2 - development (6 months)

Fit the penalised landmark baseline and limited comparators with nested internal-external validation. Produce full calibration, transportability, decision-curve, subgroup, and robustness reports.

**Gate:** external data remain untouched; analysis deviations are logged publicly.

## Phase 3 - external validation (6 months)

Run frozen models in held-out region and later time period. Permit only prespecified recalibration analyses. Complete PROBAST+AI and TRIPOD+AI reporting.

**Gate:** failure on calibration, net benefit, subgroup safety, or workload triggers redesign or stop.

## Phase 4 - prospective silent validation (12 months)

Run behind the scenes, display nothing, and measure drift, latency, missing data, alert burden, fairness, and operational reliability. Independent board reviews quarterly.

**Gate:** only unanimous safety/ethics approval and all quantitative criteria allow an impact-study application.

## Phase 5 - impact study (separate protocol)

Evaluate a co-designed supportive workflow against usual care, preferably cluster randomised. Measure patient benefit and harm, coercion, equity, workload, trust, and implementation fidelity. No deployment by default at study end.

## Indicative team

Psychiatry, nursing, violence prevention, epidemiology, biostatistics, ML, registry science, health informatics, ethics, law/data protection, information security, human factors, health economics, regional operations, and patient/public partners.
