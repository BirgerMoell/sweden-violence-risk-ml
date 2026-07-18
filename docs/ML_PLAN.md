# Machine-learning implementation plan

## Estimand first

For each eligible weekly landmark, estimate `P(first_interpersonal_violence in next 30 days | information available at landmark)`. Predictions are probabilities, never labels such as “violent person.”

## Pipeline

```text
source snapshots -> availability timestamps -> cohort/landmarks -> locked outcome
  -> person-grouped temporal partitions -> fold-local preprocessing
  -> transparent baseline + ML comparator -> fold-local calibration
  -> external region/time evaluation -> decision curves + subgroup audit
  -> prospective silent validation
```

### Data contract

Each raw field must include source system, semantic definition, observation time, availability time, coding era, missingness meaning, and permitted use. The availability time - not merely event time - controls leakage. See `DATA_DICTIONARY.md`.

### Reference implementation

The public package deliberately uses synthetic tabular data and a small dependency surface. It demonstrates:

- person-grouped geographic/temporal splits;
- feature exclusion and time-order assertions;
- a logistic baseline and histogram gradient boosting comparator;
- out-of-fold calibration;
- calibration slope/intercept, Brier score, AUROC, AUPRC, and subgroup summaries;
- machine-readable outputs.

It is a scaffold, not a fitted Swedish model. Production extraction adapters remain private to data controllers; their schemas and tests can be public.

## Modelling decisions

1. Freeze predictor domains before outcome access.
2. Retain continuous variables; model nonlinearity rather than arbitrary bins.
3. Penalise rather than univariably screen predictors.
4. Tune with nested forward-chaining grouped validation.
5. Use class weights only inside sensitivity analysis; never change the validation prevalence.
6. Calibrate from out-of-fold development predictions, then freeze.
7. Compare against the transparent baseline using paired bootstrap differences, calibration, and net benefit - not only AUROC.
8. Treat explainability as supporting documentation, not proof of correctness or causality. Prefer native interpretability; for boosting, report permutation importance and carefully bounded local explanations.

## Leakage checklist

- Person identifiers never span train/test partitions.
- Predictors have `available_at <= landmark_at`.
- No discharge summary, incident response, restraint, injury code, police contact, or documentation written after the landmark enters predictors.
- Codebooks and mappings are versioned by calendar time.
- Imputation, scaling, feature selection, resampling, and calibration are learned without test data.
- Hyperparameter search never sees external-region or future-period labels.
- Multiple landmarks from one outcome episode do not create duplicate positive leakage.

## Evaluation outputs

Each evaluation produces a JSON model card fragment, calibration plot, decision curve, score distribution, alert burden table, site/time table, subgroup audit, and failure analysis. Confidence intervals use person-level cluster bootstrap. Low-count subgroup estimates are suppressed or combined under a prespecified privacy rule, while the inability to assess fairness is explicitly reported.

## Recalibration and updating

Estimate calibration intercept/slope by site and quarter. A predefined monitoring rule may trigger intercept-only recalibration; more extensive updating requires a versioned protocol and fresh validation. Never silently learn online from operational outcomes.

## Clinical utility is a separate study

If silent validation succeeds, compare a supported clinician workflow with usual care in a prospective cluster-randomised or stepped-wedge impact evaluation. Outcomes must include violence, coercive measures, false alerts, service use, patient-reported trust, inequity, and unintended consequences. Model accuracy alone cannot establish benefit.
