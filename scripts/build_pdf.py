from pathlib import Path
from xml.sax.saxutils import escape

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import mm
from reportlab.platypus import PageBreak, Paragraph, SimpleDocTemplate, Spacer, Table, TableStyle

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "output" / "pdf" / "proposed-study.pdf"

INK = colors.HexColor("#11261f")
TEAL = colors.HexColor("#0c7664")
ACID = colors.HexColor("#c9f05a")
PAPER = colors.HexColor("#f2f0e8")
MUTED = colors.HexColor("#5c6c66")

styles = getSampleStyleSheet()
styles.add(ParagraphStyle(name="CoverKicker", parent=styles["Normal"], fontName="Helvetica-Bold", fontSize=9, leading=12, textColor=ACID, spaceAfter=20, tracking=1.6))
styles.add(ParagraphStyle(name="CoverTitle", parent=styles["Title"], fontName="Helvetica-Bold", fontSize=36, leading=38, textColor=colors.white, alignment=TA_CENTER, spaceAfter=18))
styles.add(ParagraphStyle(name="CoverSub", parent=styles["Normal"], fontName="Helvetica", fontSize=13, leading=20, textColor=colors.HexColor("#d7e2dd"), alignment=TA_CENTER))
styles.add(ParagraphStyle(name="H1x", parent=styles["Heading1"], fontName="Helvetica-Bold", fontSize=23, leading=27, textColor=INK, spaceBefore=8, spaceAfter=12))
styles.add(ParagraphStyle(name="H2x", parent=styles["Heading2"], fontName="Helvetica-Bold", fontSize=13, leading=17, textColor=TEAL, spaceBefore=14, spaceAfter=6))
styles.add(ParagraphStyle(name="Bodyx", parent=styles["BodyText"], fontName="Helvetica", fontSize=9.3, leading=14, textColor=INK, spaceAfter=7))
styles.add(ParagraphStyle(name="Smallx", parent=styles["BodyText"], fontName="Helvetica", fontSize=7.8, leading=11, textColor=MUTED))
styles.add(ParagraphStyle(name="Callout", parent=styles["BodyText"], fontName="Helvetica-Bold", fontSize=11, leading=16, textColor=INK, backColor=colors.HexColor("#e5efbd"), borderPadding=12, spaceBefore=8, spaceAfter=14))


def header_footer(canvas, doc):
    canvas.saveState()
    if doc.page > 1:
        canvas.setStrokeColor(colors.HexColor("#d7d8d0"))
        canvas.line(20 * mm, 282 * mm, 190 * mm, 282 * mm)
        canvas.setFont("Helvetica", 7.5)
        canvas.setFillColor(MUTED)
        canvas.drawString(20 * mm, 286 * mm, "SÄKER-ML Sweden · Proposed study · v0.1")
        canvas.drawRightString(190 * mm, 12 * mm, str(doc.page))
    canvas.restoreState()


def p(text, style="Bodyx"):
    return Paragraph(escape(text), styles[style])


story = []
cover = Table([[p("SÄKER-ML SWEDEN", "CoverKicker")], [p("Prediction must earn the right to be useful", "CoverTitle")], [p("A multicentre Swedish study proposal for developing and externally validating dynamic machine-learning models for short-term interpersonal violence in specialist psychiatric care", "CoverSub")], [Spacer(1, 28 * mm)], [p("RESEARCH-ONLY PROPOSAL · 18 JULY 2026", "CoverKicker")]], colWidths=[170 * mm], rowHeights=[20 * mm, 50 * mm, 45 * mm, 45 * mm, 20 * mm])
cover.setStyle(TableStyle([("BACKGROUND", (0, 0), (-1, -1), INK), ("VALIGN", (0, 0), (-1, -1), "MIDDLE"), ("ALIGN", (0, 0), (-1, -1), "CENTER"), ("BOX", (0, 0), (-1, -1), 0, INK)]))
story += [Spacer(1, 20 * mm), cover, PageBreak()]

story += [p("Executive summary", "H1x"), p("This proposal translates the critical appraisal by Kozhevnikova and colleagues into a Swedish research design. Their 2026 review identified 38 studies and 40 models: only eight studies reported calibration, three performed external validation, and 31 were at high risk of bias. No current model was recommended for implementation."), p("The proposed study asks whether information already available in specialist psychiatric care can estimate 30-day interpersonal-violence risk and remain calibrated in another Swedish region and later calendar period. It deliberately separates model development from proof and then requires prospective silent validation before any clinical impact study.", "Callout")]

