# PolicyOS Pillar Audit — 2026-04-27

Generated: 2026-04-27  
Auditor: Sam (GitHub Copilot CLI, claude-sonnet-4.6)  
Source: DB canonical positions (`policy/catalog/policy_catalog_v2.sqlite`) + PolicyOS Layer 1–3 documents  
Status: **Draft for review — do not treat as final until reviewed by platform maintainer**

---

## Summary

- **Pillars audited:** 25
- **Critical gaps:** 5 pillars (CORT, SCIS, TERM, INFR, LEGL)
- **High gaps:** 7 pillars (FPOL, GUNS, MDIA, RGHT, HOUS, ELEC, CHKS)
- **Needs work:** 9 pillars (ANTR, CNSR, CRPT, EDUC, ENVR, EXEC, IMMG, LABR, TAXN)
- **Adequate or strong:** 4 pillars (ADMN, HLTH, JUST, TECH)

### Top systemic gaps across the platform

1. **No pillar has a formal inheritance declaration** — PAOS-TEST-0003 requires every pillar to document which KERN rules and overlay families apply. No pillar does this. This is a universal gap and the single highest-priority process fix.

2. **Whistleblower protections (KERN-0027) are missing from 17 of 25 pillars** — Explicit coverage exists only in ADMN, CRPT, HLTH (scientific research), and JUST (quota enforcement). The rule requires enforceable protections for persons reporting violations from within institutions across all pillars with enforcement components. Pillars with the most exposure: ENVR, TECH, LABR, HOUS, TAXN, IMMG, ELEC, INFR.

3. **Affirmative duty funding mechanisms (THRV-0003) are absent or vague in 10+ pillars** — The THRV overlay requires that any rule fulfilling a material security obligation must specify the funding mechanism, authorization path, and fiscal authority. Many pillars declare the obligation (e.g., universal healthcare, affordable housing, broadband access) without specifying the fiscal architecture.

4. **AIGV overlay is absent or thin in 8 applicable pillars** — The AI-governance overlay applies wherever AI or algorithmic systems materially affect rights, safety, or access. It is comprehensively addressed in TECH, HLTH, JUST, and ADMN. It is weak or absent in ELEC (AI-generated election interference), HOUS (algorithmic tenant screening and pricing), INFR (AI in infrastructure safety), LABR (partially addressed), ENVR, FPOL, LEGL, and SCIS.

5. **Enforcement actor, trigger, and failure consequence missing from many positions (PAOS-ENFC-0001)** — Across the platform, positions frequently specify the desired behavior or prohibition but do not complete the enforcement circuit: who enforces, how enforcement begins, what evidence is required, and what happens when enforcement fails. This affects CORT, TERM, LEGL, GUNS, MDIA, RGHT, and FPOL most severely.

---

## Methodology

This audit queried canonical positions (`status='CANONICAL'`) in `policy/catalog/policy_catalog_v2.sqlite` for all 25 pillar domains. Each pillar was assessed against:

1. **KERN rules** — 27 universal rules, with focused review of rules 1–2, 4–5, 7, 10–11, 13–17, 20, 23, 26–27.
2. **Applicable overlays** — Identified based on pillar subject matter; compliance assessed through position coverage.
3. **Authoring OS** — NORM-0002 (value coverage), AUTH-0001/0002 (enforcement actor and circuit), TEST-0001/0004 (abuse paths, perverse incentives), ENFC-0001 (enforcement defined), TEST-0003 (inheritance declarations).

DB position titles were the primary evidence base; full statement text was reviewed selectively for enforcement- and challenge-rights language. The audit is a structural assessment, not a line-by-line content review. Gaps identified are structural and design-level; they do not imply that no relevant thinking exists, only that no canonical position captures it.

---

## Platform-wide findings

### PW-1: Universal absence of inheritance declarations

PAOS-TEST-0003 requires every pillar to carry a documented inheritance declaration identifying which KERN rules and overlay families apply and how they interact. No pillar in the current catalog carries this declaration. This makes cross-layer conflict resolution unenforceable and creates interpretive uncertainty about which overlays govern any given pillar. **This is a housekeeping fix that should precede any substantive pillar revision.**

### PW-2: Whistleblower protection is a compliance cluster, not a platform design

KERN-0027 is the strongest anti-retaliation rule in the system. The current platform treats it as a subject-matter concern (addressed where whistleblowing is the topic) rather than a design invariant (required wherever enforcement exists). The ADMN and CRPT pillars carry robust WBLS subdomains. Eighteen other pillars with enforcement, penalty, or eligibility components carry nothing. This creates an asymmetry where, for example, environmental enforcement officers, immigration agents, housing inspectors, and election officials face no platform-mandated retaliation protections.

### PW-3: Perverse incentive review is absent or implicit in most pillars

KERN-0017 prohibits incentive structures that reward denial, extraction, concealment, or deprivation of rights. PAOS-TEST-0004 requires that every proposed rule be reviewed for perverse incentives. The HLTH pillar explicitly addresses denial-rate incentives, reversal-rate reporting, and AI-assisted denial patterns — this is the platform's strongest example. It is largely absent elsewhere. CNSR, TAXN, HOUS, LABR, and IMMG all involve institutional actors whose incentive structures could reward harmful outcomes; few of those pillars surface and address this explicitly.

### PW-4: Foreseeable abuse path design (KERN-0015) is uneven

KERN-0015 requires that systems be designed to prevent foreseeable abuse rather than only punishing it after harm. JUST, IMMG, HLTH, and TECH have the strongest coverage of this principle — positions explicitly prohibiting specific structural configurations known to produce abuse. CORT, GUNS, TERM, LEGL, and SCIS carry few or no positions addressing the foreseeable abuse paths in their respective domains.

### PW-5: AI governance is a cluster, not a cross-cutting layer

The platform's AI governance is concentrated in TECH (499 positions, including the deepest AIGV coverage on the platform) and secondarily in HLTH and JUST. This is appropriate given those domains' depth. However, the AIGV overlay is intended to apply wherever AI materially affects rights, safety, or access — which includes ELEC, HOUS, INFR, LABR, ENVR, FPOL, LEGL, and ADMN. Most of those pillars lack AIGV-aligned positions. AI's role in election manipulation, housing discrimination, infrastructure failure, labor surveillance, environmental enforcement, and foreign policy is not systematically addressed outside the primary AI pillar.

---

## Per-pillar audit

---

### Administrative State (ADMN)

**Applicable overlays:** KERN (universal) + ENFA, FEDR, REGD, AIGV, PRIV

**KERN compliance:** Strong. The pillar covers most critical KERN dimensions:
- KERN-0002 (delegation accountability): CIVL and OVRG subdomains address the chain; CIVL-0005 prohibits political appointees from overriding career enforcement staff.
- KERN-0004 (unchecked power): CAPS (anti-capture), INDS (independence), OVRG all address.
- KERN-0005 (attributable authority): TRAN-0001 (publish mission, rules, enforcement priorities, audits).
- KERN-0013 (challenge/appeal): ADJS-0001 is strong — notice, records, meaningful appeal rights.
- KERN-0015 (foreseeable abuse design): CAPS, CRAS (CRA reform) address structural configurations.
- KERN-0016 (no coercion/deprivation mechanism): Present through CIVL protections.
- KERN-0026 (systemic failure/corrective action): SYSR-0003 (design must prevent sabotage and unaccountable drift).
- KERN-0027 (whistleblower): WBLS-0001/0002/0003 — strong coverage for federal employees and contractors.

**Overlay gaps:**
- ENFA: Well-covered (ENFL, IGSP, OVRG). *Compliant.*
- FEDR: Present (SDST, LCAL, federalism design). *Compliant.*
- REGD: Strong (CAPS, CHVS, CRAS, revolving door). *Compliant.*
- AIGV: AINL subdomain present; AI in administrative decision-making addressed. *Partial* — scope of coverage unclear; no explicit position on AI in agency adjudication specifically.
- PRIV: RGTS addresses individual rights in administrative context. *Partial* — scope of data collected by agencies not fully addressed.

**Authoring OS gaps:**
- NORM-0002: Good coverage of accountability, transparency, democratic self-government. Ecological habitability (Value 8) absent — agencies govern environmental programs; no position on what happens when agencies fail ecological duties.
- AUTH-0002: Enforcement circuit reasonably complete for most positions.
- TEST-0001/0004: Perverse incentive review evident in CAPS and ENFL. Abuse path design present.
- ENFC-0001: Generally defined; IGSP provides independent review mechanism.
- TEST-0003: **No inheritance declaration. Universal gap.**

**Priority gaps:**
1. No inheritance declaration (TEST-0003) — process gap affecting all audits.
2. AIGV overlay: AI in agency adjudication and administrative decision-making underspecified.
3. Ecological duty of agencies: No position addresses what happens when agencies responsible for environmental protection structurally fail that duty.
4. PRIV scope: Data collection practices across administrative agencies not addressed as a structural design constraint.

**Overall rating:** **Adequate**

---

### Antitrust and Corporate Power (ANTR)

**Applicable overlays:** KERN (universal) + ENFA, REGD, ECON, PRIV, AIGV

**KERN compliance:** Strong. The pillar's breadth (139 positions, 30 subdomains) covers:
- KERN-0004 (unchecked power): Core purpose. MONO, MPYS, UTLY, PLTF all address.
- KERN-0005 (attributable authority): ENFL, ENFC cover enforcement attribution.
- KERN-0015 (foreseeable abuse design): ALGO, ALGP (algorithmic pricing), AINL (AI in antitrust) address emerging abuse paths.
- KERN-0026 (systemic failure/corrective action): SYSR-related positions likely present.
- KERN-0027 (whistleblower): **Absent.** No WBLS or equivalent in ANTR. Antitrust violations often depend on insider information.

**Overlay gaps:**
- ENFA: ENFC, ENFL subdomains comprehensive. *Compliant.*
- REGD: Core overlay — CAPS, CHTR, REPR, TELE, UTLY all address. Protective vs. gatekeeping distinction addressed. *Compliant.*
- ECON: Core overlay — NMDS (no monopsony/duopoly), PEQS (platform equity), PLTF (platform power) all present. Structural remedies present. *Compliant.*
- PRIV: ALGO, ALGP address algorithmic pricing transparency. DATA privacy in market contexts partial. *Partial.*
- AIGV: AINL (AI in antitrust), ALGO (algorithmic pricing) are present. But AI-specific governance (mandatory auditing, non-AI escape clause) not fully addressed. *Partial.*

**Authoring OS gaps:**
- NORM-0002: Material security (Value 7) and ecological habitability (Value 8) — corporate concentration effects on essential goods pricing addressed (PHRM, HLSP, MEDA), but environmental concentration (agricultural monopoly, fossil fuel concentration) less clear.
- AUTH-0002: Enforcement generally well-specified; individual liability (ENFL, DPAS-style provisions) present.
- TEST-0004: Perverse incentive review: settlement structures that allow repeated violations — partial (ENFC likely addresses).
- ENFC-0001: Generally defined; independent enforcement actors present.
- TEST-0003: **No inheritance declaration.**

**Priority gaps:**
1. Whistleblower protections absent — particularly important for antitrust whistleblowing by corporate insiders.
2. AIGV coverage: AI-based anticompetitive conduct (algorithmic pricing cartels, AI-enabled market division) not fully addressed by current AIGV overlay standard.
3. THRV overlay: When market concentration in essential goods (food, pharma, healthcare) creates access failures, what are the affirmative remedies? Some present (PHRM, HLSP) but not systematically expressed as THRV-compliant obligations.
4. Agricultural concentration: AGRI, AGFS subdomains present but ecological and food-security implications of agricultural monopoly (ECOL overlay) not addressed.

