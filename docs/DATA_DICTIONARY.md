# Minimum common data model

| Field | Type | Role | Timing rule |
|---|---|---|---|
| `person_id` | string | grouping only | pseudonymous; never a predictor |
| `region` | category | site/transport audit | known at landmark |
| `landmark_at` | datetime | index time | defines prediction origin |
| `available_at` | datetime per source record | leakage control | must be <= landmark |
| `age` | continuous | candidate predictor | at landmark |
| `recorded_sex` | category | candidate/audit | source and meaning documented |
| `recent_emergency_contacts_30d` | count | candidate predictor | contact completed before landmark |
| `recent_inpatient_days_30d` | count | candidate predictor | accrued before landmark |
| `prior_violence_count` | count | candidate predictor | outcome-independent record available before landmark |
| `substance_use_dx` | binary | candidate predictor | diagnosis available before landmark |
| `care_intensity_change_14d` | numeric | candidate predictor | based on prior contacts only |
| `outcome_30d` | binary | primary label | first event after landmark through day 30 |

Each production variable also needs: source owner, extraction query version, semantic definition, units, coding system/version, permissible missing values, update latency, provenance, legal justification, retention, and quality checks.
