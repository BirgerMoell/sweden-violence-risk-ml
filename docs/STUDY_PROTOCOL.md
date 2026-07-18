# Proposed study protocol

## Title

SÄKER-ML: multicentre development and external validation of dynamic models for short-term interpersonal violence in Swedish specialist psychiatric care.

Version 0.1, 18 July 2026. This is a proposal, not an approved protocol.

## Rationale and objective

The source review found apparently strong discrimination but weak evidence of clinical usefulness: 31/38 studies were at high risk of bias, only 8 reported calibration, and only 3 reported external validation. We therefore ask a narrower question: can routinely available information, known before a weekly prediction landmark, estimate 30-day interpersonal-violence risk with adequate calibration and useful net benefit when transported across Swedish regions and time?

The primary objective is external validation of a prespecified, interpretable dynamic model. Secondary objectives compare model classes, quantify heterogeneity and fairness, and test whether any model could justify a later prospective workflow trial. Prediction is not causation; the study does not estimate effects of interventions.

## Design

Retrospective, population-based, multicentre dynamic prediction study followed by prospective silent validation. Candidate calendar window: 2016-2025 for retrospective work, then at least 12 months of silent validation. Exact years depend on data availability and approval.

### Population

Adults aged 18 or older with a new eligible episode in specialist psychiatric inpatient or outpatient care in participating regions. An episode begins after a 90-day washout without specialist psychiatric contact. Exclude records lacking a linkable pseudonymous identifier or valid time ordering. Do not exclude people because predictors are missing.

The intended-use population is psychiatric care, not the general population, courts, prisons, police, migration, social insurance, or employment.

### Prediction unit and horizons

Create one landmark per eligible person-week. At landmark time *t*, use only facts available by *t* to estimate first interpersonal physical-violence event in (t, t+30 days]. Secondary horizons are 7 and 90 days. Repeated landmarks are clustered within person.

### Outcome

Primary outcome: documented interpersonal physical violence, defined in a locked code list and ascertained from a union of:

1. regional incident-report systems and structured EHR violence/aggression fields;
2. violence-related injury or external-cause codes in the National Patient Register;
3. after an explicitly approved linkage, suspected/convicted violent offences from justice data.

Before modelling, blinded reviewers adjudicate a stratified sample of positives and negatives against a written rubric. Report positive predictive value, sensitivity, agreement, and ascertainment differences by region. Threats, self-harm, property damage, restrictive interventions, and victimisation are secondary outcomes and are not silently merged into the primary label.

### Predictors

Prespecified, clinically plausible domains measured before the landmark: age; recorded sex; prior care contacts; diagnostic groups; substance-use diagnoses; recent emergency/inpatient care; prior documented violence; prescribed medication classes; recent change in care intensity; and region/calendar variables. Protected or sensitive attributes are used for auditing, not necessarily prediction. Free text and transformer models are excluded from the primary work package.

### Data sources

- Regional EHR/patient-administration and incident systems.
- Socialstyrelsen National Patient Register (specialist inpatient/outpatient care; no primary care).
- Prescribed Drug Register, Cause of Death Register, and LISA/Statistics Sweden variables where justified.
- Justice data only under separate necessity, proportionality, secrecy, and ethics review.

Every source receives a data-provenance table, availability timestamp, coding-change log, and missingness report. Linkage occurs within approved secure environments using pseudonymised study IDs.

## Sample size

Do not use a simple “20 events per variable” rule as the sole justification. Before extraction, estimate the number of outcome events, candidate parameters, anticipated Cox-Snell R², prevalence, shrinkage target, and expected validation precision using contemporary prediction-model sample-size methods. The provisional operational target is at least 1,000 primary events for development and 200 events in each major external validation set, with 95% confidence intervals for calibration slope and clinically relevant subgroup estimates. If these thresholds or formal calculations are not met, reduce model complexity, widen the horizon, pool sites for development, or stop; do not oversample positives and report an artificial prevalence.

## Partitioning and validation

1. Lock data dictionary, estimand, code lists, and analysis plan.
2. Development: grouped, forward-chaining nested resampling across earlier years and multiple regions.
3. Geographic external validation: hold out an entire region untouched.
4. Temporal external validation: evaluate on the latest untouched period.
5. Internal-external cross-validation: rotate held-out regions to quantify heterogeneity.
6. Prospective silent validation: run without displaying scores or changing care.

All landmarks for one person stay in one partition. Imputation, scaling, feature engineering, selection, and calibration occur inside training folds. No outcome-derived feature may cross the landmark.

## Models

Primary: penalised logistic landmark model with prespecified nonlinear terms and interactions. Comparators: gradient-boosted trees and discrete-time survival model. A simple current-practice/structured-tool benchmark is included if available. Deep learning or NLP proceeds only if high-dimensional data and sample size justify it and the primary transparent model has been completed.

## Performance and analysis

Report uncertainty with cluster bootstrap confidence intervals.

- Calibration: calibration plot with flexible smoother, calibration-in-the-large, slope, integrated calibration index, and Brier score.
- Discrimination: AUROC and AUPRC with outcome prevalence.
- Clinical usefulness: decision-curve net benefit over prespecified thresholds; sensitivity, specificity, PPV, NPV, alerts per 100 landmarks, and number needed to evaluate.
- Transportability: site- and time-specific results, heterogeneity, and recalibration needs.
- Fairness: calibration, error rates, and net benefit by sex, age group, country-of-birth grouping where lawful/justified, socioeconomic position, diagnosis, and region. Report uncertainty and intersectional analyses where counts permit; do not “fix” disparities by lowering standards for a group.
- Missingness: multiple imputation or model-compatible handling inside folds; missingness indicators only when justified. Complete-case analysis is sensitivity analysis.
- Sensitivity analyses: alternative outcome definitions, horizons, first landmark only, competing death, label delay, excluding justice outcomes, and measurement drift.

No single metric or threshold constitutes success. Thresholds are selected with patients, clinicians, violence-prevention specialists, and ethicists based on explicit harms and available supportive interventions.

## Bias, reporting, and reproducibility

Use PROBAST+AI prospectively as a design checklist and report according to TRIPOD+AI. Publish a model card, data sheet, locked statistical analysis plan, code, synthetic fixtures, and all deviations. Real row-level data and fitted artifacts that could leak sensitive information will not be public.

## Ethics and safety

Obtain approval from Etikprövningsmyndigheten before processing health or offence data. The research principal, lawful basis, Article 9 condition, data protection impact assessment, secrecy review, retention period, access matrix, and incident response must be documented. Patient/public partners participate from protocol through dissemination, with specific representation from groups likely to bear false-positive harms.

The retrospective and silent-validation phases do not return scores. Any later impact trial requires a new protocol, prospective registration, human-factors testing, an effective non-punitive intervention pathway, oversight, opt-out/contest mechanisms where applicable, monitoring, and a kill switch.

## Stop/go criteria

Advance from silent validation only if all prespecified criteria pass: acceptable overall and site calibration; positive net benefit against both treat-none and current practice across the agreed range; no material unresolved subgroup harm; stable performance through time; feasible workload; secure operation; clinician and patient acceptability; and independent safety-board approval. Failure means recalibrate, redesign, or stop - not tune on the test set.