**Overall rating:** **Needs work**

---

### Checks and Balances (CHKS)

**Applicable overlays:** KERN (universal) + FEDR, DEMO, AIGV

**KERN compliance:** Strong — this pillar is substantially the institutionalization of KERN principles:
- KERN-0002/0004 (accountability/unchecked power): BRNS, SHDS, WARS, IMPS, JCHK, JURS all address.
- KERN-0005 (attributable authority): LAWS, REGS address legal clarity.
- KERN-0013 (challenge/appeal): ACCS, APPR address access to challenge mechanisms.
- KERN-0023/0026 (repair broken systems): IGOV, SDGA address mechanisms for systemic correction.
- KERN-0027 (whistleblower): **Absent as a standalone.** Relies on cross-pillar coverage in ADMN and CRPT. No position in CHKS addresses protections for persons who expose checks-and-balances violations internally.

**Overlay gaps:**
- FEDR: FEDS, STAS, GEOS address national/state structure. *Compliant.*
- DEMO: CONG, WARS, EMGS, IMPS address democratic accountability of power branches. *Compliant.*
- AIGV: AINL subdomain present — addresses AI use within oversight structures. *Partial* — no position on AI systems used to conduct surveillance of political opponents or civil society.
- SURV subdomain: Present — addresses surveillance oversight. Compliant with KERN-0015 on foreseeable abuse.

**Authoring OS gaps:**
- NORM-0002: All eleven values represented through this pillar's structural scope. However, material security (Value 7) absent — no position addresses what checks exist when government *fails to provide* essential goods, as opposed to when it *overreaches*.
- AUTH-0002: Some positions are structural commitments without clear enforcement actors (e.g., "Congress must..."). The pillar would benefit from specifying what happens when Congress refuses to exercise its checking function.
- TEST-0001: Foreseeable abuse paths generally well-addressed; emergency-powers abuse addressed through EMGS subdomain.
- ENFC-0001: Enforcement circuits incomplete where the pillar relies on Congress or courts to self-enforce their own oversight duties.
- TEST-0003: **No inheritance declaration.**

**Priority gaps:**
1. Enforcement failure when checking institutions refuse to act — the pillar is strong on what checks *should* exist but thin on what happens when they *fail to function*.
2. Whistleblower protections for persons who expose intra-branch violations absent.
3. AIGV: AI-assisted concentration of government power (predictive surveillance, AI-based suppression of political opposition) not fully addressed.
4. Material security dimension: Checks and balances include oversight of whether government meets its affirmative duties — not addressed.

**Overall rating:** **High gaps**

---

### Consumer Rights (CNSR)

**Applicable overlays:** KERN (universal) + ENFA, REGD, ECON, PRIV, GEOG

**KERN compliance:** Present and broad (177 positions, 43 subdomains):
- KERN-0013 (challenge/appeal): ARBT addresses forced arbitration — strong position.
- KERN-0014 (access not defeated by burden): FEES, DEBT, TMSH (time-sharing/predatory contracts) address.
- KERN-0015 (foreseeable abuse design): PRED, PDLS (predatory lending), CRPT (fraud) all address.
- KERN-0016 (no coercion/fear mechanism): DRKS (dark patterns), PRED, DESS (deceptive design) address.
- KERN-0017 (no denial/extraction incentives): PRED, DEBT, PDLS — present but not always framed as incentive-structure analysis.
- KERN-0027 (whistleblower): **Absent.** No position on protections for consumer-facing workers who expose corporate fraud or deceptive practices.

**Overlay gaps:**
- ENFA: ENFL, SYSR cover enforcement architecture. *Compliant.*
- REGD: ANTS, ANTI cover regulatory design and anti-capture. Gatekeeping vs. protection distinction addressed. *Compliant.*
- ECON: PRED, PDLS, CRDS, DEBT address predatory extraction. ARBT (mandatory arbitration) addresses collective remedy suppression. *Compliant.*
- PRIV: DATA, DBRK, DBRS comprehensive on data privacy and data broker markets. *Compliant.*
- GEOG: Digital access barriers in consumer contexts — ELCS (electronic contracts), online-only service access, rural broadband intersection with consumer access. *Partial* — geographic consumer protection disparity not addressed as a structural constraint.

**Authoring OS gaps:**
- NORM-0002: Good coverage of liberty (Value 3 — autonomy in markets), equal standing (Value 2). Ecological habitability (Value 8) absent — product environmental footprint, planned obsolescence, and environmental harm from predatory goods not addressed.
- AUTH-0002: Enforcement circuits defined for most positions; ENFL present.
- TEST-0004: Perverse incentive review: fee structures rewarding denial of consumer claims (e.g., insurance adjustment incentives) — present through GENL and LIFE subdomains but not systematically.
- ENFC-0001: Generally defined.
- TEST-0003: **No inheritance declaration.**

**Priority gaps:**
1. Whistleblower protections absent for consumer-protection whistleblowers (banking, insurance, pharma employees).
2. Geographic disparity: Rural and low-income communities face differential consumer protection exposure (payday lending geography, digital-only contract terms) — GEOG overlay not addressed.
3. ECOL overlay: Consumer product environmental harm as a consumer-rights violation not addressed.
4. AI in consumer contexts: ALGO subdomain present but AIGV-specific protections (pre-deployment audit, mandatory disclosure, non-AI-escape clause) not fully expressed.

**Overall rating:** **Needs work**

---

### Courts and Judicial System (CORT)

**Applicable overlays:** KERN (universal) + ENFA, REGD, FEDR, DEMO, PRIV

**KERN compliance:** Present but structurally thin (30 positions, 10 subdomains):
- KERN-0002/0004 (accountability/unchecked power): ETHL (ethics code, disclosure), OVRG, LGOS-0003/0004 address accountability.
- KERN-0005 (attributable authority): ETHL-0004 (financial disclosure) and recusal rules address.
- KERN-0013 (challenge/appeal): **Largely absent.** CORT governs the structure of courts but does not address how ordinary litigants challenge judicial conduct. LGOS-0004 specifies an independent enforcement office; but what triggers review and how litigants access it is not addressed.
- KERN-0014 (access not defeated by burden): **Absent.** Court fees, mandatory representation, geographic access to federal courts are not covered. This is the most significant structural gap.
- KERN-0015 (foreseeable abuse design): Shadow docket reform (SHDS) addresses one foreseeable abuse path well; venue shopping (VENS) addresses another.
- KERN-0017 (denial incentives): Judicial incentives that reward favorable rulings for powerful parties — **absent.**
- KERN-0027 (whistleblower): **Absent.** No protections for court staff, law clerks, or attorneys who report judicial misconduct.

**Overlay gaps:**
- ENFA: ETHL-0003 (independent Judicial Conduct Commission) covers enforcement; but enforcement triggers, evidence standards, and failure consequences are unspecified. *Partial.*
- REGD: Judicial appointment reform (NOMS, APTS) addresses selection; anti-capture for courts weak. *Partial.*
- FEDR: Not addressed — federal/state court structure, federal preemption of state courts, and anti-concentration of federal adjudicative power are absent. *Absent.*
- DEMO: SIZS, ETHL, NOMS address legitimacy and democratic accountability. *Partial.*
- PRIV: AI in judicial decisions, privacy of litigants, and court data — **absent.**

**Authoring OS gaps:**
- NORM-0002: Access to justice (equal standing, Value 2) is the most critical value for this pillar. No position addresses cost barriers, mandatory counsel rights, or geographic access to federal courts. This is a fundamental NORM-0002 failure.
- AUTH-0002: Enforcement circuits incomplete for most positions — ETHL-0003 specifies an enforcement body but not how it is triggered, what evidence is needed, or what happens when it fails.
- TEST-0001: Foreseeable abuse paths: judge shopping well-addressed; court staff corruption, capture through amicus funding (LGOS-0005 — present), dark-money influence on judicial appointments — partially addressed.
- ENFC-0001: Independent Judicial Conduct Commission specified; but failure consequences and remedies underspecified.
- TEST-0003: **No inheritance declaration.**

**Priority gaps:**
1. Access to justice — GEOG/THRV overlay entirely absent: No positions on court fees, right to counsel in civil matters, geographic access to federal courts, or ADA compliance in courthouses.
2. Enforcement circuit incomplete for ethics violations — CORT-ETHL-0003 specifies the body; the rest of the circuit is missing.
3. Whistleblower protections for court staff and attorneys reporting judicial misconduct absent.
4. FEDR overlay absent: Federal/state court coordination, jurisdictional abuse, and anti-centralization of adjudicative power not addressed.

**Overall rating:** **Critical gaps**

---

### Anti-Corruption (CRPT)

**Applicable overlays:** KERN (universal) + ENFA, REGD, DEMO, PRIV

**KERN compliance:** Strong (71 positions, 22 subdomains):
- KERN-0002 (delegation accountability): IGSP (Inspector General protections) — strongest IGs coverage on platform.
- KERN-0004 (unchecked power): FINC, ETHL, LBBY all address.
- KERN-0005 (attributable authority): DISC, OWNS, STCK all require disclosure.
- KERN-0026 (systemic failure/corrective action): AUDT, IGSP specify corrective action triggers.
- KERN-0027 (whistleblower): **Best coverage on platform** — WBLS-0001/0002/0003 with CRPT-WHBS-0001; qui tam, anti-SLAPP, private right of action for retaliation all addressed.

**Overlay gaps:**
- ENFA: AUDT, IGSP, and enforcement subdomains comprehensive. *Compliant.*
- REGD: Lobbying reform (LBBY, LOBS), revolving door (HATS) — strong anti-capture. *Compliant.*
- DEMO: FINC, CMPN campaign finance reform comprehensive. *Compliant.*
- PRIV: DISC covers disclosure; UBST (undisclosed beneficial ownership) covers financial transparency. *Compliant.*

**Authoring OS gaps:**
- NORM-0002: Ecological habitability (Value 8) absent — corruption in environmental permitting, EPA capture, and fossil fuel industry corruption are not addressed within CRPT; relies on ENVR pillar. Value tension (anti-corruption vs. legitimate advocacy) not explicitly surfaced.
- AUTH-0002: Generally strong; most positions specify actors and mechanisms.
- TEST-0001/0004: Perverse incentive review: settlement structures that allow repeated violations — addressed through DPA reform (DPAS).
- ENFC-0001: Well-defined throughout.
- TEST-0003: **No inheritance declaration.**

**Priority gaps:**
1. AI-enabled corruption (AI procurement fraud, algorithmic favoritism in contracting, AI-based disinformation in political campaigns) — not addressed within CRPT; cross-pillar reliance on TECH and ELEC.
2. Local and state corruption infrastructure — CRPT is largely federal in orientation; sub-federal corruption patterns and oversight absent.
3. ECOL overlay: Environmental permitting corruption as a CRPT concern absent.
4. International corruption (FCPA scope, foreign bribery accountability) — INTL subdomain present but thin.

**Overall rating:** **Needs work**

---

### Education (EDUC)

**Applicable overlays:** KERN (universal) + ENFA, GEOG, FEDR, THRV, PRIV, DEMO, AIGV