facts = [["Population", "Adults starting an episode of specialist psychiatric care in participating Swedish regions"], ["Prediction", "Weekly dynamic landmarks; primary 30-day horizon"], ["Primary model", "Penalised logistic landmark model"], ["Comparators", "Gradient-boosted trees and discrete-time survival"], ["Validation", "Held-out region, held-out future period, internal-external cross-validation, then silent prospective run"], ["Primary evidence", "Calibration, Brier score, discrimination, decision curves, workload and subgroup safety"], ["Operating mode", "Research only; scores are not shown or acted on"]]
t = Table([[p(a, "Smallx"), p(b, "Smallx")] for a, b in facts], colWidths=[36 * mm, 126 * mm])
t.setStyle(TableStyle([("BACKGROUND", (0, 0), (0, -1), colors.HexColor("#e2e7dc")), ("GRID", (0, 0), (-1, -1), .4, colors.HexColor("#cdd2ca")), ("VALIGN", (0, 0), (-1, -1), "TOP"), ("LEFTPADDING", (0, 0), (-1, -1), 7), ("RIGHTPADDING", (0, 0), (-1, -1), 7), ("TOPPADDING", (0, 0), (-1, -1), 6), ("BOTTOMPADDING", (0, 0), (-1, -1), 6)]))
story += [t, Spacer(1, 6 * mm), p("The project must stop, recalibrate, or redesign if calibration, net benefit, subgroup safety, privacy, workload, or operational reliability fail. A good AUROC is not a deployment criterion.")]

sections = [
("1. Research question and intended use", ["Primary estimand: for each eligible person-week, estimate the probability of first interpersonal physical violence in the next 30 days given information available at the landmark.", "The target population is specialist psychiatric care. The model is not intended for courts, policing, prisons, migration, insurance, employment, benefits, or automatic decisions. Prediction is not causal inference and does not identify which intervention will work."]),
("2. Design and population", ["Use a retrospective population-based multicentre cohort, followed by at least 12 months of prospective silent validation. Candidate retrospective years are 2016-2025, subject to approvals and stable data availability.", "Include adults aged 18 or older beginning an eligible inpatient or outpatient specialist psychiatric-care episode. Define a new episode after a 90-day washout. Create weekly landmarks during eligible episodes and keep all landmarks for one person within one validation unit."]),
("3. Outcome", ["The primary outcome is independently adjudicated interpersonal physical violence documented within 30 days. Ascertain from regional incident systems and structured EHR fields, violence-related injury/external-cause codes, and - only under a separate necessity and secrecy review - justice data.", "Lock the definition before modelling. Validate a stratified sample of positive and negative labels using blinded review. Report sensitivity, positive predictive value, agreement, and regional ascertainment differences. Threats, self-harm, property damage, victimisation, and restrictive interventions remain separate secondary outcomes."]),
("4. Predictors and data sources", ["Prespecify clinically plausible domains: age, recorded sex, prior care utilisation, diagnosis groups, substance-use diagnoses, recent emergency/inpatient care, prior documented violence, medication classes, and change in care intensity. Every predictor needs an availability timestamp and must be known before the landmark.", "Potential sources are regional EHR and incident systems, Socialstyrelsen's National Patient Register, Prescribed Drug Register and Cause of Death Register, and justified Statistics Sweden variables. The National Patient Register does not contain primary care, which constrains generalisability. Free text and transformer models are excluded from the primary work package."]),
("5. Sample size", ["Use formal prediction-model sample-size calculations based on outcome prevalence, anticipated model fit, candidate parameters, target shrinkage and calibration precision. A provisional operational target is at least 1,000 development events and 200 events in each major external validation set. If formal requirements are not met, reduce complexity, widen the horizon, pool development sites or stop. Do not manufacture prevalence by case-control oversampling."]),
("6. Models and leakage controls", ["Fit a penalised logistic landmark model as the primary transparent approach, with prespecified nonlinearities. Compare gradient boosting and a discrete-time survival model on exactly the same partitions. Complex models advance only if high-dimensional data justify them and they add calibration and net benefit.", "Split by person, region and time. Fit imputation, scaling, feature engineering, tuning and calibration inside training folds. Hold an entire region and later period untouched. Prohibit discharge summaries, incident-response records, restraint, injury codes or other facts created after the landmark from predictors."]),
("7. Evaluation", ["Report flexible calibration plots, calibration-in-the-large, calibration slope, integrated calibration index, Brier score, AUROC and AUPRC with prevalence. Use person-level cluster bootstrap confidence intervals.", "Use decision-curve analysis across thresholds chosen with patients and clinicians. Report sensitivity, specificity, PPV, NPV, alerts per 100 landmarks and number needed to evaluate. Report site/time heterogeneity and subgroup calibration, errors and net benefit with uncertainty. Inability to evaluate a small subgroup is itself a limitation."]),
("8. Governance and ethics in Sweden", ["Name the research principal and controllers; obtain Swedish ethical review before processing sensitive health or offence data; document GDPR Articles 6 and 9 bases; complete a data protection impact assessment; and obtain disclosure/secrecy decisions from each holder.", "Process pseudonymised data inside an approved Swedish/EU trusted research environment with MFA, least privilege, logging, encryption and reviewed exports. Publish code, schemas, synthetic fixtures and disclosure-checked aggregates - never row-level data or fitted weights that could leak sensitive information.", "Before any impact trial, classify the intended system under the EU AI Act and applicable medical-device rules. Research-stage assumptions must not be carried into deployment. Establish a paid patient/public panel and independent safety and ethics board."]),
("9. Stage gates", ["Phase 0: partnership, feasibility, outcome definition, sample size, ethics and DPIA. Phase 1: freeze protocol, data model and adjudication. Phase 2: development with nested internal-external validation. Phase 3: frozen geographic and temporal external validation. Phase 4: prospective silent validation. Phase 5, only under a separate protocol: a cluster-randomised or stepped-wedge impact study of a supportive, non-punitive workflow.", "Advancement requires acceptable calibration, positive net benefit against current practice, no unresolved subgroup harm, stable performance, feasible workload, secure operation, patient and clinician acceptability, and independent approval. Failure triggers redesign or stop."]),
("10. Open-science outputs", ["Publish the locked protocol and statistical analysis plan, extraction schemas, synthetic-data code, tests, analysis code, model card, data sheet, PROBAST+AI self-assessment, TRIPOD+AI report, deviations and negative findings. Real data remain under holder control. The repository is designed for scrutiny, not operational scoring."]),
]
for heading, paragraphs in sections:
    story.append(p(heading, "H1x"))
    for paragraph in paragraphs:
        story.append(p(paragraph))

