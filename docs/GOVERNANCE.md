# Governance for Sweden

This is a planning aid, not legal advice. Confirm every point with the responsible research organisation, data-protection officer, ethics authority, data holders, and legal counsel before data access.

## Required approvals and roles

- Name a Swedish `forskningshuvudman` and controller(s); document joint-controller or processor arrangements.
- Obtain ethics approval before processing sensitive health data or personal data concerning offences.
- Establish GDPR Article 6 lawful basis and Article 9 research condition; do not assume consent is the only or sufficient basis.
- Complete a data protection impact assessment because the project combines large-scale health, behavioural, and possibly offence data with profiling.
- Obtain separate disclosure/secrecy decisions and data-use agreements from each data holder.
- Define data minimisation, purpose limitation, retention, deletion/archiving, access review, incident response, and data-subject information arrangements.

## Data architecture

Use a trusted research environment in Sweden/EU. Direct identifiers remain with authorised linkage functions. Researchers receive pseudonymous IDs and only approved variables. Encrypt in transit and at rest, enforce MFA and least privilege, log queries/exports, prohibit local copies, and manually review aggregate exports. Public releases contain code, schemas, synthetic data, and disclosure-checked aggregates only.

## Legal and policy context

- Sweden's ethics framework requires review for research processing sensitive personal data or offence data.
- Socialstyrelsen registers have strong secrecy protection; release for research requires a formal assessment.
- The National Patient Register covers specialist inpatient and physician-led outpatient care and does not include primary care; this limits the target population and must be stated.
- If a later system influences access to healthcare or is used by public authorities, it may fall within EU AI Act high-risk categories or other medical-device rules depending on intended purpose. Perform a documented classification before any operational trial; research exemption assumptions must not be carried into deployment.

## Ethical red lines

The model must not be used for policing, sentencing, migration, benefits, insurance, employment, involuntary treatment, seclusion/restraint, denial of care, or automatic escalation. A score must never be the sole basis for action. Race/ethnicity proxies, nationality, neighbourhood, and socioeconomic fields require a written necessity and harm analysis; audit variables are separated from operational predictors.

## Participation and contestability

Create a paid patient/public advisory group, including people with experience of psychosis, substance-use care, compulsory care, violence, victimisation, and discriminatory systems. Co-design outcomes, acceptable thresholds, alert wording, interventions, and stop rules. Before any visible use, provide understandable information, routes to correct source data, human review, documentation of disagreement, and complaint/appeal channels.

## Oversight

An independent safety and ethics board reviews protocol deviations, privacy incidents, subgroup harms, drift, workload, and all stage transitions. Publish minutes and a limitations register with privacy-preserving redactions. Register the study and analysis plan before validation. Declare funding and conflicts.

## Threat model

Key harms include re-identification, label leakage, biased documentation, feedback loops, automation bias, false-positive coercion, missed risk, stigma, function creep, model theft, membership inference, and politically motivated repurposing. Mitigations include strict purpose binding, no public weights, minimum cell sizes, audit trails, human-factors testing, non-punitive intervention design, monitoring, contractual prohibitions, and a kill switch.

## Authoritative starting points

- [Etikprövningsmyndigheten guidance](https://etikprovningsmyndigheten.se/vagledning/)
- [Etikprövningsmyndigheten on personal data](https://etikprovningsmyndigheten.se/personuppgifter/)
- [Socialstyrelsen National Patient Register](https://www.socialstyrelsen.se/statistik-och-data/register/patientregistret/)
- [Socialstyrelsen register secrecy and data](https://www.socialstyrelsen.se/statistik-och-data/register/)
- [EU AI Act text](https://eur-lex.europa.eu/eli/reg/2024/1689/oj)