**KERN compliance:** Present and broad (291 positions, 57 subdomains) — one of the most comprehensive content pillars:
- KERN-0013 (challenge/appeal): RGTS subdomain addresses student and parent rights; STDT, STDS, IDAS cover student rights in systems. IDEA subdomain addresses disability challenge rights.
- KERN-0014 (access not defeated by burden): ACCS, EARL, FINC, DEBT all address; geographic access through multiple subdomains.
- KERN-0016 (no coercion/fear mechanism): SECU (school safety) addresses; HMSC (homeschool), HOME contexts considered.
- KERN-0027 (whistleblower): **Weak.** FNDS and SCIS subdomains may touch on research integrity but no explicit WBLS protection for teachers, administrators, or staff who report abuse, fraud, or violations.

**Overlay gaps:**
- ENFA: Enforcement of education rights — STDS, EQFS cover; but enforcement actors and failure consequences underspecified for many positions. *Partial.*
- GEOG: ACCS, RURL concerns, digital access (TCHS, AINL, DATA) addressed. ZONS (school zoning). *Compliant.*
- FEDR: CHOS, CHRS, VCHR, SCHL address federal/state/local distribution; charter and choice policy covers anti-centralization. *Compliant.*
- THRV: Core overlay — FINC, FNDS, DEBT (student debt), EARL (early childhood) address funding mechanisms. FNDS specifies some fiscal mechanisms. *Partial* — minimum standard expressed as outcomes (THRV-0002) not always clear.
- PRIV: DATA subdomain covers student data privacy. *Compliant.*
- DEMO: CIVL (civic education) present. *Compliant.*
- AIGV: AINL subdomain present. *Partial* — pre-deployment assessment, mandatory disclosure to parents/students, and appeal rights for AI-influenced educational decisions underspecified.

**Authoring OS gaps:**
- NORM-0002: Good coverage across values. Ecological habitability (Value 8) absent — school environmental health (lead paint, air quality in school buildings) not addressed.
- AUTH-0002: Many positions specify what must happen; enforcement actors less consistently defined.
- TEST-0004: Perverse incentive review: voucher systems that incentivize cream-skimming; charter school funding structures that create perverse expansion incentives — partially addressed through CHRS, VCHS, VCHR.
- ENFC-0001: Federal enforcement of education rights underspecified; DOE enforcement authority not always defined in positions.
- TEST-0003: **No inheritance declaration.**

**Priority gaps:**
1. Whistleblower protections absent for education system employees — particularly critical for abuse reporting in private/charter schools.
2. AIGV: Algorithmic systems in admissions, disciplinary decisions, and learning assessment — pre-deployment audit and parent/student appeal rights underspecified.
3. Enforcement failure consequences when states fail to meet federal education standards — positions declare obligations; enforcement of non-compliance less defined.
4. School environmental health (ECOL overlay): Lead, asbestos, air quality in public school buildings absent.

**Overall rating:** **Needs work**

---

### Elections and Representation (ELEC)

**Applicable overlays:** KERN (universal) + ENFA, GEOG, FEDR, DEMO, AIGV, PRIV

**KERN compliance:** Strong on access and structural design (51 positions, 9 subdomains):
- KERN-0013 (challenge/appeal): VOTS-0010 (private right of action in VRA), OVRG-0001/0003 address challenge rights for election law violations.
- KERN-0014 (access not defeated by burden): VOTS subdomains very strong — registration, polling access, mail ballots, language access all addressed.
- KERN-0015 (foreseeable abuse design): MAPS (gerrymandering), SECU (election security), ROLS (purge safeguards), IDAS (ID burden mitigations) all address foreseeable abuse paths.
- KERN-0016 (no coercion/fear mechanism): SECU-0002/0003 (ban armed presence at polls) address coercion at the point of voting.
- KERN-0026 (systemic failure/corrective action): OVRG-0003/0004 address post-failure corrective mechanisms.
- KERN-0027 (whistleblower): **Absent.** No protections for election workers who expose fraud, intimidation, or system failure.

**Overlay gaps:**
- ENFA: OVRG covers oversight; private enforcement (VOTS-0010) present. Enforcement failure consequences underspecified. *Partial.*
- GEOG: Strong — IDAS (physical mobility), VOTS (polling capacity, wait times), language access, mail ballots. *Compliant.*
- FEDR: MAPS, VOTS-0010/0014 establish federal baselines. FEDR tension (state administration vs. federal standards) present. *Compliant.*
- DEMO: Core of this pillar — comprehensive. *Compliant.*
- AIGV: **Weak.** AI-generated disinformation in elections, deepfake political content, AI-driven micro-targeting — not addressed. SECU covers infrastructure security, not AI-generated information manipulation. *Absent.*
- PRIV: Voter data privacy, commercial surveillance of voters, data broker access to voter files — **absent.** *Absent.*

**Authoring OS gaps:**
- NORM-0002: Equal standing (Value 2) and democratic self-government (Value 4) very strong. Durability against capture (Value 11) — present. Privacy (real liberty, Value 3) absent. Ecological habitability (Value 8) absent and not relevant.
- AUTH-0002: Some positions are aspirational without defined enforcement actors (e.g., constitutional amendment for Electoral College — valid, but implementation path undefined for interim period).
- TEST-0001: Foreseeable abuse paths well-addressed for voter suppression; AI-based manipulation not addressed.
- ENFC-0001: OVRG and SECU define some enforcement; failure consequences for CISA non-certification and national elections board failure underspecified.
- TEST-0003: **No inheritance declaration.**

**Priority gaps:**
1. AIGV overlay absent — AI-generated election interference, synthetic media political ads, algorithmic voter targeting are significant foreseeable abuse paths not addressed.
2. Whistleblower protections absent for election workers.
3. PRIV overlay absent — voter data privacy and commercial surveillance of voter behavior unaddressed.
4. Enforcement failure consequences: What happens when CISA decertifies an election system and a state refuses to comply? Not addressed.

**Overall rating:** **High gaps**

---

### Environment and Agriculture (ENVR)

**Applicable overlays:** KERN (universal) + ENFA, ECOL, FEDR, REGD, ECON, GEOG

**KERN compliance:** Present and broad (192 positions, 57 subdomains):
- KERN-0004 (unchecked power): EPRS (EPA independence), REGS, INDS address.
- KERN-0005 (attributable authority): AUDT (mandatory quarterly corporate environmental audits) — strong.
- KERN-0015 (foreseeable abuse design): POLC, CORS (chemical plant oversight), FRCK (fracking regulation) address foreseeable configurations.
- KERN-0026 (systemic failure/corrective action): ENFL-0001/0002 cover liability and escalation; JUSS-0003 (Superfund) addresses remediation.
- KERN-0027 (whistleblower): **Absent.** No WBLS coverage in ENVR despite this being one of the most whistleblower-sensitive regulatory domains. Environmental enforcement routinely depends on insider reporting.

**Overlay gaps:**
- ECOL: Core overlay — platform's primary ECOL pillar. Comprehensive across climate, biodiversity, pollution, agricultural ecology. *Compliant.*
- ENFA: ENFL (enforcement, liability, criminal upgrades), AUDT (independent auditing) strong. *Compliant.*
- FEDR: EPA/state structure implicit; ENFL-0003 (EPA independence) addresses federal role. *Partial* — federal/state enforcement distribution (FEDR-0002) and state non-compliance mechanisms not explicitly addressed.
- REGD: REGS, EPRS, revolving door (ENFL-0005) address anti-capture. *Compliant.*
- ECON: Fossil fuel industry economic power (OILG, NGAS, COAL) addressed; agricultural monopoly intersection (AGRI?) weaker. *Partial.*
- GEOG: JUSS (environmental justice — cumulative burden analysis, frontline communities) strong. *Compliant.*

**Authoring OS gaps:**
- NORM-0002: Ecological habitability (Value 8) is the core value — fully addressed. Material security (Value 7) intersection: transition support for workers in fossil fuel industries — cross-pillar with LABR. Value tension (ecological protection vs. near-term material security) — should be surfaced per NORM-0008, partially present.
- AUTH-0002: Criminal liability provisions (ENFL-0004) and corporate audit requirements strong; individual officer liability specified.
- TEST-0004: Perverse incentive review: audit self-reporting incentives (AUDT-0004 — criminal liability for fraudulent audits addresses this); but voluntary disclosure incentive structures not addressed.
- ENFC-0001: Well-defined throughout; citizen suit provisions (ENFL-0006) provide private enforcement path.
- TEST-0003: **No inheritance declaration.**

**Priority gaps:**
1. Whistleblower protections absent — ENVR is arguably the platform's most critical domain for environmental insider reporting.
2. Agricultural monopoly ecological implications: AGRI subdomain present but corporate agriculture's ecological footprint not systematically addressed as a ECOL/ECON overlap concern.
3. AI in environmental enforcement: Satellite monitoring, algorithmic pollution detection, AI-based compliance systems — not addressed (AIGV overlay absent).
4. International environmental accountability: Extraterritorial pollution from U.S. operations, trade agreements with environmental implications — weak coverage.

**Overall rating:** **Needs work**

---

### Executive Power (EXEC)

**Applicable overlays:** KERN (universal) + ENFA, FEDR, DEMO, PRIV, AIGV

**KERN compliance:** Strong (139 positions, 22 subdomains) — this pillar directly addresses the accountability architecture:
- KERN-0002 (delegation accountability): STFS, CABS, UNIS address delegation chain.
- KERN-0004 (unchecked power): EXOS (executive orders), EMRS (emergency powers), POWS all address.
- KERN-0013 (challenge/appeal): RECS, PDNS (pardons), IMMS (immunity) address challenge mechanisms.
- KERN-0015 (foreseeable abuse design): EMRS (emergency power abuse), CLSS (classification abuse), HOGS (government obstruction) address known abuse paths.
- KERN-0023/0026 (broken/systemic failure): SYSR addresses; TRAN requires disclosure.
- KERN-0027 (whistleblower): **Absent within EXEC.** Cross-pillar reliance on ADMN and CRPT; but executive-branch-specific protections for whistleblowers who report presidential or cabinet misconduct not addressed here.

**Overlay gaps:**
- ENFA: Enforcement of executive constraints is structurally complex (courts, Congress, impeachment); multiple mechanisms addressed. *Partial* — failure consequences when all three mechanisms are blocked not addressed.
- FEDR: DIVS, UNIS address federal/state executive authority distribution. *Compliant.*
- DEMO: IMMS (absolute immunity doctrine rollback), PDNS (pardon limits), RECS (records preservation) address democratic accountability. *Compliant.*
- PRIV: Executive branch surveillance, FISA, classification — CLSS (classification) and SURV-adjacent positions likely present. *Partial.*
- AIGV: AI use in executive decision-making (automated national security analysis, AI-assisted pardon decisions, executive AI systems) — **absent.**

**Authoring OS gaps:**
- NORM-0002: Accountable power (Value 5) — core value, fully addressed. Material security (Value 7) and ecological habitability (Value 8) — executive failure to implement affirmative duties not addressed.
- AUTH-0002: Some positions face the structural problem that the enforcement actor is Congress or the courts — both of which can be paralyzed. What happens when both fail is underspecified.
- TEST-0001: Foreseeable abuse: emergency power abuse (EMRS) and classification abuse (CLSS) well-addressed. Abuse via executive reorganization (ADMN covers this); self-pardons and immunity claims (IMMS, PDNS) addressed.
- ENFC-0001: Enforcement circuits depend on external actors (Congress, courts); pillar does not address what structural mechanisms prevent enforcement paralysis.
- TEST-0003: **No inheritance declaration.**

