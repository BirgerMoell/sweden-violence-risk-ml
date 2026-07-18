# SÄKER-ML Sweden

An open, reproducible study blueprint for developing and externally validating dynamic prediction models for interpersonal violence among adults receiving specialist psychiatric care in Sweden.

> **Research only.** This repository contains synthetic-data code and a proposed protocol. It is not a medical device, does not provide individual risk scores, and must not be used for care, policing, sentencing, coercion, or allocation of services.

## Why this project

Kozhevnikova et al. (2026) reviewed 38 studies and 40 violence-prediction models. Only eight studies reported calibration, only three performed external validation, and 31 were at high risk of bias. The authors do not recommend any current model for implementation. SÄKER-ML is designed around those failures: a prespecified estimand, transparent baseline, dynamic landmarks, site-held-out validation, calibration, decision-curve analysis, subgroup uncertainty, and a prospective silent-validation gate.

## Proposed study at a glance

- Population: adults (18+) starting an episode of specialist psychiatric care in participating Swedish regions.
- Unit: one landmark per person-week during an eligible care episode.
- Outcome: independently adjudicated interpersonal physical violence within 30 days; secondary 7- and 90-day horizons.
- Development: several regions and earlier calendar years.
- External validation: an untouched region plus later calendar period.
- Models: penalised logistic landmark model (primary), gradient-boosted trees, and discrete-time survival model. NLP is a separate, later work package.
- Primary performance: calibration-in-the-large, calibration slope, integrated calibration index, Brier score, AUROC, AUPRC, and decision curves.
- Use: research evaluation only; no scores returned to clinicians or authorities during development or silent validation.

## Repository map

- [STUDY_PROTOCOL.md](docs/STUDY_PROTOCOL.md) - protocol synopsis and statistical analysis plan
- [ML_PLAN.md](docs/ML_PLAN.md) - implementable ML design and leakage controls
- [GOVERNANCE.md](docs/GOVERNANCE.md) - Swedish legal, ethical, and operational safeguards
- [ROADMAP.md](docs/ROADMAP.md) - staged delivery plan and stop/go gates
- [DATA_DICTIONARY.md](docs/DATA_DICTIONARY.md) - minimum common data model
- `src/violence_risk/` - synthetic cohort, splitting, training, and evaluation code
- `tests/` - tests for temporal splitting, leakage prevention, and metrics
- `website/` - static GitHub Pages site
- `output/pdf/proposed-study.pdf` - rendered proposal

## Quick start

```bash
python -m venv .venv
source .venv/bin/activate
pip install -e '.[dev]'
python -m violence_risk.cli --config configs/demo.yaml
pytest
```

The demo generates synthetic records only. Real data must remain inside approved regional research environments and follow the governance plan.

## Reproducibility contract

The protocol and analysis plan are frozen before outcome access. Every model is evaluated on the same untouched partitions. Preprocessing is fit inside training folds. Hyperparameters are selected by nested, grouped, temporal validation. A model can advance only if calibration, net benefit, subgroup uncertainty, privacy, and workflow safety gates all pass.

## Citation

Primary source: Kozhevnikova S, Yukhnenko D, Scola G, Fazel S. *Machine learning for violence prediction: A systematic review and critical appraisal.* Journal of Criminal Justice. 2026;105:102697. [doi:10.1016/j.jcrimjus.2026.102697](https://doi.org/10.1016/j.jcrimjus.2026.102697).

## Licence and contributing

Code is MIT licensed. Documentation is CC BY 4.0. See [CONTRIBUTING.md](CONTRIBUTING.md). Security or privacy concerns should be reported privately as described in [SECURITY.md](SECURITY.md).