story += [PageBreak(), p("References and authoritative sources", "H1x")]
refs = [
"Kozhevnikova S, Yukhnenko D, Scola G, Fazel S. Machine learning for violence prediction: a systematic review and critical appraisal. Journal of Criminal Justice. 2026;105:102697. doi:10.1016/j.jcrimjus.2026.102697.",
"Collins GS et al. TRIPOD+AI statement: updated guidance for reporting clinical prediction models that use regression or machine learning methods. BMJ. 2024;385:e078378.",
"Moons KGM et al. PROBAST+AI: an updated quality, risk of bias, and applicability assessment tool for prediction models using regression or artificial intelligence methods. BMJ. 2025;388:e082505.",
"Van Calster B et al. Calibration: the Achilles heel of predictive analytics. BMC Medicine. 2019;17:230.",
"Socialstyrelsen. Patientregistret; Register and secrecy guidance. Accessed 18 July 2026.",
"Etikprövningsmyndigheten. Guidance on ethical review and personal data in research. Accessed 18 July 2026.",
"Regulation (EU) 2024/1689 (Artificial Intelligence Act). Official Journal of the European Union.",
]
for i, ref in enumerate(refs, 1):
    story.append(p(f"{i}. {ref}", "Smallx"))
story += [Spacer(1, 8 * mm), p("Status and limitation", "H2x"), p("This document is a proposed study generated from an open-access reading of the source paper and authoritative public guidance. It has not been approved by an ethics committee, data holder, region, patient group, regulator or sponsor. Legal and regulatory classification must be confirmed for the final intended use.")]

OUT.parent.mkdir(parents=True, exist_ok=True)
doc = SimpleDocTemplate(str(OUT), pagesize=A4, rightMargin=20 * mm, leftMargin=20 * mm, topMargin=20 * mm, bottomMargin=18 * mm, title="SÄKER-ML Sweden proposed study", author="SÄKER-ML contributors")
doc.build(story, onFirstPage=header_footer, onLaterPages=header_footer)
print(OUT)