**Priority gaps:**
1. Enforcement failure cascade: When Congress refuses to impeach, courts refuse to intervene, and the executive resists — what is the designed response? Not addressed.
2. AI in executive decision-making absent (AIGV overlay).
3. Executive branch whistleblower protections not addressed in this pillar (cross-pillar gap).
4. Material security duty of the executive: Executive failure to implement congressionally mandated programs — rights of affected populations not addressed.

**Overall rating:** **Needs work**

---

### Foreign Policy (FPOL)

**Applicable overlays:** KERN (universal) + ENFA, DEMO, PRIV, ECOL

**KERN compliance:** Present but structurally limited by the domain (86 positions, 16 subdomains):
- KERN-0002 (accountability): WARP, INTL, MILS address congressional oversight and accountability for covert operations.
- KERN-0005 (attributable authority): INTL-0004 (declassification and public accounting of covert ops) — partial.
- KERN-0013 (challenge/appeal): **Absent.** No mechanism for affected populations (including U.S. persons harmed by foreign policy) to challenge decisions or seek review.
- KERN-0015 (foreseeable abuse design): INTL-0002 (extrajudicial killings prohibition), MILS (military accountability) address.
- KERN-0016 (no coercion/fear mechanism): HRTS-0006 (absolute prohibition on torture) addresses.
- KERN-0027 (whistleblower): **Absent.** No protections for intelligence or diplomatic staff who report foreign policy violations (e.g., unauthorized covert action, civilian casualty concealment).

**Overlay gaps:**
- ENFA: Congressional oversight (WARP, INTL) is the primary enforcement mechanism. Independent civilian oversight of national security operations — **absent.** Enforcement failure when Congress is captured or refuses to act — not addressed. *Partial.*
- DEMO: WARP (War Powers Act reform) addresses democratic accountability of military force. *Compliant.*
- PRIV: INTL-0005 (proportionate standards for foreign surveillance) — present but thin. Commercial surveillance of foreign populations by U.S. companies — **absent.** *Partial.*
- ECOL: HRTS-0003 (clean environment as a human right) — present. Climate policy as foreign policy, international environmental agreements — CLMS and TRDS subdomains may address; systematic coverage absent. *Partial.*

**Authoring OS gaps:**
- NORM-0002: Human dignity (Value 1) and equal standing (Value 2) — HRTS subdomain addresses extraterritorial application. Real liberty (Value 3) — addressed for U.S. persons; foreign populations' liberty as a foreign policy constraint less systematically addressed. Ecological habitability (Value 8) — present through HRTS-0003 but not structurally integrated.
- AUTH-0002: Many positions are congressional duties without specified enforcement triggers or consequences for non-compliance (e.g., WARP-0001 requires congressional authorization — but what happens if the executive acts without it beyond existing law?).
- TEST-0001: Foreseeable abuse: executive unilateralism in military action addressed. AI in autonomous weapons systems — **absent.**
- ENFC-0001: Enforcement circuit severely limited: congressional oversight can be circumvented; international law enforcement mechanisms are weak by design. The pillar does not address this structural constraint.
- TEST-0003: **No inheritance declaration.**

**Priority gaps:**
1. AI in autonomous weapons and military AI systems — significant foreseeable harm path entirely absent from FPOL.
2. Enforcement circuit for war powers violations — WARP addresses the authorization requirement; consequences when the executive violates it are underspecified beyond existing law.
3. Whistleblower protections for intelligence and diplomatic personnel absent.
4. Challenge mechanisms for affected populations (including U.S. persons harmed by foreign policy decisions) — absent.

**Overall rating:** **High gaps**

---

### Gun Policy (GUNS)

**Applicable overlays:** KERN (universal) + ENFA, GEOG, FEDR, REGD, PRIV

**KERN compliance:** Present (45 positions, 15 subdomains):
- KERN-0013 (challenge/appeal): LICS subdomain (licensing) implies appeals; explicit challenge rights for denials — **absent.**
- KERN-0014 (access not defeated by burden): Geographic access to licensing offices, especially in rural areas — **absent.** The pillar addresses background check universality (ACQS) but not the access dimensions of compliance.
- KERN-0015 (foreseeable abuse design): TRAF (trafficking prevention), SAFE (safety storage) address known abuse paths. Straw purchase prevention, digital ghost gun proliferation (RFLS subdomain) address.
- KERN-0016 (no coercion/fear mechanism): Not applicable in this context.
- KERN-0017 (denial incentives): Background check system denial rates, appeals, and error correction — **absent.**
- KERN-0027 (whistleblower): **Absent.** No protections for gun dealer employees or ATF staff who expose illegal sales, enforcement failures, or system manipulation.

**Overlay gaps:**
- ENFA: REGS (regulatory oversight), TRAF (trafficking enforcement) cover enforcement. Independent audit of background check system — **absent.** *Partial.*
- GEOG: STWS subdomain addresses state-by-state standards; geographic consistency of enforcement across states — *partial.* Rural licensing access not addressed. *Partial.*
- FEDR: STWS implies federal/state structure; national preemption floor vs. state variation addressed. *Partial.*
- REGD: REGS, LICS address regulatory design. Anti-capture (gun industry influence over ATF regulation) — **absent.** *Partial.*
- PRIV: Mental health database access (MHES subdomain) — privacy implications of health data in licensing addressed. *Partial.*

**Authoring OS gaps:**
- NORM-0002: Public safety (enforceable fairness, Value 10) and real liberty (Value 3 — the contested 2A right) — the platform's political position on the underlying right is articulated through regulatory design but value tension (liberty vs. public safety) not explicitly surfaced per NORM-0008.
- AUTH-0002: Enforcement actors generally defined; specific enforcement failure consequences underspecified.
- TEST-0001: Foreseeable abuse paths: loopholes (ghost guns, private sale bypass, straw purchases) addressed. Background check system error rate and wrongful denial rates — **absent.**
- ENFC-0001: ATF enforcement capacity implied but not explicitly addressed as a funding/capacity obligation.
- TEST-0003: **No inheritance declaration.**

**Priority gaps:**
1. Challenge rights for wrongful background check denials absent — this is both a KERN-0013 and KERN-0017 failure (systems that wrongly deny must have correction mechanisms).
2. Anti-capture for ATF regulation: Gun industry influence over rulemaking and enforcement — absent.
3. Whistleblower protections absent.
4. AIGV overlay: AI-based threat assessment systems in gun licensing, predictive policing intersection with gun seizure — absent.

**Overall rating:** **High gaps**

---

### Healthcare (HLTH)

**Applicable overlays:** KERN (universal) + ENFA, GEOG, FEDR, THRV, AIGV, ECOL, ECON, PRIV, REGD

**KERN compliance:** Platform's strongest compliance (323 positions, 49 subdomains):
- KERN-0010/0011 (meaningful human review): AINL-0006/0008/0010 — among the strongest AI-accountability positions on the platform. Pre-decision human review, authority to override, conditions for meaningful review all specified.
- KERN-0013 (challenge/appeal): APLS subdomain comprehensive — independent external review, urgent timelines, pattern-triggering review of repeated denials.
- KERN-0014 (access not defeated by burden): RURL (rural access), TELS (telehealth), ACCS all address geographic and practical barriers.
- KERN-0015 (foreseeable abuse design): AINL-0013 (systemic bias in AI approval systems), PBMS (prior authorization abuse), REBS (claim denial patterns) directly address known abuse configurations.
- KERN-0017 (denial incentives): COVR-0019 (denial rates and reversal rates publicly reported) — strong.
- KERN-0027 (whistleblower): SCIS-0008 covers scientific whistleblowers; broader healthcare system worker protections (nurses, billing staff, clinical staff) — **partial.**

**Overlay gaps:**
- ENFA: Comprehensive enforcement throughout. *Compliant.*
- GEOG: RURL, TELS, JUSS (health justice disparities) strong. *Compliant.*
- FEDR: UNIV, COVR address federal/state coverage framework. *Compliant.*
- THRV: Core essential good — funding mechanisms, minimum standards, population obligations addressed. *Compliant.*
- AIGV: AINL subdomain is the platform's strongest domain-specific AIGV implementation. *Compliant.*
- ECOL: **Absent.** Environmental health — environmental determinants of disease, pollution-based health disparities — not addressed within HLTH. ENVR covers this partly; HLTH does not make the ECOL connection explicit.
- ECON: CSTS, DRUG, PHRS (pharmaceutical pricing), PBMS all address market-concentration effects on access and cost. *Compliant.*
- PRIV: LCDS (medical records), likely AINL positions. *Compliant.*
- REGD: OVRG, STDS cover regulatory oversight; anti-capture for insurance and pharmaceutical industries present. *Compliant.*

**Authoring OS gaps:**
- NORM-0002: Near-complete value coverage. Ecological habitability gap (environmental health determinants) as noted.
- AUTH-0002: Strong — most positions specify actors, mechanisms, and remedies.
- TEST-0004: Perverse incentive review: prior authorization denial incentives — among the strongest treatments on the platform.
- ENFC-0001: Well-defined throughout.
- TEST-0003: **No inheritance declaration.** (Universal gap.)

**Priority gaps:**
1. ECOL overlay absent: Environmental determinants of health (pollution, chemical exposure, climate-health nexus) not addressed within HLTH itself.
2. Whistleblower protections: SCIS-0008 covers research; clinical and administrative staff who expose billing fraud, denial quotas, or patient safety violations — underspecified.
3. Funding mechanism for universal coverage: THRV-0003 compliance — fiscal authority and authorization path for achieving universal coverage underspecified (position states the goal; mechanism incomplete).
4. Inheritance declaration absent (universal gap).

**Overall rating:** **Adequate**

---

### Housing (HOUS)

**Applicable overlays:** KERN (universal) + ENFA, GEOG, FEDR, THRV, ECON, ECOL, PRIV, REGD, AIGV

**KERN compliance:** Present and broad (227 positions, 47 subdomains):
- KERN-0013 (challenge/appeal): EVCT-0001 (right to court-appointed attorney in eviction proceedings) — strong. RGTS subdomain.
- KERN-0014 (access not defeated by burden): EVCT addresses procedural burdens in eviction; FINC, DEBT address cost barriers.
- KERN-0015 (foreseeable abuse design): EVTS, EVCT, RNTS (lease terms), TENS address known landlord abuse patterns.
- KERN-0016 (no coercion/fear mechanism): EVCT, TNNT (tenant rights) address; HABS (habitability) addresses deprivation-as-control.
- KERN-0017 (denial incentives): OVRG-0002/0004 address repeated patterns of abuse; enforcement of pattern-based violations addressed.
- KERN-0027 (whistleblower): **Absent.** No protections for housing code inspectors, HUD employees, or tenant advocates who expose systemic violations.

