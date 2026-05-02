#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Convert all status-missing policy cards in equal-justice-and-policing.html
to status-included, adding rule-stmt and rule-notes content per PAOS-TEST-0008.

Usage: python scripts/complete-missing-cards.py
"""

from pathlib import Path
from bs4 import BeautifulSoup, NavigableString

HTML_FILE = (
    Path(__file__).parent.parent / "docs/pillars/equal-justice-and-policing.html"
)

# Keys are ID suffixes (strip the leading 'JUST-').
# Each dict may contain:
#   'stmt'   → replace or insert rule-stmt (None = leave existing)
#   'notes'  → replace, insert, or append to rule-notes (None = leave existing)
#   'append' → if True, append 'notes' text to existing rule-notes content
# Cards not listed here get class+badge change only (already have full content).

CARD_CONTENT = {
    # ------------------------------------------------------------------ AINL --
    "AINL-0001": {
        "notes": (
            "AI-generated risk assessment tools, including the widely used COMPAS system, "
            "have been found to predict recidivism with no greater accuracy than untrained "
            "volunteers — approximately 65% — while producing racially disparate error patterns, "
            "falsely flagging Black defendants as high-risk at nearly twice the rate of white "
            "defendants. ProPublica's 2016 analysis of COMPAS scores in Broward County, Florida "
            "found Black defendants were 77% more likely to be flagged as future criminals and "
            "45% more likely to be flagged for violent reoffending. In State v. Loomis, "
            "881 N.W.2d 749 (Wis. 2016), the Wisconsin Supreme Court allowed reference to COMPAS "
            "scores in sentencing. Adversarial review: vendors may relabel output as "
            "'informational' rather than 'recommendation' to evade prohibition; courts may "
            "accept AI risk scores through expert witness testimony rather than direct judicial "
            "application; prohibition must include any mechanism — direct or indirect — by which "
            "AI outputs influence sentencing outcomes."
        ),
    },
    "AINL-0002": {
        "notes": (
            "Multiple peer-reviewed studies have confirmed that AI recidivism prediction tools "
            "are no more accurate than human judgment and generate racially biased error rates. "
            "The AI Now Institute (2019) documented how these tools embed historical law "
            "enforcement patterns into predictive outputs, causing feedback loops that "
            "disproportionately harm communities of color. Adversarial review: 'treatment "
            "recommendation' framing may substitute for 'sentencing recommendation' while "
            "functionally serving the same purpose; 'risk-informed programming assignment' may "
            "replicate sentencing impacts in conditions of confinement without qualifying as a "
            "sentencing decision; scope must cover pre-sentencing, sentencing, and "
            "conditions-of-incarceration decisions."
        ),
    },
    "AINL-0003": {
        "notes": (
            "The National Registry of Exonerations documented 3,200+ exonerations since 1989, "
            "representing approximately 29,000 years of wrongful imprisonment. AI-assisted "
            "pattern recognition can surface statistically anomalous cases for human review, "
            "identify Brady violations across large document sets, and flag discredited forensic "
            "methods in a class of cases at a scale exceeding human processing capacity. "
            "Adversarial review: AI case-review tools must not become a new gatekeeping layer "
            "that reduces access to review rather than expanding it; defense must have equal "
            "access to review tools as prosecution; AI-identified potential wrongful convictions "
            "must trigger human review, not automatic relief or denial; the operator of the AI "
            "tool must not have a conflict of interest in the outcome."
        ),
    },
    "AINL-0004": {
        "notes": (
            "USSC data shows Black male federal defendants received sentences averaging 13.4% "
            "longer than similarly situated white male defendants in FY 2022, controlling for "
            "legally relevant factors. AI bias auditing tools can identify statistical patterns "
            "of disparate impact in charging, plea, and sentencing decisions at scale that no "
            "individual reviewer could detect case-by-case. Adversarial review: an AI "
            "bias-finding tool controlled by the same agency being audited cannot provide "
            "independent results; bias audits without structural reforms attached produce "
            "findings with no remediation pathway; oversight requirements must specify who "
            "controls the AI, who reviews findings, and what enforceable consequences follow; "
            "AI identification of bias cannot substitute for structural change."
        ),
    },
    "AINL-0005": {
        "notes": (
            "Federal Rule of Evidence 702 and Daubert v. Merrell Dow Pharmaceuticals, "
            "509 U.S. 579 (1993) require scientific evidence to be based on sufficient facts, "
            "derive from reliable methods, and result from reliable application of those methods. "
            "AI systems using opaque proprietary models cannot meet Daubert requirements. "
            "Trade secret protections have been asserted by vendors including Northpointe "
            "(COMPAS) to resist disclosure of model methodology. Adversarial review: "
            "'transparency' must define minimum disclosure standards — model architecture, "
            "training data, validation methodology, and known error rates — not just that an AI "
            "was used; vendors claiming trade secret protection must produce methodology to a "
            "court expert under protective order; challenges to AI evidence require technical "
            "experts, creating another resource-imbalance problem."
        ),
    },
    "AINL-0006": {
        "notes": (
            "The Confrontation Clause (6th Amendment) guarantees the right to confront "
            "witnesses; AI systems are not witnesses but their outputs may function as such in "
            "practice. The European Court of Human Rights has found that use of undisclosed "
            "methods in criminal proceedings can violate Article 6 (fair trial) rights. "
            "Adversarial review: courts may classify AI output as documentary evidence rather "
            "than expert testimony, avoiding Confrontation Clause scrutiny; examination rights "
            "without funded technical resources to exercise them are hollow; courts may accept "
            "AI examination by prosecution's own experts as sufficient; the right must include "
            "access to training data, not just model description."
        ),
    },
    "AINL-0007": {
        "notes": (
            "AI-based jury selection tools have been marketed to trial consultants using social "
            "media data, demographic profiles, and behavioral models to identify and exclude "
            "unfavorable jurors. These tools allow sophisticated operationalization of implicit "
            "bias through data proxies, evading formal anti-discrimination doctrine. "
            "Batson v. Kentucky, 476 U.S. 79 (1986) prohibited racial exclusion in jury "
            "selection but requires opposing counsel to identify discriminatory strikes — a "
            "showing that AI profiling makes impossible to demonstrate. Adversarial review: "
            "AI profiling may be used during juror research phases before formal voir dire, "
            "leaving no discoverable trail; marketing these tools as 'research' allows evasion; "
            "prohibition must reach the functional activity — using AI to inform juror exclusion "
            "decisions — not just its formal label."
        ),
    },
    "AINL-0008": {
        "notes": (
            "Prosecutorial charging decisions are the most consequential and least supervised "
            "discretionary acts in the criminal justice system. Research by the Vera Institute "
            "shows that charging decisions are a primary driver of racial disparities that "
            "compound through the rest of the system. AI-assisted charging tools risk "
            "systematizing existing prosecutorial biases at scale without requiring any "
            "individual prosecutor to make a consciously biased decision. Adversarial review: "
            "'human oversight' requirements can be satisfied by nominal sign-off with no genuine "
            "review; AI tools may filter cases before a human sees them; the prohibition must "
            "require that the human making the decision actually reviewed the individual case "
            "independently, not merely approved an AI recommendation."
        ),
    },
    "AINL-0009": {
        "notes": (
            "Absent disclosure requirements, defendants cannot challenge or investigate "
            "AI-influenced decisions in their cases. The right to confrontation and to prepare a "
            "defense is meaningless if the defendant does not know that an AI tool influenced a "
            "critical decision. Adversarial review: disclosure that 'an AI was used' without "
            "disclosing what it did and its limitations is functionally inadequate; AI may "
            "influence early case assessment stages before formal proceedings begin, placing "
            "decisions outside disclosure windows; late disclosure — after plea negotiations are "
            "complete — forecloses effective challenge; disclosure standards must include timing "
            "requirements (before plea discussions) and substantive requirements (model type, "
            "purpose, known error rates)."
        ),
    },
    "AINL-0010": {
        "notes": (
            "The 2009 National Academy of Sciences report Strengthening Forensic Science in "
            "the United States found that the majority of forensic disciplines lack adequate "
            "scientific validation. The 2016 PCAST report found that bite-mark analysis, shoe "
            "print analysis, and others had error rates either unknown or unacceptably high. "
            "AI evidence systems face the same validation deficit but with additional opacity. "
            "Adversarial review: courts may apply lower standards to AI evidence because it "
            "appears more 'objective' than human expert testimony; AI validation is complicated "
            "by inability to fully examine training data; vendors may produce industry "
            "self-certification as a substitute for independent scientific validation; the "
            "standard must require published peer review, known error rates, and independent "
            "replication."
        ),
    },
    # ------------------------------------------------------------------ BALS --
    "BALS-0001": {
        "stmt": (
            "Cash bail as a condition of pretrial release is prohibited for all misdemeanor "
            "and non-violent felony offenses; for offenses involving allegations of violence, "
            "bail determinations must be individualized and based on clear and convincing "
            "evidence of flight risk or specific safety threat rather than wealth; "
            "ability-to-pay assessment is mandatory before any monetary condition of release "
            "is imposed; and courts must provide non-monetary alternatives including supervised "
            "release, check-in requirements, and targeted assistance with court appearances."
        ),
        "notes": (
            " Adversarial review: abolishing cash bail without adding supervised release "
            "infrastructure may increase the use of preventive detention as a substitute, "
            "trading one deprivation for another; 'violent offense' carve-outs must be carefully "
            "defined to prevent prosecutorial re-categorization of charges; high bail as "
            "coercive plea pressure must be expressly prohibited; jurisdictions must track "
            "changes in pretrial detention rates after bail reform to verify that abolition "
            "produces actual decreases rather than substitutions."
        ),
        "append": True,
    },
    "BALS-0002": {
        "notes": (
            "In United States v. Salerno, 481 U.S. 739 (1987), the Supreme Court upheld "
            "preventive detention provisions requiring individualized review and a finding of "
            "future dangerousness by clear and convincing evidence. Research shows that pretrial "
            "detention of even 2–3 days dramatically increases likelihood of a guilty plea, "
            "subsequent incarceration, and future criminal justice contact — independently of "
            "the underlying charges. Adversarial review: 'individualized review' requirements "
            "can be satisfied by rubber-stamp hearings in high-volume courts; prosecutors can "
            "use detention requests as plea pressure regardless of genuine flight or safety "
            "concerns; resources for monitoring alternatives must exist or 'least restrictive' "
            "standard becomes 'detention because nothing else is available.'"
        ),
    },
    "BALS-0003": {
        "notes": (
            "AI pretrial risk assessment tools including the Arnold Foundation Public Safety "
            "Assessment and Northpointe's FTA score use factors that correlate with race — "
            "prior arrests (reflecting over-policing, not criminal behavior), residential "
            "stability, employment history — to generate risk scores. A 2020 study in Science "
            "found that all three examined AI pretrial tools produced false positive rates twice "
            "as high for Black defendants as white defendants. Adversarial review: removing AI "
            "risk scores without addressing judicial bias does not eliminate the disparity — "
            "courts may replace AI scores with informal heuristics that reproduce the same "
            "patterns; the alternative to AI risk scores must be genuinely individualized "
            "review, not informal assessment that is even less constrained."
        ),
    },
    "BALS-0004": {
        "notes": (
            "In Stack v. Boyle, 342 U.S. 1 (1951), the Supreme Court held that bail must not "
            "be excessive in relation to its purpose of ensuring court appearance. Research "
            "shows that structured pretrial supervision — regular check-ins, court date "
            "reminders, targeted assistance — is as effective as monetary bail for ensuring "
            "court appearance for most defendants. Adversarial review: 'least restrictive "
            "conditions' standards can be circumvented by imposing onerous non-monetary "
            "conditions — electronic monitoring fees, daily reporting, travel restrictions — "
            "that are restrictive in practice; electronic monitoring imposes significant costs "
            "and burdens on defendants; the standard must apply to conditions in aggregate, "
            "not just to any single condition in isolation."
        ),
    },
    # ------------------------------------------------------------------ CIVL --
    "CIVL-0001": {
        "notes": (
            "The Legal Services Corporation estimates that 80% of the civil legal needs of "
            "low-income Americans go unmet. In eviction court, research shows landlords are "
            "represented by attorneys in approximately 90% of cases while tenants appear without "
            "representation in a majority of cases — a structural disadvantage producing worse "
            "outcomes regardless of the merits. Adversarial review: 'meaningful access' without "
            "defining what it means is unenforceable; legal aid referrals do not constitute "
            "meaningful access if funded capacity is insufficient to serve demand; courts may "
            "satisfy formal requirements through self-help resources while actual access remains "
            "limited."
        ),
    },
    "CIVL-0002": {
        "notes": (
            "In AT&T Mobility LLC v. Concepcion, 563 U.S. 333 (2011), the Supreme Court held "
            "that the Federal Arbitration Act preempts state laws invalidating class action "
            "waivers in arbitration agreements. In Epic Systems Corp. v. Lewis, 584 U.S. 497 "
            "(2018), the Court extended this to employment class action waivers. Approximately "
            "60 million workers are currently subject to mandatory arbitration agreements. "
            "Research by Alexander Colvin shows employees win in forced arbitration at a "
            "fraction of the rate they win in court. Adversarial review: industry will rewrite "
            "arbitration clauses to evade prohibition while preserving outcomes; 'voluntary' "
            "arbitration may be made conditions of employment; this rule requires congressional "
            "legislation to override FAA preemption."
        ),
    },
    "CIVL-0003": {
        "notes": (
            "In Wal-Mart Stores, Inc. v. Dukes, 564 U.S. 338 (2011), the Supreme Court "
            "significantly raised the bar for class certification. In Comcast Corp. v. Behrend, "
            "569 U.S. 27 (2013), the Court made it harder to certify classes where individual "
            "damages calculations differ. These decisions have dramatically reduced certified "
            "class actions in employment, consumer, and civil rights contexts. Adversarial "
            "review: class action preservation without adequate legal resources to bring class "
            "cases is hollow; cy pres settlements — where funds go to third parties rather than "
            "class members — may not serve harmed individuals."
        ),
    },
    "CIVL-0004": {
        "notes": (
            "In Boddie v. Connecticut, 401 U.S. 371 (1971), the Supreme Court held that the "
            "state may not deny access to divorce proceedings because of inability to pay court "
            "fees. Research consistently finds that court filing fees are the largest single "
            "barrier to civil justice access for low-income people; a fee of $50–$200 is "
            "prohibitive for many. Adversarial review: fee waiver processes can be made so "
            "procedurally complex that eligible applicants are deterred; automatic fee "
            "assessment systems may not route people to waiver processes; courts may charge "
            "reduced fees that are still unaffordable; waiver must be available on simple "
            "demonstration of low income, not by complex petition."
        ),
    },
    # ------------------------------------------------------------------ CONS --
    "CONS-0001": {
        "notes": (
            "In Estelle v. Gamble, 429 U.S. 97 (1976), the Supreme Court held that deliberate "
            "indifference to serious medical needs of prisoners violates the Eighth Amendment. "
            "In Brown v. Plata, 563 U.S. 493 (2011), the Court upheld an order requiring "
            "California to reduce its prison population because inadequate healthcare caused "
            "needless suffering and death. Approximately 43% of state prisoners have a current "
            "mental health diagnosis; nearly 40% have a chronic physical health condition. "
            "Adversarial review: 'adequate' healthcare has been interpreted minimally by courts "
            "deferring to corrections officials; telemedicine substitutes may not meet "
            "constitutional standards for serious conditions; healthcare cost pressure produces "
            "systematic underdiagnosis of conditions that would require treatment."
        ),
    },
    "CONS-0002": {
        "notes": (
            "The United Nations Special Rapporteur on Torture concluded that solitary "
            "confinement exceeding 15 days can constitute cruel, inhuman, or degrading treatment "
            "prohibited under international law. Research shows that even short-term solitary "
            "confinement causes or worsens psychotic episodes, PTSD, depression, and increases "
            "suicide risk. In Madrid v. Gomez, 889 F. Supp. 1146 (N.D. Cal. 1995), the court "
            "found that placing mentally ill prisoners in isolation violated the Eighth "
            "Amendment. Adversarial review: relabeling practices — 'administrative segregation,' "
            "'protective custody,' 'restrictive housing' — can replicate solitary confinement "
            "without triggering formal restrictions; facilities may increase short-duration uses "
            "to evade 'prolonged' thresholds; independent inspection is required because "
            "facilities self-report usage."
        ),
    },
    "CONS-0003": {
        "notes": (
            "Approximately 20% of people in state prisons meet criteria for a serious mental "
            "illness. People with mental illness in custody are significantly more likely to "
            "receive disciplinary sanctions for behavior that is symptomatic of their illness "
            "rather than receiving clinical intervention. This practice constitutes both cruel "
            "treatment and a failure of basic medical care obligations under Estelle v. Gamble. "
            "Adversarial review: requiring mental health treatment without adequate staffing "
            "creates paper compliance with no clinical substance; criminalization of mental "
            "illness symptoms is often worse at county jails than state prisons, and reforms "
            "must reach jails; 'treatment' requirements can be satisfied by medication "
            "administration without therapeutic programming."
        ),
    },
    "CONS-0004": {
        "notes": (
            "In Pennsylvania Department of Corrections v. Yeskey, 524 U.S. 206 (1998), the "
            "Supreme Court held unanimously that the ADA applies to state prisons. Despite this "
            "ruling, DOJ investigations have found systematic ADA failures in prisons and jails "
            "including inadequate wheelchair access, denial of sign language interpretation, and "
            "failure to provide accessible programming. Adversarial review: 'reasonable "
            "accommodation' in the correctional context is interpreted more narrowly than in "
            "community settings, with security justifications frequently used to deny "
            "accommodations that would be required elsewhere; ADA compliance requires investment "
            "that many facilities resist absent lawsuit or DOJ action."
        ),
    },
    "CONS-0005": {
        "notes": (
            "No federal agency is required to independently inspect all correctional facilities. "
            "State prison systems are largely self-inspecting; local jails are often entirely "
            "unmonitored. COVID-19 killed at least 3,000 people in U.S. prisons and jails — a "
            "death rate four times higher than the general population — partly because conditions "
            "were hidden from external oversight. Adversarial review: inspections without "
            "authority to impose consequences produce symbolic oversight; advance notice enables "
            "Potemkin compliance; reports without public accessibility have no accountability "
            "effect; facilities may avoid inspection by limiting the definition of what "
            "facilities require oversight."
        ),
    },
    # ------------------------------------------------------------------ CRTS --
    "CRTS-0001": {
        "notes": (
            "Access to Justice research consistently finds that 80% of civil legal needs go "
            "unmet, and that procedural complexity — not just cost — is a primary barrier. "
            "Self-represented litigants lose cases at significantly higher rates than represented "
            "parties even when their substantive positions are equally strong. Adversarial "
            "review: 'intelligibility' requirements may be satisfied by simplified brochures "
            "while proceedings remain inaccessible; there is no clear enforcement mechanism when "
            "courts fail intelligibility standards; intelligibility for defendants in criminal "
            "proceedings requires resources that courts have resisted funding."
        ),
    },
    "CRTS-0002": {
        "notes": (
            "Research by the National Center for Access to Justice shows that employment "
            "conflicts, transportation barriers, and disability together account for the majority "
            "of missed court appearances that lead to default judgments, bench warrants, and "
            "contempt findings. These consequences disproportionately fall on low-income "
            "defendants. Adversarial review: accommodation processes inconsistently granted "
            "across individual judges create unpredictable access; flexible scheduling systems "
            "designed without this requirement may create perverse incentives to limit "
            "accommodations; remote access technologies may impose costs or technical barriers "
            "on those they are designed to help."
        ),
    },
    "CRTS-0003": {
        "notes": (
            "Research during and after COVID-19 expansion of remote proceedings shows measurable "
            "effects on outcomes: remote participants are perceived as less credible by "
            "fact-finders, have more difficulty communicating with counsel in real time, and "
            "receive worse outcomes in credibility-dependent proceedings. The benefits of remote "
            "access — reduced transportation and work-conflict barriers — are real and must be "
            "preserved while due process risks are mitigated. Adversarial review: courts have "
            "strong cost incentives to expand remote proceedings regardless of due process "
            "effects; the distinction between access improvement and quality reduction is "
            "contested; courts need specific standards, not general principles."
        ),
    },
    "CRTS-0004": {
        "notes": (
            "Automatic default judgments for missed deadlines, bench warrants for missed "
            "hearings, and failure-to-appear charges are structural traps that convert procedural "
            "failures into criminal liability. Research by Matthew Desmond shows that 90% of "
            "Milwaukee eviction cases ended in default judgments, primarily because tenants did "
            "not know how to respond to summons. Adversarial review: reducing automatic "
            "procedural consequences may reduce incentives for timely participation; courts rely "
            "on defaults for administrative efficiency; 'reducing procedural traps' without "
            "specific rules produces no concrete requirements."
        ),
    },
    # ------------------------------------------------------------------ DEFS --
    "DEFS-0001": {
        "notes": (
            " Adversarial review: Gideon v. Wainwright, 372 U.S. 335 (1963) established the "
            "right to counsel but not what constitutes adequate representation. Strickland v. "
            "Washington, 466 U.S. 668 (1984) set a two-prong adequacy test that courts apply so "
            "deferentially that ineffective assistance claims succeed in only a fraction of "
            "cases. The ABA recommends maximum caseloads of 150 felonies or 400 misdemeanors "
            "per year; many public defenders carry two to four times those loads. Gaps: right "
            "to counsel does not automatically extend to all post-conviction proceedings in many "
            "jurisdictions; loophole: courts may appoint counsel so late in proceedings that "
            "adequate preparation is impossible while satisfying formal appointment requirements."
        ),
        "append": True,
    },
    "DEFS-0002": {
        "notes": (
            "Research by the Brennan Center for Justice found that prosecution offices typically "
            "have three to four times the staffing and resource levels of public defense offices "
            "in the same jurisdiction. State funding structures that rely on local county budgets "
            "for public defense systematically underfund it relative to prosecution, which often "
            "benefits from federal grants and forfeitures. Adversarial review: 'parity' can be "
            "defined procedurally (same budget per case) while obscuring structural advantages "
            "that are not cost-based; parity requirements without ongoing monitoring and "
            "enforcement revert to baseline underfunding; federal mandates on state criminal "
            "procedure funding face federalism challenges."
        ),
    },
    "DEFS-0003": {
        "notes": (
            "Brady v. Maryland, 373 U.S. 83 (1963) requires disclosure of material exculpatory "
            "evidence; 'materiality' is not determined until after trial — a standard that "
            "permits withholding pre-trial evidence that turns out to matter. Open-file discovery "
            "policies in some jurisdictions have improved compliance but remain voluntary. "
            "Adversarial review: 'timely' is legally undefined — disclosure on the eve of trial "
            "satisfies Brady if the defense could still use the information; prosecution controls "
            "both evidence and timing of disclosure; expert resources in public defense systems "
            "are severely under-resourced relative to what is needed to analyze complex "
            "discovery."
        ),
    },
    "DEFS-0004": {
        "notes": (
            "The Speedy Trial Act, 18 U.S.C. § 3161, sets strict time limits for federal "
            "prosecutions; state equivalents vary in stringency. Research shows that delay is "
            "routinely used strategically — by prosecution to increase plea pressure on "
            "defendants held in pretrial detention, for whom each additional day represents "
            "coercive pressure to plead guilty. Adversarial review: speedy trial waivers "
            "obtained from detained defendants facing bail-related coercion may not be genuinely "
            "voluntary; courts have broad discretion to find 'excludable' time that delays the "
            "speedy trial clock; 'procedural delay' and legitimate case complexity are difficult "
            "to distinguish in individual cases."
        ),
    },
    "DEFS-0005": {
        "notes": (
            "The 2009 NAS report Strengthening Forensic Science in the United States found that "
            "hair analysis, bite-mark comparison, shoe print analysis, and blood spatter analysis "
            "lack sufficient scientific validation for the conclusions routinely presented to "
            "juries. The Innocence Project has documented numerous wrongful convictions based on "
            "false forensic testimony. Adversarial review: challenges to forensic validity "
            "require expert witnesses, creating resource barriers for defense; courts may apply "
            "Daubert's gatekeeping function inadequately, deferring to the prosecution's "
            "institutional expert relationships; judges are often not equipped to evaluate the "
            "scientific validity of complex forensic methods."
        ),
    },
    "DEFS-0006": {
        "notes": (
            "Brady v. Maryland, 373 U.S. 83 (1963) and Giglio v. United States, 405 U.S. 150 "
            "(1972) require prosecutors to disclose material exculpatory and impeachment "
            "evidence. Research by the Innocence Project identifies Brady violations as present "
            "in 40–50% of documented wrongful convictions. The standard for 'materiality' — "
            "whether the evidence might have changed the outcome — is determined in retrospect "
            "by the same courts that convicted the defendant. Adversarial review: open-file "
            "discovery policies are voluntary and inconsistent; prosecution may withhold evidence "
            "in files not formally labeled as part of the case file; 'continuing' disclosure "
            "obligations are routinely not enforced after trial begins."
        ),
    },
    "DEFS-0007": {
        "notes": (
            "Arizona v. Youngblood, 488 U.S. 51 (1988) held that the government has no "
            "constitutional duty to preserve potentially useful (as opposed to materially "
            "exculpatory) evidence absent bad faith. This gap permits agencies to allow evidence "
            "to deteriorate or be destroyed as long as they cannot be shown to have done so in "
            "bad faith — a standard almost impossible to meet. DNA evidence is routinely "
            "destroyed before post-conviction claims can be brought. Adversarial review: "
            "'negligence' and 'indifference' are difficult to prove; agencies may adopt informal "
            "evidence-destruction policies that technically avoid 'bad faith' findings; retention "
            "is expensive and many agencies lack storage resources, creating systematic evidence "
            "loss without individual accountability."
        ),
    },
    "DEFS-0008": {
        "notes": (
            "In Connick v. Thompson, 563 U.S. 51 (2011), the Supreme Court held that a "
            "municipality is not liable under § 1983 for a Brady violation absent a pattern of "
            "violations — a standard almost impossible to meet. Individual prosecutors face "
            "professional discipline for Brady violations at very low rates. The National "
            "Registry of Exonerations documents Brady violations in approximately 40% of "
            "wrongful convictions. Adversarial review: criminal dismissal as a remedy for Brady "
            "violations benefits defendants in single cases but does not deter future violations; "
            "sanctions against individual prosecutors require judicial willingness to impose "
            "them; structural enforcement mechanisms — automatic case review, mandatory "
            "reporting — are more effective than case-by-case sanctions."
        ),
    },
    "DEFS-0009": {
        "notes": (
            "In Ake v. Oklahoma, 470 U.S. 68 (1985), the Supreme Court held that indigent "
            "defendants have a due process right to psychiatric expert assistance when sanity is "
            "a significant factor. Courts have interpreted Ake narrowly, applying it primarily "
            "to psychiatric experts. Research shows that defendants with independent forensic "
            "expert assistance are significantly more likely to successfully challenge unreliable "
            "forensic evidence. Adversarial review: court-appointed expert funding is often "
            "inadequate; courts have broad discretion to deny expert requests; prosecution "
            "retains structural advantage through government-funded crime labs; 'access' without "
            "specific funding levels and standards produces symbolic rather than meaningful "
            "access."
        ),
    },
    "DEFS-0010": {
        "notes": (
            "Research documents the use of 'litigation snowballs' — large volumes of documents, "
            "motions, and discovery produced close to trial deadlines that defense counsel with "
            "minimal resources cannot adequately review. The Innocence Project and academic "
            "researchers have identified systematic informational asymmetries as a structural "
            "driver of wrongful convictions. Adversarial review: courts have historically been "
            "reluctant to impose sanctions for legitimate-appearing litigation tactics even when "
            "they function to overwhelm defense capacity; what constitutes rewarding surprise "
            "versus legitimate aggressive litigation is subjective; specific rules — timing "
            "requirements, volume limits relative to defense resources — are more enforceable "
            "than general principles."
        ),
    },
    # ------------------------------------------------------------------ DRGS --
    "DRGS-0001": {
        "stmt": (
            "Drug enforcement strategies must transition from criminalization to public health "
            "approaches; mandatory minimum sentences for non-violent drug possession offenses "
            "are prohibited; federal and state funding incentives that reward arrest and "
            "prosecution rates for drug offenses are eliminated."
        ),
        "notes": (
            "The 'war on drugs' intensified by the Anti-Drug Abuse Act of 1986 has produced "
            "approximately 1.3 million drug arrests annually without evidence of sustained "
            "reduction in drug use rates. Portugal's 2001 decriminalization of all personal drug "
            "possession, combined with mandatory health referrals, produced documented decreases "
            "in HIV infection rates, drug-related deaths, and incarceration without increases in "
            "drug use or trafficking. Adversarial review: 'public health approach' without "
            "corresponding healthcare infrastructure creates a framework without capacity; "
            "transition from criminal to health system may produce gaps if both systems are "
            "inadequately funded; law enforcement agencies that lose arrest-metric incentives "
            "may redirect pressure to other offense categories."
        ),
    },
    "DRGS-0002": {
        "stmt": (
            "Possession of controlled substances for personal use may not be treated as a "
            "criminal offense subject to incarceration; personal possession must be addressed "
            "through public health and harm reduction frameworks; treatment referral and harm "
            "reduction services must be funded at levels sufficient to meet demand for everyone "
            "diverted from criminal prosecution."
        ),
        "notes": (
            "Decriminalization of personal drug possession removes criminal penalties for use "
            "and possession while maintaining health system responses. Research on "
            "decriminalization programs in Portugal, Switzerland, and multiple U.S. states shows "
            "no increase in drug use after decriminalization and significant reductions in harm. "
            "The majority of the 1.3 million annual drug arrests in the United States are for "
            "possession, not sale or trafficking. Adversarial review: decriminalization without "
            "adequate treatment infrastructure creates diversion with no destination; 'personal "
            "use' quantities must be defined with sufficient clarity to prevent prosecutors from "
            "charging possession-for-distribution on personal-use quantities; decriminalization "
            "at the federal level while states retain criminal penalties creates a patchwork."
        ),
    },
    "DRGS-0003": {
        "stmt": (
            "Drug enforcement spending must be redirected to treatment, harm reduction, and "
            "prevention services; federal and state funding formulas must prioritize treatment "
            "capacity over arrest and incarceration rates; drug courts must be adequately funded "
            "and structured to divert, not merely delay, criminal prosecution."
        ),
        "notes": (
            "Treatment for substance use disorder is significantly more cost-effective than "
            "incarceration as a public safety strategy: RAND Corporation and the National "
            "Institute on Drug Abuse estimate that every dollar invested in addiction treatment "
            "returns four to seven dollars in reduced drug-related crime, criminal justice costs, "
            "and theft. The majority of people in treatment report that lack of availability — "
            "not lack of desire — was their primary barrier to accessing care. Adversarial "
            "review: redirecting funding requires budget reallocation that faces institutional "
            "resistance from law enforcement agencies dependent on drug enforcement resources; "
            "'treatment' programs that are coercive, punitive, or inadequately funded may worsen "
            "outcomes; drug courts may divert people into long supervision periods with criminal "
            "consequences for treatment failure rather than providing genuine alternatives."
        ),
    },
    "DRGS-0004": {
        "stmt": (
            "Federal and state governments must establish regulatory frameworks for controlled "
            "substances that govern production, distribution, and sale through licensed systems "
            "with safety, quality, and harm reduction standards; criminal prohibition that drives "
            "substances into unregulated markets is prohibited where regulated alternatives can "
            "better protect public safety."
        ),
        "notes": (
            "Regulated substance frameworks — including cannabis legalization in 24 states and "
            "alcohol regulation nationwide — demonstrate that legalization under robust public "
            "health oversight is more effective at controlling quality, reducing illegal market "
            "violence, and targeting use disorder treatment than criminal prohibition. The "
            "fentanyl crisis illustrates the harm produced by unregulated markets: prohibition "
            "drove a shift from regulated pharmaceuticals to illicitly manufactured fentanyl "
            "analogues far more dangerous than the substances they replaced. Adversarial review: "
            "regulated frameworks require substantial administrative infrastructure; licensing "
            "systems can be captured by large commercial operators, disadvantaging harm reduction "
            "approaches; some substances present genuine public safety risks that regulation "
            "alone cannot adequately address."
        ),
    },
    "DRGS-0005": {
        "stmt": (
            "No person may be criminally penalized, arrested, or prosecuted for providing "
            "emergency medical assistance to a person experiencing a drug overdose or for being "
            "the person experiencing the overdose; Good Samaritan protections apply to all "
            "persons present at an overdose scene; law enforcement may not use an overdose call "
            "as a basis to search, arrest, or investigate the person calling for help or any "
            "other person present unless evidence of a separate crime is independently "
            "established."
        ),
        "notes": (
            "Over 100,000 Americans died of drug overdoses in 2022, including approximately "
            "70,000 from synthetic opioids. Research consistently shows that fear of arrest is "
            "the primary reason people do not call 911 during overdoses. Every state has enacted "
            "some form of a Good Samaritan law, but coverage is highly variable: many exclude "
            "protection for callers with prior drug convictions, exclude protection for the "
            "overdose victim, or provide protection only during the 911 call. Adversarial "
            "review: Good Samaritan laws requiring 'good faith' calls are sometimes interpreted "
            "to exclude calls where the caller hesitated; law enforcement may use overdose calls "
            "as investigative opportunities; protection for only the 'first-time caller' creates "
            "perverse incentives not to call after any prior police interaction; full protection "
            "must extend to all persons present regardless of their history."
        ),
    },
    # ------------------------------------------------------------------ EVDS --
    "EVDS-0001": {
        "notes": (
            "The 2009 National Academy of Sciences report Strengthening Forensic Science in "
            "the United States found that the majority of forensic science disciplines lack "
            "adequate scientific validation, peer review, and published error rate data. The "
            "2016 PCAST report specifically found that bite-mark analysis, shoe print analysis, "
            "hair comparison, and blood pattern analysis lack foundational validity at the error "
            "rates routinely implied by expert testimony. Adversarial review: courts continue "
            "admitting questionable forensic methods due to institutional reliance on existing "
            "expert structures; labs resist external validation as costly and threatening to "
            "existing conviction patterns; the 'generally accepted' standard in Frye enables "
            "courts to defer to forensic community self-certification rather than independent "
            "scientific evaluation."
        ),
    },
    "EVDS-0002": {
        "notes": (
            "The FBI acknowledged in 2015 that forensic hair analysis testimony by FBI examiners "
            "was overstated in approximately 95% of reviewed cases involving 32 executions and "
            "268 other convictions. Bite-mark analysis, arson investigation using outdated "
            "chemical indicators, and blood pattern analysis have all produced documented "
            "wrongful convictions. Adversarial review: excluding existing junk science requires "
            "review and potential resentencing of prior convictions based on that science, which "
            "courts are reluctant to undertake; labs and prosecutors who built careers on these "
            "methods resist exclusion; 'exclusion' from future proceedings does not address "
            "thousands of people currently imprisoned based on now-discredited methods."
        ),
    },
    "EVDS-0003": {
        "notes": (
            "Chain-of-custody failures — breaks in the documented record of who had access to "
            "evidence — have contributed to wrongful convictions and provide grounds for evidence "
            "exclusion. Digital evidence chain-of-custody is increasingly important and "
            "inadequately standardized: metadata tampering, unauthorized copying, and device "
            "access without documentation are documented problems. Adversarial review: "
            "chain-of-custody documentation requirements can be nominally satisfied while actual "
            "custodial integrity is compromised; rules without effective sanctions for "
            "non-compliance are advisory only; digital evidence chain-of-custody involves "
            "complex technical questions that many courts are not equipped to evaluate."
        ),
    },
    "EVDS-0004": {
        "notes": (
            "Deepfakes and AI-generated audio, video, and text are now indistinguishable from "
            "authentic recordings to unaided human perception. A 2023 study found that humans "
            "could identify AI-generated faces only approximately 50% of the time — no better "
            "than chance. Courts have no established standards for verifying the authenticity of "
            "digital evidence. Adversarial review: verification requirements may be outpaced by "
            "the speed of AI development; the obligation to verify must include a specific "
            "standard — peer-reviewed authentication methodology, not vendor certification; "
            "courts may not have technical resources to evaluate authentication claims "
            "independently; authenticated synthetic evidence used as demonstrative exhibits "
            "requires the same disclosure standards as evidence."
        ),
    },
    "EVDS-0005": {
        "notes": (
            "The discovery that forensic arson investigation was based on false fire science "
            "resulted in post-conviction review in multiple states; Texas created a Forensic "
            "Science Commission to review cases affected by discredited methods — the first "
            "state to do so. Similar reviews have occurred in hair analysis cases after the "
            "FBI's 2015 admission. Adversarial review: retroactive review programs are "
            "resource-intensive and most jurisdictions lack capacity; post-conviction review is "
            "limited by procedural bars and finality doctrines; the burden must be on the state "
            "to initiate review of its own cases when methods are discredited, not solely on "
            "individual prisoners to bring claims."
        ),
    },
    # ------------------------------------------------------------------ FFFS --
    "FFFS-0001": {
        "notes": (
            "DOJ's 2015 investigation of the Ferguson, Missouri police department documented "
            "that Ferguson used traffic fines and misdemeanor fees as a primary revenue source, "
            "generating 23% of city revenue in fiscal year 2013. People who cannot pay small "
            "fines face escalating consequences — license suspension, bench warrants, jail time "
            "— that can destroy employment and housing stability. Adversarial review: the "
            "primary driver of fine and fee revenue extraction is fiscal pressure on local "
            "governments; eliminating fine revenue without providing alternative local government "
            "funding creates structural pressure that may recreate the problem; jurisdictions "
            "facing revenue crises will resist these limits without replacement revenue."
        ),
    },
    "FFFS-0002": {
        "notes": (
            "In Bearden v. Georgia, 461 U.S. 660 (1983), the Supreme Court held that revoking "
            "probation solely because of inability to pay — without considering alternatives — "
            "violates the Equal Protection Clause. Despite this, incarceration for failure to "
            "pay fines and fees continues in many jurisdictions. Adversarial review: "
            "ability-to-pay assessments can be designed to find most people 'able to pay' at "
            "reduced amounts; assessment processes can create administrative burdens that deter "
            "people from requesting waivers; without enforcement mechanisms, assessment "
            "requirements become advisory."
        ),
    },
    "FFFS-0003": {
        "notes": (
            "In Tate v. Short, 401 U.S. 395 (1971), the Supreme Court held that a state cannot "
            "imprison a person solely for failure to pay a fine if they lack the means to do so. "
            "Despite this ruling, debtors' prison practices persist through bench warrants for "
            "missed court dates related to unpaid fines, probation revocation for non-payment, "
            "and contempt proceedings. Adversarial review: the formal prohibition is circumvented "
            "by treating non-payment as violation of a probation condition, which permits "
            "incarceration for the 'condition violation' rather than for non-payment per se; "
            "this loophole has been sustained by courts in many jurisdictions."
        ),
    },
    "FFFS-0004": {
        "notes": (
            "Research by the Brennan Center documents that late fees, interest charges, and "
            "administrative fees in justice-related debt can cause a $100 fine to balloon to "
            "thousands of dollars, creating debt that is impossible to pay and that follows "
            "people for life. DMV-related license suspension for unpaid fines affects 7 million "
            "Americans and creates barriers to employment that compound inability to pay. "
            "Adversarial review: caps on compounding charges without caps on underlying fines "
            "can still produce unaffordable outcomes; 'strictly limited' is not actionable "
            "without specific dollar limits or formulas; jurisdictions dependent on fee revenue "
            "will resist these limits."
        ),
    },
    "FFFS-0005": {
        "notes": (
            "The Brennan Center documents that low-income defendants in many jurisdictions are "
            "not informed of waiver options, income-based payment alternatives, or community "
            "service substitution — options that exist in many jurisdictions but are not "
            "proactively offered. Research shows that provision of accessible, proactively "
            "offered alternatives reduces defaults and associated collateral consequences. "
            "Adversarial review: community service alternatives must be practically accessible "
            "— not require weekday travel or impose requirements incompatible with work and "
            "caregiving; waiver processes must not require documentation that people experiencing "
            "poverty may not have; 'accessible' must be defined with specific procedural "
            "requirements."
        ),
    },
    "FFFS-0006": {
        "notes": (
            "The DOJ's 2015 Ferguson report documented the conflict of interest created when "
            "courts and law enforcement depend on fines and fees for operating revenue: it "
            "creates structural incentives to fine more people for more offenses at higher rates "
            "regardless of public safety rationale. Civil asset forfeiture generates hundreds "
            "of millions in annual revenue to law enforcement agencies, creating parallel "
            "revenue-extraction incentives. Adversarial review: eliminating revenue from fines "
            "without replacing it requires alternative funding that many local governments cannot "
            "identify; this rule faces strong fiscal resistance; 'core operating revenue' is "
            "ambiguous — any dependence on fine or forfeiture revenue creates distorting "
            "incentives."
        ),
    },
    # ------------------------------------------------------------------ IMMS --
    "IMMS-0001": {
        "notes": (
            "The United States maintains one of the largest immigration detention systems in "
            "the world, with approximately 34,000 people detained on any given day. Unlike "
            "criminal detention, immigration detention lacks statutory time limits, and "
            "individuals can be held for months or years awaiting adjudication. The Supreme "
            "Court held in Zadvydas v. Davis, 533 U.S. 678 (2001) that indefinite civil "
            "detention raises serious constitutional concerns. Adversarial review: immigration "
            "detention operates largely outside the constitutional protections that apply to "
            "criminal detention; private detention facilities are excluded from many oversight "
            "frameworks; statutory limits can be circumvented by administrative re-designation "
            "of proceedings."
        ),
    },
    "IMMS-0002": {
        "notes": (
            "Only 37% of people in immigration court have legal representation, according to "
            "DOJ data. Unrepresented immigrants are five times less likely to succeed in "
            "immigration court. Unlike criminal proceedings, there is no constitutional right "
            "to appointed counsel in immigration proceedings, which are civil in nature. "
            "Adversarial review: the right to retain counsel at one's own expense does not "
            "provide meaningful access for detained, low-income, or non-English-speaking "
            "respondents; 'meaningful access' to counsel requires funding — right without "
            "funding produces nominal but not actual access; interpretation quality in "
            "immigration proceedings is variable, and misinterpretation has caused wrongful "
            "deportation."
        ),
    },
    "IMMS-0003": {
        "notes": (
            "The Trump administration's 'zero tolerance' policy (2018) resulted in more than "
            "5,400 children being separated from parents at the southern border. Medical and "
            "psychological research documents severe, long-lasting harm to children separated "
            "from parents — including elevated rates of PTSD, depression, and developmental "
            "harm. Many families were not reunited for months; in some cases, parents were "
            "deported without their children. Adversarial review: 'narrowly defined and "
            "reviewable conditions' is a flexible standard that may be interpreted broadly; "
            "family separation as a deterrence strategy — using family harm as leverage — must "
            "be expressly prohibited regardless of stated operational justification; oversight "
            "requires real-time reporting, not after-the-fact review."
        ),
    },
    # ------------------------------------------------------------------ JUVS --
    "JUVS-0001": {
        "notes": (
            "Research on adolescent brain development establishes that the adolescent brain is "
            "not fully developed in regions governing impulse control and long-term consequence "
            "assessment until the mid-20s. This scientific consensus underpins Roper v. "
            "Simmons, 543 U.S. 551 (2005) (prohibiting juvenile death penalty), Graham v. "
            "Florida, 560 U.S. 48 (2010) (prohibiting LWOP for non-homicide juveniles), and "
            "Miller v. Alabama, 567 U.S. 460 (2012). Rehabilitation-focused approaches show "
            "significantly lower recidivism rates than punitive approaches for youth. "
            "Adversarial review: 'rehabilitation-focused' systems must be adequately funded to "
            "provide educational, therapeutic, and developmental services; relabeling punishment "
            "as 'treatment' creates systems that are punitive in practice; juvenile facilities "
            "may prioritize security over rehabilitation due to liability concerns."
        ),
    },
    "JUVS-0002": {
        "notes": (
            "Adult sentences for juveniles have been the subject of a series of Supreme Court "
            "cases limiting their scope through Roper, Graham, Miller, and Jones v. "
            "Mississippi, 593 U.S. 535 (2021). Despite these limits, children continue to be "
            "tried as adults under transfer statutes in all 50 states. Transferring youth to "
            "adult court exposes them to adult prison conditions, adult criminal records, and "
            "adult sentencing ranges. Adversarial review: 'extremely narrow conditions' for "
            "adult sentencing must include specific procedural requirements — individualized "
            "finding, age-appropriate hearing, qualified evaluation — not just general judicial "
            "discretion; transfer statutes that lower the age for automatic adult prosecution "
            "must be subject to constitutional scrutiny that currently varies by state."
        ),
    },
    "JUVS-0003": {
        "notes": (
            "Juvenile records — even dismissed charges, arrests without conviction, and "
            "proceedings from early childhood — create lifelong employment, housing, and "
            "professional licensing barriers. Petition-based sealing processes exist in most "
            "states but require legal knowledge, fees, and navigation that are systematically "
            "unavailable to the same young people most affected. Research shows that "
            "background-check systems frequently include sealed juvenile records in violation of "
            "sealing orders, because aggregators and third-party databases do not automatically "
            "honor court-ordered seals. Adversarial review: automatic sealing must include "
            "mechanisms to purge records from third-party databases; background check systems "
            "must have enforceable obligations to honor sealing; exceptions for dangerous "
            "offenses must be defined specifically to prevent exception-swallowing-the-rule "
            "dynamics."
        ),
    },
    "JUVS-0004": {
        "notes": (
            "Research by the Annie E. Casey Foundation documents that youth in correctional "
            "custody frequently receive inadequate educational services, experience high rates "
            "of abuse, and have poor mental health outcomes. The Juvenile Justice and "
            "Delinquency Prevention Act requires states to comply with core protections as a "
            "condition of federal funding, but monitoring and enforcement are inadequate. "
            "Adversarial review: 'access to' services does not guarantee quality — monitoring "
            "must assess whether services are therapeutic and educational in substance, not "
            "merely formally available; correctional facilities may prioritize security over "
            "developmental programming; youth confined in adult facilities are legally entitled "
            "to separation from adults but this requirement is inconsistently enforced."
        ),
    },
    # ------------------------------------------------------------------ LAWS --
    "LAWS-0001": {
        "notes": (
            "Qualified immunity is a judicially created doctrine — not statutory — created by "
            "the Supreme Court in Harlow v. Fitzgerald, 457 U.S. 800 (1982) and modified in "
            "Pearson v. Callahan, 555 U.S. 223 (2009) to allow courts to dismiss civil rights "
            "cases without ever deciding whether a violation occurred. This creates a catch-22 "
            "where rights cannot be clearly established because cases are dismissed before the "
            "question is answered. Research by Joanna Schwartz (UCLA) found that QI rarely "
            "affects ultimate outcomes — government indemnifies officers in almost all cases — "
            "but it adds procedural barriers that deter meritorious claims. Adversarial review: "
            "abolishing QI requires Congress to act or the Supreme Court to reverse itself; "
            "many states have abolished QI for state-law claims; abolition must specify the "
            "replacement standard — a 'reasonable officer' standard may be too low, while "
            "strict liability may overcorrect."
        ),
    },
    "LAWS-0002": {
        "notes": (
            "Personal liability for civil rights violations has been nearly eliminated by both "
            "QI and the practice of indemnification — governments pay civil judgments in almost "
            "all cases. Research by Schwartz found that individual officers personally paid only "
            "0.02% of dollars in civil rights judgments. Institutional accountability — police "
            "department liability — is also difficult: Monell v. Department of Social Services, "
            "436 U.S. 658 (1978) requires showing a municipal policy or custom caused the "
            "violation. Adversarial review: 'personal accountability' may create chilling "
            "effects on aggressive but lawful policing if not balanced with adequate "
            "indemnification for good-faith conduct; institutional accountability requires "
            "identifying a policy or custom, which protects jurisdictions that permit "
            "problematic conduct informally without formal policy adoption."
        ),
    },
    "LAWS-0003": {
        "notes": (
            "The 'clearly established' standard for qualified immunity requires identifying a "
            "prior case with nearly identical facts — a standard so demanding that courts have "
            "found QI applies even for conduct the court acknowledged was a rights violation. "
            "Courts have dismissed cases involving officers shooting fleeing suspects and using "
            "excessive force solely because no court had previously ruled on identical factual "
            "circumstances. Adversarial review: replacing the 'clearly established' standard "
            "requires specifying a different standard; 'reasonably knowable' violations is more "
            "workable but requires consistent application; if any reasonable officer could have "
            "known the conduct was wrong, that should be sufficient for liability; the "
            "replacement standard must not recreate the same practical bar through different "
            "language."
        ),
    },
    "LAWS-0004": {
        "notes": (
            "Municipal indemnification of officers is nearly universal in practice: research "
            "shows governments indemnified officers in 99.98% of civil rights lawsuits. The "
            "combination of QI and universal indemnification eliminates both the legal barrier "
            "and the financial consequence for rights violations. Indemnification policies can "
            "also be used to maintain confidentiality around settlements — prohibiting public "
            "disclosure of misconduct findings as a condition of government payment. Adversarial "
            "review: limiting indemnification for bad-faith conduct requires proving bad faith, "
            "a standard difficult to meet in practice; exposing officers to personal liability "
            "may deter qualified candidates from law enforcement positions; indemnification "
            "limits without changes to underlying QI doctrine may have limited deterrent effect."
        ),
    },
    # ------------------------------------------------------------------ LNGS --
    "LNGS-0001": {
        "notes": (
            "Title VI of the Civil Rights Act of 1964 prohibits discrimination based on "
            "national origin in programs receiving federal funds, which includes denial of "
            "language access. However, federal language access requirements are inconsistently "
            "enforced. Court interpreters are not required in all proceedings: many plea "
            "hearings, arraignments, probation meetings, and jail administrative processes lack "
            "interpretation. Adversarial review: 'qualified' interpreter standards vary by "
            "jurisdiction; remote interpretation may be inadequate for complex proceedings; "
            "courts may use bilingual court staff rather than independent interpreters, creating "
            "accuracy and conflict-of-interest concerns."
        ),
    },
    "LNGS-0002": {
        "notes": (
            "In criminal proceedings, due process requires meaningful participation including "
            "language access. However, in civil and administrative proceedings, many "
            "jurisdictions assess fees for interpretation services. Research shows that fee "
            "barriers for interpretation result in waived interpretation services, producing "
            "waiver of legal rights the person did not understand. Adversarial review: 'cost "
            "barriers' could be eliminated while creating administrative barriers — lengthy "
            "processes, documentation requirements, or advance scheduling — that functionally "
            "limit access; remote interpretation must be provided as equivalent to in-person "
            "interpretation where technically feasible."
        ),
    },
    "LNGS-0003": {
        "notes": (
            "Courts have found language access failures to be 'harmless error' even when "
            "defendants could not understand charges against them or the rights they were "
            "waiving. A guilty plea entered without understanding is constitutionally defective, "
            "but courts have upheld pleas entered through inadequate interpretation in many "
            "jurisdictions. Adversarial review: the 'harmless error' standard is applied by the "
            "same courts that permitted the error; determining what 'impairs understanding' "
            "requires retrospective assessment of comprehension that courts will resolve against "
            "defendants; structural solutions — mandatory qualified interpretation — are more "
            "effective than case-by-case harmless error review."
        ),
    },
    "LNGS-0004": {
        "notes": (
            "Google Translate and similar automated tools produce error rates of 5–15% in "
            "technical legal texts, with higher error rates for less-common languages. Legal "
            "translation requires not only linguistic accuracy but understanding of legal "
            "concepts — errors in translating terminology can result in a defendant agreeing to "
            "something they did not understand. Adversarial review: 'may not rely solely on "
            "automated translation' requires a standard for when human interpretation is "
            "required; cost pressures push courts toward automated tools; the standard must "
            "specify human interpreter requirements for specific proceeding types, not leave it "
            "to judicial discretion."
        ),
    },
    "LNGS-0005": {
        "notes": (
            "Research by the National Center for Access to Justice shows that language-access "
            "needs are frequently unidentified at intake: defendants who fear immigration "
            "consequences for disclosing language needs, or lack knowledge of available "
            "services, do not self-identify. Court systems that rely on self-identification miss "
            "the people most in need of language access. Adversarial review: proactive "
            "identification requires training and resources that many underfunded courts lack; "
            "systemic intake processes must standardize language identification without creating "
            "stigma or immigration reporting risk for those identified."
        ),
    },
    # ------------------------------------------------------------------ OVRG --
    "OVRG-0001": {
        "notes": (
            " Adversarial review: standardized data requirements can be satisfied by data that "
            "is technically comparable but practically unusable — lack of meaningful definitions, "
            "inconsistent categorization, or formats that prevent analysis; data publication "
            "without analysis produces raw numbers that obscure rather than reveal patterns; "
            "agencies may use definitional choices to make data appear more favorable; "
            "independent analysis capacity must accompany data publication requirements; data "
            "disaggregated only at agency level may not reveal officer-level or "
            "prosecutor-level patterns that are the most actionable accountability information."
        ),
        "append": True,
    },
    "OVRG-0002": {
        "notes": (
            "The U.S. Sentencing Commission's 2023 data shows Black male defendants receive "
            "sentences 13.4% longer than equivalently situated white male defendants; "
            "disaggregated data makes this disparity visible and measurable. Research by the "
            "Stanford Open Policing Project, using 100 million traffic stops, found statistically "
            "significant racial disparities in stop rates, search rates, and citation rates in "
            "the majority of examined jurisdictions — findings possible only because disaggregated "
            "data was made available for analysis. Adversarial review: disaggregation by officer "
            "and prosecutor is politically contentious but necessary for individual "
            "accountability; categories can be defined at a level of granularity that reveals "
            "nothing; quarterly reporting requirements must include specific minimum data fields, "
            "not leave field definition to agency discretion."
        ),
    },
    "OVRG-0003": {
        "notes": (
            "The Ferguson DOJ investigation was made possible by compelled access to documents "
            "the city would not have provided voluntarily. Research on police accountability "
            "boards shows that access — including subpoena power, access to body camera footage, "
            "access to personnel records, and access to facilities — is the single strongest "
            "predictor of whether oversight bodies produce meaningful accountability. "
            "Adversarial review: 'access' without the ability to compel is not true access; "
            "agencies may delay, restrict, or condition access in ways that defeat its purpose; "
            "oversight bodies need independent legal authority — not simply access on department "
            "sufferance — to conduct genuine investigations."
        ),
    },
    "OVRG-0004": {
        "notes": (
            "Research on police oversight bodies shows that audit findings and recommendations "
            "are routinely ignored absent enforceable follow-up mechanisms. The DOJ consent "
            "decree process — which imposes binding requirements and independent monitoring — "
            "has been shown to produce lasting reform in jurisdictions that remain under "
            "monitoring. Voluntary compliance with non-binding recommendations has a poor track "
            "record in law enforcement accountability contexts. Adversarial review: 'required "
            "to act' without specifying the nature of required action permits compliance theater; "
            "enforcement of action requirements requires oversight of the oversight process; "
            "audit findings that produce meaningful follow-up require political will to impose "
            "real consequences."
        ),
    },
    # ------------------------------------------------------------------ POLC --
    "POLC-0001": {
        "stmt": (
            "Law enforcement agencies may not acquire, possess, or deploy military weapons, "
            "equipment, or vehicles transferred through DoD 1033 or equivalent programs or "
            "purchased commercially to perform the same function; prohibited equipment includes "
            "tracked and armed vehicles, grenade launchers, weaponized aircraft, and equipment "
            "designed primarily for battlefield use; all prohibited equipment currently in law "
            "enforcement possession must be returned, decommissioned, or destroyed within "
            "24 months of enactment."
        ),
        "notes": (
            "The Department of Defense 1033 Program has transferred approximately $7.4 billion "
            "in surplus military equipment to civilian law enforcement agencies since 1997, "
            "including armored vehicles, grenade launchers, and aircraft. A 2014 ACLU report, "
            "'War Comes Home,' found that SWAT deployments increased by more than 1,400% between "
            "the 1970s and 2000s, with 79% of SWAT deployments used to execute search warrants "
            "— primarily for drugs. Research by Jonathan Mummolo at Princeton found that "
            "militarized policing does not improve public safety outcomes but significantly "
            "reduces civilian-police trust. Adversarial review: prohibition must cover commercial "
            "acquisition of functionally equivalent equipment, not just 1033 transfers; agencies "
            "may argue that equipment serves dual-use roles; a prohibited equipment list must be "
            "specific enough to prevent circumvention by relabeling."
        ),
    },
    "POLC-0002": {
        "stmt": (
            "Law enforcement agencies must establish and maintain community policing programs "
            "that include consistent geographic beat assignment, community liaison roles, and "
            "structured non-enforcement engagement with residents; community policing must be "
            "implemented as a structural practice, not an optional or supplemental program, and "
            "must be funded and staffed at levels sufficient to reach all communities within "
            "the jurisdiction."
        ),
        "notes": (
            "Community policing programs — when implemented substantively — are associated with "
            "improved trust between officers and residents, increased crime reporting, and better "
            "public safety outcomes. The CAHOOTS (Crisis Assistance Helping Out On The Streets) "
            "model in Eugene, Oregon — operating since 1989 — demonstrates that non-enforcement "
            "community crisis response can handle a significant percentage of 911 calls without "
            "police involvement. Adversarial review: 'community policing' has been applied as a "
            "label to programs that do not meaningfully change policing practices; officer "
            "resistance and evaluation metrics that reward arrests undermine implementation; "
            "community policing must be evaluated on community trust outcomes, not just program "
            "participation."
        ),
    },
    "POLC-0003": {
        "stmt": (
            "Law enforcement agencies must provide officers with mandatory access to confidential "
            "mental health support, including trauma-informed therapy, peer support programs, and "
            "crisis counseling; mental health care must be provided without career penalty and "
            "may not be used as the basis for adverse employment action absent an independent, "
            "documented fitness-for-duty concern; agencies must fund and staff mental health "
            "programs at levels sufficient to meet demonstrated need."
        ),
        "notes": (
            "Law enforcement officers experience elevated rates of PTSD, depression, and suicide "
            "compared with the general population; research by the Blue H.E.L.P. organization "
            "documents that officer suicides have exceeded line-of-duty deaths in recent years. "
            "Untreated officer trauma correlates with excessive force, poor judgment in crisis "
            "situations, and early career exit. Research shows that destigmatizing care-seeking "
            "— by decoupling mental health treatment from career consequences — is the most "
            "important factor in improving utilization rates. Adversarial review: mandatory "
            "mental health programs without confidentiality protections are not used; "
            "fitness-for-duty evaluation authority, if misapplied, could discipline officers for "
            "seeking care; peer support programs led by officers may inadequately address serious "
            "clinical needs."
        ),
    },
    "POLC-0004": {
        "stmt": (
            "Mental health crises, behavioral health emergencies, and calls primarily involving "
            "substance use must be routed to trained civilian crisis responders rather than armed "
            "law enforcement as a default response; law enforcement may be requested to provide "
            "backup where a genuine safety threat is present; jurisdictions must fund and staff "
            "civilian crisis response programs at levels sufficient to respond to all qualifying "
            "calls within service-level standards comparable to emergency police response."
        ),
        "notes": (
            "Approximately 25% of people killed by police have a mental health condition. "
            "Research on co-responder and alternative response models — including CAHOOTS in "
            "Eugene, Oregon (1989), the STAR program in Denver, Colorado, and the CARE program "
            "in Oakland, California — demonstrates that trained civilian responders can safely "
            "handle 96–99% of behavioral health emergency calls without police involvement. "
            "Adversarial review: crisis response programs that lack 24/7 coverage default to "
            "police response during off-peak hours; 'backup' carve-outs can expand to swallow "
            "the default rule if not tightly defined; civilian crisis workers face safety risks "
            "in environments where police presence is unavailable; funding crisis response must "
            "not result in reduced law enforcement response capacity for genuine violent "
            "emergencies."
        ),
    },
    "POLC-0005": {
        "stmt": (
            "Law enforcement officers may not use race, ethnicity, national origin, religion, "
            "or immigration status as a factor in decisions to stop, detain, question, search, "
            "or arrest any person; agencies must collect and publicly report the race, ethnicity, "
            "gender, and age of every person stopped, searched, or arrested on a monthly basis; "
            "officers found to have engaged in racial profiling must face investigation and "
            "enforceable consequences including suspension, termination, and civil liability."
        ),
        "notes": (
            "In Terry v. Ohio, 392 U.S. 1 (1968), the Supreme Court authorized stops based on "
            "'reasonable articulable suspicion' — a standard that courts have allowed to "
            "incorporate race in combination with other factors. In Floyd v. City of New York, "
            "959 F. Supp. 2d 540 (S.D.N.Y. 2013), the court found that the NYPD's "
            "stop-and-frisk program constituted a pattern of unconstitutional racial stops — "
            "85% Black and Latino, 88% resulting in no further action. The Stanford Open "
            "Policing Project documented similar patterns across 100 million traffic stops "
            "nationally. Adversarial review: 'pretext' stops that use minor traffic violations "
            "to provide legal cover for race-based investigations are difficult to prohibit "
            "without evidence of the underlying motivation; data collection creates "
            "accountability only if analyzed and acted on; banning racial profiling in formal "
            "policy while evaluating officers on arrest metrics creates structural pressure to "
            "profile."
        ),
    },
    "POLC-0006": {
        "stmt": (
            "Law enforcement officers may not carry, possess, or deploy automatic weapons or "
            "semi-automatic rifles with military-style features during regular civilian policing "
            "duties; these weapons may not be acquired through military equipment transfer "
            "programs or commercial purchase for standard patrol or enforcement operations; "
            "limited exceptions apply to specialized response units for documented active threat "
            "situations under strict protocols with mandatory review."
        ),
        "notes": (
            "Automatic and military-style weapons in civilian law enforcement create escalation "
            "risks in situations that would otherwise be resolved without lethal force. The "
            "militarized appearance and capability of law enforcement equipped with these weapons "
            "has been documented to reduce public trust and community cooperation. "
            "Cross-referenced with the gun policy pillar: arguments for civilian firearm "
            "restrictions apply with equal or greater force to law enforcement agencies that are "
            "not constitutionally required to arm patrol officers with military-grade weaponry. "
            "Adversarial review: 'limited exceptions' for specialized units may expand in "
            "practice; definitions of 'military-style features' must be specific to prevent "
            "circumvention; prohibition must include training protocols that reinforce "
            "de-escalation rather than force-first response."
        ),
    },
    "POLC-0007": {
        "stmt": (
            "Law enforcement agencies may not acquire, possess, or deploy weapons designed for "
            "military combat including explosive devices, grenade launchers, weaponized "
            "surveillance drones, offensive armored vehicles with mounted weapons, and "
            "battlefield-grade crowd control weapons; these prohibitions apply equally to "
            "acquisition through military transfer programs and commercial purchase; existing "
            "prohibited weapons must be decommissioned within 24 months."
        ),
        "notes": (
            "Military weapons in civilian law enforcement have been used in the policing of "
            "protests, raids, and community enforcement operations in ways that produce "
            "documented harm, destroy community trust, and violate civil rights. The 2014 ACLU "
            "'War Comes Home' report documented SWAT teams using armored vehicles, battering "
            "rams, and flash-bang grenades in routine drug enforcement operations against "
            "non-violent suspects. Cross-referenced with the gun policy pillar: the distinction "
            "between civilian law enforcement and military operations is a foundational principle "
            "of American constitutional government. Adversarial review: prohibition of offensive "
            "armored vehicles while permitting defensive ones requires specific technical "
            "definitions; 'weapons of war' must be defined by function, not solely by formal "
            "military designation, to prevent circumvention through commercial acquisition."
        ),
    },
    "POLC-0008": {
        "stmt": (
            "Where a law enforcement situation genuinely requires military-grade capabilities, "
            "the National Guard under gubernatorial activation through proper civilian command "
            "authority is the required deployment mechanism; local law enforcement agencies may "
            "not acquire military equipment commercially or through transfer programs as a "
            "substitute for proper National Guard activation; deployment of National Guard units "
            "requires written civilian authorization, time limits, documented objectives, and "
            "post-deployment review."
        ),
        "notes": (
            "The Posse Comitatus Act (1878) prohibits the use of federal military forces in "
            "domestic law enforcement; the National Guard is exempt from this prohibition when "
            "activated by a governor, preserving civilian command control over military-type "
            "response to domestic situations. This distinction ensures that military capabilities "
            "in domestic situations remain under civilian political accountability rather than "
            "permanent operational possession of law enforcement agencies. Research on National "
            "Guard deployments during civil unrest shows that proper activation with clear "
            "objectives and civilian oversight produces better outcomes than deployment of "
            "locally militarized police. Adversarial review: National Guard deployment under "
            "federal Title 10 authority bypasses the gubernatorial command chain and the civilian "
            "accountability it provides; the threshold for requiring military-grade capabilities "
            "must be high enough to prevent normalization of military response; post-deployment "
            "review must examine whether deployment was justified and proportionate."
        ),
    },
    "POLC-0009": {
        "stmt": (
            "Law enforcement officers must complete a minimum of 40 hours per year of "
            "non-enforcement community engagement in the geographic areas they are assigned to "
            "police, as a condition of certification; qualifying activities must build genuine "
            "community relationships and are distinct from enforcement duties; agencies must "
            "report annually on compliance and community engagement outcomes."
        ),
        "notes": (
            "Community policing research consistently identifies relationship building between "
            "officers and residents as the most important determinant of police effectiveness and "
            "public safety outcomes. Officers who have non-enforcement relationships with "
            "community members produce better outcomes in crisis situations, have higher rates of "
            "community cooperation with investigations, and experience lower rates of excessive "
            "force complaints. Adversarial review: 'community service' requirements can be "
            "satisfied by token activities that do not produce genuine relationships; "
            "enforcement-adjacent activities may be relabeled as community engagement; evaluation "
            "must measure community trust outcomes, not merely hours logged; 40 hours is a floor "
            "— agency programs should provide substantially more structured community engagement."
        ),
    },
    # POLC-0010, 0011, 0012 → class/badge change only (already have full content)
    "POLC-0013": {
        "notes": (
            "The DOJ's 2015 Ferguson investigation found that systematic destruction of officer "
            "misconduct records through collective bargaining agreement provisions enabled repeat "
            "offenders to continue policing without accountability. The 'wandering officer' "
            "phenomenon — officers with substantiated misconduct records rehired across "
            "jurisdictions — has been documented by the Washington Post and academic researchers: "
            "at least 85,000 officers nationwide have been credibly accused of misconduct, but "
            "thousands have been rehired without disclosure of prior records. Adversarial "
            "review: officer privacy interests may be asserted against disclosure of misconduct "
            "records under state public records laws; union contract provisions requiring record "
            "destruction are difficult to void without litigation; cross-jurisdictional "
            "disclosure requires a national registry that does not currently exist."
        ),
    },
    "POLC-0014": {
        "notes": (
            "Brady v. Maryland, 373 U.S. 83 (1963) and Giglio v. United States, 405 U.S. 150 "
            "(1972) require prosecutors to disclose evidence material to guilt or punishment, "
            "including witness credibility. Officers with records of dishonesty, evidence "
            "planting, or racial bias are Brady-Giglio material, but disclosure is inconsistent. "
            "In many jurisdictions, officer misconduct records are not routinely provided to "
            "prosecutors, and prosecutors do not maintain systematic Giglio lists. Adversarial "
            "review: 'suppression' of Brady/Giglio material occurs through both active "
            "non-disclosure and systemic failure to inquire; prosecutors may be unaware of "
            "relevant officer misconduct if law enforcement agencies do not proactively share "
            "records; the disclosure obligation must include a systemic investigation "
            "requirement, not just passive disclosure of known information."
        ),
    },
    "POLC-0015": {
        "notes": (
            "Research by the Buffalo News found that dozens of New York police officers found "
            "lying under oath continued working as officers; many continued to provide testimony "
            "in criminal cases. The 'testilying' phenomenon — police officers lying under oath "
            "— has been documented by researchers including Jerome Skolnick and in the work of "
            "district attorneys who maintain Giglio lists. Officers with substantiated dishonesty "
            "findings who continue testifying can corrupt criminal proceedings in ways that "
            "produce wrongful convictions. Adversarial review: 'substantiated' misconduct is "
            "rarely achieved when investigations are conducted internally; decertification "
            "processes vary dramatically by state — some have no decertification authority; "
            "officers decertified in one jurisdiction may be certified in another absent national "
            "coordination."
        ),
    },
    "POLC-0016": {
        "notes": (
            "Police union contracts in many states contain provisions requiring destruction of "
            "discipline records after short periods, confidentiality agreements covering "
            "misconduct settlements, and restrictions on what information can be shared with "
            "civilian oversight bodies or prosecutors. New York's repeal of Civil Rights Law "
            "§ 50-a in 2020 — which had shielded police personnel records from public "
            "disclosure — demonstrated that legislative action can override collective "
            "bargaining-based secrecy. Adversarial review: state laws that preempt municipal "
            "efforts to reform police contracts must be addressed at the state level; "
            "confidentiality provisions in individual misconduct settlement agreements may "
            "persist even after systemic policy changes; the provision must specify which "
            "confidentiality mechanisms are prohibited, not rely on 'secrecy' as a general "
            "category."
        ),
    },
    "POLC-0017": {
        "notes": (
            "A 2020 Associated Press investigation found that over 1,000 officers were hired in "
            "new jurisdictions after being fired or forced to resign for misconduct, including "
            "officers involved in serious civil rights violations. Research by Roger Goldman "
            "documents that police certification is controlled at the state level and that "
            "revocation in one state does not automatically prevent certification in another. "
            "Only a minority of states have comprehensive decertification processes; no national "
            "officer certification database exists. Adversarial review: a national tracking "
            "system requires federal legislation and state cooperation; privacy concerns may "
            "limit the scope of information shared; decertification authority without a "
            "comprehensive tracking system is inadequate; agencies that do not check the "
            "registry before hiring cannot be compelled to do so absent federal funding "
            "conditionality."
        ),
    },
    # ------------------------------------------------------------------ PROS --
    "PROS-0005": {
        "notes": (
            "Prosecutorial charging decisions are among the most consequential and least "
            "transparent decisions in the criminal justice system — largely unreviewable by "
            "courts and subject to almost no external oversight. Research documents that charging "
            "disparities by race are significant and compound through the rest of the justice "
            "system. AI tools marketed to prosecutors — case management systems with built-in "
            "'risk flags' and 'priority scoring' — may systematize charging disparities at scale "
            "without requiring any individual prosecutor to make a consciously biased decision. "
            "Adversarial review: 'accountable human review' can be satisfied by nominal sign-off "
            "with no genuine independent analysis; AI tools that function as filters before a "
            "prosecutor sees a case can influence outcomes without ever becoming subject to "
            "disclosure; the prohibition must define what constitutes 'independent human review' "
            "with specificity — reviewing an AI recommendation is not independent review."
        ),
    },
    # ------------------------------------------------------------------ PRPS --
    "PRPS-0001": {
        "notes": (
            "In Timbs v. Indiana, 586 U.S. 146 (2019), the Supreme Court held that the "
            "Excessive Fines Clause applies to state civil forfeiture proceedings. The Institute "
            "for Justice's 'Policing for Profit' report documented that civil forfeiture "
            "generates over $68 billion annually for law enforcement agencies, including $4.5 "
            "billion through the DOJ equitable sharing program. Many people lose property to "
            "civil forfeiture without being charged with a crime; in many jurisdictions, the "
            "cost of contesting forfeiture exceeds the value of the forfeited property. "
            "Adversarial review: requiring a criminal conviction before permanent forfeiture may "
            "create pressure to pursue criminal charges for the purpose of validating forfeiture; "
            "'clear evidentiary standards' must be specified — preponderance in a civil "
            "proceeding is insufficient given the forfeiture revenue incentive."
        ),
    },
    "PRPS-0002": {
        "notes": (
            "Civil forfeiture proceedings often involve property owners who receive no notice "
            "until after seizure, face burden-shifting rules requiring them to disprove the "
            "government's case, and have no right to appointed counsel. In many jurisdictions, "
            "the value of property seized is less than the cost of retaining counsel to contest "
            "the seizure. Research by the Institute for Justice shows that low-income people and "
            "communities of color are disproportionately targeted for civil forfeiture. "
            "Adversarial review: 'timely review' standards in forfeiture can be satisfied by "
            "preliminary hearings far short of full due process; 'clear evidentiary standards' "
            "must be defined to prevent them from functioning as rubber stamps."
        ),
    },
    "PRPS-0003": {
        "notes": (
            "The DOJ equitable sharing program distributes forfeiture revenue back to the law "
            "enforcement agencies that initiated seizures — creating a direct financial incentive "
            "to seize more property. Research by Marian Williams and colleagues found that law "
            "enforcement agencies seize more property in years when they face budget shortfalls "
            "— evidence of revenue-motivated policing. The Ferguson DOJ report documented "
            "similar patterns at the local level. Adversarial review: eliminating forfeiture as "
            "revenue without providing alternative law enforcement funding creates fiscal "
            "pressure that may recreate the incentive through other means; 'core operating "
            "revenue' is undefined — any dependence on forfeiture revenue creates distorting "
            "incentives."
        ),
    },
    "PRPS-0004": {
        "notes": (
            "Federal civil asset forfeiture allows permanent property seizure based on a "
            "preponderance of evidence standard in a civil proceeding, without a criminal "
            "conviction. The burden in many federal forfeiture actions effectively shifts to the "
            "property owner to affirmatively prove their property is not proceeds of criminal "
            "activity. New Mexico, North Carolina, and several other states have banned civil "
            "asset forfeiture absent conviction at the state level. Adversarial review: "
            "requiring conviction before forfeiture may make forfeiture nearly impossible in "
            "cases involving criminal enterprises where individuals are difficult to convict; "
            "criminal forfeiture as an alternative requires a conviction, which maintains due "
            "process; the carve-out for temporary seizure pending criminal proceedings must be "
            "strictly limited."
        ),
    },
    "PRPS-0005": {
        "notes": (
            "Temporary seizure of property pending criminal proceedings can last years where "
            "cases are complex or delayed. Extended pre-conviction seizure can destroy "
            "businesses, impoverish families, and function as punishment before any finding of "
            "guilt. Federal law permits indefinite asset freezing during prosecution under "
            "18 U.S.C. § 1963. Adversarial review: 'strong evidentiary standards' and 'strict "
            "time limits' must be specified in statute rather than left to judicial discretion; "
            "time limits must be real limits with automatic return obligations, not procedural "
            "milestones that can be extended indefinitely."
        ),
    },
    "PRPS-0006": {
        "notes": (
            "In Krimstock v. Kelly, 306 F.3d 40 (2d Cir. 2002), the Second Circuit found that "
            "due process requires prompt judicial review of vehicle seizures. Despite this, "
            "forfeiture challenge processes in many jurisdictions require hiring counsel in the "
            "jurisdiction where the seizure occurred and involve procedural complexity that is "
            "intentionally or effectively prohibitive. Institute for Justice research shows that "
            "in many jurisdictions, the majority of people whose property is seized never "
            "contest the forfeiture, not because they lack grounds but because the process is "
            "inaccessible. Adversarial review: 'meaningful and accessible' challenge processes "
            "require both procedural reform and waiver of costs; right to challenge without a "
            "right to counsel at government expense in high-value cases is functionally hollow; "
            "jurisdictions have fiscal incentives to make challenges expensive and difficult."
        ),
    },
    # ------------------------------------------------------------------ RECS --
    "RECS-0001": {
        "notes": (
            "Research by the National Reentry Resource Center documents that 70 million "
            "Americans have a criminal record, and that records create barriers to employment in "
            "approximately 75% of job categories, housing in the majority of federally assisted "
            "housing programs, and professional licensing in dozens of fields. These barriers "
            "are disproportionately borne by Black Americans, who have higher rates of criminal "
            "justice contact due to documented enforcement disparities. Adversarial review: "
            "sealing and expungement without enforcement mechanisms — requiring employers, "
            "landlords, and licensing boards to honor seals — produces paper reform; third-party "
            "background check aggregators that do not honor sealing orders must be regulated; "
            "'broad access' to sealing processes is meaningless if processes are prohibitively "
            "expensive, complex, or slow."
        ),
    },
    "RECS-0002": {
        "notes": (
            "Research by J.J. Prescott and Sonja Starr at the University of Michigan found that "
            "only 6.5% of Michigan residents eligible for expungement received it within five "
            "years, despite significant benefits documented by follow-up research. The primary "
            "barrier was procedural complexity — not lack of desire. Automatic expungement "
            "processes in states like Pennsylvania and New Jersey have dramatically increased "
            "expungement rates. Adversarial review: automatic systems must be actively monitored "
            "to catch implementation failures — records that are not purged from all systems as "
            "required; state court systems without modernized records management cannot "
            "implement automatic expungement without infrastructure investment; courts may "
            "resist automatic systems due to administrative burden."
        ),
    },
    "RECS-0003": {
        "notes": (
            "Juvenile adjudications were historically sealed automatically in most states, but "
            "this protection has eroded through exceptions for certain offenses, transfer to "
            "adult court, and technological changes that make records more accessible. Research "
            "documents that juvenile records accessed through background check systems appear "
            "more frequently in employment and housing contexts than they should under legal "
            "sealing requirements. Adversarial review: 'most cases' is ambiguous — specific "
            "offense categories must be defined for both automatic sealing and exceptions; "
            "third-party databases must be regulated and required to purge records on sealing; "
            "the 'extraordinary circumstances' exception must be defined to prevent expansion."
        ),
    },
    "RECS-0004": {
        "notes": (
            "Arrests and dismissed charges create criminal records that appear in background "
            "checks even though no conviction resulted. Research by the National Employment Law "
            "Project found that 90% of employers conduct background checks and many exclude "
            "applicants with arrest records regardless of outcome. An arrest record for a charge "
            "that was dropped, dismissed, or acquitted provides no evidence of guilt but imposes "
            "significant collateral consequences. Adversarial review: sealing dismissals without "
            "clearing them from all databases is inadequate — sealed records reappear through "
            "aggregation; the process for sealing must be immediate and automatic, not dependent "
            "on a post-disposition petition."
        ),
    },
    "RECS-0005": {
        "notes": (
            "A 2021 report by the National Consumer Law Center documented systematic violations "
            "of the Fair Credit Reporting Act by background check companies failing to honor "
            "court-ordered record seals. Research shows that even when individuals have "
            "successfully cleared their records, the records reappear in third-party databases "
            "maintained by data brokers. Adversarial review: federal FCRA enforcement of sealing "
            "compliance requires FTC resources that have not historically been adequate; "
            "state-level enforcement is inconsistent; data brokers argue that public records are "
            "public regardless of court sealing orders — a legal position that must be directly "
            "addressed by statute."
        ),
    },
    "RECS-0006": {
        "notes": (
            "Research by the National Consumer Law Center found that 52% of background check "
            "reports contain inaccurate information; approximately 22% contained charges without "
            "disposition information (showing an arrest without noting it was dismissed or "
            "acquitted). These errors disproportionately harm people of color, who have higher "
            "rates of criminal justice contact. The Fair Credit Reporting Act provides error "
            "correction rights but the process is complex and enforcement is inadequate. "
            "Adversarial review: 'accessible' processes must include specific time limits for "
            "corrections; agencies that fail to correct errors must face enforceable "
            "consequences; the burden of error correction falls entirely on individuals who may "
            "not know how to navigate the system."
        ),
    },
    # ------------------------------------------------------------------ REIS --
    "REIS-0001": {
        "notes": (
            "Research by the Collateral Consequences Resource Center documents over 44,000 "
            "state and federal collateral consequences — statutory restrictions on housing, "
            "employment, licensing, public benefits, and civic participation triggered by "
            "criminal convictions. Many of these restrictions are permanent, applying for life "
            "regardless of time elapsed or rehabilitation. Research by the American Bar "
            "Association shows these restrictions are rarely proportionate to any public safety "
            "rationale. Adversarial review: 'unnecessary' collateral consequences require "
            "individualized review that courts and agencies are not equipped to conduct at scale; "
            "many collateral consequences are imposed by agencies with no notice to the person "
            "affected; the proliferation across thousands of statutes requires comprehensive "
            "legislative audit, not case-by-case reform."
        ),
    },
    "REIS-0002": {
        "notes": (
            "The ABA Criminal Justice Standards on Collateral Sanctions (2004) recommend that "
            "collateral consequences be reviewed for proportionality, necessity, and connection "
            "to legitimate public safety rationale. Few states have conducted such reviews. "
            "Research by David Weiman and others documents that collateral consequences destroy "
            "employment and housing stability, both of which are empirically among the strongest "
            "predictors of recidivism — meaning that excessive collateral consequences may "
            "increase rather than decrease public safety risk. Adversarial review: 'clearly "
            "justified safety needs' is a standard requiring individualized assessment that "
            "administrative agencies are not equipped to apply to thousands of statutes; "
            "legislative audits face resistance from agencies that have built regulatory "
            "frameworks around existing collateral consequences."
        ),
    },
    "REIS-0003": {
        "notes": (
            "Research by the Urban Institute's Justice Policy Center shows that 95% of "
            "incarcerated people will eventually be released. Lack of identification, housing, "
            "healthcare, and employment support at release are the strongest predictors of "
            "re-incarceration within 12 months. The cost of inadequate reentry support — "
            "recidivism, re-prosecution, re-incarceration — far exceeds the cost of adequate "
            "support services. Adversarial review: reentry programs that are underfunded produce "
            "nominal services that do not meet actual needs; identification access is a "
            "prerequisite for housing and employment and is a common but under-resourced reentry "
            "service; healthcare continuity at release — particularly for mental health and "
            "substance use disorder — is the most critical and most underfunded reentry support."
        ),
    },
    "REIS-0004": {
        "notes": (
            "Research consistently shows that housing stability, employment, family connection, "
            "and access to healthcare are the most powerful predictors of successful "
            "reintegration and reduced recidivism — more predictive than surveillance, "
            "monitoring, or graduated sanctions. Policies that impose housing exclusions, "
            "employment exclusions, and civic exclusions reduce the social supports that predict "
            "success. Adversarial review: 'reintegration as a public safety goal' is a values "
            "statement requiring specific policy changes to have effect; the political environment "
            "in many jurisdictions treats post-release hardship as deserved rather than as a "
            "preventable public safety problem; this position requires direct confrontation with "
            "punitive collateral consequence frameworks."
        ),
    },
    # ------------------------------------------------------------------ REVS --
    "REVS-0001": {
        "notes": (
            " Adversarial review: post-conviction review processes are limited by finality "
            "doctrine, successive petition bars, and procedural default rules that make relief "
            "difficult to obtain even with compelling evidence; the Antiterrorism and Effective "
            "Death Penalty Act (AEDPA, 1996) imposed strict limitations on federal habeas corpus "
            "review; loophole: prosecutors may characterize new evidence as 'not newly "
            "available' to bar reopening; gap: people serving sentences without counsel cannot "
            "effectively navigate post-conviction processes; unintended consequence: expanding "
            "post-conviction review requirements without commensurate resources may lengthen "
            "proceedings and delay resolution for all parties."
        ),
        "append": True,
    },
    "REVS-0002": {
        "stmt": (
            "Every jurisdiction must establish an independent post-conviction review mechanism "
            "with authority to accept and investigate claims of innocence based on new evidence, "
            "procedural error, or discredited science; review bodies must have subpoena "
            "authority, access to case files and physical evidence, and the ability to recommend "
            "relief directly to courts; access to review must not depend on ability to pay or "
            "prior exhaustion of other remedies."
        ),
        "notes": (
            "As of 2024, approximately 30 states have established conviction integrity units, "
            "innocence projects, or formal post-conviction review mechanisms, but their "
            "authority, resources, and independence vary significantly. The National Registry of "
            "Exonerations has documented over 3,200 exonerations since 1989. Research shows "
            "that conviction integrity units with prosecutorial independence produce more "
            "exonerations than those that operate within regular case processing structures. "
            "Adversarial review: conviction integrity units within prosecutor offices have an "
            "inherent conflict of interest in reviewing that office's own convictions; "
            "'independence' must mean structural independence, not just administrative "
            "separation; funding must be adequate to investigate the full caseload of credible "
            "claims; jurisdictions without innocence infrastructure remain gaps in the national "
            "post-conviction review system."
        ),
    },
    "REVS-0003": {
        "notes": (
            "The National Registry of Exonerations has identified common contributing factors "
            "to wrongful convictions including perjury or false accusation (57% of cases), false "
            "or misleading forensic evidence (24%), police misconduct (33%), and Brady "
            "violations (over 40%). These factors, when documented in a case, are statistically "
            "associated with substantially elevated probability of wrongful conviction. "
            "Adversarial review: mandatory review triggers based on indicators may produce high "
            "volume with limited capacity to process; review must be substantive, not "
            "rubber-stamp; 'mandatory review' without specific required processes and timelines "
            "creates the form of review without the substance."
        ),
    },
    "REVS-0004": {
        "notes": (
            "AI pattern-recognition tools can identify statistical anomalies in large case sets "
            "— cases with a particular forensic expert, a particular officer, or a particular "
            "prosecutorial charging pattern — that signal elevated risk of wrongful conviction "
            "at a scale impossible through individual case review. The Innocence Project's data "
            "analysis work demonstrates that systemic factors affect classes of cases. "
            "Adversarial review: AI case pattern tools must not create new barriers to relief "
            "— findings of 'no anomaly' must not be used to deny individual claims that have "
            "independent merit; the operator of pattern-recognition AI must be independent from "
            "prosecution; identified patterns must trigger mandatory review, not merely flag "
            "cases for discretionary consideration."
        ),
    },
    "REVS-0005": {
        "notes": (
            "AEDPA's one-year limitation on federal habeas corpus petitions and successive "
            "petition bars have been applied to deny review of credible innocence claims where "
            "evidence emerged after statutory deadlines. The Supreme Court held in McQuiggin "
            "v. Perkins, 569 U.S. 383 (2013) that actual innocence can excuse procedural "
            "default — but the standard is extremely demanding. Adversarial review: removing "
            "deadline bars creates concerns about finality and the interests of victims and the "
            "public in resolution; credible evidence of innocence must be defined with a "
            "workable standard that is higher than mere possibility but not as demanding as "
            "McQuiggin; courts may apply 'credible evidence' requirements so stringently as to "
            "replicate the same barriers under a different label."
        ),
    },
    "REVS-0006": {
        "notes": (
            "The Supreme Court held in Martinez v. Ryan, 566 U.S. 1 (2012) and Trevino v. "
            "Thaler, 569 U.S. 413 (2013) that inadequate post-conviction counsel can establish "
            "cause for procedural default in habeas proceedings — but this does not create a "
            "right to appointed counsel in post-conviction proceedings. Research shows that "
            "self-represented prisoners attempting to navigate federal habeas corpus proceedings "
            "face procedural complexity that makes claims almost impossible to develop without "
            "legal assistance. Adversarial review: providing counsel access for post-conviction "
            "proceedings is resource-intensive; public defender post-conviction units are "
            "severely understaffed; the structural demand for post-conviction review counsel is "
            "substantially higher than current capacity in most jurisdictions."
        ),
    },
    "REVS-0007": {
        "notes": (
            "Cases affected by systemic misconduct — including falsified evidence by a "
            "particular crime lab analyst, discredited testimony by a particular expert, or "
            "Brady violations by a particular prosecutorial office — affect classes of "
            "convictions that individual post-conviction processes cannot efficiently address. "
            "The Massachusetts Hinton lab scandal (2012) and the Houston crime lab scandal "
            "(2002–2012) both required multi-year, multi-agency class review processes. Research "
            "by the National Registry shows that systemic-misconduct exonerations are "
            "underrepresented because class review processes do not exist in most jurisdictions. "
            "Adversarial review: systemic review programs require significant government "
            "investment and face resistance from agencies responsible for the misconduct; "
            "timelines for class review can extend for years while affected individuals remain "
            "incarcerated."
        ),
    },
    # ------------------------------------------------------------------ RSTS --
    "RSTS-0001": {
        "notes": (
            "Research on restorative justice programs — including victim-offender mediation, "
            "community circles, and reparative boards — consistently shows superior outcomes "
            "compared to incarceration on recidivism, victim satisfaction, cost, and community "
            "safety. A 2007 meta-analysis by Lawrence Sherman and Heather Strang found that "
            "restorative justice programs reduced recidivism for both violent and property "
            "offenses. Adversarial review: 'appropriate and voluntary' requires that restorative "
            "programs have genuine capacity to be refused without criminal justice consequence; "
            "restorative justice can be made coercive when offered as the only alternative to "
            "incarceration; program quality varies widely — poorly facilitated processes can "
            "retraumatize victims; restorative approaches work best for offenses where "
            "victim-offender relationships exist and are less applicable to complex or "
            "organizational crimes."
        ),
    },
    "RSTS-0002": {
        "notes": (
            "Research shows that criminal prosecution for low-level and first-time offenses "
            "produces worse outcomes than diversion — higher recidivism, greater collateral "
            "consequences, and higher costs — for the majority of people who would otherwise be "
            "eligible for diversion programs. Drug courts, mental health courts, and community "
            "supervision diversion programs have strong evidence bases when adequately funded "
            "and structured with genuine exit pathways. Adversarial review: diversion programs "
            "that impose lengthy supervision periods with criminal consequences for failure "
            "produce 'net-widening' — bringing more people under justice system control than "
            "would otherwise face consequences; diversion for some charges while maintaining "
            "prosecution for others requires clear criteria that do not reproduce racial and "
            "class disparities in access."
        ),
    },
    "RSTS-0003": {
        "notes": (
            "Restorative justice processes that are coerced — presented as the only alternative "
            "to incarceration, or conditioned on admission of guilt that can be used in "
            "subsequent proceedings — undermine due process. Admission of responsibility in "
            "restorative programs is sometimes used to support subsequent prosecution if the "
            "program fails. Adversarial review: 'voluntary' participation must be defined so "
            "that prosecutors cannot effectively compel participation by making criminal "
            "prosecution the only alternative; confidentiality of statements made in restorative "
            "processes must be protected; completion of a restorative process must not be used "
            "as evidence of guilt in any subsequent proceedings."
        ),
    },
    "RSTS-0004": {
        "notes": (
            "Research documents significant disparities in access to diversion and restorative "
            "justice programs by race, geography, and class. Diversion is more commonly offered "
            "to white, suburban, and more affluent defendants for equivalent offenses. This "
            "disparity reflects both prosecutorial discretion and program availability — rural "
            "areas and high-poverty jurisdictions have fewer diversion options. Adversarial "
            "review: formal equity requirements must be accompanied by evaluation mechanisms "
            "that identify disparate access patterns; prosecutors have broad discretion that may "
            "resist formal equity requirements; funding must support diversion and restorative "
            "programs in jurisdictions that currently have none, not only in those already "
            "operating programs."
        ),
    },
    "RSTS-0005": {
        "notes": (
            "Successful completion of diversion programs typically results in charge dismissal, "
            "but practices around subsequent record treatment vary widely. Many diversion "
            "completions create arrest records, charge records, or diversion program records "
            "that appear in background checks. Research shows that people who have successfully "
            "completed diversion programs are substantially more employed and stably housed than "
            "those who received criminal convictions. Adversarial review: 'support for "
            "dismissal' is not the same as automatic dismissal — specificity about what "
            "completion produces is required; background check systems must be required to treat "
            "successfully diverted charges identically to charges that were never filed."
        ),
    },
    # ------------------------------------------------------------------ SUPR --
    "SUPR-0001": {
        "notes": (
            "The United States has the largest probation and parole population in the world — "
            "over 4 million people. Approximately 45% of state prison admissions in many states "
            "are probation and parole revocations rather than new crimes. Research by the "
            "Columbia University Justice Lab shows that this revolving door effect accounts for "
            "a substantial portion of U.S. incarceration rates. Adversarial review: 'designed "
            "to support reintegration' requires specific structural changes to supervision "
            "requirements, revocation standards, and resource allocation that face resistance "
            "from probation and parole agencies."
        ),
    },
    "SUPR-0002": {
        "notes": (
            "Research by the Columbia University Justice Lab documents that many probation "
            "conditions are imposed as a uniform checklist rather than as individualized "
            "requirements — resulting in conditions like 'no internet use' or 'no contact with "
            "anyone with a criminal record' that are impossible to satisfy in modern life. These "
            "conditions function as traps that ensure revocation regardless of rehabilitation "
            "progress. Adversarial review: courts impose conditions from checklists without "
            "individualized assessment due to time pressure; conditions must have specific nexus "
            "to supervision rationale — the connection between condition and safety or "
            "supervision purpose must be documented; challenging conditions requires legal "
            "resources most probationers lack."
        ),
    },
    "SUPR-0003": {
        "notes": (
            "Research documents that approximately 45% of state prison admissions in "
            "high-supervision-state contexts result from technical violations of supervision "
            "conditions rather than new offenses. Technical violations include missed "
            "appointments, positive drug tests, failure to report an address change, and similar "
            "administrative failures unrelated to public safety. Adversarial review: 'should "
            "not by default trigger incarceration' leaves too much discretion — specific "
            "mandatory sanctions short of incarceration must be required for technical "
            "violations; supervision agents must not have unlimited discretion to determine what "
            "constitutes a technical violation; some technical violations have genuine public "
            "safety implications and must be addressed with proportionate responses."
        ),
    },
    "SUPR-0004": {
        "notes": (
            "In Morrissey v. Brewer, 408 U.S. 471 (1972), the Supreme Court held that parolees "
            "are entitled to due process before revocation, including notice of alleged "
            "violations and a neutral hearing body. In Gagnon v. Scarpelli, 411 U.S. 778 "
            "(1973), the Court extended similar protections to probationers. Despite these "
            "constitutional requirements, revocation hearings are often brief and heavily "
            "deferential to supervision agents. Adversarial review: formal due process "
            "requirements can be satisfied by hearings that are procedurally adequate but "
            "substantively rubber-stamp revocation recommendations; supervision agents' "
            "statements receive disproportionate weight; meaningful review requires counsel, "
            "evidence access, and genuinely neutral adjudicators."
        ),
    },
    "SUPR-0005": {
        "notes": (
            "Research documents supervision conditions including geographic restrictions that "
            "prevent people from living with family members who have criminal records, reporting "
            "requirements incompatible with employment, and drug testing requirements that "
            "conflict with prescribed medications. These conditions function as traps regardless "
            "of the supervised person's good-faith efforts to comply. Adversarial review: "
            "'impossible' conditions are often imposed by agencies under time pressure with no "
            "individualized assessment; challenging conditions requires legal resources most "
            "supervised people lack; agencies may impose restrictive conditions to manage "
            "liability rather than to achieve supervision goals."
        ),
    },
    "SUPR-0006": {
        "notes": (
            "Research documents that the risk of recidivism decreases sharply over time after "
            "release from incarceration — the aging-out effect — and that continued supervision "
            "of low-risk individuals after two to three years produces no public safety benefit "
            "while imposing significant burdens and costs. Research by the Council of State "
            "Governments Justice Center shows that automatically reducing supervision length for "
            "people who have complied with conditions for extended periods produces equivalent "
            "public safety outcomes at substantially lower cost. Adversarial review: periodic "
            "review that can extend as well as reduce supervision creates a two-edged process "
            "that may increase rather than decrease supervision length; 'clear evidence' "
            "justifying continued supervision must be defined specifically to prevent automatic "
            "extension as the default."
        ),
    },
    # ------------------------------------------------------------------ VICS --
    "VICS-0001": {
        "notes": (
            "Research on victim satisfaction with criminal justice processes consistently shows "
            "that participation and information — knowing what is happening in their case — are "
            "more important to victims than outcomes, including sentence length. The Crime "
            "Victims' Rights Act of 2004 (18 U.S.C. § 3771) establishes federal rights "
            "including notice, access to proceedings, and reasonable right to be heard. "
            "Adversarial review: victim rights must be implemented in ways that preserve "
            "defendants' due process rights — victim testimony at sentencing, victim impact "
            "evidence, and victim participation in plea negotiations must not override the "
            "presumption of innocence or defendants' confrontation rights; 'meaningful "
            "participation' must not be interpreted to give victims veto power over prosecutorial "
            "decisions."
        ),
    },
    "VICS-0002": {
        "notes": (
            "Research consistently shows that trauma-informed responses to crime victims — "
            "including stable housing, healthcare, mental health treatment, and safe environments "
            "for disclosure — improve both victim recovery and cooperation with law enforcement "
            "investigations. The Violence Against Women Act and the Victims of Crime Act (VOCA) "
            "provide federal funding for victim services, but research documents large gaps "
            "between demand and available services. Adversarial review: 'trauma-informed' "
            "services require training and infrastructure that many localities lack; services "
            "restricted to victims who cooperate with prosecution exclude many crime victims; "
            "healthcare and mental health services for victims must not be contingent on criminal "
            "prosecution."
        ),
    },
    "VICS-0003": {
        "notes": (
            "Victim rights frameworks, while legitimate and important, can be weaponized to "
            "erode defendants' due process rights when implemented without appropriate limits. "
            "Mandatory victim impact testimony, victim participation in plea decisions, and "
            "enhanced prosecution at victim request can create pressure on prosecutors to pursue "
            "more aggressive cases regardless of evidentiary merit. Adversarial review: 'may "
            "not be used to erode' requires active judicial and prosecutorial management; victim "
            "rights organizations may advocate for expanded rights without adequate attention to "
            "defense rights impacts; the tension between victim participation and defendants' "
            "rights requires ongoing institutional management, not a one-time policy decision."
        ),
    },
    "VICS-0004": {
        "notes": (
            "Research on victims' experiences in the criminal justice system shows that many "
            "victims do not want maximum punishment — they want acknowledgment, explanation, and "
            "some form of accountability. Restorative approaches that center victims' actual "
            "interests often produce more satisfaction than punitive approaches. Adversarial "
            "review: 'retribution alone' as the prohibited outcome requires a standard for when "
            "prosecutor charging and sentencing recommendations have moved from justice to "
            "retribution — a standard that is difficult to define and enforce; victims may want "
            "retributive outcomes and prosecutors may feel ethically obligated to pursue them."
        ),
    },
    "VICS-0005": {
        "notes": (
            "Research documents significant disparities in access to victim services by race, "
            "geography, citizenship, and class. Services are concentrated in jurisdictions with "
            "more resources; rural victims, immigrant victims, and victims in communities with "
            "lower income receive substantially fewer services. The U visa program provides some "
            "protection for immigrant crime victims but is administrative rather than statutory "
            "and has capacity limits. Adversarial review: 'equitable' services require both "
            "equal access and culturally competent delivery; services designed for one "
            "demographic may be inaccessible or ineffective for others; funding equity requires "
            "federal allocation formulas that reach underserved jurisdictions."
        ),
    },
    # ------------------------------------------------------------------ WITS --
    "WITS-0001": {
        "notes": (
            "Witness intimidation is a documented, serious problem that affects the ability of "
            "the justice system to function, particularly in communities with high rates of "
            "violent crime. Research by the Urban Institute documents that witness intimidation "
            "is a primary reason why many violent crimes go unsolved — witnesses who fear "
            "retaliation do not cooperate. Federal witness protection (18 U.S.C. § 1512) "
            "prohibits witness intimidation; the Witness Security Program provides physical "
            "protection for high-risk witnesses. Adversarial review: 'accountable legal "
            "protections' for witnesses must not convert witness protection into coercion — "
            "witnesses held under 'protective' arrangements without freedom to leave or "
            "communicate are effectively detained; the distinction between protection and "
            "detention must be enforced."
        ),
    },
    "WITS-0002": {
        "notes": (
            "Witness protection measures range from relocation to confidentiality orders to "
            "anonymous testimony — with varying impacts on defendants' rights. Anonymous "
            "testimony directly implicates the Confrontation Clause right to confront witnesses. "
            "Roviaro v. United States, 353 U.S. 53 (1957) established limits on informant "
            "privilege in criminal cases. Adversarial review: 'proportionate' witness protection "
            "must balance genuine threat assessment against defendants' confrontation rights; "
            "protective orders that prevent defense counsel from knowing witnesses' identities "
            "before trial create serious fairness concerns; protection measures imposed without "
            "adequate threat assessment may be used as tools for coercion."
        ),
    },
    "WITS-0003": {
        "notes": (
            "Giglio v. United States, 405 U.S. 150 (1972) requires disclosure of benefits "
            "provided to witnesses, including benefits to family members. Undisclosed benefits "
            "— reduced charges for cooperating witnesses, government payments, housing "
            "assistance — undermine the jury's ability to assess credibility. Research on "
            "informant testimony by Alexandra Natapoff documents that informant testimony is "
            "among the leading contributors to wrongful convictions. Adversarial review: "
            "'material inducements' must be defined broadly to include informal arrangements "
            "and future benefits, not just formal agreements; prosecutors may characterize "
            "arrangements as 'not yet binding' to avoid disclosure; ongoing benefits provided "
            "to witnesses post-trial without pre-trial disclosure create retroactive impeachment "
            "material that is often not disclosed."
        ),
    },
    "WITS-0004": {
        "notes": (
            "Witness intimidation by law enforcement — including threatening to report family "
            "members for immigration violations, threatening adverse action on pending cases, or "
            "using investigative power coercively against witnesses — is a documented problem in "
            "high-stakes cases. Research documents cases where police officers were found to have "
            "intimidated witnesses to suppress exculpatory testimony. Adversarial review: "
            "'officials' must be defined broadly to include law enforcement, prosecutors, and "
            "government contractors; internal investigations of official witness intimidation are "
            "subject to the same conflict-of-interest problems as other internal investigations; "
            "independent investigation authority is required."
        ),
    },
    "WITS-0005": {
        "notes": (
            "Witnesses — particularly victims who are also witnesses — experience significant "
            "psychological effects from testifying about traumatic events in adversarial "
            "proceedings. Research on trauma and memory shows that trauma can affect the "
            "accuracy and consistency of testimony in ways that are frequently misinterpreted as "
            "deception. Trauma-informed support for witnesses improves both witness welfare and "
            "the quality of testimony. Adversarial review: 'trauma-informed' support that "
            "includes coaching or preparation sessions with prosecution must be disclosed to "
            "defense; support that influences testimony content crosses from support into witness "
            "preparation that may affect adversarial fairness; support programs must be designed "
            "to support accurate testimony, not to produce consistent testimony for prosecution "
            "purposes."
        ),
    },
}  # end CARD_CONTENT


def process_card(card: "Tag", content: "dict | None", soup: BeautifulSoup) -> None:
    """Apply class, badge, stmt, and notes changes to a single status-missing card."""
    # 1. Update CSS class
    classes = card.get("class", [])
    card["class"] = [
        "status-included" if c == "status-missing" else c for c in classes
    ]

    # 2. Update badge text
    badge = card.find("span", class_="rule-badge")
    if badge:
        badge.string = "Included"

    if not content:
        return  # class/badge change only

    # 3. Handle rule-stmt
    stmt_text = content.get("stmt")
    if stmt_text:
        stmt_p = card.find("p", class_="rule-stmt")
        if stmt_p:
            stmt_p.clear()
            stmt_p.append(NavigableString(stmt_text))
        else:
            title_p = card.find("p", class_="rule-title")
            new_stmt = soup.new_tag("p")
            new_stmt["class"] = "rule-stmt"
            new_stmt.append(NavigableString(stmt_text))
            if title_p:
                title_p.insert_after(new_stmt)

    # 4. Handle rule-notes
    notes_text = content.get("notes")
    if notes_text:
        notes_p = card.find("p", class_="rule-notes")
        if notes_p:
            if content.get("append"):
                notes_p.append(NavigableString(notes_text))
            else:
                notes_p.clear()
                notes_p.append(NavigableString(notes_text))
        else:
            # Insert after rule-stmt (which may have just been inserted)
            stmt_p = card.find("p", class_="rule-stmt")
            title_p = card.find("p", class_="rule-title")
            anchor = stmt_p if stmt_p else title_p
            new_notes = soup.new_tag("p")
            new_notes["class"] = "rule-notes"
            new_notes.append(NavigableString(notes_text))
            if anchor:
                anchor.insert_after(new_notes)


def main() -> None:
    html_text = HTML_FILE.read_text(encoding="utf-8")
    soup = BeautifulSoup(html_text, "html.parser")

    missing_cards = soup.find_all("div", class_="status-missing")
    processed = 0

    for card in missing_cards:
        card_id = card.get("id", "")
        # Strip the leading 'JUST-' prefix to get the lookup key
        suffix = card_id.removeprefix("JUST-")
        content = CARD_CONTENT.get(suffix)  # None for class-only cards
        process_card(card, content, soup)
        processed += 1

    HTML_FILE.write_text(str(soup), encoding="utf-8")
    print(f"Processed {processed} status-missing cards.")

    # Verify
    remaining = str(soup).count('class="status-missing"')
    included = str(soup).count('class="status-included"')
    print(f"Remaining status-missing: {remaining}")
    print(f"Total status-included: {included}")


if __name__ == "__main__":
    main()