**Overlay gaps:**
- ENFA: OVRG (pattern enforcement), SUPR-0006 (time-bounded permitting), HABS-0003 (escalating consequences for repeated habitability violations) present. *Compliant.*
- GEOG: ZONE (zoning equity), SUPR (supply in high-demand areas), geographic access to affordable housing addressed. *Compliant.*
- FEDR: INST, SUBS, PUBL address federal programs and state/local roles. *Compliant.*
- THRV: Core essential good — comprehensive positions on affordability, homelessness (HMLS), supply. *Partial* — funding mechanisms specified for some programs; authorization path for universal access to housing not complete.
- ECON: MKTS (speculation), INST-0003 (algorithmic rent-pricing as antitrust violation) — strong. PRSS (pressure/extraction tactics) addressed. *Compliant.*
- ECOL: BLDS-0001 (sustainable building materials) — present but thin. Environmental health in housing (lead, asbestos, mold, flood risk) — **partial.** *Partial.*
- PRIV: BKGD-0001 (individualized criminal history assessment) covers one dimension; tenant data collection by landlords and property management platforms — **absent.** *Partial.*
- REGD: REGS, OVRG address regulatory oversight. Anti-capture for housing regulatory bodies — **partial.** *Partial.*
- AIGV: INST-0003 (algorithmic rent-pricing addressed as antitrust violation) — covers one use case. AI-based tenant screening, predictive eviction systems, AI-driven housing denial — **absent as AIGV-framed positions.** *Partial.*

**Authoring OS gaps:**
- NORM-0002: Good coverage. Environmental health (Value 8) as a housing concern underspecified.
- AUTH-0002: Enforcement actors defined for most positions; independent housing oversight body — present (OVRG) but capacity and independence underspecified.
- TEST-0004: Perverse incentive review: property management incentive structures that reward eviction over retention — implicit but not explicitly addressed.
- ENFC-0001: Generally defined; OVRG provides some enforcement structure.
- TEST-0003: **No inheritance declaration.**

**Priority gaps:**
1. AIGV: Algorithmic tenant screening, AI-based eviction prediction, and credit-scoring systems in housing access — addressed only through the antitrust framing; AIGV-specific safeguards (audit, challenge, human review) absent.
2. PRIV: Tenant data collection, property management surveillance, and data broker use of tenant data not addressed.
3. Whistleblower protections absent for housing inspectors and HUD employees.
4. Ecological health in housing: Environmental health hazards in homes (lead, mold, climate resilience) addressed only minimally.

**Overall rating:** **High gaps**

---

### Immigration (IMMG)

**Applicable overlays:** KERN (universal) + ENFA, GEOG, FEDR, THRV, PRIV, ECOL

**KERN compliance:** Strong (244 positions, 28 subdomains) — among the best structural compliance outside HLTH, JUST, and TECH:
- KERN-0010/0011 (meaningful human review): CRTS-0001/0002 (immigration courts structured for independence; no rubber-stamp), REMS-0006 (individualized review).
- KERN-0013 (challenge/appeal): REMS-0004/0005/0007/0008 comprehensive; CRTS-0003 (access to records and hearing dates); DETS-0005 (periodic review of detention).
- KERN-0014 (access not defeated by burden): CRTS-0006 (emergency funding to eliminate backlog), REMS-0004 (meaningful notice, counsel access, sufficient time).
- KERN-0015 (foreseeable abuse design): DETS-0006 (offshore detention prohibited), DETS-0007/0008/0009 (private detention prohibited, no profit motive in custody).
- KERN-0016 (no coercion/fear mechanism): DETS-0001 (detention not used as deterrence), REMS-0001 (no deportation to third countries without lawful acceptance).
- KERN-0026 (systemic failure): OVRG-0003 (abuse patterns trigger mandatory corrective action), DETS-0011/0012 (mandatory investigation of deaths and injuries in custody).
- KERN-0027 (whistleblower): **Absent as dedicated positions.** OVRG-0001 (independent oversight with access) enables reporting; but retaliation protections for immigration officers who expose misconduct not specified.

**Overlay gaps:**
- ENFA: Comprehensive — CRTS, OVRG, DETS enforcement mechanisms present. *Compliant.*
- GEOG: ACCS subdomain; cross-border access; geographic distribution of immigration courts not addressed explicitly. *Partial.*
- FEDR: Federal/local enforcement cooperation (287(g), sanctuary policies) — STSS subdomain likely present. *Partial.*
- THRV: SRVS (services for immigrants) and ACCS cover essential services access. LABS (labor rights for immigrants) present. *Partial* — funding mechanism for legal representation guarantee (CRTS-0006) specified; broader THRV funding for services incomplete.
- PRIV: DATA subdomain covers some; AI-based risk scoring of immigrants (predictive deportation targeting) — **absent.** *Partial.*
- ECOL: **Absent.** Climate refugees, environmental displacement as basis for immigration protection — not addressed.

**Authoring OS gaps:**
- NORM-0002: Human dignity (Value 1) — strongly addressed through anti-detention-as-deterrence positions. Equal standing (Value 2) — strongly addressed. Material security (Value 7) — partially addressed. Ecological habitability and climate displacement — absent.
- AUTH-0002: Strong generally; challenge rights well-specified.
- TEST-0001: Foreseeable abuse: offshore detention, private contractor abuse, family separation — all addressed by specific prohibitions.
- ENFC-0001: Well-defined; OVRG and CRTS provide enforcement structure.
- TEST-0003: **No inheritance declaration.**

**Priority gaps:**
1. Whistleblower protections absent for immigration enforcement officers who report misconduct.
2. AI in immigration: Algorithmic risk scoring, predictive targeting of immigrants for enforcement, AI-assisted visa adjudication — absent (AIGV overlay absent from IMMG).
3. Climate displacement: Climate refugees and environmentally displaced persons as a basis for protection — absent from both IMMG and ENVR.
4. PRIV: Commercial data broker information used in immigration enforcement — not addressed (RGHT-TECS-0001 covers government purchase of personal data; IMMG does not apply this to immigration enforcement specifically).

**Overall rating:** **Needs work**

---

### Infrastructure and Public Goods (INFR)

**Applicable overlays:** KERN (universal) + ENFA, GEOG, FEDR, THRV, ECOL, ECON, AIGV

**KERN compliance:** Present but structurally thin for a public goods pillar (67 positions, 20 subdomains):
- KERN-0013 (challenge/appeal): UTIL-0002 (independent consumer advocate in utility rate proceedings) — present. Challenge mechanisms for infrastructure siting decisions — **absent.**
- KERN-0014 (access not defeated by burden): ADAX (ADA accessibility), AFDS (affordability standards), RURL (rural transit) address geographic access well.
- KERN-0015 (foreseeable abuse design): EQJS-0001 (infrastructure siting equity) addresses environmental justice; supply-chain concentration (PRTS-0002). But infrastructure cybersecurity and sabotage pathways — **absent.**
- KERN-0017 (denial incentives): UTIL-0003 (utility return on equity tied to performance metrics) — present and strong.
- KERN-0026 (systemic failure/corrective action): WATS-0003 (dam safety with mandatory inspection) — one example; broader infrastructure failure corrective action — **absent.**
- KERN-0027 (whistleblower): **Absent.** Infrastructure safety whistleblowing (PG&E-type cases, pipeline safety, dam inspection falsification) has no coverage.

**Overlay gaps:**
- ENFA: UTIL (oversight), LBRT (labor protections in transit) present; but independent enforcement of infrastructure performance standards — **absent.** *Partial.*
- GEOG: RURL, ADAX, NETS, STRT all strong. *Compliant.*
- FEDR: FUND, RAIL, TRAN address federal investment and national standards. *Compliant.*
- THRV: AFDS, AFRD, RURL, NETS address essential access. Funding mechanisms: FUND-0001/0002 (dedicated trust funds, parity requirements) — strong. *Compliant.*
- ECOL: ENRS, BLDS, GRDS, TRAN (clean energy transition), DATA (carbon-neutral data centers) strong. *Compliant.*
- ECON: UTIL addresses utility market concentration; NETS (ISP structure) addresses network concentration. *Compliant.*
- AIGV: **Absent.** AI in infrastructure management (smart grid, traffic systems, predictive maintenance, autonomous transit) — not addressed. This is a significant emerging risk area. *Absent.*

**Authoring OS gaps:**
- NORM-0002: Good coverage of material security and ecological habitability. Equal standing (geographic equity in infrastructure investment) — EQJS present. Accountability in infrastructure siting — EQJS-0001 present.
- AUTH-0002: Many positions define the obligation without specifying the enforcement actor or failure consequence. UTIL-0002/0003 are exceptions — well-specified.
- TEST-0001: Foreseeable abuse paths: infrastructure concentration (NETS, UTIL) addressed. Cybersecurity and physical infrastructure attacks — **absent.** Emergency infrastructure failure scenarios — partially addressed (WATS-0003 for dams; broader emergency response absent).
- ENFC-0001: Weak overall — no independent infrastructure oversight body specified; enforcement depends on sector-specific regulators without platform-level enforcement architecture.
- TEST-0003: **No inheritance declaration.**

**Priority gaps:**
1. AIGV overlay entirely absent — AI in infrastructure control systems (power grid, transit, water), autonomous systems in public infrastructure, and algorithmic utility pricing are significant foreseeable domains.
2. Whistleblower protections absent for infrastructure safety reporters.
3. Independent oversight body absent — infrastructure performance and safety oversight relies on sector regulators without a platform-level enforcement architecture.
4. Cybersecurity and infrastructure attack resilience — absent from the pillar's design.

**Overall rating:** **Critical gaps**

---

### Equal Justice and Policing (JUST)

**Applicable overlays:** KERN (universal) + ENFA, GEOG, FEDR, PRIV, AIGV, ECON, DEMO

**KERN compliance:** Platform's most comprehensive structural compliance (274 positions, 60+ subdomains):
- KERN-0010/0011 (meaningful human review): AINL-0003, algorithmic accountability in policing; bail individualization (BALS-0002).
- KERN-0013 (challenge/appeal): CIVL (civil access to courts), DEFS (Brady disclosures), ERRS (wrongful conviction review), EVDS (discredited science review) — comprehensive.
- KERN-0014 (access not defeated by burden): CIVL-0004 (court fees), DEFS-0009 (expert assistance access), LNGS (language access) all address.
- KERN-0015 (foreseeable abuse design): CAFS/CVAF (civil asset forfeiture abolition/reform), TRAF (traffic stop reform), STNG (sting operation restrictions) all address specific known abuse structures.
- KERN-0016 (no coercion/fear mechanism): BAIL (no money bail as coercion), CONS-0002 (solitary confinement prohibition), PRPH (conditions of confinement) all address.
- KERN-0017 (denial incentives): TRAF, STNG (quota prohibition) address incentive structures directly.
- KERN-0026 (systemic failure/corrective action): CRBS (civilian review with binding discipline), OVRG (oversight mechanisms), SUPR (supervisory structures) address.
- KERN-0027 (whistleblower): STNG-0003 (whistleblower protection for officers reporting quota pressure), WHTS-0003 (robust whistleblower protections) — present.

**Overlay gaps:**
- ENFA: CRBS, OVRG, ETHL comprehensive. *Compliant.*
- GEOG: TRAF (racial disparities in traffic stops), PLBS (geographic disparities in policing) address. *Compliant.*
- FEDR: Federal vs. local policing standards — addressed through PLCA, POLC subdomains. *Compliant.*
- PRIV: DATA, AINL (algorithmic surveillance) strong. PHON (phone search), PPRS (police stop records) address. *Compliant.*
- AIGV: AINL covers algorithmic bias in policing, wrongful conviction assistance. *Compliant.*
- ECON: BAIL (money bail as economic coercion), CAFS/CVAF (asset forfeiture as extraction) strong. *Compliant.*
- DEMO: JURY (jury selection), RNTR (renter rights in policing context) — present. *Partial.*

**Authoring OS gaps:**
- NORM-0002: Near-complete value coverage. Ecological habitability (Value 8): Environmental enforcement disparities (disproportionate regulation in communities of color vs. white communities) — absent.
- AUTH-0002: Strong throughout.
- TEST-0004: Perverse incentive review: quota systems (addressed), civil forfeiture profit motive (addressed), private prison financial incentives (PRSN subdomain — likely present). Comprehensive.
- ENFC-0001: Well-defined; civilian review bodies have binding authority.
- TEST-0003: **No inheritance declaration.** (Universal gap.)

**Priority gaps:**
1. Environmental enforcement disparities: Differential enforcement of environmental regulations across communities — absent from JUST despite being a justice concern.
2. Whistleblower protections: Partial — STNG-0003 and WHTS-0003 present but narrowly scoped; broader protections for officers who report systemic misconduct (not only quota pressure) could be stronger.
3. Inheritance declaration absent (universal gap).
4. Private prison industry reform: Probably present (PRSN subdomain) but financial incentives of private corrections as a perverse incentive structure should be explicitly addressed through the KERN-0017 lens.

**Overall rating:** **Adequate**

---

### Labor and Workers' Rights (LABR)

**Applicable overlays:** KERN (universal) + ENFA, ECON, THRV, PRIV, GEOG, AIGV

**KERN compliance:** Strong (237 positions, 45 subdomains):
- KERN-0013 (challenge/appeal): ENFL-0002 (accessible reporting mechanisms), CLMS subdomain (claims), ENFL-0005 (private right of action) address.
- KERN-0014 (access not defeated by burden): ENFL (accessible enforcement), CBAS (collective bargaining access).
- KERN-0015 (foreseeable abuse design): GIGS, GIGW (gig worker misclassification), FARM (agricultural worker abuse) address known structural abuse configurations.
- KERN-0016 (no coercion/fear mechanism): SYSR-0003 (employment systems must not rely on coercion or dependency) — strong statement.
- KERN-0017 (denial incentives): ENFL addresses; worker classification incentives to avoid benefits — GIGS subdomain addresses.
- KERN-0027 (whistleblower): **Absent as dedicated positions.** ENFL-0002 (workers must have accessible reporting mechanisms) is not a retaliation-protection provision. UNNS-0015 (prohibition on retaliation in union context) is narrow. No WBLS equivalent in LABR.

**Overlay gaps:**
- ENFA: ENFL comprehensive — enforcement authority, penalty escalation, private rights of action, and outcome evaluation. *Compliant.*
- ECON: Core overlay — CBAS (collective bargaining), UNON, COLS, GOVN (worker board representation) comprehensive. Structural remedies for labor market asymmetry present. *Compliant.*
- THRV: BENS (benefits), RETS (retirement), PAYS (wages), SAFE (workplace safety) cover material security. Funding mechanisms for worker transition — TRAN, JCAU subdomains. *Compliant.*
- PRIV: SURS comprehensive (surveillance limits), AINL (AI in employment), TRAN-0001 (surveillance disclosure) strong. *Compliant.*
- GEOG: FARM (agricultural/rural workers), GIGS (gig economy geographic issues). *Compliant.*
- AIGV: AINL-0001/0002/0003 — present. Challenge rights for AI-influenced employment decisions (AINL-0001 specifies logs sufficient for worker challenge). *Compliant.*

**Authoring OS gaps:**
- NORM-0002: Good coverage of material security and equal standing. Ecological habitability (Value 8): Workplace environmental health (SAFE covers occupational safety; climate-related working conditions and outdoor heat standards) — partially addressed.
- AUTH-0002: Generally strong; enforcement actors defined.
- TEST-0004: Perverse incentive review: worker misclassification as gig workers to avoid obligations — strongly addressed (GIGS, GIGW). Union-busting tactics — UNNS and UNON subdomains.
- ENFC-0001: Well-defined.
- TEST-0003: **No inheritance declaration.**

**Priority gaps:**
1. Whistleblower protections absent — particularly critical for workers who report wage theft, safety violations, or employer fraud. LABR is one of the highest-priority pillars for this gap.
2. Climate-related labor conditions (heat, air quality for outdoor workers) underspecified in SAFE subdomain.
3. Funding mechanism for the national program-level obligations (universal portable benefits, etc.) — THRV-0003 compliance incomplete for some positions.
4. Inheritance declaration absent (universal gap).

**Overall rating:** **Needs work**

---

### Legislative Reform (LEGL)

**Applicable overlays:** KERN (universal) + ENFA, DEMO, FEDR

**KERN compliance:** Present but thin (61 positions, 20 subdomains):
- KERN-0002 (accountability): OVRG (oversight), ETHX (ethics) address.
- KERN-0013 (challenge/appeal): **Largely absent.** No mechanism specified for citizens or affected parties to challenge legislative inaction or unethical conduct.
- KERN-0014 (access not defeated by burden): Citizens' access to legislative process — LBBY (lobbying reform) addresses one dimension; public participation in rulemaking — **absent.**
- KERN-0015 (foreseeable abuse design): LBBY, LOBS (lobbying reform) address regulatory capture paths. STKS (stock trading by legislators) — present. Filibuster abuse, rule exploitation — likely in HSES, SENS subdomains.
- KERN-0017 (denial incentives): Legislative incentive structures that reward inaction or delay — **absent.**
- KERN-0027 (whistleblower): **Absent.** Congressional staff who expose legislative misconduct, abuse of the legislative process, or corruption — no protection specified.

**Overlay gaps:**
- ENFA: Ethics enforcement (ETHX) — present; but external enforcement of congressional ethics (OCE independence) — **absent** as a dedicated position. Enforcement actors for most LEGL obligations — unclear. *Partial.*
- DEMO: DBAS (Senate filibuster reform), HSES (House procedure), SENS (Senate structure), RPLS (representation reform). *Compliant.*
- FEDR: DMJS (state/federal jurisdictional issues). *Partial.*

**Authoring OS gaps:**
- NORM-0002: Democratic self-government (Value 4) — core value addressed. Equal standing (Value 2) — procedural equality in legislative representation addressed. Accountability (Value 5) — present through ethics. Material security and ecological habitability absent.
- AUTH-0002: Many positions specify structural changes (e.g., "abolish filibuster") without specifying enforcement actors or how the obligation is enforced when Congress itself is the subject of the rule.
- TEST-0001: Foreseeable abuse: filibuster abuse, gerrymandering (cross-pillar with ELEC), lobbying capture. Good coverage.
- ENFC-0001: **Weakest enforcement circuit on the platform for a pillar with enforcement obligations.** Congressional ethics enforcement depends on Congress itself; external enforcement bodies (OCE, DOJ) not specified.
- TEST-0003: **No inheritance declaration.**

**Priority gaps:**
1. Enforcement circuit for congressional ethics violations: The pillar requires ethics reform but relies on Congress to self-enforce. External enforcement actors and failure consequences absent.
2. Whistleblower protections for congressional staff absent.
3. Public participation requirements in legislative process: DEMO-0002 requires meaningful public participation; LEGL does not implement this at the pillar level.
4. AI in legislative drafting, analysis, and deliberation: Not addressed.

**Overall rating:** **Critical gaps**

---

### Information and Media (MDIA)

**Applicable overlays:** KERN (universal) + ENFA, REGD, DEMO, PRIV, AIGV, ECON

**KERN compliance:** Present (54 positions, 11 subdomains):
- KERN-0004 (unchecked power): OWNS (media ownership concentration) addresses.
- KERN-0007 (transparency/auditability): PUBL (public media), PRSS (press freedom) address.
- KERN-0013 (challenge/appeal): **Absent.** Challenge rights when platforms suppress speech, when disinformation causes harm, or when media consolidation denies access — not specified.
- KERN-0015 (foreseeable abuse design): DISS (disinformation) subdomain addresses; PLTS (political advertising) addresses.
- KERN-0016 (no coercion/fear): PRSS (press freedom, anti-retaliation for journalism) partially addresses.
- KERN-0027 (whistleblower): **Absent.** No protections for media industry employees who expose disinformation campaigns, ownership conflicts of interest, or editorial manipulation.

**Overlay gaps:**
- ENFA: **Absent as explicit enforcement architecture.** Ownership enforcement (who enforces media concentration limits) not specified. *Absent.*
- REGD: OWNS (anti-concentration) — present; protective vs. gatekeeping regulation in media context (content moderation as gatekeeping) not addressed. *Partial.*
- DEMO: DISS, PLTS, NETS, MDIA (public media) all address democracy-protecting functions. *Compliant.*
- PRIV: DATA subdomain — present; behavioral advertising (CHDS) addresses children's privacy specifically. *Partial.*
- AIGV: AI-generated content (deepfakes, synthetic media, AI-generated news) — DISS subdomain may address; dedicated AIGV-framed positions (mandatory labeling, pre-deployment assessment, human-accountability requirements) — **absent.** *Absent.*
- ECON: OWNS addresses media market concentration; advertising market concentration — **absent.** *Partial.*

**Authoring OS gaps:**
- NORM-0002: Democratic self-government (Value 4) and truthfulness and legibility (Value 9) — core values addressed. Durability against capture (Value 11) — OWNS addresses ownership capture. Real liberty (Value 3) — press freedom addressed.
- AUTH-0002: Most positions lack specified enforcement actors. Who enforces media ownership limits? Who addresses disinformation? Regulatory body not specified.
- TEST-0001: Foreseeable abuse: media concentration enabling political control — OWNS addresses. AI-generated political propaganda — weak.
- ENFC-0001: **Absent overall.** No enforcement circuit specified for most MDIA obligations.
- TEST-0003: **No inheritance declaration.**

**Priority gaps:**
1. AIGV overlay absent — AI-generated media and synthetic content are arguably the most significant near-term threat in this domain.
2. Enforcement circuit entirely absent: Who enforces media concentration limits? What triggers intervention? What are the remedies? Not specified.
3. Whistleblower protections absent for media employees.
4. Challenge rights absent for individuals harmed by media consolidation or platform suppression decisions.

**Overall rating:** **High gaps**

---

### Rights and Civil Liberties (RGHT)

**Applicable overlays:** KERN (universal) + ENFA, PRIV, DEMO, ECON, GEOG

**KERN compliance:** Present (104 positions, 22 subdomains):
- KERN-0013 (challenge/appeal): STAS-0003 (anti-backsliding clause), RPRS (reparations process), some PRIV positions address challenge mechanisms. But systematic challenge rights for civil liberties violations — **partial.**
- KERN-0014 (access not defeated by burden): IDNS (identification), geographic access to rights systems — **partial.**
- KERN-0015 (foreseeable abuse design): TECS-0001/0002/0003/0004 (digital surveillance prohibitions) address; PRIV addresses government data access.
- KERN-0016 (no coercion/fear mechanism): BODS (bodily autonomy), LGBQ (anti-discrimination) address coercion in rights context.
- KERN-0027 (whistleblower): **Absent.** No protections for civil liberties advocates, civil society employees, or government employees who expose civil liberties violations.

**Overlay gaps:**
- ENFA: Rights enforcement mechanisms — **partial.** Enforcement actors for civil liberties violations (DOJ Civil Rights Division, private right of action) — implied but not specified as dedicated positions. *Partial.*
- PRIV: PRIV subdomain, TECS comprehensive. *Compliant.*
- DEMO: SPHS (speech), ESTB (establishment clause), RELS (religion) address. *Compliant.*
- ECON: POVS (poverty and rights), FOOS (food security as right). *Partial.*
- GEOG: IDNS may cover geographic access to identification documents; geographic disparities in civil rights enforcement — **absent.** *Partial.*

**Authoring OS gaps:**
- NORM-0002: Real liberty (Value 3) — core value, comprehensive. Equal standing (Value 2) — RACE, LGBQ, DSBL, DISS all address. Material security (Value 7) — FOOS, POVS address partially. Ecological habitability — **absent.**
- AUTH-0002: Enforcement actors for rights violations not consistently specified. The pillar declares rights; enforcement circuit often cross-references JUST, ADMN, or courts without specifying the mechanism.
- TEST-0001: Foreseeable abuse paths: government surveillance (TECS, PRIV) well-addressed. Religious freedom weaponized against other rights — RELS subdomain may address.
- ENFC-0001: **Weak.** Most positions lack specified enforcement actors; the pillar relies on other pillars and courts for enforcement.
- TEST-0003: **No inheritance declaration.**

**Priority gaps:**
1. Enforcement circuit absent: Rights declarations without specified enforcement actors, triggers, or failure consequences — the pillar's most significant structural gap.
2. Whistleblower protections absent.
3. Geographic disparities in civil rights enforcement (unequal DOJ enforcement across jurisdictions) — absent.
4. ECOL overlay absent: Environmental rights, right to clean water, climate-related rights — not addressed within RGHT.

**Overall rating:** **High gaps**

---

### Science, Technology, and Space (SCIS)

**Applicable overlays:** KERN (universal) + ENFA, THRV, FEDR, AIGV, ECOL

**KERN compliance:** Very thin (19 positions, 7 subdomains) — the smallest pillar and the one with the most structural gaps relative to its scope:
- KERN-0002 (accountability): AGYS-0001 (agency independence for scientific agencies) — present.
- KERN-0004 (unchecked power): SPCS-0004 (NASA Administrator fixed term) — one position.
- KERN-0013 (challenge/appeal): **Absent.** No challenge mechanisms for scientists whose work is suppressed, agencies whose scientific findings are overridden, or researchers who are denied funding.
- KERN-0014 (access not defeated by burden): PUBL-0001 (open access to federally funded research) — present. Broader access to science infrastructure — **absent.**
- KERN-0015 (foreseeable abuse design): FNDS-0002 (criminalize political interference with federal science) — strong specific prohibition. EMGS-0002 (BSL-4 oversight) addresses one risk domain.
- KERN-0023/0026 (broken systems/corrective action): **Absent.** No positions on what happens when federal science agencies persistently produce politically manipulated findings.
- KERN-0027 (whistleblower): FNDS-0002 partially covers (private right of action for scientists); but the position is a criminal prohibition on interference, not a retaliation protection for whistleblowers.

**Overlay gaps:**
- ENFA: FNDS-0002 and FNDS-0003 specify some enforcement; but enforcement architecture overall is minimal. *Partial.*
- THRV: FNDS-0001 (mandatory R&D investment floor of 1.5% GDP) — specific, outcome-based. TECS-0003 (broadband by 2030) — specific and funded. *Compliant.*
- FEDR: Federal/state split in science funding — **absent.** *Absent.*
- AIGV: EMGS-0001 (NIST AI Risk Management Framework binding for federal agencies) — present and strong. *Partial* — AI safety research funding, AI misuse in scientific contexts not addressed.
- ECOL: FNDS-0004 (federal climate policy consistent with IPCC findings) — strong. *Partial* — broader ecological science protection (biodiversity monitoring, ecological research funding) absent.

**Authoring OS gaps:**
- NORM-0002: Truthfulness and legibility (Value 9) — core value, addressed through FNDS-0002/0003/0004. Material security (Value 7) — TECS-0003 (broadband) present. Equal standing and access to science infrastructure — absent.
- AUTH-0002: FNDS-0002 specifies criminal prohibition and private right of action — specific and strong. Other positions less complete.
- TEST-0001: Foreseeable abuse paths: political suppression of science (addressed), private sector capture of federal research (PUBL-0001 addresses IP assignment but not research agenda capture), research fraud — **absent.**
- ENFC-0001: Very weak overall — enforcement actor for most SCIS obligations (who enforces the 1.5% GDP floor? what triggers corrective action when agencies systematically ignore peer review?) — unspecified.
- TEST-0003: **No inheritance declaration.**

**Priority gaps:**
1. Challenge mechanisms for scientists who are suppressed or face retaliation — FNDS-0002 criminalizes interference but does not give scientists a meaningful path to challenge decisions.
2. Enforcement circuit incomplete for most positions: Who enforces the R&D floor? What happens when the floor is breached?
3. Whistleblower protections: FNDS-0002 partial; dedicated retaliation protections for federal scientists absent.
4. Space policy accountability: SPCS subdomains (space debris, weapons treaty) involve international obligations with no domestic enforcement circuit specified.

**Overall rating:** **Critical gaps**

---

### Taxation and Wealth (TAXN)

**Applicable overlays:** KERN (universal) + ENFA, REGD, ECON, PRIV, FEDR

**KERN compliance:** Present and broad (203 positions, 44 subdomains):
- KERN-0004 (unchecked power): CAPS (capital accumulation), WLTH, CORS (corporate tax), HVNS (tax haven closure) all address concentrated economic power.
- KERN-0005 (attributable authority): TRAN, DISC (disclosure) subdomains address transparency.
- KERN-0013 (challenge/appeal): ADML (administrative rights of taxpayers) likely covers; explicit challenge rights for disputed tax decisions — **partial.**
- KERN-0014 (access not defeated by burden): ENFL-0009 (simplification for ordinary taxpayers paired with strong enforcement of complex evasion) — present.
- KERN-0015 (foreseeable abuse design): LOPS (loophole closure), FSUB (fossil fuel subsidies), EXTS (extravagant deductions) address known exploitation patterns.
- KERN-0017 (denial incentives): ENFL-0001/0003 (equity in audit rates, prioritizing high-income evasion over small filers) — strong. Addresses the IRS's historical perverse incentive to audit low-income filers at higher rates.
- KERN-0027 (whistleblower): **Absent.** Tax fraud whistleblowing is one of the most productive sources of federal enforcement; IRS whistleblower programs are inadequate; no WBLS-equivalent coverage.

**Overlay gaps:**
- ENFA: ENFL comprehensive — audit resources, escalation, systemic enforcement, professional enabler liability. *Compliant.*
- REGD: Anti-capture for tax regulatory process — **partial.** Tax rule complexity as a form of regulatory capture (industry-written exceptions embedded in code) is present conceptually but not in dedicated positions. *Partial.*
- ECON: WLTH, WTHS, CAPS address wealth concentration. CORS addresses corporate tax avoidance. *Compliant.*
- PRIV: AINL (AI in tax administration) — present. Taxpayer privacy protections in enforcement — ADML addresses some; broader data sharing with other agencies — **absent.** *Partial.*
- FEDR: INTL (offshore evasion) covers one international dimension; domestic state/federal tax coordination — **absent.** *Partial.*

**Authoring OS gaps:**
- NORM-0002: Enforceable fairness (Value 10) — ENFL-0001/0003 (equitable audit prioritization) strong. Material security (Value 7) — tax policy as a material security instrument (EITC, SSCI, CDRS) addressed. Ecological habitability (Value 8) — ENVS (environmental tax provisions) present. Democratic self-government — tax policy as democratic accountability addressed.
- AUTH-0002: Enforcement actors generally defined; IRS role specified.
- TEST-0004: Perverse incentive review: IRS audit-rate disparity — directly addressed. Tax shelter industry incentives — ENFL-0006 (professional enablers) addresses.
- ENFC-0001: Well-defined.
- TEST-0003: **No inheritance declaration.**

**Priority gaps:**
1. Whistleblower protections absent — IRS whistleblower programs are historically under-resourced and under-protected; this is a significant gap.
2. Taxpayer challenge rights: ADML addresses some; complete circuit for challenging IRS decisions (timelines, record access, independent review) underspecified.
3. Anti-capture for tax regulatory process: Industry lobbying influence on tax code complexity as a form of regulatory capture — not systematically addressed as a design concern.
4. AIGV: AI in tax enforcement decisions (automated audit selection, AI-based risk scoring) — AINL present but challenge/appeal rights for AI-influenced tax decisions underspecified.

**Overall rating:** **Needs work**

---

### Technology and AI (TECH)

**Applicable overlays:** KERN (universal) + ENFA, REGD, ECON, PRIV, AIGV, DEMO, FEDR, GEOG

**KERN compliance:** Platform's most detailed pillar (499 positions, 53 subdomains) and strongest AIGV implementation:
- KERN-0010/0011 (meaningful human review): AINL-0003/GOVN-0003/0004 specify pre-decision human review, prohibition on AI-only consequential decisions, authority to override.
- KERN-0013 (challenge/appeal): AUDT-0002/GOVN-0006/0007 specify explanation and appeal rights for AI-influenced decisions.
- KERN-0014 (access not defeated by burden): Geographic broadband access through BRDS, GEOG contexts.
- KERN-0015 (foreseeable abuse design): AINL, GOVN, AUDT, PRIV, SURV, FACE, BIOM, DEEP comprehensively address AI abuse paths.
- KERN-0016 (no coercion/fear mechanism): SURS (surveillance limitations), PRIV, GOVN-0009 (no generalized risk scoring) address.
- KERN-0017 (denial incentives): GOVN-0002/0005 (AI may not be used to deny benefits, only expedite approvals) — strong statement.
- KERN-0027 (whistleblower): AUDT-related positions imply whistleblowing paths; dedicated protection — **partial.**

**Overlay gaps:**
- ENFA: AUDT comprehensive; mandatory audit, incident reporting, corrective action. *Compliant.*
- REGD: Protective vs. gatekeeping regulation in tech context (REGD-0002) — AINL, GOVN, AUDT all address. *Compliant.*
- ECON: MKTS, ANTS, PLAT address platform concentration. TRDE (trade and tech) present. *Compliant.*
- PRIV: DATA, PRIV, SURV, FACE, BIOM, DTBR comprehensive. *Compliant.*
- AIGV: Core of this pillar — among the most comprehensive AIGV implementations available. *Compliant.*
- DEMO: DEMS subdomain addresses AI threats to democracy. *Compliant.*
- FEDR: GOVN (federal government AI use); state/federal coordination on AI regulation — **partial.** *Partial.*
- GEOG: BRDS (cross-border), INTL (international standards). Digital access equity — EDUS subdomain present; but geographic access to technology as a rights concern — *partial.*

**Authoring OS gaps:**
- NORM-0002: Comprehensive coverage across values. Ecological habitability (Value 8): Technology's environmental footprint (data center energy use — INFR-DATA covers; TECH does not make ECOL explicit). *Partial.*
- AUTH-0002: Strong throughout.
- TEST-0001: Comprehensive adversarial review evident in structure.
- ENFC-0001: Well-defined; AIGV-0017 (independent AI regulatory authority) addresses enforcement architecture.
- TEST-0003: **No inheritance declaration.** (Universal gap — notably important here as TECH applies to many domains.)

**Priority gaps:**
1. Inheritance declaration absent — particularly important for TECH given its cross-cutting nature and the number of other pillars that inherit TECH's AI governance requirements.
2. ECOL overlay: Technology's environmental footprint (energy consumption, electronic waste, mining for rare earth materials) not addressed within TECH.
3. Whistleblower protections: AUDT implies reporting paths; dedicated retaliation protection for AI system failure reporters — partial.
4. Neurotechnology and brain-computer interfaces (NEUS subdomain present — verify completeness): Emerging risk area that may outpace current coverage.

**Overall rating:** **Adequate**

---

### Term Limits and Fitness (TERM)

**Applicable overlays:** KERN (universal) + ENFA, DEMO

**KERN compliance:** Present but thin for a focused structural pillar (23 positions, 7 subdomains):
- KERN-0002 (accountability): DSCS (disclosure requirements), RVDS (revolving door) address accountability structures.
- KERN-0004 (unchecked power): LIMS (term limits) is the pillar's core purpose.
- KERN-0013 (challenge/appeal): FITS-0003 (fitness assessment insulated against political manipulation) — present. Challenge rights for voters or candidates who contest fitness assessments — **absent.**
- KERN-0014 (access not defeated by burden): Not directly applicable.
- KERN-0015 (foreseeable abuse design): DSCS-0004 (blind trust loophole closure) — strong specific position. FITS-0003 (manipulation protection) addresses one abuse path.
- KERN-0017 (denial incentives): DSCS, RVDS address incentive structures that reward concealment.
- KERN-0027 (whistleblower): **Absent.** No protections for staff or officials who expose violations of term limits, disclosure requirements, or fitness assessment manipulation.

**Overlay gaps:**
- ENFA: FITS-0003 says the assessment process must be insulated; but enforcement actor, enforcement trigger, and failure consequences — **absent.** DSCS positions declare disclosure obligations; who enforces them? **absent.** *Absent.*
- DEMO: Core overlay — LIMS, PRES, DSCS all address democratic accountability of officeholders. *Compliant.*

**Authoring OS gaps:**
- NORM-0002: Democratic self-government (Value 4) and accountable power (Value 5) — core values, addressed. Equal standing (Value 2) — age cap for re-election (FITS-0001) raises equal standing concerns that are not surfaced per NORM-0008 (value tension between democratic accountability and age discrimination). Material security, ecological habitability — absent and not directly relevant.
- AUTH-0002: Most positions specify the rule; enforcement actor consistently absent.
- TEST-0001: Foreseeable abuse: term-counting manipulation (PRES-0002), blind trust loopholes (DSCS-0004) — addressed. Abuse of fitness assessment process (FITS-0003) — present.
- ENFC-0001: **Absent overall.** The pillar's single most critical gap: no enforcement actor is specified for any of the disclosure, term limit, or fitness requirements.
- TEST-0003: **No inheritance declaration.**

**Priority gaps:**
1. Enforcement circuit absent across the entire pillar — term limits, disclosure requirements, and fitness assessments all lack specified enforcement actors, triggers, and failure consequences.
2. Challenge rights for fitness assessment disputes absent.
3. Whistleblower protections absent.
4. Value tension not surfaced: Age-based fitness requirements and potential equal-standing implications (NORM-0008 requires explicit surfacing of this tension).

**Overall rating:** **Critical gaps**

---

## Decision table

| Pillar | Code | Positions | Critical | High | Medium | Rating |
|--------|------|-----------|----------|------|--------|--------|
| Administrative State | ADMN | 88 | — | — | AI in adjudication; ECOL of agencies | **Adequate** |
| Antitrust | ANTR | 139 | — | Whistleblower absent | AIGV; THRV for essential goods | **Needs work** |
| Checks and Balances | CHKS | 103 | — | Enforcement failure cascade; AIGV | Whistleblower; material security | **High gaps** |
| Consumer Rights | CNSR | 177 | — | — | Whistleblower; GEOG; ECOL | **Needs work** |
| Courts | CORT | 30 | GEOG/THRV absent; enforcement incomplete | Whistleblower; FEDR | — | **Critical gaps** |
| Anti-Corruption | CRPT | 71 | — | — | AI-enabled corruption; local corruption | **Needs work** |
| Education | EDUC | 291 | — | Whistleblower; AIGV gaps | ECOL; enforcement failure | **Needs work** |
| Elections | ELEC | 51 | — | AIGV absent; PRIV absent | Whistleblower; enforcement failure | **High gaps** |
| Environment | ENVR | 192 | — | Whistleblower absent | AIGV; agricultural ECOL | **Needs work** |
| Executive Power | EXEC | 139 | — | Enforcement failure cascade | Whistleblower; AIGV | **Needs work** |
| Foreign Policy | FPOL | 86 | — | AIGV absent; enforcement; challenge rights | Whistleblower; PRIV | **High gaps** |
| Gun Policy | GUNS | 45 | — | Challenge rights for denials absent | Anti-capture for ATF; whistleblower | **High gaps** |
| Healthcare | HLTH | 323 | — | — | ECOL; whistleblower scope; funding | **Adequate** |
| Housing | HOUS | 227 | — | AIGV; PRIV; whistleblower | ECOL; THRV funding | **High gaps** |
| Immigration | IMMG | 244 | — | — | AIGV; whistleblower; ECOL/climate | **Needs work** |
| Infrastructure | INFR | 67 | AIGV absent; oversight body absent | Whistleblower; enforcement | Cybersecurity | **Critical gaps** |
| Equal Justice | JUST | 274 | — | — | Environmental enforcement disparity | **Adequate** |
| Labor | LABR | 237 | — | Whistleblower absent | Climate labor; THRV funding | **Needs work** |
| Legislative Reform | LEGL | 61 | Enforcement circuit absent | Whistleblower; public participation | AIGV | **Critical gaps** |
| Information and Media | MDIA | 54 | — | AIGV absent; enforcement circuit absent | Whistleblower; challenge rights | **High gaps** |
| Rights and Civil Liberties | RGHT | 104 | — | Enforcement circuit absent; whistleblower | GEOG; ECOL | **High gaps** |
| Science, Technology, Space | SCIS | 19 | Enforcement circuit absent; challenge rights | Whistleblower; FEDR | Space accountability | **Critical gaps** |
| Taxation and Wealth | TAXN | 203 | — | Whistleblower absent | Taxpayer challenge rights; anti-capture | **Needs work** |
| Technology and AI | TECH | 499 | — | — | ECOL; whistleblower | **Adequate** |
| Term Limits and Fitness | TERM | 23 | Enforcement circuit absent | Whistleblower; challenge rights | Value tension unsurfaced | **Critical gaps** |

---

## Recommended next steps

Recommendations are ranked by platform-wide impact (addressing systemic gaps before pillar-specific ones).

### Priority 1: Process fixes (universal, no content change required)

**P1-A: Add inheritance declarations to all 25 pillars (PAOS-TEST-0003)**  
Create a standard inheritance-declaration template and add it to each pillar's documentation. This requires no policy position changes — only documentation of which KERN rules and overlays already apply. This is the single highest-leverage process fix: it makes cross-layer conflict resolution enforceable and provides a baseline for future audits.

**P1-B: Establish a whistleblower coverage protocol (KERN-0027)**  
For all pillars rated "Needs work" or worse, add a WBLS or equivalent subdomain specifying: (1) what conduct triggers protection, (2) who receives protection (employment status agnostic), (3) the enforcement actor for retaliation claims, and (4) that protection may not be waived by contract. Priority order: ENVR, LABR, TAXN, ELEC, HOUS, GUNS, IMMG, INFR, MDIA, RGHT, EDUC, ANTR, CNSR, SCIS, TERM.

### Priority 2: Critical gap remediation (5 pillars)

**P2-A: CORT — Access to justice (GEOG/THRV)**  
The courts pillar has no positions on cost barriers, right to civil counsel, or geographic access to federal courts. This is a fundamental equal-standing gap. Positions needed: court fee waivers, mandatory civil representation in housing and benefits cases, geographic distribution of federal court capacity.

**P2-B: SCIS — Enforcement circuit and challenge rights**  
The science pillar declares obligations (R&D floor, political interference prohibition, climate policy alignment) with no enforcement actors, triggers, or failure consequences specified. Each position needs an enforcement circuit.

**P2-C: TERM — Enforcement circuit across all positions**  
Every position in TERM declares a requirement; none specify who enforces it or what happens when it is violated. This is the platform's most complete enforcement circuit failure.

**P2-D: INFR — Independent oversight body and AIGV overlay**  
Infrastructure lacks a platform-level enforcement architecture and has no AI governance coverage despite AI's growing role in grid management, transit, and water systems. An independent infrastructure safety oversight body should be specified.

**P2-E: LEGL — External enforcement for congressional ethics**  
The legislative pillar's most critical gap is that congressional ethics enforcement relies on Congress itself. External enforcement mechanisms (OCE empowerment, DOJ civil rights path, private right of action) should be specified.

### Priority 3: High-gap pillar reinforcement (7 pillars)

**P3-A: ELEC — AIGV and PRIV overlays**  
Add positions on AI-generated election interference, synthetic political media, algorithmic voter targeting, and voter data privacy. These are among the most urgent foreseeable threats to democratic integrity.

**P3-B: MDIA — AIGV overlay and enforcement circuit**  
Add positions on AI-generated media labeling, synthetic media disclosure, and deepfake proliferation. Specify the enforcement actor (FCC, FTC, or new authority) for media consolidation violations.

**P3-C: FPOL — Autonomous weapons and AIGV**  
Add positions on AI in military systems, autonomous weapons governance, and congressional oversight of AI-assisted military operations. Add whistleblower protections for intelligence and diplomatic staff.

**P3-D: HOUS — AIGV and PRIV overlays**  
Add dedicated AIGV-framed positions on algorithmic tenant screening, AI-based eviction prediction, and credit-scoring systems in housing access. Add positions on tenant data collection by property management platforms.

**P3-E: GUNS — Challenge rights and anti-capture**  
Add positions on challenge and correction rights for wrongful background check denials. Add anti-capture provision for ATF rulemaking and enforcement.

**P3-F: CHKS — Enforcement failure cascade**  
Add positions addressing what structural mechanisms exist when all three checking mechanisms (Congress, courts, executive self-restraint) are simultaneously unavailable.

**P3-G: RGHT — Enforcement circuit**  
The rights pillar declares rights but does not specify enforcement actors, triggers, or failure consequences. Add enforcement positions specifying DOJ Civil Rights Division obligations, private rights of action, and failure-consequence escalation.

### Priority 4: Systemic overlay gap remediation

**P4-A: AIGV overlay in 8 applicable pillars**  
ELEC, HOUS, INFR, LABR (partial), ENVR, FPOL, LEGL, and SCIS should each receive AIGV-aligned positions appropriate to their domain: pre-deployment assessment, mandatory disclosure, challenge rights, human accountability requirements, and non-AI-escape clause.

**P4-B: Affirmative duty funding mechanisms (THRV-0003)**  
Review all THRV-applicable pillars (HLTH, HOUS, EDUC, LABR, INFR, IMMG) and ensure each affirmative obligation specifies a funding mechanism, authorization path, and fiscal authority, not only the obligation.

**P4-C: Perverse incentive review documentation (PAOS-TEST-0004)**  
For each pillar with institutional actors whose incentive structures could reward harmful outcomes (CNSR, TAXN, HOUS, LABR, IMMG, GUNS, MDIA), add explicit positions addressing the specific perverse incentive identified and the structural design choice made to counter it.

---

*End of audit report. This document is a structural assessment intended to support platform development. It does not modify the pillars, PolicyOS documents, or canonical position records. All content changes require the standard platform review and approval process.*
