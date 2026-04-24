# Policy Catalog Reconciliation Report

> **READ-ONLY REPORT** — No HTML or DB changes were made.
> Phase 2 migration may begin only after Ali signs off on this report.

---

## Summary

| Item | Count |
|------|-------|
| HTML policy cards (total) | 2,935 |
| HTML cards with valid ID | 2,905 |
| HTML cards with NO ID | 0 |
| HTML cards: div id ≠ code element id | 1,535 |
| HTML cards: invalid ID format | 30 |
| DB policy_items (total) | 1,554 |
| **Confirmed match** (in both HTML & DB) | **1,553** |
| Text divergence (same ID, different text) | 992 |
| **HTML-only** (on site, not in DB) | **1,277** |
| **DB-only** (in DB, not on site) | **1** |
| Duplicate IDs in HTML | 103 |

---

## HTML-only cards (on site, not in DB)

These cards exist in the HTML but have no matching `rule_id` in `policy_items`.
Per Phase 2 conflict rules: **HTML wins — DB must be backfilled.**

**By scope:**
- `ADM`: 39
- `CON`: 40
- `COR`: 66
- `ECO`: 24
- `EDU`: 10
- `ELE`: 6
- `ENV`: 52
- `EWT`: 12
- `EXE`: 114
- `FPL`: 50
- `GUN`: 10
- `HLT`: 74
- `HOU`: 143
- `IMM`: 6
- `INF`: 11
- `JUD`: 14
- `JUS`: 42
- `LAB`: 147
- `LEG`: 42
- `MED`: 16
- `PAT`: 24
- `RGT`: 36
- `RPR`: 41
- `STS`: 38
- `SYS`: 23
- `TAX`: 110
- `TEC`: 76
- `TRM`: 11

**Total: 1277**

<details>
<summary>Full list</summary>

| ID | Title | File |
|----|-------|------|
| `ADM-ADJ-002` | may not rely on opaque procedures, hidden guidance | administrative-state.html |
| `ADM-ADJ-003` | High-consequence agency decisions must be reviewable internally | administrative-state.html |
| `ADM-CAP-002` | Regulated entities may not dominate advisory boards, rulemaking | administrative-state.html |
| `ADM-CAP-003` | staff, appointees, and senior leadership must be subject | administrative-state.html |
| `ADM-CAP-004` | Revolving-door restrictions must apply before and after senior | administrative-state.html |
| `ADM-CAP-005` | Patterned agency deference to large regulated actors over | administrative-state.html |
| `ADM-CIV-002` | Core civil service protections must be established by statute, not exe | administrative-state.html |
| `ADM-COO-002` | Inter-agency coordination may not be used to evade | administrative-state.html |
| `ADM-CRA-001` | The Congressional Review Act must be reformed to require a supermajori | administrative-state.html |
| `ADM-CRA-002` | When a rule is nullified through the Congressional Review Act, the age | administrative-state.html |
| `ADM-ENF-002` | must be able to impose meaningful civil penalties | administrative-state.html |
| `ADM-ENF-003` | Repeated or systemic violations must trigger escalated review | administrative-state.html |
| `ADM-ENF-004` | Enforcement systems may not rely solely on fines | administrative-state.html |
| `ADM-FND-002` | Core regulatory and enforcement functions may not be | administrative-state.html |
| `ADM-FND-003` | with constitutionally or statutorily guaranteed public-interest duties | administrative-state.html |
| `ADM-FND-004` | Where appropriations fail, designated critical-protection agencies may | administrative-state.html |
| `ADM-IG-001` | Inspectors General must have statutory independence from agency leader | administrative-state.html |
| `ADM-IG-002` | Inspector General reports must be transmitted simultaneously to Congre | administrative-state.html |
| `ADM-IND-002` | leaders may not be removed, overruled, or replaced | administrative-state.html |
| `ADM-IND-003` | must retain operational independence in investigations, rulemaking | administrative-state.html |
| `ADM-IND-004` | Political oversight of agencies must not become political | administrative-state.html |
| `ADM-MAJ-002` | Courts may not use the major questions doctrine to strike down regulat | administrative-state.html |
| `ADM-OIR-001` | OIRA review must not be used to indefinitely delay or block rules that | administrative-state.html |
| `ADM-OIR-002` | OIRA cost-benefit analyses must incorporate distributional effects and | administrative-state.html |
| `ADM-OVR-002` | Internal oversight bodies must be protected from retaliation | administrative-state.html |
| `ADM-OVR-003` | Findings of systemic agency failure, capture, abuse | administrative-state.html |
| `ADM-PUB-002` | should provide accessible notice, comment tools, and explanatory | administrative-state.html |
| `ADM-RGT-002` | Regulated parties and affected individuals must have due | administrative-state.html |
| `ADM-RGT-003` | process must distinguish between legitimate rights protection | administrative-state.html |
| `ADM-RUL-002` | Rulemaking must be transparent, evidence-based, and publicly reviewabl | administrative-state.html |
| `ADM-RUL-003` | must be able to issue interim, emergency | administrative-state.html |
| `ADM-RUL-004` | Adaptive rulemaking authority must include review, sunset | administrative-state.html |
| `ADM-SCI-002` | scientific and technical staff must be protected from | administrative-state.html |
| `ADM-SCI-003` | must disclose the evidentiary basis for major rules | administrative-state.html |
| `ADM-SYS-002` | must be strong enough to regulate complex modern | administrative-state.html |
| `ADM-SYS-003` | design must prevent both political sabotage and unaccountable | administrative-state.html |
| `ADM-TRN-002` | must maintain public registries of major enforcement actions | administrative-state.html |
| `ADM-TRN-003` | Regulated entities may not use secrecy claims | administrative-state.html |
| `ADM-WBL-002` | The Merit Systems Protection Board and Office of Special Counsel must  | administrative-state.html |
| `CON-ALG-002` | Price personalization systems may not exploit vulnerability signals | consumer-rights.html |
| `CON-ALG-003` | Consumers have the right to know when algorithmic systems affect their | consumer-rights.html |
| `CON-AUTO-002` | Core vehicle functions may not be subscription-locked | consumer-rights.html |
| `CON-AUTO-003` | Hardware-enabled features at time of sale remain accessible | consumer-rights.html |
| `CON-CFP-001` | The CFPB must maintain independent funding and enforcement authority f | consumer-rights.html |
| `CON-CFP-002` | Consumer financial protection enforcement may not be effectively disma | consumer-rights.html |
| `CON-CFP-003` | Consumers must have a private right of action to enforce consumer fina | consumer-rights.html |
| `CON-CNS-002` | No degrading functionality when third-party consumables are used | consumer-rights.html |
| `CON-CRD-002` | Medical debt may not be reported on consumer credit reports | consumer-rights.html |
| `CON-CRD-003` | Consumers must have free, ongoing access to their credit reports and s | consumer-rights.html |
| `CON-DBR-002` | Data brokers may not sell data that enables discrimination, stalking,  | consumer-rights.html |
| `CON-DBR-003` | Data broker compilations used for consumer screening must comply with  | consumer-rights.html |
| `CON-DRK-002` | Cancellation of any subscription or service must be as easy as enrollm | consumer-rights.html |
| `CON-DRK-003` | Pre-selected options and default choices must default to the consumer’ | consumer-rights.html |
| `CON-DRK-004` | False urgency, fabricated scarcity, and fake social proof are prohibit | consumer-rights.html |
| `CON-ELC-002` | Computing hardware performance may not be subscription-gated | consumer-rights.html |
| `CON-ELC-003` | Basic device functions may not require subscriptions | consumer-rights.html |
| `CON-FEE-002` | Full upfront total price disclosure required | consumer-rights.html |
| `CON-FEE-003` | Prohibit confusing billing and negative-option renewal traps | consumer-rights.html |
| `CON-FEE-004` | Easy subscription cancellation through same enrollment medium | consumer-rights.html |
| `CON-FTR-002` | Software feature restrictions require legitimate justification | consumer-rights.html |
| `CON-GEN-002` | Ban confusion-based and friction-based business models | consumer-rights.html |
| `CON-GEN-003` | Consumers have clear enforceable rights across key areas | consumer-rights.html |
| `CON-GEN-004` | Adhesion contracts may not waive fundamental consumer rights | consumer-rights.html |
| `CON-GEN-005` | Restrict or ban mandatory arbitration in consumer contracts | consumer-rights.html |
| `CON-GEN-006` | Fine print cannot substitute for substantive fairness | consumer-rights.html |
| `CON-PDL-001` | Loans with annual percentage rates above defined thresholds must be pr | consumer-rights.html |
| `CON-PDL-002` | Repeated loan rollovers that trap borrowers in debt cycles are prohibi | consumer-rights.html |
| `CON-PDL-003` | Lenders targeting financially vulnerable communities face enhanced enf | consumer-rights.html |
| `CON-QLT-002` | Marketing claims must match actual product quality | consumer-rights.html |
| `CON-QLT-003` | Systematic low-quality manufacturing practices subject to review | consumer-rights.html |
| `CON-QLT-004` | Essential household goods need stronger baseline quality standards | consumer-rights.html |
| `CON-SUB-002` | Disclose ownership versus subscription status clearly | consumer-rights.html |
| `CON-SUB-003` | No degrading owned products to force subscription conversion | consumer-rights.html |
| `CON-SUB-004` | Core device functions may not require subscription | consumer-rights.html |
| `CON-SUB-005` | Legitimate ongoing services may use subscription models | consumer-rights.html |
| `CON-SUB-006` | Disclose owned versus service-based features at point of sale | consumer-rights.html |
| `CON-TRN-004` | Standardized disclosure of included versus paid features | consumer-rights.html |
| `CON-WAR-002` | Manufacturers must disclose support timelines at point of sale | consumer-rights.html |
| `CON-WAR-003` | Early support withdrawal must trigger remedies | consumer-rights.html |
| `COR-AGF-002` | Packer-controlled livestock contracts may not systematically disadvant | antitrust-and-corporate-power.html |
| `COR-AGF-003` | Seed, agricultural chemical, and farm technology consolidation must be | antitrust-and-corporate-power.html |
| `COR-ALG-002` | Use of pricing algorithms in concentrated markets | antitrust-and-corporate-power.html |
| `COR-ALG-003` | Firms may not outsource anti-competitive pricing behavior | antitrust-and-corporate-power.html |
| `COR-ANT-002` | Merger review must consider effects on prices, wages | antitrust-and-corporate-power.html |
| `COR-ANT-003` | Dominant firms may not acquire competitors, emerging rivals | antitrust-and-corporate-power.html |
| `COR-ANT-004` | Vertical integration that allows a firm to disadvantage | antitrust-and-corporate-power.html |
| `COR-ANT-005` | Breakup, structural separation, forced divestiture, or conduct remedie | antitrust-and-corporate-power.html |
| `COR-ANT-006` | Anti-competitive conduct may not be excused solely because | antitrust-and-corporate-power.html |
| `COR-ANT-007` | Competition enforcement must account for digital-era harms including | antitrust-and-corporate-power.html |
| `COR-ANT-008` | Ownership concentration must be monitored and published | antitrust-and-corporate-power.html |
| `COR-ASF-002` | End federal equitable sharing — prohibit federal adoption of state and | anti-corruption.html |
| `COR-AUD-002` | Both automated systems and human oversight must be | antitrust-and-corporate-power.html |
| `COR-CAP-002` | Standard-setting, repairability scoring, platform oversight, and compe | antitrust-and-corporate-power.html |
| `COR-CAP-003` | Revolving-door limits should apply in major competition, platform | antitrust-and-corporate-power.html |
| `COR-CON-002` | government has an affirmative and enforceable duty | antitrust-and-corporate-power.html |
| `COR-CON-003` | government has clear authority to break up, restructure | antitrust-and-corporate-power.html |
| `COR-CON-004` | Structural remedies, including divestiture and separation, must be | antitrust-and-corporate-power.html |
| `COR-CON-005` | Monopolies, cartels, and coordinated market control that suppress | antitrust-and-corporate-power.html |
| `COR-CON-006` | Price fixing, market allocation, bid rigging, and algorithmic | antitrust-and-corporate-power.html |
| `COR-CON-007` | Antitrust enforcement must consider impacts on competition, quality | antitrust-and-corporate-power.html |
| `COR-CON-008` | absence of immediate price increases does not constitute | antitrust-and-corporate-power.html |
| `COR-CON-009` | Firms with dominant market power are subject | antitrust-and-corporate-power.html |
| `COR-CON-010` | Dominant firms may not use control of infrastructure | antitrust-and-corporate-power.html |
| `COR-CON-011` | Firms may not evade antitrust restrictions through subsidiaries | antitrust-and-corporate-power.html |
| `COR-CON-012` | In cases involving dominant firms or high concentration | antitrust-and-corporate-power.html |
| `COR-CON-013` | Markets with high concentration must be continuously monitored | antitrust-and-corporate-power.html |
| `COR-CON-014` | Antitrust enforcement authority may not be weakened through | antitrust-and-corporate-power.html |
| `COR-EMO-002` | Mandatory divestiture or qualified blind trust as condition of taking  | anti-corruption.html |
| `COR-ENF-002` | Enforcement agencies must have authority to impose structural | antitrust-and-corporate-power.html |
| `COR-ENF-003` | Repeated or willful violations of consumer-protection, anti-monopoly,  | antitrust-and-corporate-power.html |
| `COR-ENF-004` | Private rights of action should exist for consumers | antitrust-and-corporate-power.html |
| `COR-ENF-005` | Enforcement must not rely solely on fines as | antitrust-and-corporate-power.html |
| `COR-FAR-002` | Close the "lobbying exemption" that allows foreign agent work without  | anti-corruption.html |
| `COR-FAR-003` | Ban former senior officials from registering as foreign agents for fiv | anti-corruption.html |
| `COR-FIN-005` | Mandatory disclosure of 501(c)(4) and dark-money political spending —  | anti-corruption.html |
| `COR-HAT-002` | Inspector General independence — protect IGs from politically motivate | anti-corruption.html |
| `COR-HAT-003` | Office of Government Ethics — independence, adequate resources, and bi | anti-corruption.html |
| `COR-INT-002` | Extend FCPA to cover foreign officials and agents bribing U.S. officia | anti-corruption.html |
| `COR-LAW-002` | Companies exhibiting patterns of violations must be subject | antitrust-and-corporate-power.html |
| `COR-LAW-003` | Corporate cultures that enable or fail to prevent | antitrust-and-corporate-power.html |
| `COR-LAW-004` | Board members and governing bodies may be held | antitrust-and-corporate-power.html |
| `COR-LAW-005` | Repeated or systemic violations must trigger escalating penalties | antitrust-and-corporate-power.html |
| `COR-LAW-006` | Regulatory frameworks must include proportional requirements and carve | antitrust-and-corporate-power.html |
| `COR-MKT-002` | Competition policy must protect not only price competition | antitrust-and-corporate-power.html |
| `COR-MKT-003` | Corporate scale, concentration, or integration that materially undermi | antitrust-and-corporate-power.html |
| `COR-MKT-004` | Core consumer markets must not be designed around | antitrust-and-corporate-power.html |
| `COR-MPY-002` | Mergers that significantly concentrate employer power in regional labo | antitrust-and-corporate-power.html |
| `COR-MPY-003` | No-poach and wage-fixing agreements between competing employers are pe | antitrust-and-corporate-power.html |
| `COR-NMD-002` | Digital platforms must negotiate in good faith with news publishers fo | antitrust-and-corporate-power.html |
| `COR-NMD-003` | News publishers may collectively negotiate with dominant platforms wit | antitrust-and-corporate-power.html |
| `COR-OWN-002` | Real estate beneficial ownership disclosure — close the all-cash purch | anti-corruption.html |
| `COR-OWN-003` | Beneficial ownership as condition for government contracts, grants, an | anti-corruption.html |
| `COR-PEQ-002` | Serial acquisitions and roll-up strategies that create de | antitrust-and-corporate-power.html |
| `COR-PEQ-003` | Firms in essential sectors may not load acquired | antitrust-and-corporate-power.html |
| `COR-PEQ-004` | Ownership structures that obscure control, liability, or concentration | antitrust-and-corporate-power.html |
| `COR-PIS-002` | Heightened obligations in essential sectors include stronger anti-conc | antitrust-and-corporate-power.html |
| `COR-PIS-003` | Essential-sector firms may not reduce quality, access, safety | antitrust-and-corporate-power.html |
| `COR-PIS-004` | Agricultural and food-production equipment is designated as | antitrust-and-corporate-power.html |
| `COR-PIS-005` | Commercial equipment critical to small-business operation, including f | antitrust-and-corporate-power.html |
| `COR-PLT-001` | Dominant digital platforms may not self-preference their own products  | antitrust-and-corporate-power.html |
| `COR-PLT-002` | App store platforms with dominant market position must allow alternati | antitrust-and-corporate-power.html |
| `COR-PLT-003` | Dominant platforms must provide data portability and interoperability  | antitrust-and-corporate-power.html |
| `COR-PLT-004` | Dominant platform acquisitions of nascent competitive threats must be  | antitrust-and-corporate-power.html |
| `COR-TRN-002` | Standardized public reporting should exist for product durability | antitrust-and-corporate-power.html |
| `COR-TRN-003` | Government should maintain publicly accessible databases of major | antitrust-and-corporate-power.html |
| `ECO-CTC-001` | Fully Refundable, Universal Child Tax Credit | taxation-and-wealth.html |
| `ECO-CTC-002` | Child Allowance Paid Monthly | taxation-and-wealth.html |
| `ECO-CTC-003` | Benefit Level Sufficient to Reduce Child Poverty; Indexed to Inflation | taxation-and-wealth.html |
| `ECO-CTC-004` | No Tax Filing Barrier; Automatic Enrollment | taxation-and-wealth.html |
| `ECO-CTC-005` | Child Allowance Through Age 17; Study Extension Through Age 21 for Stu | taxation-and-wealth.html |
| `ECO-GBI-001` | Guaranteed Income Floor for All Residents | taxation-and-wealth.html |
| `ECO-GBI-002` | Universal Displacement-Triggered Income Support | taxation-and-wealth.html |
| `ECO-GBI-003` | Automation Gains Must Fund a Social Dividend | taxation-and-wealth.html |
| `ECO-GBI-004` | Phased Implementation: Strengthen Existing Programs Toward Universal F | taxation-and-wealth.html |
| `ECO-GBI-005` | Prohibit Welfare Cliffs in All Means-Tested Programs | taxation-and-wealth.html |
| `ECO-IND-002` | Strategic Sector Investment and Public Financing | taxation-and-wealth.html |
| `ECO-IND-003` | Critical Supply Chain Resilience | taxation-and-wealth.html |
| `ECO-IND-004` | Rare Earth and Critical Minerals Strategy | taxation-and-wealth.html |
| `ECO-IND-005` | Buy America and Domestic Content Requirements | taxation-and-wealth.html |
| `ECO-IND-006` | Regional Industrial Policy and Manufacturing Clusters | taxation-and-wealth.html |
| `ECO-IND-007` | Worker Ownership and Democratic Enterprise in Industrial Policy | taxation-and-wealth.html |
| `ECO-IND-008` | Research and Development as Industrial Policy | taxation-and-wealth.html |
| `ECO-IND-009` | Trade Policy Aligned with Industrial Strategy | taxation-and-wealth.html |
| `ECO-IND-010` | Industrial Workforce Pipeline — Apprenticeships, Vocational Training,  | taxation-and-wealth.html |
| `ECO-SS-001` | Eliminate the Social Security Payroll Tax Wage Cap | taxation-and-wealth.html |
| `ECO-SS-002` | Supplement Social Security Funding with Automation Tax Revenue | taxation-and-wealth.html |
| `ECO-SS-003` | Substantially Increase the Social Security Minimum Benefit | taxation-and-wealth.html |
| `ECO-SS-004` | Add Caregiver Credits to Social Security Benefit Calculation | taxation-and-wealth.html |
| `ECO-SS-005` | Study and Address Occupational Inequity in Retirement Age | taxation-and-wealth.html |
| `EDU-BND-002` | Require media literacy and information literacy as core curriculum | education.html |
| `EDU-DIS-002` | Prohibit discriminatory discipline and close the school-to-prison pipe | education.html |
| `EDU-EQF-001` |  | education.html |
| `EDU-EQF-002` |  | education.html |
| `EDU-EQF-003` |  | education.html |
| `EDU-IDEA-001` |  | education.html |
| `EDU-IDEA-002` |  | education.html |
| `EDU-LIB-002` | Prohibit politically motivated book bans and curriculum prohibitions i | education.html |
| `EDU-SRC-001` |  | education.html |
| `EDU-SRC-002` |  | education.html |
| `ELE-FIN-003` | DISCLOSE Act — mandate real-time disclosure of all political spending  | elections-and-representation.html |
| `ELE-REP-004` | DC and Puerto Rico statehood — end taxation without representation for | elections-and-representation.html |
| `ELE-VOT-006` | Automatic voter registration — enroll all eligible citizens at point o | elections-and-representation.html |
| `ELE-VOT-007` | Same-day voter registration — any eligible citizen may register and vo | elections-and-representation.html |
| `ELE-VOT-008` | Restore voting rights upon completion of sentence — end felony disenfr | elections-and-representation.html |
| `ELE-VOT-009` | Ranked-choice voting for all federal elections — eliminate the spoiler | elections-and-representation.html |
| `ENV-AUD-002` | Audits must include water use, emissions, pollutants, waste | environment-and-agriculture.html |
| `ENV-AUD-003` | Audits must include both internal reporting and multiple | environment-and-agriculture.html |
| `ENV-AUD-004` | Auditors, including individuals, are criminally liable for fraudulent | environment-and-agriculture.html |
| `ENV-AUD-005` | Collusion, conspiracy, or coordinated fraud in environmental reporting | environment-and-agriculture.html |
| `ENV-CLI-002` | Establish a managed retreat and relocation assistance program for clim | environment-and-agriculture.html |
| `ENV-CLN-002` | Polluters and responsible entities must bear the cost | environment-and-agriculture.html |
| `ENV-CLN-003` | Liability rules for environmental contamination must be strong | environment-and-agriculture.html |
| `ENV-CLN-004` | Governments must have authority and dedicated funding | environment-and-agriculture.html |
| `ENV-CLN-005` | Cleanup funding mechanisms should include dedicated public funds | environment-and-agriculture.html |
| `ENV-CLN-006` | Federal, state, and local governments must coordinate active | environment-and-agriculture.html |
| `ENV-CLN-007` | Environmental cleanup programs must prioritize areas where waste | environment-and-agriculture.html |
| `ENV-CLN-008` | Public agencies must fund research, monitoring, and remediation | environment-and-agriculture.html |
| `ENV-CLN-009` | Cleanup and remediation standards must address persistent synthetic | environment-and-agriculture.html |
| `ENV-CLN-010` | Contaminated industrial, commercial, and waste sites must be | environment-and-agriculture.html |
| `ENV-CLN-011` | Brownfield and contaminated-site policy should prioritize remediation, | environment-and-agriculture.html |
| `ENV-CLN-012` | Cleanup policy must include restoration of habitats, waterways | environment-and-agriculture.html |
| `ENV-CLN-013` | Environmental restoration should prioritize biodiversity, water qualit | environment-and-agriculture.html |
| `ENV-CLN-014` | Communities affected by environmental contamination must have access | environment-and-agriculture.html |
| `ENV-CLN-015` | Cleanup progress, contamination data, and remediation outcomes | environment-and-agriculture.html |
| `ENV-CLN-016` | Cleanup obligations may not be delayed indefinitely through | environment-and-agriculture.html |
| `ENV-CLN-017` | Repeated failure to remediate known contamination must trigger | environment-and-agriculture.html |
| `ENV-CPX-002` | Return carbon pricing revenue as a per-capita dividend to protect work | environment-and-agriculture.html |
| `ENV-CPX-003` | Eliminate fossil fuel subsidies and redirect them to clean energy tran | environment-and-agriculture.html |
| `ENV-DES-002` | Use of composite, bonded, or mixed materials that | environment-and-agriculture.html |
| `ENV-ENF-002` | Repeated or large-scale violations of waste containment | environment-and-agriculture.html |
| `ENV-EPR-002` | Producers must fund and participate in systems | environment-and-agriculture.html |
| `ENV-EPR-003` | Products that are difficult to recycle, hazardous | environment-and-agriculture.html |
| `ENV-ESC-002` | Entities responsible for production, transport, or disposal | environment-and-agriculture.html |
| `ENV-ESC-003` | Release of plastics, microplastics, synthetic materials, or persistent | environment-and-agriculture.html |
| `ENV-FDS-001` |  | environment-and-agriculture.html |
| `ENV-FDS-002` |  | environment-and-agriculture.html |
| `ENV-IND-002` | Facilities must monitor, report, and mitigate waste leakage | environment-and-agriculture.html |
| `ENV-INF-002` | Landfills, transfer stations, and waste facilities must meet | environment-and-agriculture.html |
| `ENV-INF-003` | Stormwater, wastewater, and drainage systems must include filtration | environment-and-agriculture.html |
| `ENV-JUS-002` | Mandate community engagement and consent for major environmental decis | environment-and-agriculture.html |
| `ENV-JUS-003` | Prioritize Superfund cleanup and environmental remediation in historic | environment-and-agriculture.html |
| `ENV-NUC-001` |  | environment-and-agriculture.html |
| `ENV-NUC-002` |  | environment-and-agriculture.html |
| `ENV-PFAS-001` |  | environment-and-agriculture.html |
| `ENV-PFAS-002` |  | environment-and-agriculture.html |
| `ENV-PKG-002` | Reusable, refillable, or minimal packaging systems should be | environment-and-agriculture.html |
| `ENV-PLS-002` | Microplastic generation from products, manufacturing processes, and ma | environment-and-agriculture.html |
| `ENV-PLS-003` | Synthetic materials that persist in ecosystems without safe | environment-and-agriculture.html |
| `ENV-REC-002` | Recycling infrastructure must be accessible, consistent, and effective | environment-and-agriculture.html |
| `ENV-REC-003` | Materials placed into the market must be compatible | environment-and-agriculture.html |
| `ENV-REG-002` | Baseline environmental protections must include limits on emissions | environment-and-agriculture.html |
| `ENV-REG-003` | Carbon, water, and environmental offsets may not be | environment-and-agriculture.html |
| `ENV-SUB-001` |  | environment-and-agriculture.html |
| `ENV-SUB-002` |  | environment-and-agriculture.html |
| `ENV-TRN-002` | High-risk materials and sectors must be subject | environment-and-agriculture.html |
| `ENV-WTR-002` | Regulate agricultural and industrial water use to protect watersheds a | environment-and-agriculture.html |
| `ENV-WTR-003` | Require lead pipe replacement and achieve zero lead exposure in drinki | environment-and-agriculture.html |
| `EWT-DES-001` | Products must be designed for long-term use, including | environment-and-agriculture.html |
| `EWT-DES-002` | Use of non-replaceable components in high-failure areas, including | environment-and-agriculture.html |
| `EWT-LIF-001` | Manufacturers are responsible for the full lifecycle impact | environment-and-agriculture.html |
| `EWT-LIF-002` | Producers must provide accessible take-back, recycling, or refurbishme | environment-and-agriculture.html |
| `EWT-LIF-003` | Products may not be designed in ways that | environment-and-agriculture.html |
| `EWT-SUP-001` | Withdrawal of software support may not render hardware | environment-and-agriculture.html |
| `EWT-SUP-002` | Devices must retain baseline usability after end-of-support unless | environment-and-agriculture.html |
| `EWT-SYS-001` | Products must be designed, manufactured, and supported | environment-and-agriculture.html |
| `EWT-SYS-002` | Anti-waste, repairability, and anti-lock-in requirements must be integ | environment-and-agriculture.html |
| `EWT-TRN-001` | Products must disclose expected lifespan, support duration, repairabil | environment-and-agriculture.html |
| `EWT-WST-001` | Rapid product replacement cycles that drive unnecessary disposal | environment-and-agriculture.html |
| `EWT-WST-002` | Marketing practices that encourage premature replacement of functional | environment-and-agriculture.html |
| `EXE-25A-001` | Twenty-Fifth Amendment or successor constitutional framework must be | executive-power.html |
| `EXE-25A-002` | Executive incapacity rules must be clear, enforceable, medically | executive-power.html |
| `EXE-25A-003` | Temporary transfer of authority, contested incapacity, and restoration | executive-power.html |
| `EXE-25A-004` | Incapacity and succession rules must separately address | executive-power.html |
| `EXE-25A-005` | No single actor may unilaterally determine executive incapacity | executive-power.html |
| `EXE-25A-006` | Succession and incapacity rules must separately define continuity | executive-power.html |
| `EXE-25A-007` | Succession chains must prevent ambiguity, overlapping authority | executive-power.html |
| `EXE-25A-008` | Succession and incapacity rules must account for independently | executive-power.html |
| `EXE-25A-009` | Temporary transfer of authority must preserve continuity without | executive-power.html |
| `EXE-25A-010` | Succession and incapacity rules must preserve continuity within | executive-power.html |
| `EXE-25A-011` | Temporary transfer of authority must maintain stability within | executive-power.html |
| `EXE-25A-012` | Incapacity procedures for the President, Vice President, Head | executive-power.html |
| `EXE-25A-013` | Incapacity determinations must include medical, procedural, and instit | executive-power.html |
| `EXE-25A-014` | Succession within each executive lane must be automatic | executive-power.html |
| `EXE-25A-015` | Cross-lane succession may occur only under expressly defined | executive-power.html |
| `EXE-ACT-001` | Strict 30-day limit on acting officers in Senate-confirmed positions,  | executive-power.html |
| `EXE-ACT-002` | Limit recess appointments to genuine recesses — clear 10-day threshold | executive-power.html |
| `EXE-ACT-003` | Restrict acting officials from exercising final authority on major reg | executive-power.html |
| `EXE-CAB-001` | Cabinet appointment systems should be reworked to reduce | executive-power.html |
| `EXE-CAB-002` | Cabinet formation shall prioritize expertise, competence, and public | executive-power.html |
| `EXE-CAB-003` | Appointment mechanisms for major executive offices may include | executive-power.html |
| `EXE-CAB-004` | Appointment design for major executive departments should balance | executive-power.html |
| `EXE-CAB-005` | Executive appointment systems must prevent capture, cronyism | executive-power.html |
| `EXE-CAB-006` | Constitutionally established or high-risk executive departments may re | executive-power.html |
| `EXE-CLS-001` | Codify the prohibition on classifying information to conceal governmen | executive-power.html |
| `EXE-CLS-002` | Automatic declassification at 25 years with mandatory review at 10 yea | executive-power.html |
| `EXE-CLS-003` | Criminal penalties for unlawful removal or retention of classified doc | executive-power.html |
| `EXE-GRD-001` | Constitutional redesign of the executive must be tested | executive-power.html |
| `EXE-GRD-002` | Constitutional design must include explicit mechanisms to resolve | executive-power.html |
| `EXE-GRD-003` | Executive authority must remain subject to legislative oversight | executive-power.html |
| `EXE-GRD-004` | Executive design must ensure that no more than | executive-power.html |
| `EXE-GRD-005` | executive system must include explicit tie-breaking mechanisms | executive-power.html |
| `EXE-GRD-006` | Systems with multiple directly elected executive officers | executive-power.html |
| `EXE-GRD-007` | No executive office may claim superior democratic legitimacy | executive-power.html |
| `EXE-GRD-008` | Systems with staggered executive elections must include explicit | executive-power.html |
| `EXE-GRD-009` | No executive office may claim electoral mandate as | executive-power.html |
| `EXE-GRD-010` | executive system must be stress-tested against scenarios including | executive-power.html |
| `EXE-GRD-011` | Where stress testing reveals ambiguity, constitutional text | executive-power.html |
| `EXE-HOG-001` | Head of Government shall be established as | executive-power.html |
| `EXE-HOG-002` | head-of-state office, whether styled president or otherwise | executive-power.html |
| `EXE-HOG-003` | Executive design must prevent ambiguous overlap between offices | executive-power.html |
| `EXE-HOG-004` | Head of Government shall not derive authority from | executive-power.html |
| `EXE-HOG-005` | method of selection and removal of the Head | executive-power.html |
| `EXE-HOG-006` | Head of Government may be subject to legislative | executive-power.html |
| `EXE-HOG-007` | Head of Government may be supported | executive-power.html |
| `EXE-HOG-008` | Deputy Head of Government shall act under | executive-power.html |
| `EXE-HOG-009` | Deputy Head of Government shall assume the duties | executive-power.html |
| `EXE-HOG-010` | role of Deputy Head of Government must be | executive-power.html |
| `EXE-HOG-011` | Deputy Head of Government shall not exercise independent | executive-power.html |
| `EXE-HOG-012` | offices of Vice President and Deputy Head | executive-power.html |
| `EXE-HOG-013` | Deputy Head of Government may be directly elected | executive-power.html |
| `EXE-HOG-014` | Confirmation procedures must evaluate competence, independence, and co | executive-power.html |
| `EXE-HOG-015` | Head of Government may be removed through defined | executive-power.html |
| `EXE-HOG-016` | Removal mechanisms must prevent arbitrary dismissal while ensuring | executive-power.html |
| `EXE-HOG-017` | Removal procedures must not allow indefinite retention | executive-power.html |
| `EXE-HOG-018` | Head of Government shall be accountable for execution | executive-power.html |
| `EXE-HOG-019` | Head of Government shall have primary authority over | executive-power.html |
| `EXE-HOG-020` | Cabinet officers shall be operationally accountable | executive-power.html |
| `EXE-HOG-021` | Conflicts between the President and Head of Government | executive-power.html |
| `EXE-HOG-022` | Head of Government shall be directly elected | executive-power.html |
| `EXE-HOG-023` | Elections for the Head of Government shall occur | executive-power.html |
| `EXE-HOG-024` | Head of Government shall serve a fixed term | executive-power.html |
| `EXE-HOG-025` | term length of the Head of Government | executive-power.html |
| `EXE-HOG-026` | Head of Government may not be removed unilaterally | executive-power.html |
| `EXE-HOG-027` | Head of Government may be removed | executive-power.html |
| `EXE-HOG-028` | Removal of the Head of Government must require | executive-power.html |
| `EXE-HOG-029` | President may initiate formal review of the Head | executive-power.html |
| `EXE-HOG-030` | In cases of severe executive deadlock, the President | executive-power.html |
| `EXE-HOG-031` | Deputy Head of Government shall assume the duties | executive-power.html |
| `EXE-HOG-032` | Temporary assumption of duties by the Deputy Head | executive-power.html |
| `EXE-HOG-033` | Where the office of Head of Government becomes | executive-power.html |
| `EXE-HOG-034` | If the legislature fails to designate a successor | executive-power.html |
| `EXE-IMM-001` | Legislatively define narrow, bounded presidential immunity — address t | executive-power.html |
| `EXE-IMM-002` | Constitutional amendment to explicitly prohibit presidential self-pard | executive-power.html |
| `EXE-IMM-003` | Toll the statute of limitations for crimes committed while in office | executive-power.html |
| `EXE-POW-001` | Emergency, military, administrative, and appointment powers | executive-power.html |
| `EXE-POW-002` | Any executive action with significant national impact | executive-power.html |
| `EXE-POW-003` | Executive authority may not be expanded through custom | executive-power.html |
| `EXE-POW-004` | State/Continuity lane shall retain authority over constitutional conti | executive-power.html |
| `EXE-POW-005` | Authority between the two executive lanes must be | executive-power.html |
| `EXE-PRES-001` | President shall serve as head of state | executive-power.html |
| `EXE-PRES-002` | President shall retain limited veto, assent, and referral | executive-power.html |
| `EXE-PRES-003` | President’s role as commander-in-chief shall be limited | executive-power.html |
| `EXE-PRES-004` | President shall not exercise primary authority over routine | executive-power.html |
| `EXE-PRES-005` | President may participate in high-level diplomatic, treaty | executive-power.html |
| `EXE-PRES-006` | Emergency powers exercised by the President must require | executive-power.html |
| `EXE-STF-001` | Mandatory disclosure of all White House staff, advisors, and access li | executive-power.html |
| `EXE-STF-002` | Require career security clearance process for White House personnel —  | executive-power.html |
| `EXE-SYS-001` | Executive power shall be distributed across multiple constitutionally | executive-power.html |
| `EXE-SYS-002` | executive branch shall consist of three primary offices | executive-power.html |
| `EXE-SYS-003` | All executive powers must be explicitly assigned | executive-power.html |
| `EXE-SYS-004` | No executive authority may be exercised based | executive-power.html |
| `EXE-SYS-005` | Executive design must minimize personalism, prevent self-protection fr | executive-power.html |
| `EXE-SYS-006` | Executive office titles and structures must be designed | executive-power.html |
| `EXE-SYS-007` | Head of Government may also be designated | executive-power.html |
| `EXE-SYS-008` | Deputy Head of Government may be designated | executive-power.html |
| `EXE-SYS-009` | Election cycles for executive offices must be structured | executive-power.html |
| `EXE-SYS-010` | Staggered elections must not create persistent legitimacy conflicts | executive-power.html |
| `EXE-SYS-011` | Executive offices with overlapping timeframes must have clearly | executive-power.html |
| `EXE-SYS-012` | Executive offices within the same functional lane | executive-power.html |
| `EXE-SYS-013` | Staggered executive elections must reduce the risk | executive-power.html |
| `EXE-TRN-001` | Presidential transition cooperation made a legal obligation, not a nor | executive-power.html |
| `EXE-TRN-002` | Real-time preservation of presidential records — automated archiving,  | executive-power.html |
| `EXE-TRN-003` | Continuity of government — clear operational succession and disability | executive-power.html |
| `EXE-VP-001` | Vice President shall be directly elected and hold | executive-power.html |
| `EXE-VP-002` | Vice President shall serve as primary continuity officer | executive-power.html |
| `EXE-VP-003` | Vice President shall participate in defined executive review | executive-power.html |
| `EXE-VP-004` | Vice President shall have defined interbranch coordination responsibil | executive-power.html |
| `EXE-VP-005` | Direct election of the vice president must be | executive-power.html |
| `EXE-VP-006` | Vice President’s authority must be structured to support | executive-power.html |
| `EXE-VP-007` | Vice President shall be directly elected | executive-power.html |
| `EXE-VP-008` | Vice President’s term must align with continuity | executive-power.html |
| `EXE-VP-009` | Vice President shall have no routine authority | executive-power.html |
| `EXE-VP-010` | Vice President may participate in executive conflict-resolution proced | executive-power.html |
| `FPL-AID-001` | Condition all foreign assistance on verifiable human rights compliance | foreign-policy.html |
| `FPL-AID-002` | End strategic aid to authoritarian and oppressive governments | foreign-policy.html |
| `FPL-AID-003` | Restore USAID independence and evaluate all aid programs on developmen | foreign-policy.html |
| `FPL-AID-004` | Design aid programs to benefit populations, not governing elites | foreign-policy.html |
| `FPL-AID-005` | Invest in global public health as a core foreign policy and security o | foreign-policy.html |
| `FPL-ARM-001` | Prohibit arms transfers to governments committing war crimes or crimes | foreign-policy.html |
| `FPL-ARM-002` | War crimes trigger a mandatory multi-year arms embargo with potential  | foreign-policy.html |
| `FPL-ARM-003` | Ratify the United Nations Arms Trade Treaty | foreign-policy.html |
| `FPL-ARM-004` | Enforce and substantially strengthen the Leahy Law | foreign-policy.html |
| `FPL-ARM-005` | Require affirmative Congressional approval for all major arms sales | foreign-policy.html |
| `FPL-ARM-006` | Mandate end-use monitoring with real legal consequences for violations | foreign-policy.html |
| `FPL-ARM-007` | Mandate full public transparency in all U.S. arms transfers | foreign-policy.html |
| `FPL-CLM-001` | Treat climate change as a core foreign policy and national security pr | foreign-policy.html |
| `FPL-CLM-002` | Honor, exceed, and permanently commit to Paris Agreement obligations | foreign-policy.html |
| `FPL-CLM-003` | Fulfill U.S. climate finance obligations to developing nations | foreign-policy.html |
| `FPL-CLM-004` | Recognize climate displacement and support international climate refug | foreign-policy.html |
| `FPL-CLM-005` | Eliminate fossil fuel financing through U.S. international financial i | foreign-policy.html |
| `FPL-DPL-001` | Establish diplomatic primacy — force is a genuine last resort | foreign-policy.html |
| `FPL-DPL-002` | Be a constructive, paying, reform-supporting member of the United Nati | foreign-policy.html |
| `FPL-DPL-003` | Engage constructively with international rule-of-law institutions incl | foreign-policy.html |
| `FPL-DPL-004` | Default to multilateral frameworks over unilateral action for shared g | foreign-policy.html |
| `FPL-DPL-005` | Invest in conflict prevention at scale proportionate to conflict respo | foreign-policy.html |
| `FPL-DPL-006` | Accept and respond substantively to international human rights account | foreign-policy.html |
| `FPL-HRT-001` | Reaffirm the Universal Declaration of Human Rights as the foundation o | foreign-policy.html |
| `FPL-HRT-002` | Recognize digital rights as fundamental human rights | foreign-policy.html |
| `FPL-HRT-003` | Recognize a clean, healthy, and sustainable environment as a human rig | foreign-policy.html |
| `FPL-HRT-004` | Defend LGBTQ+ rights as non-derogable human rights in all foreign enga | foreign-policy.html |
| `FPL-HRT-005` | Defend women's rights and gender equality as non-negotiable foreign po | foreign-policy.html |
| `FPL-HRT-006` | Maintain an absolute, non-derogable prohibition on torture and extraor | foreign-policy.html |
| `FPL-HRT-007` | Consistently oppose arbitrary detention, enforced disappearances, and  | foreign-policy.html |
| `FPL-INT-001` | Require genuine congressional oversight and approval for covert action | foreign-policy.html |
| `FPL-INT-002` | Prohibit extrajudicial killings outside active armed conflict and requ | foreign-policy.html |
| `FPL-INT-003` | Prohibit U.S. intelligence support to security forces that commit huma | foreign-policy.html |
| `FPL-INT-004` | Mandate systematic declassification and public accounting of historica | foreign-policy.html |
| `FPL-INT-005` | Subject mass surveillance of foreign populations to legal standards pr | foreign-policy.html |
| `FPL-MIL-001` | Require comprehensive human rights impact assessments for all private  | foreign-policy.html |
| `FPL-MIL-002` | Subject AI weapons, autonomous systems, and surveillance technology to | foreign-policy.html |
| `FPL-MIL-003` | Close the revolving door between senior DoD officials and defense cont | foreign-policy.html |
| `FPL-MIL-004` | Regulate offensive cyber capabilities and spyware as weapons under exp | foreign-policy.html |
| `FPL-MIL-005` | Require full DoD financial audit passage as a precondition for real bu | foreign-policy.html |
| `FPL-RSP-001` | Formally acknowledge U.S. responsibility for destabilized countries an | foreign-policy.html |
| `FPL-RSP-002` | Commit to sustained reconstruction and stabilization assistance for Ir | foreign-policy.html |
| `FPL-RSP-003` | Acknowledge the 1953 CIA-orchestrated coup in Iran as a foundation for | foreign-policy.html |
| `FPL-RSP-004` | Establish an independent mechanism to review and account for past U.S. | foreign-policy.html |
| `FPL-RSP-005` | Provide reparative development assistance to nations demonstrably harm | foreign-policy.html |
| `FPL-TRD-001` | Prohibit preferential trade agreements with forced labor states | foreign-policy.html |
| `FPL-TRD-002` | Require binding, enforceable ILO-standard labor provisions in all trad | foreign-policy.html |
| `FPL-TRD-003` | Apply the Uyghur Forced Labor Prevention Act framework globally | foreign-policy.html |
| `FPL-TRD-004` | Condition trade relationships on verifiable labor rights and human rig | foreign-policy.html |
| `FPL-TRD-005` | Design trade agreements to prevent race-to-the-bottom on labor costs a | foreign-policy.html |
| `GUN-AMO-001` | Background checks required for all ammunition purchases | gun-policy.html |
| `GUN-AMO-002` | Ammunition sales records and reporting for bulk purchases | gun-policy.html |
| `GUN-LIC-001` | Firearm purchaser licensing — permit required before purchase | gun-policy.html |
| `GUN-LIC-002` | Mandatory waiting period for all firearm purchases | gun-policy.html |
| `GUN-SAF-001` | Prohibit manufacture, transfer, or possession of unserialized firearms | gun-policy.html |
| `GUN-SAF-002` | Mandate microstamping technology on all new semi-automatic handguns ma | gun-policy.html |
| `GUN-SAF-003` | Fund smart gun technology research and remove legal barriers to smart  | gun-policy.html |
| `GUN-STW-001` | Enhanced straw purchase penalties with mandatory minimum prosecution | gun-policy.html |
| `GUN-STW-002` | Firearms trafficking as a standalone federal felony with enhanced pena | gun-policy.html |
| `GUN-STW-003` | Firearm manufacturer civil liability for negligent distribution and fo | gun-policy.html |
| `HLT-COV-032` | Preventative care coverage mandate | healthcare.html |
| `HLT-COV-033` | Weight management as covered care | healthcare.html |
| `HLT-COV-034` | Preventative mental wellness visits | healthcare.html |
| `HLT-COV-035` | Cosmetic and reconstructive procedures for documented mental or emotio | healthcare.html |
| `HLT-COV-036` | Chronic pain as a covered primary condition | healthcare.html |
| `HLT-COV-037` | Functional medicine and quality-of-life care for chronic conditions | healthcare.html |
| `HLT-CRN-002` | Cover long-term disability management and return-to-work support | healthcare.html |
| `HLT-DIS-001` | Mandate inclusion of underrepresented populations in all federally fun | healthcare.html |
| `HLT-DIS-002` | Fund dedicated research into Black maternal mortality and obstetric di | healthcare.html |
| `HLT-DIS-003` | Fund LGBTQ+ health disparities research and require disaggregated data | healthcare.html |
| `HLT-DIS-004` | Fund research on Native American and Alaska Native health disparities  | healthcare.html |
| `HLT-DIS-005` | Require disaggregated data for Asian American and Pacific Islander pop | healthcare.html |
| `HLT-DIS-006` | Fund research into the social determinants of health and structural dr | healthcare.html |
| `HLT-DNT-002` | Include vision care in the mandatory coverage floor | healthcare.html |
| `HLT-HRG-001` |  | healthcare.html |
| `HLT-HRG-002` |  | healthcare.html |
| `HLT-LCD-001` |  | healthcare.html |
| `HLT-LCD-002` |  | healthcare.html |
| `HLT-MAT-002` | Require coverage of doula, midwifery, and comprehensive postpartum car | healthcare.html |
| `HLT-NUT-001` | Fund federal research into ultra-processed food consumption and chroni | healthcare.html |
| `HLT-NUT-002` | Require independence in the Dietary Guidelines for Americans process | healthcare.html |
| `HLT-NUT-003` | Fund research into food deserts, dietary access, and structural driver | healthcare.html |
| `HLT-NUT-004` | Create a continuously updated National Nutrition Database grounded in  | healthcare.html |
| `HLT-NUT-005` | Fund longitudinal research on diet, mental health, energy, and quality | healthcare.html |
| `HLT-NUT-006` | Require independent replication before industry-funded nutrition resea | healthcare.html |
| `HLT-NUT-007` | Fund research into the microbiome and its role in health and disease | healthcare.html |
| `HLT-NUT-008` | Integrate nutrition into medical education and primary care practice | healthcare.html |
| `HLT-ORD-001` |  | healthcare.html |
| `HLT-ORD-002` |  | healthcare.html |
| `HLT-PAN-001` |  | healthcare.html |
| `HLT-RTT-001` | Establish a general right to access investigational treatments under p | healthcare.html |
| `HLT-RTT-002` | Require licensed physician oversight for all investigational treatment | healthcare.html |
| `HLT-RTT-003` | Require informed consent, independent evaluation, and second opinion | healthcare.html |
| `HLT-RTT-004` | Define patient eligibility criteria | healthcare.html |
| `HLT-RTT-005` | Mandate research data contribution from all investigational treatment  | healthcare.html |
| `HLT-RTT-006` | Establish strict patient data privacy and security standards | healthcare.html |
| `HLT-RTT-007` | Create a national public research database for investigational treatme | healthcare.html |
| `HLT-RTT-008` | Protect physicians acting in good faith under approved protocols | healthcare.html |
| `HLT-RTT-009` | Preserve government regulatory authority; no commercial access created | healthcare.html |
| `HLT-RTT-010` | Require evidence-based, apolitical rescheduling review for substances  | healthcare.html |
| `HLT-RTT-011` | Expand FDA expanded access and streamline compassionate use pathways | healthcare.html |
| `HLT-RTT-012` | Prohibit exploitation of right-to-try patients | healthcare.html |
| `HLT-SCI-001` | Establish a federal minimum for public research investment | healthcare.html |
| `HLT-SCI-002` | Protect research independence from commercial interference | healthcare.html |
| `HLT-SCI-003` | Mandate open access for all federally funded research | healthcare.html |
| `HLT-SCI-004` | Prioritize neglected and under-commercially-funded research areas | healthcare.html |
| `HLT-SCI-005` | Fund research replication and negative results reporting | healthcare.html |
| `HLT-SCI-006` | Establish independent scientific advisory bodies free from political a | healthcare.html |
| `HLT-SCI-007` | Fund a national research infrastructure for emerging and investigation | healthcare.html |
| `HLT-SCI-008` | Protect scientific whistleblowers and dissenting researchers | healthcare.html |
| `HLT-SUP-005` | Make adverse event reporting for supplements mandatory | healthcare.html |
| `HLT-SUP-006` | Create a national, publicly accessible supplement safety and evidence  | healthcare.html |
| `HLT-SUP-007` | Fund crowdsourced safety surveillance for supplements using patient-re | healthcare.html |
| `HLT-SUP-008` | Require pre-market safety notification for new supplement ingredients | healthcare.html |
| `HLT-SUP-009` | Combat supplement misinformation through accessible public evidence re | healthcare.html |
| `HLT-SUP-010` | Require disclosure of commercial funding in supplement research and re | healthcare.html |
| `HLT-VAC-001` | Fund development of vaccines for underserved infectious disease target | healthcare.html |
| `HLT-VAC-002` | Create a real-time, publicly accessible national vaccine safety survei | healthcare.html |
| `HLT-VAC-003` | Fund the largest independent vaccine safety studies ever conducted and | healthcare.html |
| `HLT-VAC-004` | Create a Vaccine Evidence Portal for public trust-building and plain-l | healthcare.html |
| `HLT-VAC-005` | Ensure all evidence-based vaccines are covered without cost-sharing un | healthcare.html |
| `HLT-VAC-006` | Fund research into vaccine hesitancy and evidence-based communication  | healthcare.html |
| `HLT-WEL-001` | Integrate the WHO definition of health into federal healthcare policy | healthcare.html |
| `HLT-WEL-002` | Fund research into interventions that improve energy, mood, and daily  | healthcare.html |
| `HLT-WEL-003` | Require patient-reported outcome measures in all federally funded heal | healthcare.html |
| `HLT-WEL-004` | Fund research into longevity, healthy aging, and compression of morbid | healthcare.html |
| `HLT-WEL-005` | Fund mental wellness and positive psychology research, not only mental | healthcare.html |
| `HLT-WEL-006` | Redesign healthcare quality measurement to capture wellness and qualit | healthcare.html |
| `HLT-WMH-001` | Mandate NIH research funding proportional to disease burden for condit | healthcare.html |
| `HLT-WMH-002` | Require inclusion of women in all federally funded clinical trials and | healthcare.html |
| `HLT-WMH-003` | Fund dedicated research programs for endometriosis, PCOS, and other ch | healthcare.html |
| `HLT-WMH-004` | Establish a national research agenda for menopause and female aging | healthcare.html |
| `HLT-WMH-005` | Fund research into maternal mental health and the perinatal period | healthcare.html |
| `HLT-WMH-006` | Address the sex-based gap in cardiovascular disease research and clini | healthcare.html |
| `HOU-ALT-002` | Public subsidy and land policy should favor ownership | housing.html |
| `HOU-ALT-003` | Social housing systems should include mixed-income models that | housing.html |
| `HOU-ALT-004` | Community land trusts, cooperatives, and nonprofit housing models | housing.html |
| `HOU-BLD-002` | Residential construction incentives should prioritize long-term durabi | housing.html |
| `HOU-BLD-003` | Publicly supported housing development should favor construction stand | housing.html |
| `HOU-BLD-004` | Housing production systems must incentivize construction of affordable | housing.html |
| `HOU-BLD-005` | Regulatory frameworks must be evaluated to remove unnecessary | housing.html |
| `HOU-BLD-006` | Housing construction and renovation policy must minimize material | housing.html |
| `HOU-BLD-007` | Residential construction may not rely on materials, methods | housing.html |
| `HOU-BLD-008` | Publicly supported housing and large-scale residential development sho | housing.html |
| `HOU-CLT-002` | Public land may be conveyed to community land trusts at below-market c | housing.html |
| `HOU-CLT-003` | CLT resale restrictions must be honored and enforced through deed cove | housing.html |
| `HOU-CLT-004` | Federal housing programs must be evaluated on long-term affordability  | housing.html |
| `HOU-EVI-002` | No eviction may occur without judicial review; administrative | housing.html |
| `HOU-EVI-003` | Tenants must have access to legal representation in | housing.html |
| `HOU-EVI-004` | Eviction timelines must provide sufficient time for tenants | housing.html |
| `HOU-EVI-005` | Evictions based on minor, technical, or non-material lease | housing.html |
| `HOU-EVI-006` | Retaliatory evictions for reporting code violations, asserting tenant | housing.html |
| `HOU-EVI-007` | Evictions may not be used as a tool | housing.html |
| `HOU-EVI-008` | Serial eviction filings without legitimate cause must trigger | housing.html |
| `HOU-EVI-009` | Landlords may not use threats, lockouts, utility shutoffs | housing.html |
| `HOU-EVI-010` | Eviction for nonpayment must include mandatory opportunity for | housing.html |
| `HOU-EVI-011` | Courts must consider temporary hardship, income disruption, or | housing.html |
| `HOU-EVI-012` | Evictions for small or de minimis arrears that | housing.html |
| `HOU-EVT-001` | Tenants facing eviction must have access to government-funded legal re | housing.html |
| `HOU-EVT-002` | Evictions may proceed only for just cause as defined by statute | housing.html |
| `HOU-EVT-003` | Eviction court records may not be publicly disclosed in ways that perm | housing.html |
| `HOU-EXT-002` | Landlords, developers, and housing owners may not rely | housing.html |
| `HOU-EXT-003` | Publicly subsidized or publicly supported housing may not | housing.html |
| `HOU-FIN-002` | Adjustable-rate, variable-risk, or complex mortgage products must meet | housing.html |
| `HOU-FIN-003` | Lenders must retain accountability for long-term loan performance | housing.html |
| `HOU-GEN-002` | Redevelopment and upzoning policies must include anti-displacement saf | housing.html |
| `HOU-GEN-003` | Communities facing gentrification pressure should receive targeted pre | housing.html |
| `HOU-GEN-004` | Public investment and infrastructure improvements may not be | housing.html |
| `HOU-GEN-005` | Housing and development policy must prevent predictable displacement | housing.html |
| `HOU-HAB-002` | Housing policy must treat livability as a core | housing.html |
| `HOU-HAB-003` | Repeated failure to maintain habitable housing must trigger | housing.html |
| `HOU-HAB-004` | Residents must have accessible mechanisms to report unsafe | housing.html |
| `HOU-HML-002` | Access to housing may not be conditioned on | housing.html |
| `HOU-HML-003` | Homelessness interventions must include access to supportive services | housing.html |
| `HOU-HML-004` | Emergency shelters must meet safety, sanitation, and dignity | housing.html |
| `HOU-HML-005` | Criminalization of homelessness through bans on sleeping, resting | housing.html |
| `HOU-HOA-002` | HOA governance must include due process, transparent rules | housing.html |
| `HOU-HOA-003` | HOA fines, liens, and enforcement powers must be | housing.html |
| `HOU-HOA-004` | HOAs may not impose rules that violate protected | housing.html |
| `HOU-HOA-005` | State law should provide oversight, complaint mechanisms, and | housing.html |
| `HOU-HOA-006` | HOA rules may not be used to block | housing.html |
| `HOU-HOA-007` | HOAs may not use aesthetic rules to force | housing.html |
| `HOU-INS-002` | Insurance markets may not withdraw or price-gouge entire | housing.html |
| `HOU-IZN-002` | Inclusionary affordable units must remain affordable through long-term | housing.html |
| `HOU-IZN-003` | Inclusionary requirements must advance economic integration, not unit  | housing.html |
| `HOU-LND-002` | Land-use policy must support long-term housing stability rather | housing.html |
| `HOU-MHO-002` | Lot rent increases in manufactured housing communities must be regulat | housing.html |
| `HOU-MHO-003` | Manufactured housing must meet quality standards without barriers to e | housing.html |
| `HOU-MKT-002` | Government should limit speculative bulk acquisition of single-family | housing.html |
| `HOU-MKT-003` | Ownership concentration in residential housing markets must be | housing.html |
| `HOU-MKT-004` | Corporate ownership of single-family homes and other owner-occupancy-o | housing.html |
| `HOU-MKT-005` | Institutional and corporate ownership caps should apply in | housing.html |
| `HOU-MKT-006` | Bulk acquisition of single-family homes, starter homes, or | housing.html |
| `HOU-MKT-007` | Shell-company, affiliate, and fragmented-title structures may not be | housing.html |
| `HOU-MKT-008` | Ownership-concentration rules must distinguish between dense rental ho | housing.html |
| `HOU-MKT-009` | Housing policy may not prioritize asset appreciation or | housing.html |
| `HOU-MKT-010` | Tax, financing, and regulatory systems must not disproportionately | housing.html |
| `HOU-MKT-011` | Residential housing must not be treated primarily as | housing.html |
| `HOU-MKT-012` | Ownership concentration that enables coordinated pricing, rent inflati | housing.html |
| `HOU-MKT-013` | Use of algorithmic or coordinated systems to artificially | housing.html |
| `HOU-MKT-014` | Residential housing markets are subject to heightened antitrust | housing.html |
| `HOU-MKT-015` | Landlords, property managers, investors, and pricing vendors may | housing.html |
| `HOU-MKT-016` | Use of algorithmic rent-setting systems in concentrated housing | housing.html |
| `HOU-MKT-017` | Large-scale residential ownership structures that enable anti-competit | housing.html |
| `HOU-OVR-002` | Repeated patterns of unsafe housing, speculative extraction, or | housing.html |
| `HOU-OVR-003` | Housing regulators must track and publish standardized data | housing.html |
| `HOU-OVR-004` | Repeated patterns of abuse, neglect, collusion, unsafe conditions | housing.html |
| `HOU-OWN-002` | Housing policy must identify and reform legal, tax | housing.html |
| `HOU-OWN-003` | The cost of homeownership must be evaluated as | housing.html |
| `HOU-OWN-004` | Homeownership policy should prioritize long-term resident ownership an | housing.html |
| `HOU-OWN-005` | Housing policy must ensure that ordinary income earners | housing.html |
| `HOU-OWN-006` | First-time homebuyers must have access to fair financing | housing.html |
| `HOU-OWN-007` | Down payment assistance, public financing tools, or equivalent | housing.html |
| `HOU-PRS-002` | Anti-displacement protections must be built into redevelopment, rezoni | housing.html |
| `HOU-PRS-003` | Communities facing gentrification pressure must receive proactive tena | housing.html |
| `HOU-PUB-002` | Public housing systems must receive stable maintenance funding | housing.html |
| `HOU-PUB-003` | Residents of public housing must have enforceable rights | housing.html |
| `HOU-PUB-004` | Public housing policy must prioritize long-term quality, safety | housing.html |
| `HOU-PUB-005` | Governments must directly develop, own, or support large-scale | housing.html |
| `HOU-PUB-006` | Public or social housing must be integrated into | housing.html |
| `HOU-PUB-007` | Public housing development must prioritize long-term affordability, du | housing.html |
| `HOU-PUB-008` | Public and social housing must be protected from | housing.html |
| `HOU-PUB-009` | Public-housing management systems must be audited for maintenance | housing.html |
| `HOU-PUB-010` | Public or social housing may not be neglected | housing.html |
| `HOU-QLT-002` | Large-scale subdivision builders and mass residential developers must | housing.html |
| `HOU-QLT-003` | Housing policy should discourage construction patterns that maximize | housing.html |
| `HOU-QLT-004` | Historic housing districts and architecturally significant neighborhoo | housing.html |
| `HOU-QLT-005` | Developers responsible for repeated quality failures, unsafe construct | housing.html |
| `HOU-REG-002` | Housing regulation may not be weakened in ways | housing.html |
| `HOU-REG-003` | Land-use and zoning regulation may not be used | housing.html |
| `HOU-REG-004` | Building and safety codes must be strengthened or | housing.html |
| `HOU-REG-005` | Regulatory reform in housing must target unnecessary delay | housing.html |
| `HOU-REG-006` | Industry influence over housing regulation must be limited | housing.html |
| `HOU-RGT-002` | Access to housing must be practical in reality | housing.html |
| `HOU-RGT-003` | Housing systems must be designed to reduce extraction | housing.html |
| `HOU-RNT-002` | Sudden, excessive rent increases that displace tenants without | housing.html |
| `HOU-RNT-003` | Rent-setting practices that rely on coordinated pricing systems | housing.html |
| `HOU-RPR-002` | Manufacturers, builders, and contractors must not restrict access | housing.html |
| `HOU-RPR-003` | Housing systems must not rely on proprietary, locked | housing.html |
| `HOU-RPR-004` | Policies must prevent forced full-system replacement where repair | housing.html |
| `HOU-RPR-005` | Repairability must be considered a core design requirement | housing.html |
| `HOU-RPR-006` | Tenants must have the right to request and | housing.html |
| `HOU-RPR-007` | In cases of landlord failure to maintain habitable | housing.html |
| `HOU-RPR-008` | Housing systems must prioritize long lifecycle durability, repairabili | housing.html |
| `HOU-RPR-009` | Core housing systems including HVAC, plumbing, electrical systems | housing.html |
| `HOU-RPR-010` | Manufacturers and service providers may not use software | housing.html |
| `HOU-RPR-011` | Building systems installed in homes, apartments, and public | housing.html |
| `HOU-SOI-002` | Housing voucher programs must be paired with access enforcement to ens | housing.html |
| `HOU-SOI-003` | Rental listing platforms may not enable source-of-income discriminatio | housing.html |
| `HOU-STR-001` | Short-term rental platforms must collect and disclose listing data to  | housing.html |
| `HOU-STR-002` | Municipalities must have authority to restrict whole-unit short-term r | housing.html |
| `HOU-STR-003` | Commercial short-term rental operators may not operate residential uni | housing.html |
| `HOU-SUB-002` | Public subsidies must be tied to measurable affordability | housing.html |
| `HOU-SUP-002` | Restrictive zoning, exclusionary land-use rules, and permitting system | housing.html |
| `HOU-SUP-003` | Housing supply reform should prioritize abundant, family-capable, tran | housing.html |
| `HOU-SUP-004` | Inclusionary requirements, affordability set-asides, public-developmen | housing.html |
| `HOU-SUP-005` | Zoning and land-use systems may not be structured | housing.html |
| `HOU-SUP-006` | Permitting and approval processes must be time-bounded, predictable | housing.html |
| `HOU-SUP-007` | Discretionary approval systems that allow arbitrary denial of | housing.html |
| `HOU-SYS-002` | Housing reform should be based on root-cause analysis | housing.html |
| `HOU-SYS-003` | Housing, healthcare, employment, and social-service systems must be | housing.html |
| `HOU-SYS-004` | Systems must intervene early to prevent eviction and | housing.html |
| `HOU-SYS-005` | Housing is an essential public-interest sector and is | housing.html |
| `HOU-SYS-006` | Housing policy must measure success by affordability, stability | housing.html |
| `HOU-TAX-002` | Property tax increases for primary residences should be | housing.html |
| `HOU-TAX-003` | Tax policy should distinguish between primary residences and | housing.html |
| `HOU-TEN-002` | Administrative barriers, legal complexity, and code-enforcement weakne | housing.html |
| `HOU-TEN-003` | Housing code enforcement must be proactive, adequately funded | housing.html |
| `HOU-TEN-004` | Tenants must have the right to clear, stable | housing.html |
| `HOU-TEN-005` | Lease renewals and terminations must be governed by | housing.html |
| `HOU-TEN-006` | Tenants must have protection from sudden or extreme | housing.html |
| `HOU-TEN-007` | Tenants must have the right to organize, form | housing.html |
| `HOU-VAC-002` | Vacancy taxes or equivalent anti-speculation tools should apply | housing.html |
| `HOU-VAC-003` | Housing policy should discourage land banking and empty-home | housing.html |
| `HOU-VAC-004` | Legitimate exceptions to vacancy restrictions may include temporary | housing.html |
| `HOU-VAC-005` | Policies must prevent speculative holding of residential property | housing.html |
| `HOU-VAC-006` | Rapid speculative turnover practices that destabilize housing markets | housing.html |
| `IMM-CLM-002` | Provide temporary protected status automatically for nationals of coun | immigration.html |
| `IMM-CLM-003` | Lead international efforts to establish a climate refugee legal framew | immigration.html |
| `IMM-DACA-001` |  | immigration.html |
| `IMM-DACA-002` |  | immigration.html |
| `IMM-SL-001` |  | immigration.html |
| `IMM-SL-002` |  | immigration.html |
| `INF-AFD-002` | Municipal and cooperative broadband networks must be permitted and sup | infrastructure-and-public-goods.html |
| `INF-EQJ-002` | Clean energy infrastructure investment must be distributed equitably a | infrastructure-and-public-goods.html |
| `INF-LBR-002` | Workers displaced by federally mandated infrastructure transition must | infrastructure-and-public-goods.html |
| `INF-NET-004` | FCC broadband coverage maps must use verified, address-level data; pro | infrastructure-and-public-goods.html |
| `INF-NET-005` | Federal broadband funding must not flow to areas where coverage maps o | infrastructure-and-public-goods.html |
| `INF-PRT-001` | Invest in modernizing U.S. port infrastructure and require that federa | infrastructure-and-public-goods.html |
| `INF-PRT-002` | Establish domestic production capacity requirements for critical goods | infrastructure-and-public-goods.html |
| `INF-RAIL-003` | Separate the Northeast Corridor into an independent public authority a | infrastructure-and-public-goods.html |
| `INF-TRN-006` | Build a national public EV charging network with mandatory coverage in | infrastructure-and-public-goods.html |
| `INF-WAT-002` | Mandate replacement of all lead service lines and lead plumbing in sch | infrastructure-and-public-goods.html |
| `INF-WAT-003` | Establish a federal dam safety program with mandatory inspection, clas | infrastructure-and-public-goods.html |
| `JUD-APT-001` | President must nominate to fill judicial and executive vacancies withi | courts-and-judicial-system.html |
| `JUD-LGO-002` | Jurisdiction stripping authority with procedural safeguards | courts-and-judicial-system.html |
| `JUD-LGO-003` | Supermajority requirement to overturn Supreme Court precedent | courts-and-judicial-system.html |
| `JUD-LGO-004` | Independent enforcement office for judicial recusal and financial disc | courts-and-judicial-system.html |
| `JUD-LGO-005` | Amicus curiae funding and coordination disclosure | courts-and-judicial-system.html |
| `JUD-LGO-006` | Federal judiciary demographic diversity requirements | courts-and-judicial-system.html |
| `JUD-LGO-007` | Administrative law judges — independence protections against political | courts-and-judicial-system.html |
| `JUD-LGO-008` | Independent bipartisan commission for court structural reform | courts-and-judicial-system.html |
| `JUD-NOM-002` | Merit-based judicial selection commissions | courts-and-judicial-system.html |
| `JUD-NOM-003` | Pre-confirmation financial and relationship disclosure | courts-and-judicial-system.html |
| `JUD-SHD-002` | Nationwide injunctions from single district judges subject to expedite | courts-and-judicial-system.html |
| `JUD-SIZ-002` | 18-year staggered terms for Supreme Court justices | courts-and-judicial-system.html |
| `JUD-SIZ-003` | Lower federal court expansion to address case backlog | courts-and-judicial-system.html |
| `JUD-VEN-002` | Mandatory random case assignment; forum shopping prohibited | courts-and-judicial-system.html |
| `JUS-CRB-001` | Civilian review boards must have independent subpoena power | equal-justice-and-policing.html |
| `JUS-CRB-002` | Civilian review boards must have binding discipline authority, not mer | equal-justice-and-policing.html |
| `JUS-CRB-003` | Civilian review boards must be structurally independent from the polic | equal-justice-and-policing.html |
| `JUS-DAT-001` | Criminal justice systems must collect and publish standardized | equal-justice-and-policing.html |
| `JUS-DAT-002` | Data must be disaggregated to detect bias systemic | equal-justice-and-policing.html |
| `JUS-DAT-003` | Public access to justice-system data must be free | equal-justice-and-policing.html |
| `JUS-ERR-001` | Mechanisms must exist to identify correct and remedy | equal-justice-and-policing.html |
| `JUS-ERR-002` | Discovery of systemic error patterns must trigger mandatory | equal-justice-and-policing.html |
| `JUS-ERR-003` | Individuals wrongfully convicted must receive compensation support | equal-justice-and-policing.html |
| `JUS-ERR-004` | People wrongfully convicted are entitled to compensation, restoration | equal-justice-and-policing.html |
| `JUS-ERR-005` | Compensation for wrongful conviction must increase where | equal-justice-and-policing.html |
| `JUS-ERR-006` | In cases of malicious, vindictive, or politically motivated | equal-justice-and-policing.html |
| `JUS-ERR-007` | Wrongful-conviction remedies should include compensation for lost libe | equal-justice-and-policing.html |
| `JUS-ETH-001` | Prosecutors and regulators must disclose conflicts, including prior | equal-justice-and-policing.html |
| `JUS-ETH-002` | Cooling-off periods apply before and after public service | equal-justice-and-policing.html |
| `JUS-PLB-001` | Plea bargaining systems may not be structured | equal-justice-and-policing.html |
| `JUS-PLB-002` | Defendants must have access to all relevant evidence | equal-justice-and-policing.html |
| `JUS-PLB-003` | Plea agreements must be reviewed for fairness | equal-justice-and-policing.html |
| `JUS-PLB-004` | differential between plea offers and post-trial sentencing exposure | equal-justice-and-policing.html |
| `JUS-PLB-005` | Defendants must receive full discovery and a minimum | equal-justice-and-policing.html |
| `JUS-PLB-006` | Courts must review pleas for fairness, proportionality | equal-justice-and-policing.html |
| `JUS-POL-010` | Restrict and effectively prohibit no-knock warrant execution | equal-justice-and-policing.html |
| `JUS-POL-011` | Prohibit predictive policing systems using algorithmic or AI-based ind | equal-justice-and-policing.html |
| `JUS-POL-012` | Mandate public transparency for police union contracts; void accountab | equal-justice-and-policing.html |
| `JUS-PPR-001` | DOJ pattern-or-practice investigation authority must be mandatory, not | equal-justice-and-policing.html |
| `JUS-PPR-002` | Consent decrees must include independent monitors and may not be disso | equal-justice-and-policing.html |
| `JUS-PPR-003` | Federal law enforcement funding conditioned on pattern-or-practice com | equal-justice-and-policing.html |
| `JUS-PPV-001` | Federal government must phase out use of private prisons and private i | equal-justice-and-policing.html |
| `JUS-PPV-002` | Private prison and detention operators may not lobby for criminal just | equal-justice-and-policing.html |
| `JUS-PTL-001` | Monetary bail systems that condition pretrial liberty | equal-justice-and-policing.html |
| `JUS-PTL-002` | Pretrial conditions must be time-limited, reviewable | equal-justice-and-policing.html |
| `JUS-SNT-001` | Sentencing must follow transparent, evidence-based guidelines with req | equal-justice-and-policing.html |
| `JUS-SNT-002` | Sentencing data must be publicly reported and disaggregated | equal-justice-and-policing.html |
| `JUS-SNT-003` | Ability to pay may not reduce custodial accountability | equal-justice-and-policing.html |
| `JUS-SOL-001` | Statutes of limitations for violent assault sexual assault | equal-justice-and-policing.html |
| `JUS-SOL-002` | Legal frameworks must allow reopening or continuation | equal-justice-and-policing.html |
| `JUS-SOL-003` | Limitations rules must not function to shield perpetrators | equal-justice-and-policing.html |
| `JUS-TRN-001` | Ex parte communications with judges or prosecutors outside | equal-justice-and-policing.html |
| `JUS-TRN-002` | Material meetings between defense and prosecutors in serious | equal-justice-and-policing.html |
| `JUS-WHT-001` | Enforcement agencies must maintain specialized units with adequate | equal-justice-and-policing.html |
| `JUS-WHT-002` | Statutes of limitations for complex financial crimes | equal-justice-and-policing.html |
| `JUS-WHT-003` | Whistleblower protections and incentives must be robust | equal-justice-and-policing.html |
| `LAB-AI-002` | AI systems affecting hiring, pay, scheduling, productivity, discipline | labor-and-workers-rights.html |
| `LAB-AI-003` | Employment AI may not move from assistive use | labor-and-workers-rights.html |
| `LAB-AUT-002` | Workers and their representatives must have the right | labor-and-workers-rights.html |
| `LAB-AUT-003` | Automation may not be used as a pretext | labor-and-workers-rights.html |
| `LAB-BEN-002` | Essential worker protections and benefits may not depend | labor-and-workers-rights.html |
| `LAB-BEN-003` | Benefit systems must be designed to support continuity | labor-and-workers-rights.html |
| `LAB-BEN-004` | Portable benefit systems should allow workers to accrue | labor-and-workers-rights.html |
| `LAB-BEN-005` | Employers and platforms must contribute proportionally to portable | labor-and-workers-rights.html |
| `LAB-BEN-006` | Portable benefits may not be used as a | labor-and-workers-rights.html |
| `LAB-BEN-007` | Benefit portability systems must be standardized, transparent, and | labor-and-workers-rights.html |
| `LAB-BEN-008` | Access to healthcare should not depend on retaining | labor-and-workers-rights.html |
| `LAB-BEN-009` | Employment transitions, layoffs, reduced hours, or platform deactivati | labor-and-workers-rights.html |
| `LAB-BEN-010` | Labor policy should reduce coercive dependence on employer-tied | labor-and-workers-rights.html |
| `LAB-CBA-002` | Failure to reach a first contract within a | labor-and-workers-rights.html |
| `LAB-CBA-003` | Collective bargaining systems should include sectoral or industry-wide | labor-and-workers-rights.html |
| `LAB-CBA-004` | Sectoral agreements may set minimum standards for wages | labor-and-workers-rights.html |
| `LAB-CBA-005` | Sectoral bargaining structures must include representation for workers | labor-and-workers-rights.html |
| `LAB-CBA-006` | Collective bargaining must include wages, benefits, scheduling, workpl | labor-and-workers-rights.html |
| `LAB-CBA-007` | Workers must have the ability to bargain over | labor-and-workers-rights.html |
| `LAB-CBA-008` | Collective agreements must be enforceable, with mechanisms for | labor-and-workers-rights.html |
| `LAB-CBA-009` | Violations of collective agreements must result in meaningful | labor-and-workers-rights.html |
| `LAB-CLM-002` | Outdoor and warehouse workers must receive additional climate-specific | labor-and-workers-rights.html |
| `LAB-CLM-003` | Workers may not be retaliated against for refusing to work in dangerou | labor-and-workers-rights.html |
| `LAB-CLS-002` | Misclassification of employees as independent contractors must be | labor-and-workers-rights.html |
| `LAB-COE-002` | Workers must have meaningful ability to leave employment | labor-and-workers-rights.html |
| `LAB-COL-002` | Employers may not engage in union-busting, intimidation, or | labor-and-workers-rights.html |
| `LAB-COL-003` | Workers must have a real, enforceable ability to | labor-and-workers-rights.html |
| `LAB-COL-004` | Collective bargaining is a fundamental counterbalance to concentrated | labor-and-workers-rights.html |
| `LAB-COL-005` | Collective bargaining rights must apply across all sectors | labor-and-workers-rights.html |
| `LAB-COL-006` | Legal barriers that prevent workers from organizing based | labor-and-workers-rights.html |
| `LAB-COL-007` | Public-sector workers must have the right to organize | labor-and-workers-rights.html |
| `LAB-COL-008` | Restrictions on collective action in essential services must | labor-and-workers-rights.html |
| `LAB-CRC-001` | Affordable child care must be treated as public infrastructure prerequ | labor-and-workers-rights.html |
| `LAB-CRC-002` | Large employers must provide or fund child care benefits for workers w | labor-and-workers-rights.html |
| `LAB-CRC-003` | Child care workers must receive wages, benefits, and training comparab | labor-and-workers-rights.html |
| `LAB-DOM-002` | Domestic workers must have written contracts, rest period rights, and  | labor-and-workers-rights.html |
| `LAB-DOM-003` | Home care workers are entitled to workers’ compensation and social ins | labor-and-workers-rights.html |
| `LAB-ENF-002` | Workers must have accessible mechanisms to report violations | labor-and-workers-rights.html |
| `LAB-ENF-003` | Labor enforcement agencies must have sufficient authority, funding | labor-and-workers-rights.html |
| `LAB-ENF-004` | Repeated violations of labor rights must trigger escalating | labor-and-workers-rights.html |
| `LAB-ENF-005` | Workers must have private rights of action to | labor-and-workers-rights.html |
| `LAB-ENF-006` | Labor enforcement agencies must have authority to investigate | labor-and-workers-rights.html |
| `LAB-ENF-007` | Labor rights must be enforceable through public enforcement | labor-and-workers-rights.html |
| `LAB-ENF-008` | Repeat labor violators must be subject to escalating | labor-and-workers-rights.html |
| `LAB-ENF-009` | Labor systems must be evaluated for real-world outcomes | labor-and-workers-rights.html |
| `LAB-GIG-002` | Employment classification must reflect the reality of control | labor-and-workers-rights.html |
| `LAB-GIG-003` | Workers must be classified as employees where the | labor-and-workers-rights.html |
| `LAB-GIG-004` | Independent contractor classification is permitted only where workers | labor-and-workers-rights.html |
| `LAB-GIG-005` | Misclassification to avoid wages, benefits, or protections must | labor-and-workers-rights.html |
| `LAB-GIG-006` | Platform workers must receive compensation that meets or | labor-and-workers-rights.html |
| `LAB-GIG-007` | Pay calculations must include all working time, including | labor-and-workers-rights.html |
| `LAB-GIG-008` | Workers must be reimbursed for necessary work-related expenses | labor-and-workers-rights.html |
| `LAB-GIG-009` | Platforms must provide clear, real-time information about pay | labor-and-workers-rights.html |
| `LAB-GIG-010` | Workers must have access to detailed earnings records | labor-and-workers-rights.html |
| `LAB-GIG-011` | Workers subject to algorithmic management must have the | labor-and-workers-rights.html |
| `LAB-GIG-012` | Algorithmic systems may not be used to impose | labor-and-workers-rights.html |
| `LAB-GIG-013` | Workers must have the right to contest, appeal | labor-and-workers-rights.html |
| `LAB-GIG-014` | Platforms may not suspend, deactivate, or restrict worker | labor-and-workers-rights.html |
| `LAB-GIG-015` | Automated deactivations must be subject to human review | labor-and-workers-rights.html |
| `LAB-GIG-016` | Platforms may not use behavioral nudges, gamification, or | labor-and-workers-rights.html |
| `LAB-GIG-017` | Workers must have the ability to reject work | labor-and-workers-rights.html |
| `LAB-GIG-018` | Gig and platform workers have the right to | labor-and-workers-rights.html |
| `LAB-GIG-019` | Platforms may not classify workers in ways that | labor-and-workers-rights.html |
| `LAB-GIG-020` | Workers must have access to and control over | labor-and-workers-rights.html |
| `LAB-GIG-021` | Workers must be able to transfer relevant work | labor-and-workers-rights.html |
| `LAB-GIG-022` | Rating systems must be transparent, fair, and protected | labor-and-workers-rights.html |
| `LAB-GIG-023` | Workers must have the ability to challenge inaccurate | labor-and-workers-rights.html |
| `LAB-GIG-024` | Platform workers must have access to benefits including | labor-and-workers-rights.html |
| `LAB-GIG-025` | Benefits systems must be designed to follow workers | labor-and-workers-rights.html |
| `LAB-GIG-026` | Platforms may not manipulate availability, visibility, or scheduling | labor-and-workers-rights.html |
| `LAB-GIG-027` | Platforms may not restructure, reclassify, or redesign systems | labor-and-workers-rights.html |
| `LAB-GIG-028` | Labor laws must be enforced against platforms with | labor-and-workers-rights.html |
| `LAB-GIG-029` | Repeated violations by platforms may trigger operational restrictions | labor-and-workers-rights.html |
| `LAB-GOV-002` | Large firms may be required to include worker | labor-and-workers-rights.html |
| `LAB-GOV-003` | Worker governance mechanisms must be structured to provide | labor-and-workers-rights.html |
| `LAB-HRS-002` | Excessive working hours that undermine health, safety, or | labor-and-workers-rights.html |
| `LAB-HRS-003` | Workers must receive overtime compensation for hours worked | labor-and-workers-rights.html |
| `LAB-HRS-004` | Workers must have scheduling protections that account for | labor-and-workers-rights.html |
| `LAB-HRS-005` | Employers may not rely on unstable on-call scheduling | labor-and-workers-rights.html |
| `LAB-LVE-002` | Paid leave must be sufficient in duration and | labor-and-workers-rights.html |
| `LAB-LVE-003` | Workers may not be penalized, retaliated against, or | labor-and-workers-rights.html |
| `LAB-LVE-004` | Governments must ensure leave access for small-business employees | labor-and-workers-rights.html |
| `LAB-LVE-005` | Leave systems must account for caregiving, family emergencies | labor-and-workers-rights.html |
| `LAB-NCP-002` | No-poach and non-solicitation agreements may not function as de facto  | labor-and-workers-rights.html |
| `LAB-NCP-003` | Workers must have enforceable damages claims for unlawful mobility res | labor-and-workers-rights.html |
| `LAB-OWN-002` | Governments should support formation and scaling of worker | labor-and-workers-rights.html |
| `LAB-OWN-003` | Workers should have pathways to ownership transition when | labor-and-workers-rights.html |
| `LAB-OWN-004` | Workers should share in gains from productivity, automation | labor-and-workers-rights.html |
| `LAB-OWN-005` | Compensation systems may not allocate the overwhelming majority | labor-and-workers-rights.html |
| `LAB-OWN-006` | Public incentives, procurement, or tax benefits may be | labor-and-workers-rights.html |
| `LAB-PAY-003` | Wage theft, misclassification, unpaid labor, and delayed payment | labor-and-workers-rights.html |
| `LAB-PAY-004` | Extreme disparities between executive compensation and worker pay | labor-and-workers-rights.html |
| `LAB-PAY-005` | Firms must disclose compensation ratios between executives and | labor-and-workers-rights.html |
| `LAB-PAY-006` | Tax, regulatory, or governance mechanisms may be used | labor-and-workers-rights.html |
| `LAB-PAY-007` | Compensation structures may not incentivize short-term extraction at | labor-and-workers-rights.html |
| `LAB-PBN-002` | Platforms and businesses using contractor labor must contribute to por | labor-and-workers-rights.html |
| `LAB-PBN-003` | Workers must be able to accumulate paid leave and retirement savings a | labor-and-workers-rights.html |
| `LAB-PLT-002` | Platforms may not use algorithmic control, opacity, or | labor-and-workers-rights.html |
| `LAB-PLT-003` | Workers must have the right to transparency and | labor-and-workers-rights.html |
| `LAB-PRL-002` | Prison labor performed for private corporate benefit must receive fair | labor-and-workers-rights.html |
| `LAB-PRL-003` | Supply chains must be audited for and free of forced labor at all tier | labor-and-workers-rights.html |
| `LAB-RET-002` | Retirement systems must be designed to protect workers | labor-and-workers-rights.html |
| `LAB-RGT-002` | Workers must have access to clear, enforceable labor | labor-and-workers-rights.html |
| `LAB-RGT-003` | Labor rights must apply equally to full-time, part-time | labor-and-workers-rights.html |
| `LAB-SCH-002` | Last-minute schedule changes must be compensated with premium pay | labor-and-workers-rights.html |
| `LAB-SCH-003` | Workers must have the right to request flexible or stable scheduling w | labor-and-workers-rights.html |
| `LAB-SFT-002` | Workers must have the right to report unsafe | labor-and-workers-rights.html |
| `LAB-SUR-002` | Continuous monitoring of workers through cameras, biometrics, keystrok | labor-and-workers-rights.html |
| `LAB-SUR-003` | Worker data collection must be transparent, minimal, and | labor-and-workers-rights.html |
| `LAB-SUR-004` | Workers must have the right to know what | labor-and-workers-rights.html |
| `LAB-SUR-005` | Surveillance systems may not be used to enforce | labor-and-workers-rights.html |
| `LAB-SYS-002` | Workers must share in the economic value they | labor-and-workers-rights.html |
| `LAB-SYS-003` | Employment systems must not rely on coercion, dependency | labor-and-workers-rights.html |
| `LAB-TRN-002` | Economic transition systems must be designed to support | labor-and-workers-rights.html |
| `LAB-TRN-003` | Employers and platforms that materially displace labor through | labor-and-workers-rights.html |
| `LAB-UNN-002` | Employers may not delay, challenge, or obstruct union | labor-and-workers-rights.html |
| `LAB-UNN-003` | Where a majority of workers demonstrate support through | labor-and-workers-rights.html |
| `LAB-UNN-004` | Workers must have the option to form unions | labor-and-workers-rights.html |
| `LAB-UNN-005` | Employers may not engage in union-busting practices, including | labor-and-workers-rights.html |
| `LAB-UNN-006` | Retaliation against workers for organizing activity, including firing | labor-and-workers-rights.html |
| `LAB-UNN-007` | Violations of union rights must carry meaningful penalties | labor-and-workers-rights.html |
| `LAB-UNN-008` | Employers may not fragment workforces, misclassify roles, or | labor-and-workers-rights.html |
| `LAB-UNN-009` | Multi-entity corporate structures may not be used to | labor-and-workers-rights.html |
| `LAB-UNN-010` | Workers must have access to communication channels to | labor-and-workers-rights.html |
| `LAB-UNN-011` | Employers may not restrict lawful communication among workers | labor-and-workers-rights.html |
| `LAB-UNN-012` | Individuals who direct, authorize, or knowingly participate in | labor-and-workers-rights.html |
| `LAB-UNN-013` | Personal liability applies to executives, managers, HR personnel | labor-and-workers-rights.html |
| `LAB-UNN-014` | Use of third-party firms, consultants, or intermediaries does | labor-and-workers-rights.html |
| `LAB-UNN-015` | Prohibited conduct includes retaliation, intimidation, coercion, surve | labor-and-workers-rights.html |
| `LAB-UNN-016` | Individuals found liable for union-busting may be subject | labor-and-workers-rights.html |
| `LAB-UNN-017` | Civil penalties must be scaled to deter misconduct | labor-and-workers-rights.html |
| `LAB-UNN-018` | Willful, repeated, or egregious violations of labor rights | labor-and-workers-rights.html |
| `LAB-UNN-019` | Criminal liability must require clear evidence of intent | labor-and-workers-rights.html |
| `LAB-UNN-020` | Individuals may not evade liability through corporate structures | labor-and-workers-rights.html |
| `LAB-UNN-021` | Individuals found liable for serious labor violations may | labor-and-workers-rights.html |
| `LAB-UNN-022` | Financial penalties for union-busting violations must be substantial | labor-and-workers-rights.html |
| `LAB-UNN-023` | Penalties must be tied to company size and | labor-and-workers-rights.html |
| `LAB-UNN-024` | Large firms may not face reduced effective penalties | labor-and-workers-rights.html |
| `LAB-UNN-025` | Each act of retaliation, interference, or unlawful conduct | labor-and-workers-rights.html |
| `LAB-UNN-026` | Ongoing violations must trigger daily or periodic escalating | labor-and-workers-rights.html |
| `LAB-UNN-027` | Repeat or patterned violations must trigger enhanced penalties | labor-and-workers-rights.html |
| `LAB-UNN-028` | Persistent noncompliance may result in structural remedies, including | labor-and-workers-rights.html |
| `LAB-UNN-029` | Workers harmed by union-busting must receive full restitution | labor-and-workers-rights.html |
| `LAB-UNN-030` | Remedies must account for chilling effects on organizing | labor-and-workers-rights.html |
| `LAB-UNN-031` | Firms found to have engaged in serious or | labor-and-workers-rights.html |
| `LAB-UNN-032` | Labor violations and penalties must be publicly disclosed | labor-and-workers-rights.html |
| `LAB-UNN-033` | Settlements may not eliminate accountability for systemic or | labor-and-workers-rights.html |
| `LEG-BBA-001` | Oppose constitutional balanced budget amendment as economically harmfu | legislative-reform.html |
| `LEG-BBA-002` | Establish a statutory long-term fiscal sustainability framework — not  | legislative-reform.html |
| `LEG-CAP-001` | Substantially increase congressional staff salaries and total staff ca | legislative-reform.html |
| `LEG-CAP-002` | Restore the Office of Technology Assessment with independent mandate | legislative-reform.html |
| `LEG-CAP-003` | Mandatory member schedule — minimum days in session with committee att | legislative-reform.html |
| `LEG-COM-001` | Replace seniority-only committee assignments with merit and expertise  | legislative-reform.html |
| `LEG-COM-002` | Restore committee markup authority — prohibit floor consideration of b | legislative-reform.html |
| `LEG-COM-003` | Committee chair term limits — maximum six consecutive years in any sin | legislative-reform.html |
| `LEG-DB-001` | Establish searchable public federal law database | legislative-reform.html |
| `LEG-DB-002` | Database includes judicial opinions and agency interpretations | legislative-reform.html |
| `LEG-DB-003` | Database allows structured public comment and annotation | legislative-reform.html |
| `LEG-DB-004` | Law database must be free, searchable, and accessible | legislative-reform.html |
| `LEG-DMJ-002` | Representational systems require periodic democratic review | legislative-reform.html |
| `LEG-DRF-003` | Large sections require plain-language summaries | legislative-reform.html |
| `LEG-DRF-004` | Each provision must be relevant to the law's stated purpose | legislative-reform.html |
| `LEG-DRF-005` | Laws reviewed for loopholes and exploit paths before passage | legislative-reform.html |
| `LEG-DRF-006` | Conflicts with existing law reconciled before enactment | legislative-reform.html |
| `LEG-EXE-001` | Legislature may select or remove head of government | legislative-reform.html |
| `LEG-HSE-001` | House must represent population proportionally as primary body | legislative-reform.html |
| `LEG-HSE-002` | House must expand to restore representational accuracy | legislative-reform.html |
| `LEG-HSE-003` | House is primary origin of fiscal and domestic legislation | legislative-reform.html |
| `LEG-LOB-001` | Extend congressional revolving door cooling-off period to five years | legislative-reform.html |
| `LEG-LOB-002` | Real-time lobbying disclosure — replace quarterly reports with continu | legislative-reform.html |
| `LEG-LOB-003` | Earmark transparency reform — full disclosure required; outright ban r | legislative-reform.html |
| `LEG-LOB-004` | Revolving door extended to executive branch senior officials and indep | legislative-reform.html |
| `LEG-OVR-001` | Congress must have strong oversight and enforcement powers | legislative-reform.html |
| `LEG-OVR-002` | Oversight cannot be blocked by executive privilege or partisanship | legislative-reform.html |
| `LEG-PRO-002` | Systems must resolve persistent deadlock between chambers | legislative-reform.html |
| `LEG-PRO-003` | Discharge petition reform — lower threshold and automatic scheduling f | legislative-reform.html |
| `LEG-PRO-004` | Proxy voting prohibited for floor votes; remote voting infrastructure  | legislative-reform.html |
| `LEG-REV-001` | Permanent body annually reviews federal laws for obsolescence | legislative-reform.html |
| `LEG-REV-002` | Review body recommends repeal, consolidation, or modernization | legislative-reform.html |
| `LEG-REV-003` | Review process includes public reporting and cleanup packages | legislative-reform.html |
| `LEG-RPL-002` | Repeal Comstock Act and similar archaic morality laws | legislative-reform.html |
| `LEG-SEN-001` | Senate may use population-weighted voting to reduce imbalance | legislative-reform.html |
| `LEG-SEN-002` | Senate may include both state-based and population-based seats | legislative-reform.html |
| `LEG-SEN-004` | House may have final legislative authority after Senate review | legislative-reform.html |
| `LEG-STK-001` | Ban on individual stock trading by members of Congress, senior staff,  | legislative-reform.html |
| `LEG-STK-002` | Strengthen STOCK Act enforcement — automatic civil penalties and an in | legislative-reform.html |
| `LEG-STR-001` | Bicameralism retained but each chamber needs distinct purpose | legislative-reform.html |
| `LEG-SYS-001` | Legislature must reflect democracy with power safeguards | legislative-reform.html |
| `LEG-SYS-002` | No persistent minority governance without democratic justification | legislative-reform.html |
| `MED-DIS-001` |  | information-and-media.html |
| `MED-DIS-002` |  | information-and-media.html |
| `MED-DIS-003` |  | information-and-media.html |
| `MED-LNJ-001` |  | information-and-media.html |
| `MED-LNJ-002` |  | information-and-media.html |
| `MED-NET-002` | Treat broadband internet access as a public utility | information-and-media.html |
| `MED-NET-003` | Guarantee universal affordable broadband access as essential public in | information-and-media.html |
| `MED-OWN-002` | Prohibit private equity and hedge fund acquisition of local news outle | information-and-media.html |
| `MED-OWN-003` | Require disclosure of media ownership, beneficial ownership, and fundi | information-and-media.html |
| `MED-OWN-004` | Create a public interest journalism fund to support local and investig | information-and-media.html |
| `MED-PLT-002` | Require platforms to publish and allow auditing of algorithmic amplifi | information-and-media.html |
| `MED-PLT-003` | Prohibit deceptive design practices that manipulate user behavior on i | information-and-media.html |
| `MED-PLT-004` | Require labeling of AI-generated content and synthetic media | information-and-media.html |
| `MED-PUB-002` | Require public agencies to make government information accessible with | information-and-media.html |
| `MED-S230-001` |  | information-and-media.html |
| `MED-S230-002` |  | information-and-media.html |
| `PAT-ANT-001` | Patent rights may not be used to justify | technology-and-ai.html |
| `PAT-ANT-002` | Patent enforcement strategies that function as anti-competitive tools | technology-and-ai.html |
| `PAT-INT-001` | Patent rights may not be used to block | technology-and-ai.html |
| `PAT-INT-002` | Circumvention of technical protections for the purpose | technology-and-ai.html |
| `PAT-INT-003` | Patent enforcement may not be used to restrict | technology-and-ai.html |
| `PAT-LIC-001` | Compulsory licensing must be available where patent control | technology-and-ai.html |
| `PAT-LIC-002` | Essential sectors including healthcare, agriculture, infrastructure, a | technology-and-ai.html |
| `PAT-RPR-001` | Repair, maintenance, and restoration of legally owned products | technology-and-ai.html |
| `PAT-RPR-002` | Replacement parts, consumables, and repair processes | technology-and-ai.html |
| `PAT-SCP-001` | Patent duration and scope must be calibrated | technology-and-ai.html |
| `PAT-SCP-002` | Extensions, evergreening, and minor modification strategies that artif | technology-and-ai.html |
| `PAT-SFT-001` | Abstract software concepts, algorithms, and general computational meth | technology-and-ai.html |
| `PAT-SFT-002` | Software patents must be narrowly defined, technically specific | technology-and-ai.html |
| `PAT-SFT-003` | Patent claims that would prevent independent implementation | technology-and-ai.html |
| `PAT-SYS-001` | patent system must promote genuine innovation, public benefit | technology-and-ai.html |
| `PAT-THK-001` | Accumulation of large patent portfolios for the primary | technology-and-ai.html |
| `PAT-THK-002` | Patent thickets that create unreasonable barriers to entry | technology-and-ai.html |
| `PAT-THK-003` | Regulatory bodies must have authority to limit, unwind | technology-and-ai.html |
| `PAT-TR-001` | Patent enforcement may not be conducted | technology-and-ai.html |
| `PAT-TR-002` | Entities that do not produce, license in good | technology-and-ai.html |
| `PAT-TR-003` | Courts must have authority to require fee-shifting, sanctions | technology-and-ai.html |
| `PAT-TR-004` | Patent-assertion entities may not use shell structures | technology-and-ai.html |
| `PAT-TRN-001` | Patent ownership, licensing structures, and enforcement activity | technology-and-ai.html |
| `PAT-TRN-002` | Shell ownership structures used to obscure patent control | technology-and-ai.html |
| `RGT-DIS-001` | Abolish Subminimum Wage: Repeal Section 14(c) of the Fair Labor Standa | rights-and-civil-liberties.html |
| `RGT-DIS-002` | Eliminate SSDI Processing Backlogs | rights-and-civil-liberties.html |
| `RGT-DIS-003` | Eliminate the SSDI Earnings Cliff | rights-and-civil-liberties.html |
| `RGT-DIS-004` | Vocational Rehabilitation as an Entitlement | rights-and-civil-liberties.html |
| `RGT-DIS-005` | Full Funding for Supported Employment Programs | rights-and-civil-liberties.html |
| `RGT-DIS-006` | Strengthen ADA Enforcement | rights-and-civil-liberties.html |
| `RGT-DIS-007` | Disability-Inclusive Poverty Reduction Goals | rights-and-civil-liberties.html |
| `RGT-DIS-008` | Home and Community-Based Services as a Medicaid Entitlement | rights-and-civil-liberties.html |
| `RGT-FOO-001` | The Right to Food Is a Fundamental Right | rights-and-civil-liberties.html |
| `RGT-FOO-002` | SNAP Must Be Adequately Funded; Benefits Must Reflect Actual Food Cost | rights-and-civil-liberties.html |
| `RGT-FOO-003` | Work Requirements for Food Assistance Prohibited Where Individual Cann | rights-and-civil-liberties.html |
| `RGT-FOO-004` | Universal School Meals Without Charge; School Lunch Debt Practices Pro | rights-and-civil-liberties.html |
| `RGT-FOO-005` | Federal Investment to Address Food Deserts | rights-and-civil-liberties.html |
| `RGT-FOO-006` | Full Funding and Modernization of WIC | rights-and-civil-liberties.html |
| `RGT-POV-001` | Elimination of Poverty as Explicit National Policy Goal | rights-and-civil-liberties.html |
| `RGT-POV-002` | Comprehensive Poverty Measurement Using Both OPM and SPM | rights-and-civil-liberties.html |
| `RGT-POV-003` | Poverty Impact Assessment Required for Major Federal Legislation | rights-and-civil-liberties.html |
| `RGT-POV-004` | Annual Disaggregated Poverty Reporting | rights-and-civil-liberties.html |
| `RGT-POV-005` | Poverty Reduction Is Cross-Pillar; All Relevant Policy Must Be Evaluat | rights-and-civil-liberties.html |
| `RGT-RPR-001` | Acknowledge reparations obligation | rights-and-civil-liberties.html |
| `RGT-RPR-002` | Commission to study and recommend redress | rights-and-civil-liberties.html |
| `RGT-RPR-003` | Redress must be substantive, not symbolic | rights-and-civil-liberties.html |
| `RGT-RPR-004` | No retaliation or penalty for reparations advocacy | rights-and-civil-liberties.html |
| `RGT-SPH-001` | Federal anti-SLAPP legislation to protect free speech and public parti | rights-and-civil-liberties.html |
| `RGT-SPH-002` | Right to peaceful assembly and protest — ban on kettling, crowd contro | rights-and-civil-liberties.html |
| `RGT-SPH-003` | Religious freedom is not a license to discriminate against others in p | rights-and-civil-liberties.html |
| `RGT-SPH-004` | Right to disconnect — employees have a legally enforceable right to be | rights-and-civil-liberties.html |
| `RGT-STA-001` | Federal statute codifying reproductive rights while constitutional ame | rights-and-civil-liberties.html |
| `RGT-STA-002` | Federal statute codifying LGBTQ+ protections in employment, housing, a | rights-and-civil-liberties.html |
| `RGT-STA-003` | Anti-backsliding: once a right is recognized, it may not be eliminated | rights-and-civil-liberties.html |
| `RGT-TEC-002` | Fourth Amendment warrant requirement extended to all digital communica | rights-and-civil-liberties.html |
| `RGT-TEC-003` | Reform the third-party doctrine — sharing data with a service provider | rights-and-civil-liberties.html |
| `RGT-TEC-004` | FISA court reform — mandatory adversarial advocate, transparency, and  | rights-and-civil-liberties.html |
| `RGT-TEC-005` | National Security Letter gag orders must be subject to judicial review | rights-and-civil-liberties.html |
| `RGT-TEC-006` | Regulate data brokers — individuals have rights of access, correction, | rights-and-civil-liberties.html |
| `RGT-TEC-007` | Prohibit mass biometric surveillance; biometric data requires affirmat | rights-and-civil-liberties.html |
| `RPR-AGR-001` | Full diagnostic access required for agricultural equipment | consumer-rights.html |
| `RPR-AGR-002` | Dealer-only repair access restriction is prohibited | consumer-rights.html |
| `RPR-AGR-003` | Software locks may not prevent lawful equipment repair | consumer-rights.html |
| `RPR-AGR-004` | Unauthorized repair may not trigger equipment degradation | consumer-rights.html |
| `RPR-AGR-005` | Time-sensitive equipment must be repairable without unreasonable delay | consumer-rights.html |
| `RPR-AGR-006` | Prevent repair bottlenecks during critical agricultural periods | consumer-rights.html |
| `RPR-AGR-007` | Parts, tools, and manuals available at fair and reasonable terms | consumer-rights.html |
| `RPR-AGR-008` | Equipment ownership may not be reduced to a license | consumer-rights.html |
| `RPR-AGR-009` | Contractual repair restrictions on owned equipment are unenforceable | consumer-rights.html |
| `RPR-AGR-010` | No exclusive repair market control through technical restrictions | consumer-rights.html |
| `RPR-AGR-011` | Agricultural repair violations trigger accelerated enforcement | consumer-rights.html |
| `RPR-ANTI-001` | No restriction of repair to authorized service networks | consumer-rights.html |
| `RPR-ANTI-002` | DRM and component pairing systems blocking repair are prohibited | consumer-rights.html |
| `RPR-ANTI-003` | Third-party repair may not void warranty unless causally linked | consumer-rights.html |
| `RPR-AUTO-001` | Vehicles must provide independent diagnostic and repair access | consumer-rights.html |
| `RPR-AUTO-002` | Repair rights apply to all vehicles including agricultural and industr | consumer-rights.html |
| `RPR-COM-001` | Repair rights apply fully to commercial equipment | consumer-rights.html |
| `RPR-COM-002` | Manufacturers may not restrict diagnostic information access | consumer-rights.html |
| `RPR-COM-003` | Error systems may not obscure faults or mislead operators | consumer-rights.html |
| `RPR-COM-004` | Authorized-only repair restrictions are prohibited where access is lim | consumer-rights.html |
| `RPR-COM-005` | Software-enforced service monopolies are prohibited | consumer-rights.html |
| `RPR-COM-006` | Equipment design may not predictably cause extended repair-related dow | consumer-rights.html |
| `RPR-COM-007` | Recurring failure states due to design lockout subject to review | consumer-rights.html |
| `RPR-COM-008` | Manufacturers may not obscure repair pathways or conceal faults | consumer-rights.html |
| `RPR-COM-009` | Third-party repair tools and interfaces may not be blocked | consumer-rights.html |
| `RPR-COM-010` | Manufacturers may not interfere with third-party repair solutions | consumer-rights.html |
| `RPR-DES-001` | Products must be designed for reasonable disassembly | consumer-rights.html |
| `RPR-DES-002` | Wear components must be individually replaceable | consumer-rights.html |
| `RPR-DES-003` | Manufacturers must publish repairability scores | consumer-rights.html |
| `RPR-ELC-001` | Consumer electronics must allow component-level repair | consumer-rights.html |
| `RPR-ENF-001` | Regulators may compel access to repair materials | consumer-rights.html |
| `RPR-ENF-002` | Violations carry penalties, private right of action, and injunction | consumer-rights.html |
| `RPR-ENF-003` | Safety claims blocking repair must be specifically demonstrated | consumer-rights.html |
| `RPR-ENF-004` | Repair standards cover vehicles, electronics, farm, medical devices | consumer-rights.html |
| `RPR-ENF-005` | Public procurement favors repairable and sustainable products | consumer-rights.html |
| `RPR-LIFE-001` | Products must meet minimum durability standards by category | consumer-rights.html |
| `RPR-LIFE-002` | Manufacturers must support products for a minimum period | consumer-rights.html |
| `RPR-LIFE-003` | Artificial lifespan limitation through software is prohibited | consumer-rights.html |
| `RPR-SYS-001` | Right to repair owned products without unreasonable restriction | consumer-rights.html |
| `RPR-SYS-002` | Manufacturers must provide repair access at fair and reasonable terms | consumer-rights.html |
| `RPR-SYS-003` | Products may not be designed to prevent repair | consumer-rights.html |
| `STS-AGY-001` | Reform FDA approval pathways to be faster without reducing safety or e | science-technology-space.html |
| `STS-AGY-002` | Reduce FDA's structural dependence on industry user fees as its primar | science-technology-space.html |
| `STS-AGY-003` | Protect CDC's operational independence and data reporting from politic | science-technology-space.html |
| `STS-AGY-004` | Establish NIST as the authoritative neutral standards body for AI, qua | science-technology-space.html |
| `STS-AGY-005` | Create permanent cross-agency science councils for integrated research | science-technology-space.html |
| `STS-AGY-006` | Expand federal research partnerships with land-grant universities, HBC | science-technology-space.html |
| `STS-DEB-001` | Fund Space Force and interagency debris tracking and active orbital cl | science-technology-space.html |
| `STS-DEB-002` | Assign financial responsibility for end-of-life satellite disposal to  | science-technology-space.html |
| `STS-DEB-003` | Cap large satellite constellation authorizations without approved debr | science-technology-space.html |
| `STS-DEB-004` | Make approved deorbit plans a mandatory condition of FCC spectrum and  | science-technology-space.html |
| `STS-DEB-005` | Lead the development of an international space traffic management trea | science-technology-space.html |
| `STS-DEB-006` | Designate Kessler syndrome prevention as a national security and econo | science-technology-space.html |
| `STS-EDU-001` | Establish a federal strategy and dedicated funding for public science  | science-technology-space.html |
| `STS-EDU-002` | Adopt a science-and-belief coexistence framework that broadens science | science-technology-space.html |
| `STS-EDU-003` | Protect evidence-based K-12 science curricula from political interfere | science-technology-space.html |
| `STS-EDU-004` | Create a National Science Communication Fund to support accessible, ac | science-technology-space.html |
| `STS-EDU-005` | Sustain federal investment in science museums, planetariums, and publi | science-technology-space.html |
| `STS-FND-001` | Establish a mandatory minimum federal investment in basic and applied  | science-technology-space.html |
| `STS-FND-002` | Replace annual grant cycles with five-year funding windows for all maj | science-technology-space.html |
| `STS-FND-003` | Prohibit industry-funded research from serving as the sole evidentiary | science-technology-space.html |
| `STS-FND-004` | Create formal cross-agency research partnerships across CDC, FDA, NASA | science-technology-space.html |
| `STS-FND-005` | Require a funding commitment whenever a federal agency determines that | science-technology-space.html |
| `STS-FND-006` | Require immediate, barrier-free public access to all federally funded  | science-technology-space.html |
| `STS-INT-001` | Maintain U.S. leadership in international scientific treaty frameworks | science-technology-space.html |
| `STS-INT-002` | Reinstate and expand international climate science cooperation as a pe | science-technology-space.html |
| `STS-INT-003` | Build pandemic preparedness as permanent global research infrastructur | science-technology-space.html |
| `STS-INT-004` | Treat U.S. scientific credibility as a foreign policy asset and scienc | science-technology-space.html |
| `STS-PUB-001` | Create a national open-access research database for all publicly funde | science-technology-space.html |
| `STS-PUB-002` | Require pre-publication quality screening for sample adequacy, researc | science-technology-space.html |
| `STS-PUB-003` | Require plain-language summaries alongside every published paper from  | science-technology-space.html |
| `STS-PUB-004` | Mandate pre-registration of study methodology before data collection f | science-technology-space.html |
| `STS-PUB-005` | Require independent replication before high-impact studies can serve a | science-technology-space.html |
| `STS-PUB-006` | Require publication of negative results to combat publication bias | science-technology-space.html |
| `STS-SPC-001` | Restore and maintain a NASA-operated crewed spacecraft capability inde | science-technology-space.html |
| `STS-SPC-002` | Restore NASA's capability to service, repair, and upgrade orbital infr | science-technology-space.html |
| `STS-SPC-003` | Provide NASA with multi-year budget stability and long-range program p | science-technology-space.html |
| `STS-SPC-004` | Recognize space exploration as a source of national inspiration and a  | science-technology-space.html |
| `STS-SPC-005` | Extend the ISS cooperation model to deep space exploration through per | science-technology-space.html |
| `SYS-AGY-001` | Restore removal-for-cause protection for heads of independent regulato | checks-and-balances.html |
| `SYS-AGY-002` | Civil service anti-politicization — prohibit reclassification of caree | checks-and-balances.html |
| `SYS-AGY-003` | Protect state sovereignty — establish anti-preemption floor for more-p | checks-and-balances.html |
| `SYS-EMG-001` | Automatic 90-day sunset on national emergency declarations with requir | checks-and-balances.html |
| `SYS-EMG-002` | Prohibit use of emergency declarations to circumvent congressional app | checks-and-balances.html |
| `SYS-EMG-003` | Fast-track judicial review for emergency declarations — justiciable st | checks-and-balances.html |
| `SYS-IMP-001` | Enforce the Impoundment Control Act — criminal penalties for unlawful  | checks-and-balances.html |
| `SYS-IMP-002` | Automatic continuing resolutions — end government shutdowns as politic | checks-and-balances.html |
| `SYS-LAW-001` | Laws and system rules must be enforceable, clear | checks-and-balances.html |
| `SYS-LAW-002` | Laws should be written with definite terms, explicit | checks-and-balances.html |
| `SYS-LAW-003` | Flexibility clauses must be bounded, reviewable, and tied | checks-and-balances.html |
| `SYS-REG-001` | Regulation must protect safety, quality, fairness | checks-and-balances.html |
| `SYS-REG-002` | Regulatory systems must distinguish between protections that materiall | checks-and-balances.html |
| `SYS-REG-003` | Removal or modification of regulations must be evidence-based | checks-and-balances.html |
| `SYS-REG-004` | Regulations that protect safety, habitability, environmental integrity | checks-and-balances.html |
| `SYS-REG-005` | Regulatory processes may not be structured to create | checks-and-balances.html |
| `SYS-REG-006` | Regulatory systems must include safeguards against regulatory capture | checks-and-balances.html |
| `SYS-REG-007` | Regulation must be enforceable in practice; under-enforced | checks-and-balances.html |
| `SYS-REG-008` | Regulatory frameworks must be periodically reviewed to remove | checks-and-balances.html |
| `SYS-REG-009` | Mandatory compliance with oversight body findings — binding remedial o | checks-and-balances.html |
| `SYS-WPR-001` | Enforce the War Powers Resolution — automatic funding cut-off for unau | checks-and-balances.html |
| `SYS-WPR-002` | Repeal and replace open-ended AUMFs with time-limited, scope-defined a | checks-and-balances.html |
| `SYS-WPR-003` | Strict limits on domestic deployment of military forces — strengthen P | checks-and-balances.html |
| `TAX-ADM-002` | Automated tax-administration systems must be transparent, reviewable | taxation-and-wealth.html |
| `TAX-ADM-003` | IRS modernization must prioritize public usability, fraud detection | taxation-and-wealth.html |
| `TAX-AI-002` | Organizations that replace or substantially displace human labor | taxation-and-wealth.html |
| `TAX-AI-003` | AI taxation applies where automation materially reduces labor | taxation-and-wealth.html |
| `TAX-AI-004` | AI tax obligations must be based on measurable | taxation-and-wealth.html |
| `TAX-AI-005` | AI taxation systems must prevent avoidance through reclassification | taxation-and-wealth.html |
| `TAX-AI-006` | Companies may not evade AI taxation by shifting | taxation-and-wealth.html |
| `TAX-AI-007` | Revenue from AI-related taxation should support workforce transition | taxation-and-wealth.html |
| `TAX-AI-008` | AI tax systems must balance innovation incentives | taxation-and-wealth.html |
| `TAX-AI-009` | Beneficial uses of AI that improve safety, accessibility | taxation-and-wealth.html |
| `TAX-AI-010` | Companies deriving disproportionate economic power from AI systems | taxation-and-wealth.html |
| `TAX-BEP-002` | Transfer pricing must reflect real market value | taxation-and-wealth.html |
| `TAX-BEP-003` | Artificial profit allocation to low-tax jurisdictions without correspo | taxation-and-wealth.html |
| `TAX-CAP-002` | Preferential treatment of capital income that disproportionately benef | taxation-and-wealth.html |
| `TAX-CAP-003` | Long-term investment incentives may be preserved only where | taxation-and-wealth.html |
| `TAX-CAP-004` | Capital gains must be taxed in a manner | taxation-and-wealth.html |
| `TAX-CAP-005` | Unrealized gains at extreme wealth levels may be | taxation-and-wealth.html |
| `TAX-CAP-006` | Step-up in basis rules that eliminate tax | taxation-and-wealth.html |
| `TAX-CAP-007` | Compensation or value derived from personal labor | taxation-and-wealth.html |
| `TAX-CAP-008` | Carried interest, performance allocation, and similar mechanisms that | taxation-and-wealth.html |
| `TAX-CDR-002` | Senior executive branch officials must disclose tax returns annually d | taxation-and-wealth.html |
| `TAX-CDR-003` | Large corporations must publicly disclose country-by-country tax repor | taxation-and-wealth.html |
| `TAX-COR-002` | Corporate tax systems must be designed to prevent | taxation-and-wealth.html |
| `TAX-COR-003` | Corporations may not use shell entities, internal royalty | taxation-and-wealth.html |
| `TAX-COR-004` | Corporate tax systems must reflect real economic activity | taxation-and-wealth.html |
| `TAX-COR-005` | Corporations must pay a minimum effective tax rate | taxation-and-wealth.html |
| `TAX-COR-006` | Effective tax rate calculations must account for global | taxation-and-wealth.html |
| `TAX-DED-002` | Excessive executive compensation, stock-based compensation, and simila | taxation-and-wealth.html |
| `TAX-DED-003` | Interest deductions may be limited where used | taxation-and-wealth.html |
| `TAX-DED-004` | Internal financial arrangements, including intercompany loans, royalti | taxation-and-wealth.html |
| `TAX-DED-005` | Transactions lacking economic substance beyond tax reduction | taxation-and-wealth.html |
| `TAX-DMJ-002` | legitimacy of the tax system depends on visible | taxation-and-wealth.html |
| `TAX-DMJ-003` | tax system must be visibly fair in practice | taxation-and-wealth.html |
| `TAX-DMJ-004` | Simplicity, fairness, and enforceability are co-equal design goals | taxation-and-wealth.html |
| `TAX-ENF-002` | Repeated, willful, or large-scale tax evasion must trigger | taxation-and-wealth.html |
| `TAX-ENF-003` | Tax audits and investigations must prioritize large-scale evasion | taxation-and-wealth.html |
| `TAX-ENF-004` | Professional facilitators of tax fraud or abusive tax | taxation-and-wealth.html |
| `TAX-ENF-005` | Tax enforcement must prioritize large corporations, complex structures | taxation-and-wealth.html |
| `TAX-ENF-006` | Professional enablers of corporate tax avoidance, including law | taxation-and-wealth.html |
| `TAX-ENF-007` | Repeated or large-scale corporate tax avoidance must trigger | taxation-and-wealth.html |
| `TAX-ENF-008` | Corporations may not indefinitely delay tax enforcement through | taxation-and-wealth.html |
| `TAX-ENF-009` | Simplification for ordinary taxpayers must be paired | taxation-and-wealth.html |
| `TAX-ENF-010` | Enforcement resources must be allocated according to risk | taxation-and-wealth.html |
| `TAX-ENV-002` | Environmental taxation must be structured to reduce pollution | taxation-and-wealth.html |
| `TAX-ENV-003` | Environmental taxes and fees may not be used | taxation-and-wealth.html |
| `TAX-ENV-004` | Carbon-intensive activity may be subject to direct taxation | taxation-and-wealth.html |
| `TAX-ENV-005` | Environmental tax systems must not rely on unverifiable | taxation-and-wealth.html |
| `TAX-ENV-006` | Carbon pricing or equivalent environmental taxation must be | taxation-and-wealth.html |
| `TAX-ENV-007` | Environmental tax systems must distinguish between productive necessit | taxation-and-wealth.html |
| `TAX-ENV-008` | Water extraction and intensive water use may be | taxation-and-wealth.html |
| `TAX-ENV-009` | Water-related taxation and pricing must account for local | taxation-and-wealth.html |
| `TAX-ENV-010` | Large-scale industrial water use may be subject | taxation-and-wealth.html |
| `TAX-ENV-011` | Water taxation and fee systems must not undermine | taxation-and-wealth.html |
| `TAX-ENV-012` | Polluting activities and persistent pollutants may be subject | taxation-and-wealth.html |
| `TAX-ENV-013` | Tax and fee systems may be used | taxation-and-wealth.html |
| `TAX-ENV-014` | Environmental taxes must account for lifecycle harm, including | taxation-and-wealth.html |
| `TAX-ENV-015` | Environmental tax policy should incentivize durable products, repairab | taxation-and-wealth.html |
| `TAX-ENV-016` | Tax advantages may be used to support repair | taxation-and-wealth.html |
| `TAX-ENV-017` | Tax policy may disfavor disposable, non-repairable, short-lifecycle | taxation-and-wealth.html |
| `TAX-ENV-018` | Environmental tax systems must include strong anti-evasion rules | taxation-and-wealth.html |
| `TAX-ENV-019` | Corporations may not reduce environmental tax obligations through | taxation-and-wealth.html |
| `TAX-ENV-020` | Imports and cross-border supply chains may be subject | taxation-and-wealth.html |
| `TAX-ENV-021` | Revenue from environmental taxation should support environmental clean | taxation-and-wealth.html |
| `TAX-ENV-022` | Environmental tax revenue should also support household cost | taxation-and-wealth.html |
| `TAX-ENV-023` | Environmental tax systems must be designed so that | taxation-and-wealth.html |
| `TAX-ENV-024` | Environmental tax systems must be transparent, publicly understandable | taxation-and-wealth.html |
| `TAX-ENV-025` | Entities subject to environmental taxes or fees | taxation-and-wealth.html |
| `TAX-ENV-026` | Environmental tax enforcement must coordinate with environmental regul | taxation-and-wealth.html |
| `TAX-ENV-027` | Fraud, concealment, collusion, or knowing misreporting in environmenta | taxation-and-wealth.html |
| `TAX-ENV-028` | Auditors, executives, officers, and responsible individuals may be | taxation-and-wealth.html |
| `TAX-ENV-029` | Repeated or systemic environmental tax violations must trigger | taxation-and-wealth.html |
| `TAX-ENV-030` | Environmental taxation must be integrated with direct environmental | taxation-and-wealth.html |
| `TAX-ENV-031` | Environmental taxes, fees, and incentives must be reviewed | taxation-and-wealth.html |
| `TAX-ENV-032` | Small-business carveouts or proportional treatment may be used | taxation-and-wealth.html |
| `TAX-EST-002` | Estate and inheritance tax systems must be structured | taxation-and-wealth.html |
| `TAX-EST-003` | Trusts, foundations, and other structures may not be | taxation-and-wealth.html |
| `TAX-EXT-002` | Tax policy may not incentivize financial engineering, short-term | taxation-and-wealth.html |
| `TAX-FTT-002` | FTT proceeds must fund public investment, social insurance, or deficit | taxation-and-wealth.html |
| `TAX-FTT-003` | FTT design must protect retail investors and pension funds from undue  | taxation-and-wealth.html |
| `TAX-GOV-002` | Revolving-door practices between regulators and regulated entities | taxation-and-wealth.html |
| `TAX-HVN-002` | United States should impose strong anti-haven rules | taxation-and-wealth.html |
| `TAX-HVN-003` | Tax liability must follow beneficial ownership, effective control | taxation-and-wealth.html |
| `TAX-HVN-004` | Corporations claiming offshore residence or foreign profit allocation | taxation-and-wealth.html |
| `TAX-HVN-005` | Ultra-wealthy individuals who move assets, tax domicile | taxation-and-wealth.html |
| `TAX-HVN-006` | Anti-tax-haven rules must distinguish ordinary expatriates and legitim | taxation-and-wealth.html |
| `TAX-INC-002` | Tax incentives may not reward stock buybacks, financial | taxation-and-wealth.html |
| `TAX-INC-003` | Public subsidies and tax advantages should favor durable | taxation-and-wealth.html |
| `TAX-INC-004` | Corporate tax structures should reward long-term investment, worker | taxation-and-wealth.html |
| `TAX-INC-005` | Corporate tax incentives may not reward offshoring, wage | taxation-and-wealth.html |
| `TAX-INT-002` | Trade, banking, sanctions, and diplomatic tools may be | taxation-and-wealth.html |
| `TAX-INT-003` | Foreign-policy and treaty tools should support transparency | taxation-and-wealth.html |
| `TAX-LOP-002` | Corporate tax law must be regularly reviewed | taxation-and-wealth.html |
| `TAX-LVT-002` | Land value tax must exempt improvements to encourage productive use | taxation-and-wealth.html |
| `TAX-LVT-003` | Speculative land holding without productive use must bear higher tax b | taxation-and-wealth.html |
| `TAX-PMT-001` | Federal income tax must apply steeply progressive marginal rates on ex | taxation-and-wealth.html |
| `TAX-PMT-002` | Alternative minimum tax mechanisms must prevent high-income earners fr | taxation-and-wealth.html |
| `TAX-PMT-003` | Stepped-up basis at death must be eliminated or replaced with deemed r | taxation-and-wealth.html |
| `TAX-TRN-002` | High-risk tax structures and large offshore holdings | taxation-and-wealth.html |
| `TAX-TRN-003` | Secrecy structures designed to conceal effective control | taxation-and-wealth.html |
| `TAX-TRN-004` | Large corporations must publicly report revenue, profit, tax | taxation-and-wealth.html |
| `TAX-TRN-005` | Corporate structures, subsidiaries, and ownership chains must be | taxation-and-wealth.html |
| `TAX-WTH-002` | Tax rules may not systematically privilege wealth accumulation | taxation-and-wealth.html |
| `TAX-WTH-003` | Extremely large accumulations of wealth may be subject | taxation-and-wealth.html |
| `TAX-WTH-004` | Tax systems must prevent extreme concentration of wealth | taxation-and-wealth.html |
| `TAX-WTH-005` | Extremely large concentrations of wealth may be subject | taxation-and-wealth.html |
| `TAX-WTH-006` | Wealth-tax systems must include strong valuation, anti-evasion | taxation-and-wealth.html |
| `TAX-WTH-007` | High-wealth individuals may not use trusts, pass-through entities | taxation-and-wealth.html |
| `TAX-WTH-008` | Tax systems must apply heightened reporting, audit | taxation-and-wealth.html |
| `TAX-WTH-009` | Artificial conversion of labor income into lower-taxed capital | taxation-and-wealth.html |
| `TAX-WTH-010` | Personal tax avoidance schemes that rely on entity | taxation-and-wealth.html |
| `TEC-CHD-002` | AI companion systems may not be designed | technology-and-ai.html |
| `TEC-CHD-003` | AI systems may not simulate friendship, romance, parental | technology-and-ai.html |
| `TEC-CHD-004` | Child-directed AI systems may not use persuasive design | technology-and-ai.html |
| `TEC-CHD-005` | AI systems for children must minimize data collection | technology-and-ai.html |
| `TEC-CHD-006` | High-risk generative features for minors, including sexually explicit | technology-and-ai.html |
| `TEC-CHD-007` | AI systems used by minors must include strong | technology-and-ai.html |
| `TEC-CHD-008` | Deepfake generation involving minors or school communities | technology-and-ai.html |
| `TEC-CHD-009` | Schools and guardians must have transparent controls over | technology-and-ai.html |
| `TEC-CHD-010` | AI systems may not replace qualified human support | technology-and-ai.html |
| `TEC-CHD-011` | Platforms hosting child-facing AI systems must maintain strong | technology-and-ai.html |
| `TEC-CHD-012` | Research on child impacts of AI systems, including | technology-and-ai.html |
| `TEC-DEM-002` | Deepfakes and synthetic impersonation of candidates, election official | technology-and-ai.html |
| `TEC-DEM-003` | AI-generated political advertising must carry clear provenance, sponso | technology-and-ai.html |
| `TEC-DEM-004` | Platforms must maintain rapid-response systems for synthetic election | technology-and-ai.html |
| `TEC-DEM-005` | AI systems may not be used to microtarget | technology-and-ai.html |
| `TEC-DEM-006` | Political campaigns, parties, PACs, and major advocacy entities | technology-and-ai.html |
| `TEC-DEM-007` | AI may not be used to impersonate voters | technology-and-ai.html |
| `TEC-DEM-008` | Election administration agencies may not rely on opaque | technology-and-ai.html |
| `TEC-DEM-009` | AI tools used in election administration must be | technology-and-ai.html |
| `TEC-DEM-010` | AI systems may not be used to suppress | technology-and-ai.html |
| `TEC-DEM-011` | Platforms and political advertisers may not use generative | technology-and-ai.html |
| `TEC-DEM-012` | Synthetic civic content affecting elections must be preserved | technology-and-ai.html |
| `TEC-DEM-013` | Public repositories of detected election-related synthetic media | technology-and-ai.html |
| `TEC-DEM-014` | Journalists, researchers, and election monitors must have lawful | technology-and-ai.html |
| `TEC-DEM-015` | AI moderation systems used in election contexts | technology-and-ai.html |
| `TEC-DEM-016` | Emergency election-content interventions by platforms or government | technology-and-ai.html |
| `TEC-DEM-017` | AI systems may not be used to fabricate | technology-and-ai.html |
| `TEC-ENV-022` | Water consumption caps | technology-and-ai.html |
| `TEC-ENV-023` | Water-stressed region restrictions | technology-and-ai.html |
| `TEC-ENV-024` | Groundwater and aquifer protection | technology-and-ai.html |
| `TEC-ENV-025` | Water recycling and reclamation | technology-and-ai.html |
| `TEC-ENV-026` | Drought contingency requirements | technology-and-ai.html |
| `TEC-ENV-027` | Community water impact review | technology-and-ai.html |
| `TEC-FMD-001` | Developers of foundation models above a defined capability threshold m | technology-and-ai.html |
| `TEC-FMD-002` | Foundation model developers must disclose whether training data includ | technology-and-ai.html |
| `TEC-FMD-003` | High-capability foundation models must undergo mandatory red-team safe | technology-and-ai.html |
| `TEC-FMD-004` | Operators deploying foundation models in high-risk applications must c | technology-and-ai.html |
| `TEC-HAR-002` | Platform algorithmic systems may not amplify, recommend, or distribute | technology-and-ai.html |
| `TEC-HAR-003` | Victims of coordinated online harassment have enforceable rights to pl | technology-and-ai.html |
| `TEC-INF-002` | Critical infrastructure AI may not be deployed | technology-and-ai.html |
| `TEC-INF-003` | Human operators must retain real-time override authority over | technology-and-ai.html |
| `TEC-INF-004` | AI systems in critical infrastructure must be tested | technology-and-ai.html |
| `TEC-INF-005` | Critical infrastructure operators must maintain fallback modes that | technology-and-ai.html |
| `TEC-INF-006` | AI-enabled cybersecurity tools may assist detection and response | technology-and-ai.html |
| `TEC-INF-007` | AI systems may not be used to optimize | technology-and-ai.html |
| `TEC-INF-008` | Procurement of AI for critical infrastructure must require | technology-and-ai.html |
| `TEC-INF-009` | Critical infrastructure AI incidents must be reported | technology-and-ai.html |
| `TEC-INF-010` | Operators may not rely on vendor opacity | technology-and-ai.html |
| `TEC-INF-011` | Essential public infrastructure using AI must maintain recordkeeping | technology-and-ai.html |
| `TEC-INF-012` | Concentration of control over AI-enabled critical systems | technology-and-ai.html |
| `TEC-LIA-001` | AI developers and deployers bear strict civil liability for physical,  | technology-and-ai.html |
| `TEC-LIA-002` | When AI system opacity makes it difficult for a harmed person to prove | technology-and-ai.html |
| `TEC-LIA-003` | AI developers and deployers must maintain incident logs, preserve deci | technology-and-ai.html |
| `TEC-MED-002` | Large platforms must audit recommender systems for amplification | technology-and-ai.html |
| `TEC-MED-003` | Users must have meaningful control over recommendation systems | technology-and-ai.html |
| `TEC-MED-004` | Platforms must disclose major ranking objectives and material | technology-and-ai.html |
| `TEC-MED-005` | AI-generated news summaries, civic explainers, or public-information t | technology-and-ai.html |
| `TEC-MED-006` | Dominant platforms may not use AI systems | technology-and-ai.html |
| `TEC-MKT-002` | AI pricing and wage-setting systems in markets affecting housing, empl | technology-and-ai.html |
| `TEC-NEU-001` | Neural data — data directly or indirectly derived from brain activity  | technology-and-ai.html |
| `TEC-NEU-002` | Prohibit the use of neural data for employment decisions, law enforcem | technology-and-ai.html |
| `TEC-NEU-003` | Brain-computer interface devices must meet pre-market safety and infor | technology-and-ai.html |
| `TEC-PRT-001` | Users have the right to download and transfer all their data from any  | technology-and-ai.html |
| `TEC-PRT-002` | Large platforms must support standardized interoperability protocols a | technology-and-ai.html |
| `TEC-PRT-003` | Platforms may not impose technical, contractual, or legal barriers tha | technology-and-ai.html |
| `TEC-PUB-002` | AI systems used in core government services must use auditable, non-pr | technology-and-ai.html |
| `TEC-PUB-003` | Productivity gains from AI deployment in publicly funded services must | technology-and-ai.html |
| `TEC-SCI-002` | Use of AI in research writing, coding, data | technology-and-ai.html |
| `TEC-SCI-003` | Scientific publishing systems must prohibit undisclosed AI-generated m | technology-and-ai.html |
| `TEC-SCI-004` | Research institutions must maintain policies for provenance, disclosur | technology-and-ai.html |
| `TEC-SCI-005` | AI may assist scientific analysis, but | technology-and-ai.html |
| `TEC-SCI-006` | Funding agencies and journals should require reproducibility | technology-and-ai.html |
| `TEC-SCI-007` | Scientific databases and search systems must guard against | technology-and-ai.html |
| `TEC-SCI-008` | Publicly funded research using AI should prioritize openness | technology-and-ai.html |
| `TEC-SCI-009` | Institutions must maintain misconduct procedures specifically addressi | technology-and-ai.html |
| `TEC-SCI-010` | AI systems may not be used to generate | technology-and-ai.html |
| `TRM-DSC-001` | Real-time financial disclosure for federal officeholders and senior of | term-limits-and-fitness.html |
| `TRM-DSC-002` | Federal officeholders may not hold individual stocks in industries the | term-limits-and-fitness.html |
| `TRM-DSC-003` | Mandatory disclosure and resolution of foreign financial relationships | term-limits-and-fitness.html |
| `TRM-FIT-001` | Age cap for re-election to federal office | term-limits-and-fitness.html |
| `TRM-FIT-002` | Independent medical and cognitive fitness review for federal officehol | term-limits-and-fitness.html |
| `TRM-FIT-003` | Fitness assessment process must be insulated against political manipul | term-limits-and-fitness.html |
| `TRM-FIT-004` | Candidates age 65 and older must disclose results of independent medic | term-limits-and-fitness.html |
| `TRM-PRE-001` | Constitutional enforcement of the 22nd Amendment — no workarounds thro | term-limits-and-fitness.html |
| `TRM-PRE-002` | Presidential term counting must include partial terms served following | term-limits-and-fitness.html |
| `TRM-RVD-001` | Expanded cooling-off period — five years before lobbying Congress or f | term-limits-and-fitness.html |
| `TRM-RVD-002` | Lifetime ban on foreign government lobbying for former senior intellig | term-limits-and-fitness.html |

</details>

---

## DB-only items (in DB, not on site)

These items are in `policy_items` but have no matching ID on the site.
Per Phase 2 conflict rules: **Add as proposal card to HTML.**

> ⚠️ NOTE: DB `status = 'MISSING'` does NOT reliably indicate the item is absent
> from the site. Many HTML cards were added after the DB was built from source logs.
> This list reflects IDs genuinely absent from HTML, not the DB status field.

**By scope:**
- `TAX`: 1

**Total: 1**

<details>
<summary>Full list</summary>

| ID | Statement | DB Status |
|----|-----------|-----------|
| `TAX-GEN-001` | Tax systems must be progressive overall and may not shift disproportio | INCLUDED |

</details>

---

## Text divergences (same ID, different text)

These items are in both HTML and DB, but the text appears to differ.
**These require human review — do not auto-resolve.**

> ⚠️ **False positive note:** Most of these are NOT real content conflicts. The HTML
> `<p class="rule-title">` element shows a condensed display version of the position
> (often omitting the implied subject, e.g., "must provide clear notice..." rather than
> "Agency adjudication systems must provide clear notice..."). The DB holds the full
> canonical statement. In the vast majority of cases, the HTML and DB describe the same
> position — the DB is more complete, not contradictory. A human reviewer should confirm
> before treating any of these as requiring a content change. True divergences (where
> meaning actually differs) are expected to be a small fraction of this list.

**Total: 992**

| ID | HTML title | DB statement | File |
|----|-----------|--------------|------|
| `ADM-ADJ-001` | adjudication systems must provide clear notice, records | Agency adjudication systems must provide clear notice,  | administrative-state.html |
| `ADM-CAP-001` | must be structurally insulated from regulated-industry  | Agencies must be structurally insulated from regulated- | administrative-state.html |
| `ADM-CIV-001` | Career civil servants may not be reclassified as at-wil | Career federal employees in competitive service positio | administrative-state.html |
| `ADM-COO-001` | with overlapping jurisdiction must coordinate enforceme | Agencies with overlapping jurisdiction must coordinate  | administrative-state.html |
| `ADM-ENF-001` | must have sufficient investigatory powers, subpoena aut | Agencies must have sufficient investigatory powers, sub | administrative-state.html |
| `ADM-FND-001` | charged with protecting rights, public safety, markets, | Agencies charged with protecting rights, public safety, | administrative-state.html |
| `ADM-IND-001` | must be protected from arbitrary defunding, bad-faith u | Agencies must be protected from arbitrary defunding, ba | administrative-state.html |
| `ADM-MAJ-001` | Congress must explicitly confirm agency authority for m | Congress must affirmatively exercise its authority to c | administrative-state.html |
| `ADM-PUB-001` | rulemaking and oversight processes must include meaning | Agency rulemaking and oversight processes must include  | administrative-state.html |
| `ADM-RGT-001` | authority may not be exercised through arbitrary, discr | Agency authority may not be exercised through arbitrary | administrative-state.html |
| `ADM-RUL-001` | must have authority to issue, revise, and clarify | Agencies must have authority to issue, revise, and clar | administrative-state.html |
| `ADM-SCI-001` | relying on scientific, medical, technical, or economic  | Agencies relying on scientific, medical, technical, or  | administrative-state.html |
| `ADM-SYS-001` | agencies are legitimate constitutional instruments of d | Administrative agencies are legitimate constitutional i | administrative-state.html |
| `ADM-TRN-001` | must publish clear public information about mission, ru | Agencies must publish clear public information about mi | administrative-state.html |
| `ADM-WBL-001` | Federal employees must be protected from retaliation fo | Federal employees who report illegal orders, scientific | administrative-state.html |
| `CON-ALG-001` | Algorithmic pricing and offers may not discriminate bas | Pricing algorithms, personalized offer systems, and con | consumer-rights.html |
| `CON-CNS-001` | No required proprietary consumables where alternatives  | Products may not require proprietary consumables or sub | consumer-rights.html |
| `CON-CRD-001` | Credit reports must be accurate and disputes must be me | Credit reporting agencies must maintain accurate consum | consumer-rights.html |
| `CON-DBR-001` | Data brokers must register, disclose their sources, and | Commercial data brokers that compile, sell, or share co | consumer-rights.html |
| `CON-DRK-001` | Deceptive interface design that manipulates consumer ch | Interface designs that deliberately manipulate consumer | consumer-rights.html |
| `CON-ENF-001` | Violations require restoration, restitution, and penalt | Violations of ownership-based functionality rules must  | consumer-rights.html |
| `CON-ENF-002` | Private right of action for unlawful post-purchase rest | Consumers must have a private right of action where pro | consumer-rights.html |
| `CON-FEE-001` | Prohibit hidden fees, drip pricing, and junk fees | Hidden fees, junk fees, drip pricing, and post-selectio | consumer-rights.html |
| `CON-FTR-001` | May not artificially disable available hardware feature | Manufacturers may not artificially disable or withhold  | consumer-rights.html |
| `CON-GEN-001` | Prohibit deceptive and exploitative business practices | Consumer protection law must prohibit deceptive, coerci | consumer-rights.html |
| `CON-OWN-001` | Purchase conveys full access to core functionality | Purchase of a physical product conveys full access to i | consumer-rights.html |
| `CON-OWN-002` | Ownership may not be converted to subscription dependen | Ownership of a product may not be converted into a subs | consumer-rights.html |
| `CON-QLT-001` | Products must meet minimum durability and quality stand | Consumer products must meet minimum durability, safety, | consumer-rights.html |
| `CON-SUB-001` | Subscriptions may not replace feasible ownership | Subscription models may not be structured to replace ow | consumer-rights.html |
| `CON-TRN-005` | Post-sale paywalling of previously included features pr | Post-sale changes that move previously included feature | consumer-rights.html |
| `CON-WAR-001` | Warranties must be understandable, fair, and enforceabl | Warranty systems must be understandable, fair, and enfo | consumer-rights.html |
| `COR-ASF-001` | Prohibit civil asset forfeiture without criminal convic | The federal government and any state or local law enfor | anti-corruption.html |
| `COR-EMO-001` | Establish a statutory enforcement mechanism for the emo | Congress must enact a statute establishing a clear caus | anti-corruption.html |
| `COR-FAR-001` | Strengthen FARA enforcement with mandatory registration | The Foreign Agents Registration Act (22 U.S.C. §§ 611–6 | anti-corruption.html |
| `COR-INT-001` | Full U.S. implementation of UNCAC obligations — asset r | The United States must fully implement all obligations  | anti-corruption.html |
| `COR-OWN-001` | Full public beneficial ownership registry — strengthen  | The beneficial ownership reporting framework establishe | anti-corruption.html |
| `ECO-AUT-001` | Automation Tax on Labor Displacement | Companies that replace or materially displace human lab | taxation-and-wealth.html |
| `ECO-AUT-002` | Automation Tax Revenue for Public Benefit | Revenue from AI or automated-labor taxation should be u | taxation-and-wealth.html |
| `ECO-AUT-003` | Structure Tax to Discourage Irresponsible Displacement | AI or automated-labor taxation should be structured to  | taxation-and-wealth.html |
| `ECO-EQT-001` | Equal Pay and Economic Opportunity | Guarantee equal pay and equal economic opportunity rega | taxation-and-wealth.html |
| `ECO-IND-001` | National Industrial Strategy | Establish national manufacturing and industrial policy  | taxation-and-wealth.html |
| `ECO-INS-001` | AI Cannot Deny Insurance Without Human Review | AI systems may not be used to deny restrict or reduce i | taxation-and-wealth.html |
| `ECO-INS-002` | Independent Human Judgment Required | Human reviewers in insurance decisions must exercise in | taxation-and-wealth.html |
| `ECO-SMB-001` | Small Business Healthcare Coverage Support | Provide subsidies carveouts or public support to help s | taxation-and-wealth.html |
| `EDU-BND-001` | Guarantee broadband access and devices for all K–12 stu | Every K–12 student must have reliable broadband interne | education.html |
| `EDU-DIS-001` | Replace zero-tolerance discipline with restorative just | Schools must transition away from zero-tolerance, punit | education.html |
| `EDU-FIN-001` | EDU|FIN|Student loan debt forgiveness or large-scale re | Student loan debt forgiveness or large-scale restructur | education.html |
| `EDU-LIB-001` | Protect K–12 teachers from retaliation for teaching evi | K–12 teachers must be protected from disciplinary actio | education.html |
| `EDU-STD-001` | EDU|STD|Education standards must include protections ag | Education standards must include protections against po | education.html |
| `ELE-IDA-001` | Mandatory free voter ID assistance | Free voter ID assistance | elections-and-representation.html |
| `ELE-IDA-002` | Legal representation and case management | Legal and case support for ID access | elections-and-representation.html |
| `ELE-IDA-003` | Free transportation to ID-issuing offices | If a state requires voter ID, it must provide free tran | elections-and-representation.html |
| `ELE-IDA-004` | Proactive outreach — state finds the voter | States requiring voter ID must proactively identify and | elections-and-representation.html |
| `ELE-IDA-005` | Mobility must not be a barrier to voter ID | Physical mobility must not be a barrier to obtaining vo | elections-and-representation.html |
| `ENV-CLI-001` | Require federal climate adaptation plans for all major  | All major federal infrastructure programs and agencies  | environment-and-agriculture.html |
| `ENV-CPX-001` | Establish a carbon price that reflects the full social  | The United States must implement a carbon pricing mecha | environment-and-agriculture.html |
| `ENV-JUS-001` | Prohibit siting of polluting facilities that creates di | Environmental permitting processes must include a cumul | environment-and-agriculture.html |
| `ENV-REG-001` | Environmental Protection Agency must be constitutionall | The Environmental Protection Agency must be constitutio | environment-and-agriculture.html |
| `ENV-WTR-001` | Establish a federal right to clean water for all reside | Access to safe, affordable drinking water is a fundamen | environment-and-agriculture.html |
| `GUN-ACQ-001` | Universal background checks for all acquisitions | Require background checks for all firearm acquisitions | gun-policy.html |
| `GUN-ACQ-002` | Background checks cover all transfers including private | Background check requirement applies to all transfers i | gun-policy.html |
| `GUN-ACQ-003` | Comprehensive and interoperable background check databa | Background check databases must be comprehensive, inter | gun-policy.html |
| `GUN-BAN-001` | Ban weapons of war from civilian ownership | Ban private ownership of weapons of war including autom | gun-policy.html |
| `GUN-BAN-002` | Evasion-resistant definition of weapons of war | Definition of weapons of war must be evasion-resistant  | gun-policy.html |
| `GUN-MHE-001` | Dangerousness-based mental health evaluation | Mental health evaluations for gun ownership must be nar | gun-policy.html |
| `GUN-MHE-002` | No blanket exclusion based on diagnosis alone | Prohibit blanket exclusion from firearm ownership based | gun-policy.html |
| `GUN-MIL-003` | Militia transparency and accountability requirements | Require militias to maintain membership records, financ | gun-policy.html |
| `GUN-MIL-004` | Government oversight of militia training | Federal and state governments must have oversight autho | gun-policy.html |
| `GUN-MIL-005` | Regulated militias integrated into disaster relief | Provide mechanisms for regulated militias to train for  | gun-policy.html |
| `GUN-REG-001` | Constitutional authority to regulate firearms | Amend the Constitution to explicitly affirm government  | gun-policy.html |
| `GUN-RFL-001` | Federal minimum standards for red flag laws | Establish federal minimum standards for red flag / extr | gun-policy.html |
| `GUN-TRN-001` | Mandatory safety training for firearm ownership | Require safety training as a condition of firearm owner | gun-policy.html |
| `GUN-TRN-002` | Mandatory de-escalation training for ownership | Require de-escalation training as a condition of firear | gun-policy.html |
| `GUN-TRN-003` | Safe storage requirement | Require secure storage of firearms; safe storage law as | gun-policy.html |
| `HLT-AI-001` | High-risk AI classification | AI systems in healthcare must be treated as high-risk s | healthcare.html |
| `HLT-AI-002` | AI as support, not replacement | AI systems may support but not replace licensed medical | healthcare.html |
| `HLT-AI-003` | Clinical decision support limits | AI systems may be used for clinical decision support on | healthcare.html |
| `HLT-AI-004` | Evidence standards before deployment | AI systems must meet strong evidence standards for safe | healthcare.html |
| `HLT-AI-005` | Continuous monitoring requirement | Deployed healthcare AI systems must be continuously mon | healthcare.html |
| `HLT-AI-006` | No independent diagnosis or prescription | AI systems may not independently diagnose or prescribe  | healthcare.html |
| `HLT-AI-007` | AI may not deny care | AI systems may not be used to deny restrict or limit me | healthcare.html |
| `HLT-AI-007A` | Independent clinical judgment required | Human reviewers must exercise independent clinical judg | healthcare.html |
| `HLT-AI-007B` | AI for approval only, not denial | AI systems may be used to assist or expedite approval o | healthcare.html |
| `HLT-AI-007C` | Prior human review for denials | Human review must occur prior to any denial decision an | healthcare.html |
| `HLT-AI-007E` | Independent evaluation required for denials | All denial decisions must be based on independent clini | healthcare.html |
| `HLT-AI-007F` | No systemic bias from AI prioritization | AI systems used to assist approvals must not create sys | healthcare.html |
| `HLT-AI-007G` | Equal human consideration for non-AI-flagged cases | Case review systems must ensure that requests not prior | healthcare.html |
| `HLT-AI-008` | No opaque triage decisions | AI systems may not make opaque triage or prioritization | healthcare.html |
| `HLT-AI-009` | AI may not prioritize cost over outcomes | Coverage decision-making entities must not use AI syste | healthcare.html |
| `HLT-AI-010` | Access to explanations and appeals | Patients and providers must have access to explanations | healthcare.html |
| `HLT-AI-011` | Right to human care | Patients have the right to receive care from qualified  | healthcare.html |
| `HLT-AI-012` | Informed consent and opt-out | Patients must be informed when AI systems are used in t | healthcare.html |
| `HLT-AI-013` | Strict data protections | Healthcare data used by AI systems must be treated as h | healthcare.html |
| `HLT-AI-014` | No commercial data exploitation | Healthcare data may not be used for advertising profili | healthcare.html |
| `HLT-AI-015` | Training data ethical standards | Training data for healthcare AI must meet strict ethica | healthcare.html |
| `HLT-AI-016` | Fail-safe design | Healthcare AI systems must fail safely and defer to hum | healthcare.html |
| `HLT-AI-017` | No unwarranted certainty | AI systems may not present outputs with unwarranted cer | healthcare.html |
| `HLT-AI-018` | Bias evaluation and mitigation | Healthcare AI systems must be evaluated and mitigated f | healthcare.html |
| `HLT-AI-019` | No disparity worsening | AI deployment must not worsen disparities in healthcare | healthcare.html |
| `HLT-AI-020` | AI for research acceleration | AI may be used to accelerate medical research and drug  | healthcare.html |
| `HLT-AI-021` | Research funding for neglected conditions | Increase funding for research into under-studied condit | healthcare.html |
| `HLT-AI-022` | Priority for underfunded diseases | Public funding priorities must include diseases and con | healthcare.html |
| `HLT-AI-023` | Science-based AI policy | Healthcare AI policy and approvals must be grounded in  | healthcare.html |
| `HLT-AI-024` | Safe AI integration | AI systems must be integrated into healthcare systems i | healthcare.html |
| `HLT-AI-025` | Interoperability with privacy protections | Healthcare AI systems should support interoperability a | healthcare.html |
| `HLT-APL-001` | Fast, meaningful, independent appeals | Patients and providers must have access to fast meaning | healthcare.html |
| `HLT-APL-002` | Urgent appeal timelines | Appeals involving urgent medically necessary treatment  | healthcare.html |
| `HLT-APL-004` | Pattern review and penalties | Successful appeals should trigger review of the underly | healthcare.html |
| `HLT-CLM-001` | Establish coverage and preparedness standards for clima | Coverage systems must include treatment for climate-rel | healthcare.html |
| `HLT-COV-005` | Tighter denial limits | Establish tighter overall rules limiting denial of heal | healthcare.html |
| `HLT-COV-006` | Overhaul insurance to reduce denials | Until universal healthcare is implemented overhaul heal | healthcare.html |
| `HLT-COV-007` | Faster coverage decision timelines | Require faster timelines for healthcare coverage decisi | healthcare.html |
| `HLT-COV-008` | Expedited appeal processes | Require expedited appeal processes for denials of healt | healthcare.html |
| `HLT-COV-010` | Protect pre-existing condition bans | Protect and strengthen bans on denial of coverage based | healthcare.html |
| `HLT-COV-011` | Expand coverage for under-covered conditions | Expand required coverage for conditions that are often  | healthcare.html |
| `HLT-COV-012` | Require mental healthcare coverage | Require coverage of mental healthcare including talk th | healthcare.html |
| `HLT-COV-013` | Psychedelic therapy coverage | Require coverage of psychedelic therapy where medically | healthcare.html |
| `HLT-COV-014` | Nationwide in-network care | Require health plans to provide nationwide in-network c | healthcare.html |
| `HLT-COV-015` | Expand HSA-style tools | Expand HSA-style health spending cards or equivalent he | healthcare.html |
| `HLT-COV-016` | Ban high-deductible-only plans | Ban employers from offering only high-deductible health | healthcare.html |
| `HLT-COV-017` | Employers pay all premiums | Require employers to pay all health insurance premiums  | healthcare.html |
| `HLT-COV-018` | Fair coverage processes | Healthcare coverage or service may not be denied restri | healthcare.html |
| `HLT-COV-019` | Clear standards for denials | Any adverse coverage decision must be based on clear me | healthcare.html |
| `HLT-COV-020` | Public reporting of denial rates | Denial rates delay patterns and reversal rates must be  | healthcare.html |
| `HLT-COV-021` | Penalties for repeated unjustified denials | Repeated unjustified denial or delay of medically neces | healthcare.html |
| `HLT-COV-022` | Mandatory care floor | Coverage systems must include a broad mandatory floor o | healthcare.html |
| `HLT-COV-023` | No vague exclusions | Coverage exclusions may not be written so broadly or va | healthcare.html |
| `HLT-COV-024` | Clear language and pro-access interpretation | Coverage rules must be written in clear language and in | healthcare.html |
| `HLT-COV-025` | Evidence-based coverage inclusion | Coverage systems must include medicines procedures ther | healthcare.html |
| `HLT-COV-026` | Permanent pre-existing condition protections | Protections against denial or exclusion based on pre-ex | healthcare.html |
| `HLT-COV-027` | No indirect pre-existing condition exclusion | Coverage systems must not use pre-existing-condition lo | healthcare.html |
| `HLT-COV-028` | Expand historically under-covered conditions | Coverage requirements must be expanded for conditions t | healthcare.html |
| `HLT-COV-029` | Mental health parity | Coverage systems must include mental healthcare on pari | healthcare.html |
| `HLT-COV-030` | No mental health access discrimination | Coverage systems may not impose narrower networks harsh | healthcare.html |
| `HLT-COV-031` | Emerging evidence-based therapies | Where evidence and law support it coverage systems shou | healthcare.html |
| `HLT-CRN-001` | Require coverage of post-acute sequelae of infectious d | Coverage systems must classify post-acute sequelae of i | healthcare.html |
| `HLT-CST-001` | Cost-sharing must not block access | Deductibles copays and out-of-pocket cost structures mu | healthcare.html |
| `HLT-CST-002` | Regulate cost-sharing for patient protection | Healthcare cost-sharing rules must be regulated to prot | healthcare.html |
| `HLT-CST-003` | Broad health spending tool access | Health spending cards or equivalent patient-directed to | healthcare.html |
| `HLT-CST-004` | No cost barriers for chronic/preventive care | Cost-sharing design may not be used to discourage care  | healthcare.html |
| `HLT-DNT-001` | Include dental care in the mandatory coverage floor | Coverage systems must include comprehensive dental care | healthcare.html |
| `HLT-EMP-001` | No high-deductible-only employer plans | Employers may not satisfy healthcare obligations by off | healthcare.html |
| `HLT-EMP-002` | Employers pay full premiums | Employers should be required to pay the full premium co | healthcare.html |
| `HLT-EMP-003` | Small business supports | Small businesses should receive subsidies public suppor | healthcare.html |
| `HLT-EMP-004` | Prevent underinsurance disguised as coverage | Employer-based health coverage rules during the transit | healthcare.html |
| `HLT-JUS-001` | Guarantee healthcare for incarcerated individuals equiv | Every person in state or federal custody has a constitu | healthcare.html |
| `HLT-MAT-001` | Mandate maternal mortality review and racial equity rep | Every state must maintain a maternal mortality review c | healthcare.html |
| `HLT-MHC-002` | Mental health AI as high-risk | AI systems in mental health must be regulated as high-r | healthcare.html |
| `HLT-MHC-003` | AI may not replace clinicians in high-risk determinatio | AI systems may not replace licensed clinicians in diagn | healthcare.html |
| `HLT-MHC-004` | No AI-only suicide/crisis decisions | AI systems may not serve as the sole decision-maker in  | healthcare.html |
| `HLT-MHC-005` | Human accountability required | A clearly identifiable licensed human professional must | healthcare.html |
| `HLT-MHC-006` | AI as assistive tool only | AI may be used as an assistive tool in mental healthcar | healthcare.html |
| `HLT-MHC-007` | Evidence standards for mental health AI | AI systems used in mental health care must meet strong  | healthcare.html |
| `HLT-MHC-008` | Continuous monitoring for mental health AI | Mental health AI systems must be continuously monitored | healthcare.html |
| `HLT-MHC-009` | No deceptive AI therapist presentation | AI systems marketed for mental health support may not d | healthcare.html |
| `HLT-MHC-010` | No emotional dependency cultivation | AI systems may not be designed to cultivate emotional d | healthcare.html |
| `HLT-MHC-011` | Clear AI disclosure | Any AI system offering mental health support must clear | healthcare.html |
| `HLT-MHC-013` | Escalation pathways to human care | Mental health AI systems must include clear escalation  | healthcare.html |
| `HLT-MHC-014` | No false reassurance | Mental health AI systems may not provide false reassura | healthcare.html |
| `HLT-MHC-015` | Fail safely to human care | Where mental health AI systems are uncertain or out of  | healthcare.html |
| `HLT-MHC-016` | Enhanced mental health data privacy | Data generated through AI mental health interactions mu | healthcare.html |
| `HLT-MHC-017` | No commercial mental health data exploitation | Mental health AI data may not be sold shared for advert | healthcare.html |
| `HLT-MHC-018` | No discriminatory use of mental health data | Mental health data inferred or collected by AI systems  | healthcare.html |
| `HLT-MHC-019` | Explicit informed consent | Consent for use of mental health AI systems and their d | healthcare.html |
| `HLT-MHC-020` | Evidence required for efficacy claims | AI systems may not claim mental health efficacy diagnos | healthcare.html |
| `HLT-MHC-021` | Independent evaluation required | Mental health AI systems must be subject to independent | healthcare.html |
| `HLT-MHC-022` | Disclose risks and failure modes | Material risks limitations and known failure modes of m | healthcare.html |
| `HLT-MHC-023` | Right to human mental healthcare | People must retain a right to access human mental healt | healthcare.html |
| `HLT-MHC-024` | Coercive AI deployment safeguards | AI mental health tools may not be imposed coercively in | healthcare.html |
| `HLT-MHC-025` | No behavioral conformity enforcement | AI systems may not be used to enforce behavioral confor | healthcare.html |
| `HLT-MHC-026` | School AI risk-scoring restrictions | Schools may not rely on opaque AI mental health or risk | healthcare.html |
| `HLT-MHC-027` | Prison/detention AI restrictions | Jails prisons detention facilities and similar institut | healthcare.html |
| `HLT-MHC-028` | Public benefits AI assessment limits | Public benefits or disability systems may not use opaqu | healthcare.html |
| `HLT-MHC-029` | Insurers may not use AI to deny mental health care | AI systems may not be used by insurers or payers to den | healthcare.html |
| `HLT-MHC-030` | AI not substitute for licensed care | AI systems may not be used as a substitute for access t | healthcare.html |
| `HLT-MHC-031` | Data retention limits and user control | Mental health AI systems must implement strict limits o | healthcare.html |
| `HLT-MHC-032` | Training data consent standards | Training data for mental health AI systems must not inc | healthcare.html |
| `HLT-MHC-033` | Clear capability limits | Mental health AI systems must clearly define their role | healthcare.html |
| `HLT-MHC-034` | No manipulative behavior modification | AI systems may not use mental health interactions to ma | healthcare.html |
| `HLT-MHC-035` | No surveillance integration | Mental health AI systems may not be integrated with sur | healthcare.html |
| `HLT-MHC-036` | Research ethical review standards | Use of AI mental health systems in experimental or rese | healthcare.html |
| `HLT-MHC-037` | Fund independent AI mental health research | Fund independent research into the short-term and long- | healthcare.html |
| `HLT-MHC-038` | Ban conversational AI for young children | Ban use of AI systems designed for conversational emoti | healthcare.html |
| `HLT-MHC-039` | Graduated age-based AI restrictions | Establish graduated age-based restrictions for AI syste | healthcare.html |
| `HLT-MHC-040` | Minor-accessible AI data limits | AI systems accessible to minors must include strict lim | healthcare.html |
| `HLT-MHC-041` | No direct-to-consumer mental health AI treatment | AI systems may not be marketed or deployed as standalon | healthcare.html |
| `HLT-MHC-042` | Limited crisis support AI | Limited use of AI systems for crisis support may be per | healthcare.html |
| `HLT-MHC-043` | Clinical data consent for training | Mental health data from licensed providers therapy sess | healthcare.html |
| `HLT-MHC-044` | Identifiable clinical data training prohibition | Use of identifiable clinical mental health data for AI  | healthcare.html |
| `HLT-MHC-045` | Mental health interaction data storage limits | Mental health data generated through AI interactions ma | healthcare.html |
| `HLT-MHC-046` | Robust de-identification for training data | All training data used in mental health AI systems must | healthcare.html |
| `HLT-MHC-047` | No re-identification of anonymized data | AI systems must not be designed or used to re-identify  | healthcare.html |
| `HLT-NET-001` | Adequate networks for all services | Health plans must maintain adequate networks for all co | healthcare.html |
| `HLT-NET-002` | National networks required | Health plan networks must function nationally rather th | healthcare.html |
| `HLT-NET-003` | Out-of-network coverage when network inadequate | If adequate in-network care is not available within rea | healthcare.html |
| `HLT-NET-004` | No patient penalty for network failures | Patients may not be penalized for obtaining necessary c | healthcare.html |
| `HLT-OVR-001` | Public reporting of coverage metrics | Coverage entities must publicly report denial rates app | healthcare.html |
| `HLT-OVR-002` | Oversight authority and enforcement | Healthcare oversight bodies must have authority to inve | healthcare.html |
| `HLT-OVR-003` | No hiding behind proprietary claims | Coverage entities may not hide harmful practices behind | healthcare.html |
| `HLT-OVR-004` | Corrective action and suspension authority | Regulators must be empowered to require corrective acti | healthcare.html |
| `HLT-PAU-001` | Strict limits on prior authorization | Prior authorization requirements must be strictly limit | healthcare.html |
| `HLT-PAU-002` | Transparent prior authorization systems | Prior authorization systems must be transparent clinica | healthcare.html |
| `HLT-PAU-003` | Reduce repeated prior authorization burden | Repeated approval of the same type of medically necessa | healthcare.html |
| `HLT-PAU-004` | No prior authorization disruption of continuity | Prior authorization may not be used to disrupt continui | healthcare.html |
| `HLT-RSR-001` | Increase funding for neglected conditions | Public healthcare and research policy must increase fun | healthcare.html |
| `HLT-RSR-002` | Priority for stigmatized conditions | Research priorities should include stigmatized or less  | healthcare.html |
| `HLT-RSR-003` | Resist commercial research bias | Healthcare governance should not allow commercial buzz  | healthcare.html |
| `HLT-RX-001` | Broad prescription access required | Drug coverage systems must include broad access to medi | healthcare.html |
| `HLT-RX-002` | Fast formulary exception pathways | Patients must have fast and meaningful exception pathwa | healthcare.html |
| `HLT-RX-003` | No harmful step-therapy loops | Coverage systems may not force repeated medication fail | healthcare.html |
| `HLT-RX-004` | Coverage for neglected condition medications | Coverage for medications should include neglected or un | healthcare.html |
| `HLT-RX-005` | Controlled substance quotas ensure access | Production quotas and regulatory limits on controlled m | healthcare.html |
| `HLT-RX-006` | No artificial medication shortages | Regulatory systems may not restrict supply of approved  | healthcare.html |
| `HLT-RX-007` | Quotas based on real-world demand | Controlled substance quotas must be based on real-world | healthcare.html |
| `HLT-RX-008` | Rapid response to medication shortages | When shortages of controlled medications occur regulato | healthcare.html |
| `HLT-RX-009` | No geographic medication access restrictions | Patients must be able to access prescribed controlled m | healthcare.html |
| `HLT-RX-010` | Balanced access expansion with safeguards | Expansion of access to controlled medications must be p | healthcare.html |
| `HLT-RX-011` | No patient-uncontrolled treatment disruption | Patients receiving ongoing treatment with controlled me | healthcare.html |
| `HLT-STD-005` | Strict maximum response timelines | Healthcare coverage decisions and prior authorization d | healthcare.html |
| `HLT-STD-006` | Accelerated urgent decision timelines | Urgent and emergency-related coverage determinations mu | healthcare.html |
| `HLT-STD-007` | Presumptive approval if timelines missed | If a coverage decision is not made within required time | healthcare.html |
| `HLT-STD-008` | No delay as denial strategy | Administrative delay may not be used as a strategy to a | healthcare.html |
| `HLT-SUP-001` | Fund comprehensive supplement research through NCCIH | Supplement research funding | healthcare.html |
| `HLT-SUP-002` | Reform supplement labeling to reflect actual evidence | Supplement labeling standards | healthcare.html |
| `HLT-SUP-003` | Require independent laboratory testing and quality cert | Supplement lab transparency | healthcare.html |
| `HLT-SUP-004` | Establish minimum quality standards for supplement manu | Minimum supplement quality standards | healthcare.html |
| `HLT-TRL-001` | Streamlined new treatment approvals | Approvals and trials for new treatments funded and stre | healthcare.html |
| `HLT-TRN-001` | Regulate transition-state coverage systems | Until universal single-payer healthcare is implemented  | healthcare.html |
| `HLT-TRN-002` | Immediate improvement without delay | Transition-state healthcare reform must be designed to  | healthcare.html |
| `HOU-CLT-001` | Community land trusts must be recognized and supported  | Government must recognize community land trusts and sha | housing.html |
| `HOU-IZN-001` | Large residential developments must include affordable  | Residential developments above a defined unit threshold | housing.html |
| `HOU-MHO-001` | Mobile home park residents must have protections agains | Residents of mobile home parks and manufactured housing | housing.html |
| `HOU-PUB-001` | Government-owned or publicly administered housing must  | Public and social housing must be maintained as a perma | housing.html |
| `HOU-SOI-001` | Landlords may not refuse housing based on lawful source | Landlords, property managers, and rental listing platfo | housing.html |
| `HOU-TEN-001` | Tenants must have enforceable rights to habitability, r | Tenants must have meaningful protection from retaliator | housing.html |
| `IMM-ACC-001` | Access to Services | Immigration status may affect specific program eligibil | immigration.html |
| `IMM-ACC-002` | Access to Services | Children within United States jurisdiction must have me | immigration.html |
| `IMM-ACC-003` | Access to Services | Local access to healthcare schooling identification sup | immigration.html |
| `IMM-ACC-004` | Access to Services | Public-service systems should provide clear multilingua | immigration.html |
| `IMM-ACC-005` | Access to Services | Basic access to reporting crime seeking emergency help  | immigration.html |
| `IMM-ACC-006` | Access to Services | State and local institutions may not use ordinary publi | immigration.html |
| `IMM-ADM-001` | Administration & Process | Immigration systems must be funded and staffed to reduc | immigration.html |
| `IMM-ADM-002` | Administration & Process | Administrative simplification should reduce complexity  | immigration.html |
| `IMM-ADM-003` | Administration & Process | People must have accessible status updates document acc | immigration.html |
| `IMM-ADM-004` | Administration & Process | Immigration forms notices deadlines and legal standards | immigration.html |
| `IMM-ADM-005` | Administration & Process | Backlog reduction efforts may not sacrifice accuracy du | immigration.html |
| `IMM-ADM-006` | Administration & Process | Immigration applicants must have clear access to case s | immigration.html |
| `IMM-ADM-007` | Administration & Process | Immigration agencies may not use contradictory document | immigration.html |
| `IMM-ADM-008` | Administration & Process | Where agency error delay or lost records materially har | immigration.html |
| `IMM-ASY-001` | Asylum & Humanitarian Protection | People seeking asylum or humanitarian protection must h | immigration.html |
| `IMM-ASY-002` | Asylum & Humanitarian Protection | Asylum systems may not rely on impossible deadlines ina | immigration.html |
| `IMM-ASY-003` | Asylum & Humanitarian Protection | Credibility determinations in asylum and humanitarian c | immigration.html |
| `IMM-ASY-004` | Asylum & Humanitarian Protection | People with credible fear or other serious protection c | immigration.html |
| `IMM-ASY-005` | Asylum & Humanitarian Protection | Humanitarian protection systems must be designed to acc | immigration.html |
| `IMM-ASY-006` | Asylum & Humanitarian Protection | Asylum and refugee procedures must include clear timely | immigration.html |
| `IMM-ASY-007` | Asylum & Humanitarian Protection | Credible-fear and related threshold screenings must be  | immigration.html |
| `IMM-ASY-008` | Asylum & Humanitarian Protection | People seeking asylum or refugee protection must have s | immigration.html |
| `IMM-ASY-009` | Asylum & Humanitarian Protection | Asylum adjudication must account for trauma memory disr | immigration.html |
| `IMM-ASY-010` | Asylum & Humanitarian Protection | Children survivors of trafficking survivors of gender-b | immigration.html |
| `IMM-ASY-011` | Asylum & Humanitarian Protection | Detention may not be used to pressure abandonment of as | immigration.html |
| `IMM-ASY-012` | Asylum & Humanitarian Protection | Asylum and refugee decisions must be explained clearly  | immigration.html |
| `IMM-ASY-013` | Asylum & Humanitarian Protection | Return or removal decisions in protection cases must in | immigration.html |
| `IMM-BRD-002` | Border Governance | Border enforcement powers must be clearly limited by co | immigration.html |
| `IMM-BRD-003` | Border Governance | Use of force in border contexts must be strictly constr | immigration.html |
| `IMM-BRD-004` | Border Governance | Border processing systems must be designed for order an | immigration.html |
| `IMM-BRD-005` | Border Governance | Border enforcement may not be militarized in ways that  | immigration.html |
| `IMM-BRD-006` | Border Governance | Border officials and agencies must be subject to strong | immigration.html |
| `IMM-BRD-007` | Border Governance | Independent review mechanisms must investigate deaths a | immigration.html |
| `IMM-BRD-008` | Border Governance | Border enforcement may not use deprivation of food wate | immigration.html |
| `IMM-BRD-009` | Border Governance | Border processing facilities must meet humane standards | immigration.html |
| `IMM-BRD-010` | Border Governance | Emergency border powers may not be used as permanent su | immigration.html |
| `IMM-CIT-001` | Citizenship & Naturalization | Pathways to citizenship should be clear affordable and  | immigration.html |
| `IMM-CIT-002` | Citizenship & Naturalization | Citizenship systems should not be structured to preserv | immigration.html |
| `IMM-CIT-003` | Citizenship & Naturalization | Birthright citizenship must remain explicit and protect | immigration.html |
| `IMM-CIT-004` | Citizenship & Naturalization | Long-term lawful residents should have fair and stable  | immigration.html |
| `IMM-CIT-005` | Citizenship & Naturalization | Naturalization systems should be clear affordable timel | immigration.html |
| `IMM-CIT-006` | Citizenship & Naturalization | Citizenship eligibility processes should not be distort | immigration.html |
| `IMM-CIT-007` | Citizenship & Naturalization | Long-term lawful residents should not remain in extende | immigration.html |
| `IMM-CIT-008` | Citizenship & Naturalization | Naturalization procedures should include accessible lan | immigration.html |
| `IMM-CIT-009` | Citizenship & Naturalization | The citizenship process may include lawful standards fo | immigration.html |
| `IMM-CIT-010` | Citizenship & Naturalization | Fees and procedural burdens in citizenship processes sh | immigration.html |
| `IMM-CLM-001` | Create a climate displacement visa category for people  | The United States must establish a humanitarian visa ca | immigration.html |
| `IMM-CON-001` | Contractor Accountability | Private contractors involved in immigration processing  | immigration.html |
| `IMM-CON-002` | Contractor Accountability | Immigration contractors may not claim secrecy proprieta | immigration.html |
| `IMM-CON-003` | Contractor Accountability | Contractors performing immigration-related functions mu | immigration.html |
| `IMM-CON-004` | Contractor Accountability | No contractor compensation structure may reward detenti | immigration.html |
| `IMM-CON-005` | Contractor Accountability | Immigration-service contracts must prioritize rights pr | immigration.html |
| `IMM-CON-006` | Contractor Accountability | Government may not fragment immigration functions acros | immigration.html |
| `IMM-CON-007` | Contractor Accountability | People harmed by immigration contractors must have full | immigration.html |
| `IMM-CON-008` | Contractor Accountability | Independent oversight bodies must have full access to c | immigration.html |
| `IMM-CON-009` | Contractor Accountability | Immigration enforcement detention adjudication and core | immigration.html |
| `IMM-CON-010` | Contractor Accountability | Core immigration functions include detention custody tr | immigration.html |
| `IMM-CON-011` | Contractor Accountability | Limited use of contractors may be permitted for non-cor | immigration.html |
| `IMM-CON-012` | Contractor Accountability | Contractors may not exercise authority over individuals | immigration.html |
| `IMM-CON-013` | Contractor Accountability | No compensation structure may reward detention volume e | immigration.html |
| `IMM-CON-014` | Contractor Accountability | Government entities may not indirectly outsource core i | immigration.html |
| `IMM-CON-015` | Contractor Accountability | All permitted contractors must be subject to full publi | immigration.html |
| `IMM-CON-016` | Contractor Accountability | Individuals harmed by contractor actions must have full | immigration.html |
| `IMM-CRT-001` | Courts & Adjudication | Immigration adjudication systems must be structured for | immigration.html |
| `IMM-CRT-002` | Courts & Adjudication | Immigration courts or equivalent adjudicative bodies sh | immigration.html |
| `IMM-CRT-003` | Courts & Adjudication | People in immigration proceedings must have clear acces | immigration.html |
| `IMM-CRT-004` | Courts & Adjudication | Adjudicators in immigration systems must receive trauma | immigration.html |
| `IMM-DAT-001` | Data Privacy & Surveillance | Immigration systems may not use broad data surveillance | immigration.html |
| `IMM-DAT-002` | Data Privacy & Surveillance | Data-sharing between immigration systems and other gove | immigration.html |
| `IMM-DAT-003` | Data Privacy & Surveillance | Immigration data must be treated as highly sensitive an | immigration.html |
| `IMM-DAT-004` | Data Privacy & Surveillance | Record systems must include correction mechanisms so pe | immigration.html |
| `IMM-DET-001` | Detention & Custody | Immigration detention must be strictly limited and may  | immigration.html |
| `IMM-DET-002` | Detention & Custody | Indefinite immigration detention is prohibited | immigration.html |
| `IMM-DET-003` | Detention & Custody | Detention conditions must meet strong standards for hea | immigration.html |
| `IMM-DET-004` | Detention & Custody | Alternatives to detention should be preferred where app | immigration.html |
| `IMM-DET-005` | Detention & Custody | Immigration detention must be subject to prompt individ | immigration.html |
| `IMM-DET-006` | Detention & Custody | Use of offshore or legally exceptional detention struct | immigration.html |
| `IMM-DET-007` | Detention & Custody | Private immigration detention facilities are prohibited | immigration.html |
| `IMM-DET-008` | Detention & Custody | Detention custody transportation or confinement of immi | immigration.html |
| `IMM-DET-009` | Detention & Custody | Government may not use private contractors to evade acc | immigration.html |
| `IMM-DET-010` | Detention & Custody | Any non-private immigration detention or custody settin | immigration.html |
| `IMM-DET-011` | Detention & Custody | Deaths injuries medical neglect sexual abuse and seriou | immigration.html |
| `IMM-DET-012` | Detention & Custody | Contractor or agency employees involved in immigration  | immigration.html |
| `IMM-DOC-001` | Documentation & Identity | Immigration and travel document systems must respect up | immigration.html |
| `IMM-DOC-002` | Documentation & Identity | Removal of sex and gender markers from passports and id | immigration.html |
| `IMM-DUE-001` | Due Process & Rights | People in immigration proceedings must have meaningful  | immigration.html |
| `IMM-DUE-002` | Due Process & Rights | People must have timely access to counsel or accredited | immigration.html |
| `IMM-DUE-003` | Due Process & Rights | Immigration proceedings may not rely on rushed scheduli | immigration.html |
| `IMM-DUE-004` | Due Process & Rights | Immigration decisions must be reviewable and may not be | immigration.html |
| `IMM-DUE-005` | Due Process & Rights | Interpretation and translation services must be availab | immigration.html |
| `IMM-DUE-006` | Due Process & Rights | All persons within the United States or under the custo | immigration.html |
| `IMM-DUE-007` | Due Process & Rights | Immigration status may not be used to deny or diminish  | immigration.html |
| `IMM-DUE-008` | Due Process & Rights | Individuals in immigration detention or proceedings mus | immigration.html |
| `IMM-DUE-009` | Due Process & Rights | Habeas corpus protections apply fully to all individual | immigration.html |
| `IMM-DUE-010` | Due Process & Rights | Immigration detention and removal decisions must remain | immigration.html |
| `IMM-DUE-011` | Due Process & Rights | No category of person within United States jurisdiction | immigration.html |
| `IMM-ENF-001` | Enforcement Structure | Immigration and Customs Enforcement in its current form | immigration.html |
| `IMM-ENF-002` | Enforcement Structure | Any replacement immigration-enforcement structure must  | immigration.html |
| `IMM-ENF-003` | Enforcement Structure | Immigration enforcement agencies may not use broad disc | immigration.html |
| `IMM-ENF-004` | Enforcement Structure | Immigration enforcement functions must be structurally  | immigration.html |
| `IMM-ENF-005` | Enforcement Structure | Replacement structures must include strong anti-abuse s | immigration.html |
| `IMM-FAM-001` | Family Unity & Protection | Family separation in immigration enforcement is prohibi | immigration.html |
| `IMM-FAM-002` | Family Unity & Protection | Immigration systems must prioritize family unity and pr | immigration.html |
| `IMM-FAM-003` | Family Unity & Protection | Children in immigration systems must receive heightened | immigration.html |
| `IMM-FAM-004` | Family Unity & Protection | Families may not be coerced into waiver or removal deci | immigration.html |
| `IMM-INT-001` | Integration & Support | Immigration policy should support stable local integrat | immigration.html |
| `IMM-INT-002` | Integration & Support | People with pending lawful-status or protection claims  | immigration.html |
| `IMM-INT-003` | Integration & Support | Administrative limbo should not be treated as an accept | immigration.html |
| `IMM-INT-004` | Integration & Support | Immigration-system design should reduce fear-driven avo | immigration.html |
| `IMM-LAB-001` | Labor Protections | Immigration status may not be used by employers to supp | immigration.html |
| `IMM-LAB-002` | Labor Protections | All workers regardless of immigration status must be pr | immigration.html |
| `IMM-LAB-003` | Labor Protections | Reporting labor abuse wage theft trafficking or unsafe  | immigration.html |
| `IMM-LAB-004` | Labor Protections | Visa and work authorization systems must be designed to | immigration.html |
| `IMM-LAB-005` | Labor Protections | Pathways tied to labor participation should not functio | immigration.html |
| `IMM-LAB-006` | Labor Protections | Visa and work authorization systems may not be structur | immigration.html |
| `IMM-LAB-007` | Labor Protections | Workers on employer-tied visas must have meaningful por | immigration.html |
| `IMM-LAB-008` | Labor Protections | Immigration-dependent labor systems must include safegu | immigration.html |
| `IMM-LAB-009` | Labor Protections | Workers pursuing labor claims safety claims or traffick | immigration.html |
| `IMM-LAB-010` | Labor Protections | Immigration pathways connected to labor should prioriti | immigration.html |
| `IMM-OVR-001` | Oversight & Transparency | Immigration agencies and detention systems must be subj | immigration.html |
| `IMM-OVR-002` | Oversight & Transparency | Immigration systems must publish standardized data on d | immigration.html |
| `IMM-OVR-003` | Oversight & Transparency | Patterns of abuse rights violations discriminatory enfo | immigration.html |
| `IMM-OVR-004` | Oversight & Transparency | Immigration officials and agencies may not evade accoun | immigration.html |
| `IMM-REF-001` | Refugee Resettlement | The United States should maintain a robust refugee rese | immigration.html |
| `IMM-REF-002` | Refugee Resettlement | Refugee admissions and resettlement may not be arbitrar | immigration.html |
| `IMM-REF-003` | Refugee Resettlement | Refugee systems must include predictable processing cap | immigration.html |
| `IMM-REF-005` | Refugee Resettlement | Refugee eligibility and processing standards must be cl | immigration.html |
| `IMM-REF-007` | Refugee Resettlement | Refugee systems should coordinate with state and local  | immigration.html |
| `IMM-REF-008` | Refugee Resettlement | Refugees should have clear pathways from initial admiss | immigration.html |
| `IMM-REF-010` | Refugee Resettlement | Refugee systems must be subject to strong public oversi | immigration.html |
| `IMM-REM-001` | Removal & Deportation | People may not be deported to countries that are not th | immigration.html |
| `IMM-REM-002` | Removal & Deportation | Removal may not be carried out to any country where the | immigration.html |
| `IMM-REM-003` | Removal & Deportation | Third-country removals require strict legal standards m | immigration.html |
| `IMM-REM-004` | Removal & Deportation | Removal proceedings must include meaningful notice acce | immigration.html |
| `IMM-REM-005` | Removal & Deportation | No person may be deported while a timely appeal motion  | immigration.html |
| `IMM-REM-006` | Removal & Deportation | Removal orders must be based on individualized review a | immigration.html |
| `IMM-REM-007` | Removal & Deportation | People facing removal must have access to the full fact | immigration.html |
| `IMM-REM-008` | Removal & Deportation | Immigration systems must include strong safeguards agai | immigration.html |
| `IMM-REM-009` | Removal & Deportation | Where credible evidence suggests a removal may be unlaw | immigration.html |
| `IMM-REM-010` | Removal & Deportation | Wrongful removal must trigger mandatory review accounta | immigration.html |
| `IMM-REM-011` | Removal & Deportation | Removal decisions must account for family unity caregiv | immigration.html |
| `IMM-REM-012` | Removal & Deportation | People may not be removed in ways that knowingly cut of | immigration.html |
| `IMM-REM-013` | Removal & Deportation | Removal procedures involving children families disabled | immigration.html |
| `IMM-REM-014` | Removal & Deportation | Government agencies must publicly report standardized d | immigration.html |
| `IMM-REM-015` | Removal & Deportation | Expedited or summary removal procedures must be strictl | immigration.html |
| `IMM-REM-016` | Removal & Deportation | Removal transport and handoff procedures must be docume | immigration.html |
| `IMM-RGT-001` | Core Rights Principles | Immigration policy must respect human rights due proces | immigration.html |
| `IMM-RGT-002` | Core Rights Principles | Immigration systems may not rely on cruelty degradation | immigration.html |
| `IMM-RGT-003` | Core Rights Principles | Immigration law and administration must be clear consis | immigration.html |
| `IMM-RGT-004` | Core Rights Principles | Geography language wealth or access to counsel must not | immigration.html |
| `IMM-RGT-005` | Core Rights Principles | Immigration policy enforcement and adjudication may not | immigration.html |
| `IMM-RGT-006` | Core Rights Principles | Immigration rules criteria and processes must be writte | immigration.html |
| `IMM-RGT-007` | Core Rights Principles | Selective enforcement targeting based on protected char | immigration.html |
| `IMM-RGT-008` | Core Rights Principles | The United States may not create parallel systems of ju | immigration.html |
| `IMM-RGT-009` | Core Rights Principles | Differences in immigration status may affect specific l | immigration.html |
| `IMM-SRV-001` | Services & Sanctuary | People within United States jurisdiction must have acce | immigration.html |
| `IMM-SRV-002` | Services & Sanctuary | Seeking emergency care basic healthcare or medically ne | immigration.html |
| `IMM-SRV-003` | Services & Sanctuary | Immigration status may not be used to deny medically ne | immigration.html |
| `IMM-SRV-004` | Services & Sanctuary | Children within United States jurisdiction must have me | immigration.html |
| `IMM-SRV-005` | Services & Sanctuary | Schools and educational institutions may not be convert | immigration.html |
| `IMM-SRV-006` | Services & Sanctuary | Immigration-related fear must not be allowed to undermi | immigration.html |
| `IMM-SRV-007` | Services & Sanctuary | Essential public-service systems should include firewal | immigration.html |
| `IMM-SRV-008` | Services & Sanctuary | Routine use of healthcare schools shelters labor agenci | immigration.html |
| `IMM-SRV-009` | Services & Sanctuary | Public institutions must provide clear multilingual gui | immigration.html |
| `IMM-SRV-010` | Services & Sanctuary | Where immigration status affects eligibility for specif | immigration.html |
| `IMM-SRV-011` | Services & Sanctuary | Benefit systems must not use confusing status rules con | immigration.html |
| `IMM-SRV-012` | Services & Sanctuary | Children mixed-status families and other vulnerable hou | immigration.html |
| `IMM-STS-001` | Status & Pathways | Immigration policy should provide realistic lawful path | immigration.html |
| `IMM-STS-002` | Status & Pathways | Status-adjustment systems should be clear affordable an | immigration.html |
| `IMM-STS-003` | Status & Pathways | People brought to the country as children or raised sub | immigration.html |
| `IMM-STS-004` | Status & Pathways | Immigration law should reduce long-term undocumented li | immigration.html |
| `IMM-STS-005` | Status & Pathways | Status eligibility should account for family unity labo | immigration.html |
| `IMM-STS-006` | Status & Pathways | The overall system for obtaining visas green cards perm | immigration.html |
| `IMM-STS-007` | Status & Pathways | Visa and permanent-residence systems should be simplifi | immigration.html |
| `IMM-STS-008` | Status & Pathways | Application fees and procedural burdens for visas green | immigration.html |
| `IMM-STS-009` | Status & Pathways | Backlogs in family-based employment-based and humanitar | immigration.html |
| `IMM-STS-010` | Status & Pathways | Lawful-status systems must include clearer timelines st | immigration.html |
| `IMM-STS-011` | Status & Pathways | Status pathways must be designed to reduce dependency o | immigration.html |
| `IMM-STS-012` | Status & Pathways | Long-term temporary-status limbo should be reduced by c | immigration.html |
| `IMM-SYS-001` | System Design | Lawful immigration pathways should be designed to reduc | immigration.html |
| `IMM-SYS-002` | System Design | Immigration policy should be designed to reduce limbo f | immigration.html |
| `IMM-SYS-003` | System Design | Immigration systems must be evaluated not only for enfo | immigration.html |
| `IMM-SYS-004` | System Design | Any future immigration reforms must be tested against a | immigration.html |
| `IMM-TRF-001` | Trafficking Protections | Immigration systems must include strong protections for | immigration.html |
| `IMM-TRF-002` | Trafficking Protections | People reporting trafficking forced labor or coercive e | immigration.html |
| `IMM-TRF-003` | Trafficking Protections | Trafficking-related immigration protections must be acc | immigration.html |
| `IMM-TRF-004` | Trafficking Protections | Immigration and labor systems should coordinate to iden | immigration.html |
| `IMM-TRF-005` | Trafficking Protections | Survivors of trafficking and severe exploitation should | immigration.html |
| `IMM-VIS-001` | Visas & Legal Immigration | Visa categories and lawful-entry pathways should be mod | immigration.html |
| `IMM-VIS-002` | Visas & Legal Immigration | Immigration pathways should be structured to reduce ext | immigration.html |
| `IMM-VIS-003` | Visas & Legal Immigration | Green-card and permanent-residence systems should have  | immigration.html |
| `IMM-VIS-004` | Visas & Legal Immigration | Applicants for visas green cards and permanent residenc | immigration.html |
| `IMM-VIS-005` | Visas & Legal Immigration | Application requirements should be simplified and stand | immigration.html |
| `IMM-VIS-006` | Visas & Legal Immigration | Fees for visas green cards and permanent residence shou | immigration.html |
| `IMM-VIS-007` | Visas & Legal Immigration | Family-based and humanitarian pathways should not be st | immigration.html |
| `IMM-VIS-008` | Visas & Legal Immigration | Long-term residents with stable ties should have realis | immigration.html |
| `IMM-VIS-009` | Visas & Legal Immigration | Immigration pathways should be resilient against admini | immigration.html |
| `IMM-VIS-010` | Visas & Legal Immigration | The visa system must be comprehensively modernized to r | immigration.html |
| `IMM-VIS-011` | Visas & Legal Immigration | Visa categories should be simplified clarified and reor | immigration.html |
| `IMM-VIS-012` | Visas & Legal Immigration | Overlapping or contradictory visa rules should be reduc | immigration.html |
| `IMM-VIS-013` | Visas & Legal Immigration | Visa pathways should be designed to reflect real family | immigration.html |
| `IMM-VIS-014` | Visas & Legal Immigration | Visa adjudications must operate under transparent targe | immigration.html |
| `IMM-VIS-015` | Visas & Legal Immigration | Applicants must have meaningful access to real-time cas | immigration.html |
| `IMM-VIS-016` | Visas & Legal Immigration | Administrative delay may not be used as a de facto deni | immigration.html |
| `IMM-VIS-017` | Visas & Legal Immigration | Visa adjudication standards must be clear consistent an | immigration.html |
| `IMM-VIS-018` | Visas & Legal Immigration | Requests for documentation or proof in visa cases must  | immigration.html |
| `IMM-VIS-019` | Visas & Legal Immigration | Applicants must have meaningful opportunities to correc | immigration.html |
| `IMM-VIS-020` | Visas & Legal Immigration | Employment-based visa systems must reduce dependency on | immigration.html |
| `IMM-VIS-021` | Visas & Legal Immigration | Student and trainee visa systems must protect against e | immigration.html |
| `IMM-VIS-022` | Visas & Legal Immigration | Temporary visa systems should not be designed to keep p | immigration.html |
| `IMM-VIS-023` | Visas & Legal Immigration | Family-based visa systems should prioritize reunificati | immigration.html |
| `IMM-VIS-024` | Visas & Legal Immigration | Family-based applicants should not face excessive docum | immigration.html |
| `IMM-VIS-025` | Visas & Legal Immigration | Visa fees must be regulated so they cover legitimate ad | immigration.html |
| `IMM-VIS-026` | Visas & Legal Immigration | Fee waivers reductions or public support should be avai | immigration.html |
| `IMM-VIS-027` | Visas & Legal Immigration | Visa systems should include clear mechanisms for transi | immigration.html |
| `IMM-VIS-028` | Visas & Legal Immigration | People should not be forced into repeated cycles of tem | immigration.html |
| `IMM-VIS-029` | Visas & Legal Immigration | Applicants already in lawful immigration processes shou | immigration.html |
| `IMM-VIS-030` | Visas & Legal Immigration | Major changes to visa systems should include transition | immigration.html |
| `INF-AFD-001` | Internet, electricity, and water must be affordable to  | Federal law must establish affordability standards and  | infrastructure-and-public-goods.html |
| `INF-BLD-002` | Carbon-Neutral Infrastructure | Require infrastructure systems and buildouts to be carb | information-and-media.html |
| `INF-ENR-004` | End Fossil Fuel Subsidies | End oil and coal subsidies | information-and-media.html |
| `INF-ENR-005` | Guarantee Fossil Fuel Phaseout | Guarantee phaseout of oil and coal for energy productio | information-and-media.html |
| `INF-EQJ-001` | Infrastructure siting decisions must not disproportiona | Major infrastructure siting decisions — including highw | infrastructure-and-public-goods.html |
| `INF-GRD-003` | Carbon-Neutral Power Grid | Require a carbon-neutral or carbon-negative power grid | information-and-media.html |
| `INF-LBR-001` | All federally funded infrastructure projects must pay p | All infrastructure projects receiving federal funding,  | infrastructure-and-public-goods.html |
| `INF-RAIL-001` | Modernize Rail System | Modernize the U.S. rail system | information-and-media.html |
| `INF-TRN-002` | Prioritize Accessible Public Transit | Prioritize reliable affordable and accessible public tr | information-and-media.html |
| `INF-TRN-004` | Require Hybrid Capability in Transition | Require at minimum plug-in hybrid capability during tra | information-and-media.html |
| `INF-TRN-005` | Strict Fuel Efficiency Standards | Establish extremely strict fuel-efficiency standards du | information-and-media.html |
| `JUD-LGO-001` | Congressional supermajority override of SCOTUS decision | Congress may reinstate a federal statute invalidated by | courts-and-judicial-system.html |
| `JUD-NOM-001` | Senate must act on judicial nominees within 90 days | The Senate must hold confirmation hearings and vote on  | courts-and-judicial-system.html |
| `JUD-SHD-001` | Shadow docket orders require supermajority and written  | Emergency or shadow docket orders issued without full b | courts-and-judicial-system.html |
| `JUD-SIZ-001` | Supreme Court size set by constitutional amendment or s | Supreme Court size must be set by constitutional amendm | courts-and-judicial-system.html |
| `JUS-AI-001` | Ban AI sentencing determinations | AI systems may not be used to determine or recommend cr | equal-justice-and-policing.html |
| `JUS-AI-002` | Ban AI recidivism predictions in sentencing | AI risk assessment tools predicting recidivism dangerou | equal-justice-and-policing.html |
| `JUS-AI-003` | AI for wrongful conviction identification | AI may be used to assist in identifying wrongful convic | equal-justice-and-policing.html |
| `JUS-AI-004` | AI for bias identification under oversight | AI systems should be used to identify and mitigate bias | equal-justice-and-policing.html |
| `JUS-AI-005` | AI evidence transparency requirements | AI-generated evidence or analysis may not be used in co | equal-justice-and-policing.html |
| `JUS-AI-006` | Right to examine AI systems | Defendants must have the right to examine challenge and | equal-justice-and-policing.html |
| `JUS-AI-007` | Ban AI juror profiling | AI systems may not be used to profile rank or exclude j | equal-justice-and-policing.html |
| `JUS-AI-008` | Ban AI prosecutorial automation | AI systems may not be used to recommend or automate pro | equal-justice-and-policing.html |
| `JUS-AI-009` | Mandatory AI disclosure | All use of AI in legal proceedings must be disclosed to | equal-justice-and-policing.html |
| `JUS-AI-010` | AI evidence validity standards | AI evidence must meet strict reliability and scientific | equal-justice-and-policing.html |
| `JUS-BAL-001` | End cash bail systems | End or sharply limit cash bail systems that criminalize | equal-justice-and-policing.html |
| `JUS-BAL-002` | Limit pretrial detention | Pretrial detention must be limited to cases with clear  | equal-justice-and-policing.html |
| `JUS-BAL-003` | Ban AI bail risk scores | AI systems may not be used to assign bail or pretrial r | equal-justice-and-policing.html |
| `JUS-BAL-004` | Least restrictive pretrial conditions | Pretrial release decisions must favor the least restric | equal-justice-and-policing.html |
| `JUS-CIV-001` | Meaningful civil court access | People must have meaningful access to civil courts for  | equal-justice-and-policing.html |
| `JUS-CIV-002` | Ban or limit forced arbitration | Forced arbitration clauses that strip people of meaning | equal-justice-and-policing.html |
| `JUS-CIV-003` | Preserve class actions | Class actions and collective remedies must remain avail | equal-justice-and-policing.html |
| `JUS-CIV-004` | Eliminate fee barriers to justice | Court fees filing costs and procedural burdens must not | equal-justice-and-policing.html |
| `JUS-CON-001` | Retain human rights in custody | People in custody retain human rights including access  | equal-justice-and-policing.html |
| `JUS-CON-002` | Ban or limit solitary confinement | Solitary confinement must be banned or strictly limited | equal-justice-and-policing.html |
| `JUS-CON-003` | Mental health treatment in custody | Mental health needs in custody must be treated medicall | equal-justice-and-policing.html |
| `JUS-CON-004` | Disability access in detention | Disability access and accommodation must be guaranteed  | equal-justice-and-policing.html |
| `JUS-CON-005` | Independent facility inspections | Independent inspections and public reporting are requir | equal-justice-and-policing.html |
| `JUS-CRT-001` | Design for intelligibility | Justice systems must be designed for intelligibility an | equal-justice-and-policing.html |
| `JUS-CRT-002` | Accessible court participation | Courts must provide accessible notice scheduling and pa | equal-justice-and-policing.html |
| `JUS-CRT-003` | Remote tools preserve due process | Remote participation tools may improve access but may n | equal-justice-and-policing.html |
| `JUS-CRT-004` | Reduce procedural traps | Justice institutions must identify and reduce procedura | equal-justice-and-policing.html |
| `JUS-DEF-001` | Right to competent counsel | Every person facing serious criminal charges must have  | equal-justice-and-policing.html |
| `JUS-DEF-002` | Public defense funding parity | Public defense systems must be funded at levels suffici | equal-justice-and-policing.html |
| `JUS-DEF-003` | Timely access to evidence | Defendants must have timely access to discovery evidenc | equal-justice-and-policing.html |
| `JUS-DEF-004` | Prevent procedural delay undermining defense | Courts must not permit procedural delay or administrati | equal-justice-and-policing.html |
| `JUS-DEF-005` | Right to challenge evidence validity | Defendants must have the right to challenge the scienti | equal-justice-and-policing.html |
| `JUS-DEF-006` | Broad timely disclosure | Disclosure obligations must be broad continuing and tim | equal-justice-and-policing.html |
| `JUS-DEF-007` | Preserve exculpatory evidence | Prosecutors and law enforcement must preserve potential | equal-justice-and-policing.html |
| `JUS-DEF-008` | Enforce disclosure failures | Failure to disclose material evidence should carry enfo | equal-justice-and-policing.html |
| `JUS-DEF-009` | Expert assistance access | Defendants must have meaningful access to expert assist | equal-justice-and-policing.html |
| `JUS-DEF-010` | Prevent resource imbalance advantage | Procedural rules must not be structured in ways that re | equal-justice-and-policing.html |
| `JUS-DRG-003` | Redirect to treatment | Redirect funding to treatment | equal-justice-and-policing.html |
| `JUS-DRG-005` | No overdose assistance penalty | No penalty for overdose assistance | equal-justice-and-policing.html |
| `JUS-EVD-001` | Forensic scientific validity | Forensic methods used in court must meet strict scienti | equal-justice-and-policing.html |
| `JUS-EVD-002` | Exclude junk science | Junk science and unsupported forensic techniques must b | equal-justice-and-policing.html |
| `JUS-EVD-003` | Chain-of-custody standards | Digital and physical evidence must maintain transparent | equal-justice-and-policing.html |
| `JUS-EVD-004` | Identify synthetic evidence | Synthetic or AI-generated evidence must be clearly iden | equal-justice-and-policing.html |
| `JUS-EVD-005` | Review when science discredited | When foundational science behind a conviction is later  | equal-justice-and-policing.html |
| `JUS-FFF-001` | Ban revenue-extraction justice | Justice systems must not use fines fees and monetary pe | equal-justice-and-policing.html |
| `JUS-FFF-002` | Assess ability to pay | Ability to pay must be assessed before imposing or enfo | equal-justice-and-policing.html |
| `JUS-FFF-003` | Ban incarceration for inability to pay | People may not be incarcerated detained or otherwise de | equal-justice-and-policing.html |
| `JUS-FFF-004` | Limit compounding penalties | Late fees interest penalties and compounding charges in | equal-justice-and-policing.html |
| `JUS-FFF-005` | Accessible payment alternatives | Courts and agencies must provide accessible alternative | equal-justice-and-policing.html |
| `JUS-FFF-006` | Ban justice revenue dependency | Justice institutions may not depend on fines fees or ci | equal-justice-and-policing.html |
| `JUS-IMM-001` | Due process limits on immigration detention | Immigration detention must be subject to strict due pro | equal-justice-and-policing.html |
| `JUS-IMM-002` | Immigration counsel access | People in immigration proceedings must have meaningful  | equal-justice-and-policing.html |
| `JUS-IMM-003` | Ban coercive family separation | Family separation and coercive detention practices must | equal-justice-and-policing.html |
| `JUS-JUV-001` | Prioritize rehabilitation for youth | Juvenile justice systems must prioritize rehabilitation | equal-justice-and-policing.html |
| `JUS-JUV-002` | Limit adult sentencing for children | Children may not be subjected to adult sentencing stand | equal-justice-and-policing.html |
| `JUS-JUV-003` | Automatic juvenile record sealing | Juvenile records should be sealed or expunged automatic | equal-justice-and-policing.html |
| `JUS-JUV-004` | Youth custody services | Youth in custody must retain access to education mental | equal-justice-and-policing.html |
| `JUS-LAW-001` | Abolish qualified immunity | Qualified immunity is abolished and may not be used to  | equal-justice-and-policing.html |
| `JUS-LAW-002` | Government official accountability | Government officials including law enforcement must be  | equal-justice-and-policing.html |
| `JUS-LAW-003` | Remove prior-case-law requirement | Legal standards for accountability must not require vic | equal-justice-and-policing.html |
| `JUS-LAW-004` | Indemnification limits | Governments may provide indemnification for officials a | equal-justice-and-policing.html |
| `JUS-LNG-001` | Interpretation at every stage | People involved in justice proceedings must have meanin | equal-justice-and-policing.html |
| `JUS-LNG-002` | Free language access | Interpreter and translation access must be provided wit | equal-justice-and-policing.html |
| `JUS-LNG-003` | Language failures not harmless | Language access failures may not be treated as harmless | equal-justice-and-policing.html |
| `JUS-LNG-004` | Limit automated translation | Critical justice proceedings may not rely solely on aut | equal-justice-and-policing.html |
| `JUS-LNG-005` | Proactive language-access identification | Justice institutions must proactively identify language | equal-justice-and-policing.html |
| `JUS-OVR-001` | Publish standardized justice data | Justice institutions must publish standardized data on  | equal-justice-and-policing.html |
| `JUS-OVR-002` | Disaggregate disparity data | Justice data must be disaggregated to identify racial g | equal-justice-and-policing.html |
| `JUS-OVR-004` | Require action on audit findings | Justice agencies must be required to act on audit findi | equal-justice-and-policing.html |
| `JUS-POL-013` | Preserve and disclose misconduct records | Law enforcement misconduct records relevant to credibil | equal-justice-and-policing.html |
| `JUS-POL-014` | Disclose Brady and Giglio material | Prosecutors must disclose credibility-related misconduc | equal-justice-and-policing.html |
| `JUS-POL-015` | Consequences for officer dishonesty | Police officers with substantiated records of dishonest | equal-justice-and-policing.html |
| `JUS-POL-016` | Ban misconduct concealment | Law enforcement agencies may not use internal secrecy c | equal-justice-and-policing.html |
| `JUS-POL-017` | Track misconduct across jurisdictions | Independent systems should track officer misconduct pat | equal-justice-and-policing.html |
| `JUS-PRO-001` | Ban coercive charging | Prosecutors may not use charging decisions to coerce pl | equal-justice-and-policing.html |
| `JUS-PRO-002` | Automatic exculpatory disclosure | Prosecutors must disclose exculpatory evidence fully pr | equal-justice-and-policing.html |
| `JUS-PRO-003` | Ban retaliatory prosecution | Retaliatory or politically motivated prosecution is pro | equal-justice-and-policing.html |
| `JUS-PRO-004` | Prosecutorial transparency and audit | Prosecutorial offices must be subject to transparency a | equal-justice-and-policing.html |
| `JUS-PRO-005` | Ban AI prosecutorial automation | AI systems may not independently recommend charges plea | equal-justice-and-policing.html |
| `JUS-PRP-001` | Ban or limit civil forfeiture | Civil forfeiture should be banned or strictly limited a | equal-justice-and-policing.html |
| `JUS-PRP-003` | Ban forfeiture as revenue | Justice agencies may not rely on forfeiture or seized a | equal-justice-and-policing.html |
| `JUS-PRP-004` | Ban civil forfeiture without conviction | Civil asset forfeiture is prohibited and property may n | equal-justice-and-policing.html |
| `JUS-PRP-005` | Strict limits on temporary seizure | Temporary seizure of property prior to conviction must  | equal-justice-and-policing.html |
| `JUS-PRP-006` | Accessible seizure contest processes | Property owners must have meaningful accessible and tim | equal-justice-and-policing.html |
| `JUS-REC-001` | Broad expungement access | People should have broad access to sealing expungement  | equal-justice-and-policing.html |
| `JUS-REC-002` | Automatic expungement | Expungement and sealing should be automatic in many cat | equal-justice-and-policing.html |
| `JUS-REC-003` | Automatic juvenile sealing | Juvenile records should be sealed or expunged automatic | equal-justice-and-policing.html |
| `JUS-REC-004` | Seal dismissed and acquitted charges | Dismissed charges acquittals and invalidated conviction | equal-justice-and-policing.html |
| `JUS-REC-005` | Honor expungement in systems | Background-check systems and public records systems mus | equal-justice-and-policing.html |
| `JUS-REC-006` | Accessible record correction | People must have accessible processes to correct errors | equal-justice-and-policing.html |
| `JUS-REI-001` | Reduce collateral consequences | People completing sentences should not face unnecessary | equal-justice-and-policing.html |
| `JUS-REI-002` | Limit collateral consequences | Collateral consequences must be reviewed limited and ti | equal-justice-and-policing.html |
| `JUS-REI-003` | Reentry support services | Reentry support should include access to identification | equal-justice-and-policing.html |
| `JUS-REI-004` | Prioritize reintegration | Justice policy should prioritize reintegration and stab | equal-justice-and-policing.html |
| `JUS-REV-001` | Expand post-conviction review | Post-conviction review processes must be expanded and a | equal-justice-and-policing.html |
| `JUS-REV-003` | Wrongful conviction triggers review | Wrongful-conviction indicators must trigger mandatory r | equal-justice-and-policing.html |
| `JUS-REV-004` | AI for wrongful conviction patterns | AI may be used to identify patterns of wrongful convict | equal-justice-and-policing.html |
| `JUS-REV-005` | No artificial deadlines for relief | Post-conviction review should not be restricted by arti | equal-justice-and-policing.html |
| `JUS-REV-006` | Access to post-conviction resources | People seeking post-conviction relief must have meaning | equal-justice-and-policing.html |
| `JUS-REV-007` | Presumptive systemic review | Justice systems should create presumptive review pathwa | equal-justice-and-policing.html |
| `JUS-RST-001` | Restorative justice pathways | Justice systems should include restorative justice path | equal-justice-and-policing.html |
| `JUS-RST-002` | Expand diversion programs | Diversion programs should be expanded to reduce unneces | equal-justice-and-policing.html |
| `JUS-RST-003` | Preserve due process in diversion | Restorative and diversion programs must not be coercive | equal-justice-and-policing.html |
| `JUS-RST-004` | Equitable diversion access | Access to restorative justice and diversion should not  | equal-justice-and-policing.html |
| `JUS-SUP-001` | Support reintegration not reincarceration | Probation and parole systems must be designed to suppor | equal-justice-and-policing.html |
| `JUS-SUP-002` | Narrow tailored supervision conditions | Conditions of probation and parole must be narrowly tai | equal-justice-and-policing.html |
| `JUS-SUP-003` | Limit technical violation incarceration | Technical violations that do not involve new serious cr | equal-justice-and-policing.html |
| `JUS-SUP-004` | Due process for revocation | Revocation of probation or parole must require meaningf | equal-justice-and-policing.html |
| `JUS-SUP-005` | Prevent impossible conditions | Probation and parole systems must not impose impossible | equal-justice-and-policing.html |
| `JUS-SUP-006` | Periodic supervision review | Supervision terms should be periodically reviewed and s | equal-justice-and-policing.html |
| `JUS-VIC-001` | Victim protection and participation | Victims of crime must have access to protection informa | equal-justice-and-policing.html |
| `JUS-VIC-002` | Trauma-informed victim services | Victim-support systems should include trauma-informed s | equal-justice-and-policing.html |
| `JUS-VIC-003` | Preserve evidentiary standards | Victims’ rights frameworks may not be used to erode evi | equal-justice-and-policing.html |
| `JUS-VIC-004` | Justice not retribution alone | Victim participation must be structured to support just | equal-justice-and-policing.html |
| `JUS-VIC-005` | Equitable victim support access | Access to victim-support services must be equitable and | equal-justice-and-policing.html |
| `JUS-WIT-001` | Protect witnesses from retaliation | Witnesses must be protected from intimidation retaliati | equal-justice-and-policing.html |
| `JUS-WIT-002` | Proportionate witness protection | Witness-protection measures must be proportionate revie | equal-justice-and-policing.html |
| `JUS-WIT-003` | Disclose witness inducements | Courts and prosecutors must disclose material inducemen | equal-justice-and-policing.html |
| `JUS-WIT-004` | Penalize witness intimidation | Witness intimidation by officials law enforcement litig | equal-justice-and-policing.html |
| `LAB-CLM-001` | All workers have the right to safe temperatures and hea | All workers have an enforceable right to protection fro | labor-and-workers-rights.html |
| `LAB-DOM-001` | Domestic workers must be covered by full labor law prot | Domestic workers&#x2014;including nannies, housekeepers | labor-and-workers-rights.html |
| `LAB-PAY-002` | Wage systems must be transparent, predictable, and free | The federal minimum wage must be set at a level suffici | labor-and-workers-rights.html |
| `LAB-PBN-001` | Benefits must travel with workers across employment rel | Social insurance systems and workplace benefits&#x2014; | labor-and-workers-rights.html |
| `LAB-PRL-001` | Prison labor may not be compelled without fair compensa | Incarcerated workers performing labor may not be compel | labor-and-workers-rights.html |
| `LAB-SCH-001` | Workers in covered industries must receive advance noti | Workers in retail, food service, hospitality, and other | labor-and-workers-rights.html |
| `LAB-SFT-001` | Employers must provide safe working conditions and may | All workers have the right to a safe workplace and empl | labor-and-workers-rights.html |
| `LEG-DMJ-001` | Structural minority rule over national policy is prohib | Legislative systems must prevent structural minority ru | legislative-reform.html |
| `LEG-DRF-001` | Binding drafting standards required for all new federal | A constitutional amendment or equivalent binding rule s | legislative-reform.html |
| `LEG-DRF-002` | Each new law requires plain-language statement of purpo | Every new law must include a plain-language statement o | legislative-reform.html |
| `LEG-PRO-001` | Filibuster and indefinite minority obstruction must end | Legislative procedure may not allow indefinite minority | legislative-reform.html |
| `LEG-RPL-001` | Repeal Alien Enemies Act and related emergency abuse fr | Repeal the Alien Enemies Act framework and related emer | legislative-reform.html |
| `LEG-SEN-003` | Senate may serve as review body rather than co-equal ve | The Senate may serve as a review, delay, and revision b | legislative-reform.html |
| `MED-NET-001` | Restore and permanently codify net neutrality in federa | Internet service providers must treat all legal interne | information-and-media.html |
| `MED-OWN-001` | Establish and enforce media ownership limits to prevent | No single entity may own more than one daily newspaper, | information-and-media.html |
| `MED-PLT-001` | Require transparency in platform content moderation pol | Digital platforms with significant user reach must publ | information-and-media.html |
| `MED-PUB-001` | Guarantee and expand public media funding insulated fro | Federal funding for public media — including the Corpor | information-and-media.html |
| `OVR-BRN-001` | Independent Oversight Boards for Each Branch | Each branch of government and major constitutional body | checks-and-balances.html |
| `OVR-BRN-002` | Oversight Board Independence | Oversight boards must be independent from the bodies th | checks-and-balances.html |
| `OVR-FED-001` | Federal Independent Oversight Body | Establish a federal independent oversight and investiga | checks-and-balances.html |
| `OVR-FED-002` | Authority Over Federally Elected Officials | Federal oversight body has authority to investigate any | checks-and-balances.html |
| `OVR-FED-003` | Oversight Body Composition and Elected Component | Federal oversight body includes one elected member and  | checks-and-balances.html |
| `OVR-FED-004` | Subpoena and Deposition Powers | Federal oversight body has subpoena and deposition powe | checks-and-balances.html |
| `OVR-FND-001` | Guaranteed Adequate Funding | Funding for oversight and investigation bodies must be  | checks-and-balances.html |
| `OVR-FND-002` | Automatic Extension if Funding Not Passed | If funding is not passed oversight bodies automatically | checks-and-balances.html |
| `OVR-FND-003` | Automatic Extension Includes 10% Increase | Automatic funding extension includes a 10 percent incre | checks-and-balances.html |
| `OVR-FND-004` | Funding Separate from Overseen Departments | Oversight funding must be separate from the departments | checks-and-balances.html |
| `OVR-FND-005` | Protection from Political and External Influence | Oversight funding must be protected from political and  | checks-and-balances.html |
| `OVR-JUR-001` | Jurisdiction Over State Officials | Federal oversight body may investigate governors and hi | checks-and-balances.html |
| `OVR-JUR-002` | Jurisdiction Over Failed State Oversight | Federal oversight body may investigate state oversight  | checks-and-balances.html |
| `OVR-STA-001` | State Oversight Boards Required | Each state must establish its own independent oversight | checks-and-balances.html |
| `OVR-STA-002` | Directly Elected Members | State oversight boards include directly elected members | checks-and-balances.html |
| `OVR-STA-003` | Appointed Members Balance | State oversight boards include members appointed by leg | checks-and-balances.html |
| `SYS-AI-001` | Prohibition on Asymmetrical AI Processes | AI-assisted decision systems must not create asymmetric | checks-and-balances.html |
| `SYS-AI-002` | Independent Human Judgment Required for Material Harm | Any decision that materially harms restricts or denies  | checks-and-balances.html |
| `SYS-AI-004` | Equal and Timely Consideration Regardless of AI Score | All individuals must receive equal and timely considera | checks-and-balances.html |
| `SYS-AI-005` | AI Bias Detection and Mitigation | AI systems used in decision-making processes must inclu | checks-and-balances.html |
| `SYS-AI-006` | Continuous Auditing for Bias and Disparate Impact | Decision-making systems using AI must be continuously a | checks-and-balances.html |
| `SYS-AI-007` | Domain-Specific AI Rules | Each policy domain or pillar must define its own AI sys | checks-and-balances.html |
| `SYS-FED-001` | High-Risk Systems Not Fully Centralized | High-risk systems must not be fully centralized | checks-and-balances.html |
| `SYS-FED-003` | Federal Standards for Elections | Federal sets standards but not direct control of electi | checks-and-balances.html |
| `SYS-FND-001` | Platform as Policy and Strategy | Platform is both a policy framework and long-term strat | checks-and-balances.html |
| `SYS-FND-008` | Movement Not Left vs Right | Movement is not left vs right | checks-and-balances.html |
| `SYS-FND-018` | Core Values: Truth, Equality, Freedom, Dignity | Core values include truth equality freedom dignity | checks-and-balances.html |
| `SYS-GEO-004` | Cross-State Access Guaranteed | Cross-state access must be guaranteed | checks-and-balances.html |
| `SYS-GEO-005` | Travel Support When Local Care Unavailable | Travel support required when local care unavailable | checks-and-balances.html |
| `TAX-CDR-001` | Candidates for federal office must publicly disclose ta | Candidates for President, Vice President, and federal e | taxation-and-wealth.html |
| `TAX-COR-001` | Corporations must pay meaningful taxes on real economic | Corporate tax rates must be sufficient to prevent profi | taxation-and-wealth.html |
| `TAX-ENF-001` | Tax enforcement agencies must be well funded, technical | The IRS must be funded and staffed to enforce tax law e | taxation-and-wealth.html |
| `TAX-FTT-001` | Securities and derivatives transactions may be subject  | Financial transactions in stocks, bonds, and derivative | taxation-and-wealth.html |
| `TAX-INT-001` | United States should pursue international agreements an | The United States should pursue international agreement | taxation-and-wealth.html |
| `TAX-LVT-001` | Land value taxation may capture publicly created land v | Tax policy may employ land value taxation to capture th | taxation-and-wealth.html |
| `TEC-AGE-002` | No centralized databases | Age verification systems must not create centralized da | technology-and-ai.html |
| `TEC-AGE-003` | Allow privacy-preserving alternatives | Allow age assurance mechanisms that preserve privacy su | technology-and-ai.html |
| `TEC-AGE-004` | Data minimization and deletion | Any permitted age verification system must minimize dat | technology-and-ai.html |
| `TEC-AGE-005` | Narrow scope requirements | Age verification requirements must be narrowly scoped t | technology-and-ai.html |
| `TEC-AGE-006` | Ban surveillance proxy use | Governments and private entities may not use age verifi | technology-and-ai.html |
| `TEC-AI-001` | High-risk AI requires review | High-risk AI systems must be subject to heightened gove | technology-and-ai.html |
| `TEC-AI-002` | No automation without accountability | AI systems that affect rights liberty healthcare educat | technology-and-ai.html |
| `TEC-AI-003` | Rights to notice and review | No fully automated decisions in critical domains withou | technology-and-ai.html |
| `TEC-AI-004` | Transparency and auditability | AI systems used in public-sector decision-making must b | technology-and-ai.html |
| `TEC-AI-006` | Testing for bias and safety | AI systems must be tested for bias safety reliability a | technology-and-ai.html |
| `TEC-AI-007` | Documentation disclosure | Covered AI systems must maintain model cards documentat | technology-and-ai.html |
| `TEC-AI-008` | No secret law | Secret law or undisclosed AI decision systems must not  | technology-and-ai.html |
| `TEC-ALG-001` | Disclosure of algorithmic influence | People must be told when AI or algorithmic systems mate | technology-and-ai.html |
| `TEC-ALG-002` | Right to contest decisions | People must have the right to contest materially harmfu | technology-and-ai.html |
| `TEC-ALG-003` | Non-algorithmic alternatives | Users must have access to non-algorithmic or less perso | technology-and-ai.html |
| `TEC-ALG-004` | Ban manipulative optimization | Ban manipulative algorithmic optimization that targets  | technology-and-ai.html |
| `TEC-ALG-005` | Disclose ranking objectives | Platforms must disclose core ranking and recommendation | technology-and-ai.html |
| `TEC-ALG-006` | Protected researcher access | Independent researchers must have protected access to p | technology-and-ai.html |
| `TEC-AUD-001` | Independent auditing requirement | Covered AI systems must support independent auditing fo | technology-and-ai.html |
| `TEC-AUD-002` | Meaningful redress for harms | Affected individuals must have access to meaningful exp | technology-and-ai.html |
| `TEC-AUD-003` | Forensic logging | Organizations deploying high-risk AI must keep logs suf | technology-and-ai.html |
| `TEC-AUD-004` | Public AI registry | Government use of AI must be cataloged in a public regi | technology-and-ai.html |
| `TEC-AUD-005` | Oversight of classified systems | Classified or sensitive AI systems must still be subjec | technology-and-ai.html |
| `TEC-AUT-001` | Strict safeguards for high-risk systems | High-risk autonomous systems must not be deployed where | technology-and-ai.html |
| `TEC-AUT-002` | No replacement of accountable humans | AI systems used in healthcare education benefits housin | technology-and-ai.html |
| `TEC-AUT-003` | Prohibit automated denial systems | Automated denial systems for benefits care housing or l | technology-and-ai.html |
| `TEC-AUT-004` | Human override authority | Government agencies must maintain human override author | technology-and-ai.html |
| `TEC-BIO-002` | Ban real-time crowd tracking | Ban real-time biometric tracking of crowds or demonstra | technology-and-ai.html |
| `TEC-BIO-003` | No general identity infrastructure | Biometric systems may not be used as general identity i | technology-and-ai.html |
| `TEC-BIO-004` | Strict safeguards where permitted | Where biometrics are permitted they must require strict | technology-and-ai.html |
| `TEC-BIO-005` | Heightened data protection | Biometric data must be treated as highly sensitive prot | technology-and-ai.html |
| `TEC-DAT-001` | Prohibit unauthorized cross-agency surveillance fusion | Ban or strictly limit cross-agency fusion of surveillan | technology-and-ai.html |
| `TEC-DAT-002` | Ban secret dossiers | Ban creation of secret AI-generated behavioral dossiers | technology-and-ai.html |
| `TEC-DAT-003` | Ban government use of commercial data | Ban use of commercially acquired bulk location biometri | technology-and-ai.html |
| `TEC-EDU-001` | AI must enhance not replace learning | AI systems in education must enhance learning without r | technology-and-ai.html |
| `TEC-EDU-002` | No replacement of human educators | AI systems may not replace human educators in primary s | technology-and-ai.html |
| `TEC-EDU-003` | Support not substitute | AI systems may be used to support educators and student | technology-and-ai.html |
| `TEC-EDU-004` | No sole-basis grading | AI systems may not be the sole basis for grading or eva | technology-and-ai.html |
| `TEC-EDU-005` | Right to human review | Students have the right to human review of AI-influence | technology-and-ai.html |
| `TEC-EDU-006` | Clear policies on AI use | Educational institutions must establish clear policies  | technology-and-ai.html |
| `TEC-EDU-007` | Evaluate for bias | AI systems used in education must be evaluated for bias | technology-and-ai.html |
| `TEC-EDU-008` | Accessibility and equity | AI tools used in education must be accessible to all st | technology-and-ai.html |
| `TEC-EDU-009` | Data minimization | Student data collected by AI systems must be limited to | technology-and-ai.html |
| `TEC-EDU-010` | No commercial use of student data | Student data may not be sold shared or used for adverti | technology-and-ai.html |
| `TEC-EDU-011` | Enhanced protections for minors | Enhanced privacy protections are required for minors us | technology-and-ai.html |
| `TEC-EDU-012` | Ban invasive surveillance | Ban use of AI systems for invasive surveillance of stud | technology-and-ai.html |
| `TEC-EDU-013` | No emotion inference | AI systems may not be used to infer student emotions at | technology-and-ai.html |
| `TEC-EDU-014` | No behavioral scoring | Educational institutions may not use AI systems to assi | technology-and-ai.html |
| `TEC-EDU-015` | Disclose AI-generated content | AI-generated educational content must be clearly identi | technology-and-ai.html |
| `TEC-EDU-016` | No ideological manipulation | AI systems may not be used to impose ideological viewpo | technology-and-ai.html |
| `TEC-EDU-017` | Support critical thinking | Educational use of AI must support development of criti | technology-and-ai.html |
| `TEC-EDU-018` | Accessibility for disabilities | AI may be used to improve accessibility for students wi | technology-and-ai.html |
| `TEC-EDU-019` | Multilingual support | AI systems should support multilingual education and re | technology-and-ai.html |
| `TEC-EDU-020` | Disclosure requirement | Educational institutions must disclose use of AI system | technology-and-ai.html |
| `TEC-EDU-021` | Regular independent audits | AI systems used in education must be subject to regular | technology-and-ai.html |
| `TEC-EDU-022` | No proprietary opacity | Vendors providing AI systems to educational institution | technology-and-ai.html |
| `TEC-EDU-023` | Demonstrate educational benefit | AI systems must demonstrate educational benefit through | technology-and-ai.html |
| `TEC-EDU-024` | Informed consent for testing | Students may not be used as unwitting test subjects for | technology-and-ai.html |
| `TEC-ENV-001` | Sustainable operations required | AI systems and infrastructure must not externalize envi | technology-and-ai.html |
| `TEC-ENV-002` | Carbon neutrality requirement | Large-scale AI systems and data centers must meet stric | technology-and-ai.html |
| `TEC-ENV-003` | Energy disclosure | Operators of large AI systems must publicly disclose en | technology-and-ai.html |
| `TEC-ENV-004` | Renewable energy supply | High-consumption AI infrastructure must supply or offse | technology-and-ai.html |
| `TEC-ENV-005` | Water usage disclosure | AI infrastructure operators must disclose water usage i | technology-and-ai.html |
| `TEC-ENV-006` | Water resource protection | AI systems must not disproportionately strain local wat | technology-and-ai.html |
| `TEC-ENV-007` | Materials sourcing standards | Materials used in AI hardware including rare earth elem | technology-and-ai.html |
| `TEC-ENV-008` | Lifecycle responsibility | AI hardware producers must be responsible for full life | technology-and-ai.html |
| `TEC-ENV-009` | Durability and repairability | AI-related hardware must meet durability repairability  | technology-and-ai.html |
| `TEC-ENV-010` | Recycling programs | Operators must implement responsible recycling and disp | technology-and-ai.html |
| `TEC-ENV-011` | Internalize environmental costs | Companies developing or deploying AI systems must inter | technology-and-ai.html |
| `TEC-ENV-012` | Environmental impact assessments | Large-scale AI deployments must undergo environmental i | technology-and-ai.html |
| `TEC-ENV-013` | Support climate efforts | AI should be used to support climate modeling environme | technology-and-ai.html |
| `TEC-ENV-014` | Resource optimization | AI may be used to optimize energy water and resource us | technology-and-ai.html |
| `TEC-ENV-015` | Grid modernization support | AI systems may support modernization of electrical grid | technology-and-ai.html |
| `TEC-ENV-016` | No misrepresentation | AI companies may not misrepresent environmental impact  | technology-and-ai.html |
| `TEC-ENV-017` | Standardized reporting | Environmental reporting for AI systems must follow stan | technology-and-ai.html |
| `TEC-ENV-018` | Environmental justice protection | AI infrastructure may not disproportionately locate env | technology-and-ai.html |
| `TEC-ENV-019` | No global offloading | Environmental costs of AI supply chains must not be off | technology-and-ai.html |
| `TEC-ENV-020` | Integration with national policy | AI infrastructure policy must integrate with national e | technology-and-ai.html |
| `TEC-ENV-021` | Noise pollution standards | Establish standards for noise pollution from AI data ce | technology-and-ai.html |
| `TEC-FIN-001` | Fairness and transparency in finance | AI systems in finance credit and insurance must not und | technology-and-ai.html |
| `TEC-FIN-002` | No automated denial of credit | AI systems may not independently deny credit loans mort | technology-and-ai.html |
| `TEC-FIN-003` | Human review before denial | Any decision that would deny restrict or materially wor | technology-and-ai.html |
| `TEC-FIN-004` | No opaque criteria | AI systems used in underwriting or creditworthiness ass | technology-and-ai.html |
| `TEC-FIN-005` | Anti-discrimination requirement | AI systems in finance and insurance must not discrimina | technology-and-ai.html |
| `TEC-FIN-006` | Regular audits for bias | AI systems used in lending underwriting pricing or clai | technology-and-ai.html |
| `TEC-FIN-007` | No automated insurance denial | AI systems may not independently deny restrict reduce o | technology-and-ai.html |
| `TEC-FIN-008` | Independent human judgment required | Human reviewers in insurance decisions may not rely sol | technology-and-ai.html |
| `TEC-FIN-009` | AI for approval not denial | AI systems may be used to assist or expedite approval o | technology-and-ai.html |
| `TEC-FIN-010` | No negative inference from AI | Absence of AI approval or recommendation may not be use | technology-and-ai.html |
| `TEC-FIN-011` | No behavioral surveillance scoring | AI systems may not use generalized behavioral surveilla | technology-and-ai.html |
| `TEC-FIN-012` | Transparent risk scoring | Risk scoring in finance and insurance must be based on  | technology-and-ai.html |
| `TEC-FIN-013` | No vulnerability profiling | AI systems may not use individualized vulnerability pro | technology-and-ai.html |
| `TEC-FIN-014` | Fair housing access | AI systems used in mortgage housing finance or rental s | technology-and-ai.html |
| `TEC-FIN-015` | Tenant screening limits | Tenant screening and housing-related AI systems may not | technology-and-ai.html |
| `TEC-FIN-016` | Right to explanation | People have the right to a meaningful explanation of AI | technology-and-ai.html |
| `TEC-FIN-017` | Right to appeal | People must have access to a timely human appeal proces | technology-and-ai.html |
| `TEC-FIN-018` | Disclosure requirement | Entities using AI in consequential financial or insuran | technology-and-ai.html |
| `TEC-FIN-019` | Data minimization | AI systems in finance and insurance may collect only da | technology-and-ai.html |
| `TEC-FIN-020` | No data sales or repurposing | Financial and insurance data used by AI systems may not | technology-and-ai.html |
| `TEC-FIN-021` | No secret profile enrichment | Entities may not secretly enrich financial or insurance | technology-and-ai.html |
| `TEC-FIN-022` | No cross-system denial loops | AI systems may not be used to create cross-system denia | technology-and-ai.html |
| `TEC-FIN-024` | No proprietary opacity | Trade secrecy or proprietary claims may not be used to  | technology-and-ai.html |
| `TEC-FIN-025` | Documentation requirement | Entities deploying consequential AI systems in finance  | technology-and-ai.html |
| `TEC-FIN-026` | No exploitation of vulnerability | AI systems may not be used to identify and exploit fina | technology-and-ai.html |
| `TEC-FIN-027` | No impersonation | AI systems in finance and insurance may not impersonate | technology-and-ai.html |
| `TEC-FIN-028` | Public-interest standards for essential systems | Where finance credit or insurance systems function as e | technology-and-ai.html |
| `TEC-FIN-029` | No automatic exclusion from essential systems | AI systems must not be allowed to automatically exclude | technology-and-ai.html |
| `TEC-GOV-001` | Preserve due process and rights | AI systems used by government or public-service entitie | technology-and-ai.html |
| `TEC-GOV-002` | No automated denial of benefits | AI systems may not independently deny terminate reduce  | technology-and-ai.html |
| `TEC-GOV-003` | Human decision-maker before harm | Any decision that would deny reduce terminate or delay  | technology-and-ai.html |
| `TEC-GOV-004` | Independent human judgment required | Human reviewers may not rely solely on AI-generated rec | technology-and-ai.html |
| `TEC-GOV-005` | AI for approval not denial | AI systems may be used to help identify likely eligibil | technology-and-ai.html |
| `TEC-GOV-006` | Right to explanation | Individuals have the right to a meaningful explanation  | technology-and-ai.html |
| `TEC-GOV-007` | Right to appeal | Individuals must have a timely accessible appeal proces | technology-and-ai.html |
| `TEC-GOV-008` | Disclosure requirement | Government agencies must clearly disclose when AI syste | technology-and-ai.html |
| `TEC-GOV-009` | No behavioral scoring | Government may not use AI systems to assign generalized | technology-and-ai.html |
| `TEC-GOV-010` | No discriminatory profiling | Government AI systems may not use protected characteris | technology-and-ai.html |
| `TEC-GOV-011` | No social conformity scoring | Government may not use AI systems to monitor or score b | technology-and-ai.html |
| `TEC-GOV-012` | Access to human representatives | People must retain access to human government represent | technology-and-ai.html |
| `TEC-GOV-013` | No forced AI-only channels | Government may not force individuals into AI-only servi | technology-and-ai.html |
| `TEC-GOV-014` | Accessibility for vulnerable populations | AI-enabled public services must be accessible to disabl | technology-and-ai.html |
| `TEC-GOV-015` | No automated disability denials | AI systems may not be used to deny disability benefits  | technology-and-ai.html |
| `TEC-GOV-016` | No mass fraud sweeps | Government may not use AI systems to conduct mass fraud | technology-and-ai.html |
| `TEC-GOV-017` | No automated termination of essential benefits | AI systems may not automatically terminate housing food | technology-and-ai.html |
| `TEC-GOV-018` | No automated immigration decisions | AI systems may not independently determine immigration  | technology-and-ai.html |
| `TEC-GOV-019` | No credibility inference in immigration | Government may not use AI systems to infer truthfulness | technology-and-ai.html |
| `TEC-GOV-020` | Human review for immigration decisions | Any AI-influenced immigration or detention decision mus | technology-and-ai.html |
| `TEC-GOV-021` | Vendor accountability | Private vendors and contractors supplying AI systems to | technology-and-ai.html |
| `TEC-GOV-022` | No proprietary opacity | Trade secrecy or proprietary claims may not be used to  | technology-and-ai.html |
| `TEC-GOV-023` | Procurement disclosure | Government procurement of AI systems must include publi | technology-and-ai.html |
| `TEC-GOV-024` | Regular independent audits | Government AI systems must undergo regular independent  | technology-and-ai.html |
| `TEC-GOV-025` | Public AI registry | All materially consequential government AI systems must | technology-and-ai.html |
| `TEC-GOV-026` | Sunset and reauthorization | Government AI systems affecting rights benefits or lega | technology-and-ai.html |
| `TEC-GOV-027` | Explicit legal authority required | Government agencies may not deploy consequential AI sys | technology-and-ai.html |
| `TEC-GOV-028` | No unwitting test subjects | Government may not use the public as unwitting test sub | technology-and-ai.html |
| `TEC-GOV-029` | Right to challenge system legality | Individuals must be able to challenge not only a govern | technology-and-ai.html |
| `TEC-HAR-001` | Platforms must implement effective systems to prevent a | Digital platforms with significant user bases must impl | technology-and-ai.html |
| `TEC-IMM-001` | Ban opaque immigration AI | Ban use of opaque or unreviewable AI systems in immigra | technology-and-ai.html |
| `TEC-IMM-002` | Ban risk scoring for detention | Ban AI risk scoring systems used to justify immigration | technology-and-ai.html |
| `TEC-INT-004` | Common carrier treatment | Internet service providers and core digital network inf | technology-and-ai.html |
| `TEC-INT-005` | Non-discrimination requirement | Common carrier obligations must prohibit discrimination | technology-and-ai.html |
| `TEC-INT-006` | No blocking or throttling | Network operators may not prioritize degrade or block t | technology-and-ai.html |
| `TEC-INT-007` | Narrow technical exceptions | Net neutrality frameworks must allow narrowly scoped ex | technology-and-ai.html |
| `TEC-INT-008` | Transparent exceptions | All exceptions to neutrality must be transparent audita | technology-and-ai.html |
| `TEC-INT-009` | Protection from rollback | Core neutrality and access protections must be insulate | technology-and-ai.html |
| `TEC-JUD-001` | No AI sentencing | AI systems may not be used to determine sentencing bail | technology-and-ai.html |
| `TEC-JUD-002` | No risk scoring | AI systems may not assign risk scores for recidivism da | technology-and-ai.html |
| `TEC-JUD-003` | No jury profiling | AI systems may not be used to profile influence or sele | technology-and-ai.html |
| `TEC-JUD-004` | Strict admissibility standards | AI-generated or AI-analyzed evidence must meet strict s | technology-and-ai.html |
| `TEC-JUD-005` | Right to examine AI evidence | Defendants and parties must have the right to examine c | technology-and-ai.html |
| `TEC-JUD-006` | AI for wrongful conviction review | AI may be used to assist in identifying wrongful convic | technology-and-ai.html |
| `TEC-JUD-007` | Identify systemic bias | AI should be used to identify systemic bias in sentenci | technology-and-ai.html |
| `TEC-JUD-008` | No AI final determinations | Judges and court staff may not rely on AI systems to ma | technology-and-ai.html |
| `TEC-JUD-009` | Clerical use only with disclosure | AI may be used to assist with clerical summarization re | technology-and-ai.html |
| `TEC-JUD-010` | Disclose material AI use | Courts must disclose material use of AI in opinion draf | technology-and-ai.html |
| `TEC-JUD-011` | No unfair docket prioritization | AI systems may not be used to prioritize dockets motion | technology-and-ai.html |
| `TEC-JUD-012` | Preserve accountable reasoning | Any AI-assisted judicial workflow must preserve a human | technology-and-ai.html |
| `TEC-JUD-013` | Evidence authentication | AI-generated or AI-enhanced evidence must be authentica | technology-and-ai.html |
| `TEC-JUD-014` | Technical disclosure for challenge | Parties must receive sufficient technical disclosure to | technology-and-ai.html |
| `TEC-JUD-015` | Scientific validation required | Courts may not admit AI outputs as expert-like evidence | technology-and-ai.html |
| `TEC-JUD-016` | Synthetic media high-risk | Synthetic media evidence must be presumptively treated  | technology-and-ai.html |
| `TEC-JUD-017` | Preserve analysis logs | If AI is used to analyze evidence all material logs mod | technology-and-ai.html |
| `TEC-JUD-018` | Defense access to AI disclosures | If prosecutors or the state use AI systems in investiga | technology-and-ai.html |
| `TEC-JUD-019` | Defense funding for AI parity | Public defenders and defense counsel must be provided f | technology-and-ai.html |
| `TEC-JUD-020` | No AI-driven plea pressure | AI systems may not be used to pressure plea deals throu | technology-and-ai.html |
| `TEC-JUD-021` | Guard against prosecutorial AI advantage | Courts must guard against prosecutorial advantage creat | technology-and-ai.html |
| `TEC-JUD-022` | No juror profiling | AI systems may not be used to profile rank influence or | technology-and-ai.html |
| `TEC-JUD-023` | AI reconstructions must be disclosed | AI-generated reconstructions simulations or visualizati | technology-and-ai.html |
| `TEC-JUD-024` | No AI summaries to juries | Courts may not provide juries with AI-generated summari | technology-and-ai.html |
| `TEC-JUD-025` | No distortion of evidentiary record | Jury-facing use of AI must not distort the evidentiary  | technology-and-ai.html |
| `TEC-JUD-026` | Default to prohibition | AI use in courts and legal proceedings must default to  | technology-and-ai.html |
| `TEC-JUD-027` | Ban AI-generated evidence | AI-generated or AI-fabricated evidence including images | technology-and-ai.html |
| `TEC-JUD-028` | Ban AI-enhanced evidence | AI-enhanced evidence that alters interpretation content | technology-and-ai.html |
| `TEC-JUD-029` | Analytical use only | AI may be used only for analytical purposes on existing | technology-and-ai.html |
| `TEC-JUD-030` | No generative AI for evidence | Generative AI systems including large language models m | technology-and-ai.html |
| `TEC-JUD-031` | Verifiable methods only | Permitted analytical systems must use verifiable reprod | technology-and-ai.html |
| `TEC-JUD-032` | Disclose analytical AI use | Any use of AI in evidence analysis must be explicitly d | technology-and-ai.html |
| `TEC-JUD-033` | No black-box systems | Black-box AI systems that cannot be meaningfully explai | technology-and-ai.html |
| `TEC-JUD-034` | AI not expert witnesses | AI systems may not be presented as expert witnesses or  | technology-and-ai.html |
| `TEC-JUD-035` | Human experts accountable | All expert testimony must be provided by qualified huma | technology-and-ai.html |
| `TEC-JUD-036` | Disclose AI-assisted expert analysis | Human experts using AI-assisted analysis must disclose  | technology-and-ai.html |
| `TEC-JUD-037` | No AI-drafted opinions | Judges and justices may not use generative AI systems t | technology-and-ai.html |
| `TEC-JUD-038` | No AI legal reasoning | AI systems may not substitute for judicial reasoning le | technology-and-ai.html |
| `TEC-JUD-039` | Limited clerical use | AI may be used for limited clerical tasks such as docum | technology-and-ai.html |
| `TEC-JUD-040` | No AI reconstructions to juries | AI-generated reconstructions simulations or demonstrati | technology-and-ai.html |
| `TEC-JUD-041` | No AI summaries of evidence to juries | AI systems may not be used to summarize interpret or pr | technology-and-ai.html |
| `TEC-JUD-042` | No AI influence on jurors | AI systems may not be used to influence juror perceptio | technology-and-ai.html |
| `TEC-JUD-043` | Recognize AI risks | Courts must recognize that AI systems can amplify confi | technology-and-ai.html |
| `TEC-JUD-044` | Elevated scrutiny standards | Any permitted AI-assisted analysis must meet elevated s | technology-and-ai.html |
| `TEC-JUD-045` | Right to challenge AI analysis | All parties must have full rights to challenge any AI-a | technology-and-ai.html |
| `TEC-JUD-046` | Reproducibility requirement | AI-assisted analysis must be reproducible by opposing p | technology-and-ai.html |
| `TEC-JUD-047` | Preserve analysis logs | All AI-assisted evidentiary analysis must include prese | technology-and-ai.html |
| `TEC-JUD-048` | Audit access requirement | Courts and opposing parties must have access to all mat | technology-and-ai.html |
| `TEC-JUD-049` | No AI family court determinations | AI systems may not be used to determine custody visitat | technology-and-ai.html |
| `TEC-JUD-050` | No parental fitness inference | AI systems may not infer parental fitness abuse risk cr | technology-and-ai.html |
| `TEC-JUD-051` | No AI in family court recommendations | Family courts may not rely on AI-generated summaries re | technology-and-ai.html |
| `TEC-JUD-052` | Disclose family court AI use | Any AI-assisted tool used in family court administratio | technology-and-ai.html |
| `TEC-JUD-053` | No automated evictions | AI systems may not be used to automate or materially dr | technology-and-ai.html |
| `TEC-JUD-054` | No tenant risk scoring | Courts may not rely on AI-generated tenant risk scores  | technology-and-ai.html |
| `TEC-JUD-055` | Disclose housing AI use | Landlords and housing litigants using AI-assisted evide | technology-and-ai.html |
| `TEC-JUD-056` | No eviction acceleration through AI | Housing courts must not use AI systems to accelerate ca | technology-and-ai.html |
| `TEC-JUD-057` | No AI in administrative adjudication | AI systems may not independently determine outcomes in  | technology-and-ai.html |
| `TEC-JUD-058` | No opaque scoring in administrative hearings | Administrative adjudication may not rely on opaque AI s | technology-and-ai.html |
| `TEC-JUD-059` | Disclose AI in administrative proceedings | Parties in administrative proceedings have the right to | technology-and-ai.html |
| `TEC-JUD-060` | Administrative appeal rights | Administrative agencies must provide meaningful human r | technology-and-ai.html |
| `TEC-JUD-061` | No AI probation/parole decisions | AI systems may not be used to determine probation parol | technology-and-ai.html |
| `TEC-JUD-062` | No proxy-based supervision scoring | AI systems may not assign supervision risk scores based | technology-and-ai.html |
| `TEC-JUD-063` | Individualized human review required | Probation and parole decisions must be based on individ | technology-and-ai.html |
| `TEC-JUD-064` | AI to identify bias in probation | AI may be used to identify patterns of bias inconsisten | technology-and-ai.html |
| `TEC-JUD-065` | No AI fines and fees escalation | AI systems may not be used to escalate fines fees colle | technology-and-ai.html |
| `TEC-JUD-066` | No payment coercion through AI | Courts and governments may not use AI to pressure payme | technology-and-ai.html |
| `TEC-JUD-067` | No AI debt-to-punishment escalation | AI systems may not be used to convert administrative de | technology-and-ai.html |
| `TEC-JUD-068` | AI to identify predatory fine patterns | AI may be used to identify unlawful disparities or pred | technology-and-ai.html |
| `TEC-JUD-069` | AI for legal aid access | AI may be used to assist legal aid intake document navi | technology-and-ai.html |
| `TEC-JUD-070` | Disclose legal-aid AI limits | AI tools used in legal-aid contexts must clearly disclo | technology-and-ai.html |
| `TEC-JUD-071` | Public legal-aid tools must be fair | Public legal-aid AI tools must be designed for accessib | technology-and-ai.html |
| `TEC-JUD-072` | Fund public legal access tools | Governments and courts should fund public-interest lega | technology-and-ai.html |
| `TEC-JUD-073` | AI records systems must be auditable | AI systems used to classify search summarize or priorit | technology-and-ai.html |
| `TEC-JUD-074` | No unequal filing access | Court administrative AI systems may not create unequal  | technology-and-ai.html |
| `TEC-JUD-075` | Preserve record accuracy | Public court records systems using AI must preserve acc | technology-and-ai.html |
| `TEC-JUD-076` | Human override for court admin AI | Courts must maintain human override and review mechanis | technology-and-ai.html |
| `TEC-JUD-077` | AI limited to assistive functions | Where AI is permitted in judicial contexts it must be l | technology-and-ai.html |
| `TEC-JUD-078` | No credibility assessment | AI systems may not be used to assess credibility truthf | technology-and-ai.html |
| `TEC-JUD-079` | No behavioral inference in court | Behavioral biometric or speech-analysis AI tools may no | technology-and-ai.html |
| `TEC-JUD-080` | No AI alteration of police footage | AI systems may not be used to reinterpret enhance or se | technology-and-ai.html |
| `TEC-JUD-081` | Preserve full context in evidence | AI-assisted analysis of law-enforcement evidence must p | technology-and-ai.html |
| `TEC-JUD-082` | No sole-basis AI translation | AI translation or interpretation systems may not be use | technology-and-ai.html |
| `TEC-JUD-083` | Human interpreters required | Human-certified interpreters are required for critical  | technology-and-ai.html |
| `TEC-JUD-084` | Forensic AI validation required | AI systems used in forensic laboratories must meet stri | technology-and-ai.html |
| `TEC-JUD-085` | Test forensic AI systems | Forensic AI systems must be independently tested for ac | technology-and-ai.html |
| `TEC-JUD-086` | No AI reconstruction of sealed records | AI systems may not reconstruct infer or surface sealed  | technology-and-ai.html |
| `TEC-JUD-087` | Enforce record protections | Use of AI to bypass legal protections on records privac | technology-and-ai.html |
| `TEC-JUD-088` | No AI influence campaigns on juries | AI-generated content may not be used to influence juror | technology-and-ai.html |
| `TEC-JUD-089` | Mitigate public AI influence on trials | Courts must recognize and mitigate risks of AI-driven p | technology-and-ai.html |
| `TEC-JUD-090` | AI version control required | AI systems used in any permitted judicial context must  | technology-and-ai.html |
| `TEC-JUD-091` | Revalidate AI changes | Material changes to AI systems used in legal contexts m | technology-and-ai.html |
| `TEC-JUD-092` | No shift of burden or standards | Use of AI systems may not shift burden of proof evident | technology-and-ai.html |
| `TEC-JUD-093` | Transparent AI procurement | Courts and judicial systems must use transparent procur | technology-and-ai.html |
| `TEC-JUD-094` | Independent validation before deployment | AI systems may not be deployed in judicial contexts wit | technology-and-ai.html |
| `TEC-JUD-095` | Authority to suspend AI systems | Courts must maintain the authority to suspend or prohib | technology-and-ai.html |
| `TEC-JUD-096` | Party right to request suspension | Parties must have the right to request suspension of AI | technology-and-ai.html |
| `TEC-LAB-001` | Protect worker rights and dignity | AI systems in employment must not undermine worker righ | technology-and-ai.html |
| `TEC-LAB-002` | No automated employment decisions | AI systems may not make fully automated hiring firing p | technology-and-ai.html |
| `TEC-LAB-003` | No opaque candidate filtering | AI systems may not be used to filter or rank job candid | technology-and-ai.html |
| `TEC-LAB-004` | Evaluate for bias | AI systems used in employment must be evaluated and mit | technology-and-ai.html |
| `TEC-LAB-005` | Right to explanation | Applicants and employees have the right to receive mean | technology-and-ai.html |
| `TEC-LAB-006` | Ban intrusive monitoring | Ban use of AI systems for continuous intrusive monitori | technology-and-ai.html |
| `TEC-LAB-007` | No emotion inference | Ban use of AI systems to infer or monitor worker emotio | technology-and-ai.html |
| `TEC-LAB-008` | No outside-hours monitoring | Employers may not use AI systems to monitor or infer wo | technology-and-ai.html |
| `TEC-LAB-009` | No sole-basis discipline or termination | AI systems may not be used as the sole basis for discip | technology-and-ai.html |
| `TEC-LAB-010` | Transparent productivity scoring | AI-generated productivity or performance scores must be | technology-and-ai.html |
| `TEC-LAB-011` | No coercive productivity targets | AI systems may not be used to coerce workers into unsaf | technology-and-ai.html |
| `TEC-LAB-012` | Right to refuse harmful AI | Workers must have the right to refuse use of AI systems | technology-and-ai.html |
| `TEC-LAB-013` | Access to human managers | Workers must have access to human managers or decision- | technology-and-ai.html |
| `TEC-LAB-014` | Data minimization | AI systems may only collect worker data that is strictl | technology-and-ai.html |
| `TEC-LAB-015` | No data sales or repurposing | Worker data collected through AI systems may not be sol | technology-and-ai.html |
| `TEC-LAB-016` | Right to access and correct data | Workers have the right to access review and correct dat | technology-and-ai.html |
| `TEC-LAB-017` | Disclosure requirement | Employers must disclose use of AI systems in hiring mon | technology-and-ai.html |
| `TEC-LAB-018` | Regular independent audits | AI systems used in employment must be subject to regula | technology-and-ai.html |
| `TEC-LAB-019` | Documentation requirement | Employers must maintain documentation of AI system desi | technology-and-ai.html |
| `TEC-LAB-020` | Ban behavior prediction scoring | Ban AI systems that assign risk scores predicting emplo | technology-and-ai.html |
| `TEC-LAB-021` | Ban anti-union AI | Ban use of AI systems to identify monitor or suppress u | technology-and-ai.html |
| `TEC-LAB-022` | Validate personality assessments | Ban use of AI systems that infer personality traits or  | technology-and-ai.html |
| `TEC-LAB-023` | Worker role in AI deployment | Workers or their representatives must have a role in re | technology-and-ai.html |
| `TEC-LAB-024` | Collective bargaining over AI | Use of AI systems affecting working conditions must be  | technology-and-ai.html |
| `TEC-MHC-001` | AI assists not replaces clinicians | AI mental-health tools may assist but must not replace  | technology-and-ai.html |
| `TEC-MHC-002` | Prohibit manipulative AI systems | AI systems designed for emotional dependency manipulati | technology-and-ai.html |
| `TEC-MHC-003` | Evaluate for mental health harms | Platforms and AI systems must be evaluated for mental-h | technology-and-ai.html |
| `TEC-MHC-004` | Stronger protections for minors | Children and adolescents require stronger protections a | technology-and-ai.html |
| `TEC-MHC-005` | Disclosure in sensitive contexts | Users must be clearly informed when they are interactin | technology-and-ai.html |
| `TEC-MIL-001` | Meaningful human control required | Use of AI in military and intelligence contexts must pr | technology-and-ai.html |
| `TEC-MIL-002` | Ban autonomous lethal targeting | Ban AI systems that can independently select and engage | technology-and-ai.html |
| `TEC-MIL-003` | Ban AI force initiation | Ban deployment of AI systems that can initiate or escal | technology-and-ai.html |
| `TEC-MIL-004` | Ban nuclear AI | Ban use of AI systems in nuclear command control target | technology-and-ai.html |
| `TEC-MIL-005` | Ban AI target generation | Ban AI systems from generating, recommending, or priori | technology-and-ai.html |
| `TEC-MIL-005A` | No target filtering or ranking | AI systems may not be used to narrow, filter, or rank p | technology-and-ai.html |
| `TEC-MIL-006` | Identified human decision-maker | All use of lethal force involving AI systems must inclu | technology-and-ai.html |
| `TEC-MIL-007` | Logging and auditability | All AI-assisted military decisions must be logged and a | technology-and-ai.html |
| `TEC-MIL-008` | Transparency for human oversight | AI systems used in military decision-making must provid | technology-and-ai.html |
| `TEC-MIL-009` | Testing and reliability | AI systems used in military contexts must meet strict r | technology-and-ai.html |
| `TEC-MIL-010` | Ban mass intelligence fusion | Ban large-scale AI-driven intelligence surveillance sys | technology-and-ai.html |
| `TEC-MIL-011` | No profiling for targeting | Ban use of AI to profile individuals or populations for | technology-and-ai.html |
| `TEC-MIL-012` | Compliance with laws of armed conflict | All AI military systems must comply with principles of  | technology-and-ai.html |
| `TEC-MIL-013` | Clear attribution of responsibility | Responsibility for actions taken using AI systems must  | technology-and-ai.html |
| `TEC-MIL-014` | No evasion of accountability | Use of AI systems must not be used to obscure responsib | technology-and-ai.html |
| `TEC-MIL-015` | Congressional authorization required | Deployment of new classes of AI-enabled military capabi | technology-and-ai.html |
| `TEC-MIL-016` | Limits on executive authority | Executive authority may not unilaterally expand the use | technology-and-ai.html |
| `TEC-MIL-018` | Controlled testing required | AI systems intended for military use must undergo contr | technology-and-ai.html |
| `TEC-MIL-019` | No real-world testing | Ban use of real-world military operations as primary te | technology-and-ai.html |
| `TEC-MIL-021` | Contractor accountability | Private contractors developing AI for military use are  | technology-and-ai.html |
| `TEC-MIL-022` | No outsourcing of authority | Government may not outsource decision-making authority  | technology-and-ai.html |
| `TEC-MIL-023` | Export controls | Establish controls on export of high-risk military AI s | technology-and-ai.html |
| `TEC-MIL-024` | Defensive AI permitted | AI systems may be used in defensive or non-person-targe | technology-and-ai.html |
| `TEC-MIL-025` | No repurposing defensive AI | Defensive AI systems must not be repurposed or extended | technology-and-ai.html |
| `TEC-MIL-026` | AI for analysis not targeting | AI may be used for analysis classification and situatio | technology-and-ai.html |
| `TEC-MIL-027` | Ban offensive lethal AI | Ban use of AI systems in the execution of offensive let | technology-and-ai.html |
| `TEC-MIL-028` | Limited guidance use | AI systems may be used in limited weapon guidance roles | technology-and-ai.html |
| `TEC-MIL-029` | Guidance parameters strictly defined | Guidance systems must not alter expand reinterpret or s | technology-and-ai.html |
| `TEC-MIL-030` | No new target selection by guidance | Guidance systems must be incapable of selecting new tar | technology-and-ai.html |
| `TEC-MIL-031` | Human responsibility for guidance outcomes | Human operators remain fully responsible for all outcom | technology-and-ai.html |
| `TEC-MIL-032` | Defensive systems against non-human threats | AI may be used in defensive systems including missile i | technology-and-ai.html |
| `TEC-MIL-033` | Support international treaties | Promote and pursue international treaties to limit and  | technology-and-ai.html |
| `TEC-MIL-034` | Treaty goal: ban autonomous weapons | International agreements should seek to prohibit fully  | technology-and-ai.html |
| `TEC-MIL-035` | Treaty goal: ban targeting AI | International treaties should establish bans on AI syst | technology-and-ai.html |
| `TEC-MIL-036` | Treaty goal: ban nuclear AI | International treaties should restrict AI use in nuclea | technology-and-ai.html |
| `TEC-MIL-037` | Treaty mechanisms | Treaties should include transparency reporting requirem | technology-and-ai.html |
| `TEC-MIL-038` | Prevent AI arms races | International efforts should aim to prevent destabilizi | technology-and-ai.html |
| `TEC-MIL-039` | Export controls in treaties | Support international controls on export and proliferat | technology-and-ai.html |
| `TEC-MIL-040` | Strong sanctions for violations | Violations of international military-AI treaty obligati | technology-and-ai.html |
| `TEC-MIL-041` | Sanctions for prohibited systems | Sanctions for deployment or export of prohibited milita | technology-and-ai.html |
| `TEC-MIL-042` | Narrow reciprocal exceptions | If an adversary deploys prohibited military AI systems, | technology-and-ai.html |
| `TEC-MIL-043` | Temporary reciprocal measures | Any reciprocal exception to military AI prohibitions mu | technology-and-ai.html |
| `TEC-MIL-044` | Core prohibitions remain | Core prohibitions on nuclear AI control, fully autonomo | technology-and-ai.html |
| `TEC-MIL-045` | Autonomous targeting as war crime | Use of AI systems to autonomously select or engage huma | technology-and-ai.html |
| `TEC-MIL-046` | Target generation as unlawful | Deployment of AI systems that generate or recommend hum | technology-and-ai.html |
| `TEC-MIL-047` | Violations of armed conflict principles | Use of AI systems in ways that violate principles of di | technology-and-ai.html |
| `TEC-MIL-048` | Precision guidance exception | Use of AI solely for precision guidance to reduce colla | technology-and-ai.html |
| `TEC-MIL-049` | Commanders remain liable | Individuals and commanders remain legally responsible f | technology-and-ai.html |
| `TEC-MIL-050` | Dedicated cyber branch | Establish a dedicated and fully developed cyber branch  | technology-and-ai.html |
| `TEC-MIL-051` | Cyber defense mission | The cyber branch shall be responsible for defense of cr | technology-and-ai.html |
| `TEC-MIL-052` | Offensive cyber limits | Offensive cyber operations must be strictly limited aut | technology-and-ai.html |
| `TEC-MIL-053` | Minimize civilian cyber impact | Cyber operations must minimize impact on civilian infra | technology-and-ai.html |
| `TEC-MIL-054` | Cyber branch oversight | All cyber military operations are subject to oversight  | technology-and-ai.html |
| `TEC-MIL-055` | No domestic cyber surveillance | The cyber military branch may not be used for domestic  | technology-and-ai.html |
| `TEC-MIL-056` | Coordination with civilian agencies | The cyber branch must coordinate with civilian agencies | technology-and-ai.html |
| `TEC-MIL-057` | International cyber norms | The cyber branch should operate in alignment with inter | technology-and-ai.html |
| `TEC-MKT-001` | Shared algorithmic systems used to coordinate prices ac | The use of shared algorithmic systems, common pricing s | technology-and-ai.html |
| `TEC-OVR-001` | Public AI surveillance registry | Require public registration and disclosure of all gover | technology-and-ai.html |
| `TEC-OVR-002` | Regular independent audits | Require regular independent audits of all authorized go | technology-and-ai.html |
| `TEC-OVR-003` | Sunset and reauthorization | All government AI surveillance authorities and systems  | technology-and-ai.html |
| `TEC-PRV-001` | Right to access without identification | Individuals have the right to access lawful online cont | technology-and-ai.html |
| `TEC-PRV-002` | Protect anonymous use | Anonymous and pseudonymous use of the internet must be  | technology-and-ai.html |
| `TEC-SUR-002` | Ban AI mass public surveillance | Ban AI-powered mass surveillance of public spaces excep | technology-and-ai.html |
| `TEC-SUR-004` | Ban government data purchases | Government may not purchase commercially collected surv | technology-and-ai.html |
| `TEC-SUR-005` | Strict warrant requirements | Require strict warrants minimization procedures and aud | technology-and-ai.html |
| `TEC-SUR-008` | Automatic expiration | Surveillance authorities must expire automatically unle | technology-and-ai.html |
| `TEC-SUR-009` | Ban network mapping | Ban AI systems that map political social religious or a | technology-and-ai.html |
| `TEC-SUR-010` | Protect journalists and attorneys | Ban AI-enabled surveillance of journalists sources atto | technology-and-ai.html |
| `TEC-SYN-001` | Ban deceptive synthetic media | Synthetic media must not be used to deceive the public  | technology-and-ai.html |
| `TEC-SYN-002` | Ban synthetic impersonation | Ban the use of AI-generated media to impersonate a real | technology-and-ai.html |
| `TEC-SYN-003` | Ban identity verification bypass | Ban use of synthetic media to bypass identity verificat | technology-and-ai.html |
| `TEC-SYN-004` | Ban non-consensual sexual content | Ban creation and distribution of non-consensual synthet | technology-and-ai.html |
| `TEC-SYN-005` | Ban false harmful depiction | Ban synthetic media that falsely depicts a real person  | technology-and-ai.html |
| `TEC-SYN-006` | Ban political manipulation | Ban use of synthetic media in political advertising or  | technology-and-ai.html |
| `TEC-SYN-007` | Ban misleading about officials | Ban synthetic media used to materially mislead the publ | technology-and-ai.html |
| `TEC-SYN-008` | Ban coordinated deception | Ban coordinated use of synthetic media to mislead the p | technology-and-ai.html |
| `TEC-SYN-009` | Disclosure requirement | Require clear disclosure when media is substantially AI | technology-and-ai.html |
| `TEC-SYN-010` | Provenance markers required | Require AI-generated video and audio to include persist | technology-and-ai.html |
| `TEC-SYN-011` | Open-source detection | Provenance markers must be detectable using publicly av | technology-and-ai.html |
| `TEC-SYN-012` | Safeguards against removal | Developers of generative media systems must implement r | technology-and-ai.html |
| `TEC-SYN-013` | Allow parody and satire | Allow synthetic media for parody, satire, or artistic e | technology-and-ai.html |
| `TEC-SYN-014` | Allow disclosed journalism use | Allow use of synthetic media in journalism or documenta | technology-and-ai.html |
| `TEC-SYN-015` | Allow consensual use | Allow use of synthetic media depicting real individuals | technology-and-ai.html |

---

## ID mismatches (div `id` attribute ≠ `<code class="rule-id">` element)

The `<code class="rule-id">` is the authoritative policy ID.
The `id=` attribute on the div is the HTML fragment anchor and should match.
These are data integrity issues to fix before Phase 2.

**Total: 1535**

<details>
<summary>Full list (grouped by file)</summary>

### administrative-state.html (55 mismatches)

| div id | rule-id code | Title |
|--------|-------------|-------|
| `ADM-ADM-001` | `ADM-AGY-001` | Congress explicitly empowered to create agencies |
| `ADM-ADM-002` | `ADM-CHV-001` | Restore Chevron deference |
| `ADM-ADM-003` | `ADM-CON-001` | Enshrine core federal departments in the Constitut |
| `ADM-ADM-004` | `ADM-SYS-001` | agencies are legitimate constitutional instruments |
| `ADM-ADM-005` | `ADM-SYS-002` | must be strong enough to regulate complex modern |
| `ADM-ADM-006` | `ADM-SYS-003` | design must prevent both political sabotage and un |
| `ADM-ADM-007` | `ADM-ENF-001` | must have sufficient investigatory powers, subpoen |
| `ADM-ADM-008` | `ADM-ENF-002` | must be able to impose meaningful civil penalties |
| `ADM-ADM-009` | `ADM-ENF-003` | Repeated or systemic violations must trigger escal |
| `ADM-ADM-010` | `ADM-ENF-004` | Enforcement systems may not rely solely on fines |
| `ADM-ADM-011` | `ADM-TRN-001` | must publish clear public information about missio |
| `ADM-ADM-012` | `ADM-TRN-002` | must maintain public registries of major enforceme |
| `ADM-ADM-013` | `ADM-TRN-003` | Regulated entities may not use secrecy claims |
| `ADM-ADM-014` | `ADM-OVR-001` | Major agencies must have independent internal over |
| `ADM-ADM-015` | `ADM-OVR-002` | Internal oversight bodies must be protected from r |
| `ADM-ADM-016` | `ADM-OVR-003` | Findings of systemic agency failure, capture, abus |
| `ADM-ADM-017` | `ADM-CAP-001` | must be structurally insulated from regulated-indu |
| `ADM-ADM-018` | `ADM-CAP-002` | Regulated entities may not dominate advisory board |
| `ADM-ADM-019` | `ADM-CAP-003` | staff, appointees, and senior leadership must be s |
| `ADM-ADM-020` | `ADM-CAP-004` | Revolving-door restrictions must apply before and  |
| `ADM-ADM-021` | `ADM-CAP-005` | Patterned agency deference to large regulated acto |
| `ADM-ADM-022` | `ADM-ADJ-001` | adjudication systems must provide clear notice, re |
| `ADM-ADM-023` | `ADM-ADJ-002` | may not rely on opaque procedures, hidden guidance |
| `ADM-ADM-024` | `ADM-ADJ-003` | High-consequence agency decisions must be reviewab |
| `ADM-ADM-025` | `ADM-COO-001` | with overlapping jurisdiction must coordinate enfo |
| `ADM-ADM-026` | `ADM-COO-002` | Inter-agency coordination may not be used to evade |
| `ADM-ADM-027` | `ADM-FND-001` | charged with protecting rights, public safety, mar |
| `ADM-ADM-028` | `ADM-FND-002` | Core regulatory and enforcement functions may not  |
| `ADM-ADM-029` | `ADM-FND-003` | with constitutionally or statutorily guaranteed pu |
| `ADM-ADM-030` | `ADM-FND-004` | Where appropriations fail, designated critical-pro |
| `ADM-ADM-031` | `ADM-IND-001` | must be protected from arbitrary defunding, bad-fa |
| `ADM-ADM-032` | `ADM-IND-002` | leaders may not be removed, overruled, or replaced |
| `ADM-ADM-033` | `ADM-IND-003` | must retain operational independence in investigat |
| `ADM-ADM-034` | `ADM-IND-004` | Political oversight of agencies must not become po |
| `ADM-ADM-035` | `ADM-PUB-001` | rulemaking and oversight processes must include me |
| `ADM-ADM-036` | `ADM-PUB-002` | should provide accessible notice, comment tools, a |
| `ADM-ADM-037` | `ADM-RGT-001` | authority may not be exercised through arbitrary,  |
| `ADM-ADM-038` | `ADM-RGT-002` | Regulated parties and affected individuals must ha |
| `ADM-ADM-039` | `ADM-RGT-003` | process must distinguish between legitimate rights |
| `ADM-ADM-040` | `ADM-RUL-001` | must have authority to issue, revise, and clarify |
| `ADM-ADM-041` | `ADM-RUL-002` | Rulemaking must be transparent, evidence-based, an |
| `ADM-ADM-042` | `ADM-RUL-003` | must be able to issue interim, emergency |
| `ADM-ADM-043` | `ADM-RUL-004` | Adaptive rulemaking authority must include review, |
| `ADM-ADM-044` | `ADM-SCI-001` | relying on scientific, medical, technical, or econ |
| `ADM-ADM-045` | `ADM-SCI-002` | scientific and technical staff must be protected f |
| `ADM-ADM-046` | `ADM-SCI-003` | must disclose the evidentiary basis for major rule |
| `ADM-CIV-001` | `CIV-VTL-001` | Vital records obtainable at any courthouse or reco |
| `ADM-CIV-002` | `CIV-VTL-002` | No requirement to travel to the issuing courthouse |
| `ADM-CIV-003` | `CIV-VTL-003` | Vital records access includes marriage licenses, n |
| `ADM-CIV-004` | `CIV-VTL-004` | Certified vital records must be easily obtainable  |
| `ADM-CIV-005` | `CIV-VTL-005` | Mailed vital records must be sent by certified, tr |
| `ADM-CIV-006` | `ADM-CIV-001` | Career civil servants may not be reclassified as a |
| `ADM-CIV-007` | `ADM-CIV-002` | Core civil service protections must be established |
| `ADM-OIRA-001` | `ADM-OIR-001` | OIRA review must not be used to indefinitely delay |
| `ADM-OIRA-002` | `ADM-OIR-002` | OIRA cost-benefit analyses must incorporate distri |

### antitrust-and-corporate-power.html (74 mismatches)

| div id | rule-id code | Title |
|--------|-------------|-------|
| `ANT-COR-001` | `COR-FIN-001` | Ban Corporate Political Donations |
| `ANT-COR-002` | `COR-FIN-002` | Ban Super PACs |
| `ANT-COR-003` | `COR-FIN-003` | Limit Individual Donations |
| `ANT-COR-004` | `COR-FIN-004` | Limit Political Ad Spending |
| `ANT-MED-001` | `COR-CON-001` | Concentration of economic power that undermines co |
| `ANT-MED-002` | `COR-CON-002` | government has an affirmative and enforceable duty |
| `ANT-MED-003` | `COR-CON-003` | government has clear authority to break up, restru |
| `ANT-MED-004` | `COR-CON-004` | Structural remedies, including divestiture and sep |
| `ANT-MED-005` | `COR-CON-005` | Monopolies, cartels, and coordinated market contro |
| `ANT-MED-006` | `COR-CON-006` | Price fixing, market allocation, bid rigging, and  |
| `ANT-MED-007` | `COR-CON-007` | Antitrust enforcement must consider impacts on com |
| `ANT-MED-008` | `COR-CON-008` | absence of immediate price increases does not cons |
| `ANT-MED-009` | `COR-CON-009` | Firms with dominant market power are subject |
| `ANT-MED-010` | `COR-CON-010` | Dominant firms may not use control of infrastructu |
| `ANT-MED-011` | `COR-CON-011` | Firms may not evade antitrust restrictions through |
| `ANT-MED-012` | `COR-CON-012` | In cases involving dominant firms or high concentr |
| `ANT-MED-013` | `COR-CON-013` | Markets with high concentration must be continuous |
| `ANT-MED-014` | `COR-CON-014` | Antitrust enforcement authority may not be weakene |
| `ANT-MED-015` | `COR-ANT-001` | Anti-monopoly law must be strengthened to prevent  |
| `ANT-MED-016` | `COR-ANT-002` | Merger review must consider effects on prices, wag |
| `ANT-MED-017` | `COR-ANT-003` | Dominant firms may not acquire competitors, emergi |
| `ANT-MED-018` | `COR-ANT-004` | Vertical integration that allows a firm to disadva |
| `ANT-MED-019` | `COR-ANT-005` | Breakup, structural separation, forced divestiture |
| `ANT-MED-020` | `COR-ANT-006` | Anti-competitive conduct may not be excused solely |
| `ANT-MED-021` | `COR-ANT-007` | Competition enforcement must account for digital-e |
| `ANT-MED-022` | `COR-ANT-008` | Ownership concentration must be monitored and publ |
| `ANT-MED-023` | `COR-ALG-001` | Algorithmic systems may not be used to coordinate |
| `ANT-MED-024` | `COR-ALG-002` | Use of pricing algorithms in concentrated markets |
| `ANT-MED-025` | `COR-ALG-003` | Firms may not outsource anti-competitive pricing b |
| `ANT-MED-026` | `COR-MKT-001` | Markets must serve the public interest |
| `ANT-MED-027` | `COR-MKT-002` | Competition policy must protect not only price com |
| `ANT-MED-028` | `COR-MKT-003` | Corporate scale, concentration, or integration tha |
| `ANT-MED-029` | `COR-MKT-004` | Core consumer markets must not be designed around |
| `ANT-MED-030` | `COR-PEQ-001` | Private-equity and other highly leveraged ownershi |
| `ANT-MED-031` | `COR-PEQ-002` | Serial acquisitions and roll-up strategies that cr |
| `ANT-MED-032` | `COR-PEQ-003` | Firms in essential sectors may not load acquired |
| `ANT-MED-033` | `COR-PEQ-004` | Ownership structures that obscure control, liabili |
| `ANT-MED-034` | `COR-PIS-001` | Firms operating in essential sectors including hou |
| `ANT-MED-035` | `COR-PIS-002` | Heightened obligations in essential sectors includ |
| `ANT-MED-036` | `COR-PIS-003` | Essential-sector firms may not reduce quality, acc |
| `ANT-MED-037` | `COR-PIS-004` | Agricultural and food-production equipment is desi |
| `ANT-MED-038` | `COR-PIS-005` | Commercial equipment critical to small-business op |
| `ANT-MED-039` | `COR-CAP-001` | Industry may not dominate the bodies that regulate |
| `ANT-MED-040` | `COR-CAP-002` | Standard-setting, repairability scoring, platform  |
| `ANT-MED-041` | `COR-CAP-003` | Revolving-door limits should apply in major compet |
| `ANT-MED-042` | `COR-ENF-001` | Antitrust and consumer-protection enforcement agen |
| `ANT-MED-043` | `COR-ENF-002` | Enforcement agencies must have authority to impose |
| `ANT-MED-044` | `COR-ENF-003` | Repeated or willful violations of consumer-protect |
| `ANT-MED-045` | `COR-ENF-004` | Private rights of action should exist for consumer |
| `ANT-MED-046` | `COR-ENF-005` | Enforcement must not rely solely on fines as |
| `ANT-MED-047` | `COR-LAW-001` | Corporate officers, executives, and responsible in |
| `ANT-MED-048` | `COR-LAW-002` | Companies exhibiting patterns of violations must b |
| `ANT-MED-049` | `COR-LAW-003` | Corporate cultures that enable or fail to prevent |
| `ANT-MED-050` | `COR-LAW-004` | Board members and governing bodies may be held |
| `ANT-MED-051` | `COR-LAW-005` | Repeated or systemic violations must trigger escal |
| `ANT-MED-052` | `COR-LAW-006` | Regulatory frameworks must include proportional re |
| `ANT-MED-053` | `COR-AUD-001` | Corporate audits must follow standardized formats  |
| `ANT-MED-054` | `COR-AUD-002` | Both automated systems and human oversight must be |
| `ANT-MED-055` | `COR-TRN-001` | Dominant firms in essential sectors must disclose  |
| `ANT-MED-056` | `COR-TRN-002` | Standardized public reporting should exist for pro |
| `ANT-MED-057` | `COR-TRN-003` | Government should maintain publicly accessible dat |
| `ANT-MPY-001` | `COR-MPY-001` | Labor market concentration constitutes an antitrus |
| `ANT-MPY-002` | `COR-MPY-002` | Mergers that significantly concentrate employer po |
| `ANT-MPY-003` | `COR-MPY-003` | No-poach and wage-fixing agreements between compet |
| `ANT-AGF-001` | `COR-AGF-001` | Agricultural processing and food distribution conc |
| `ANT-AGF-002` | `COR-AGF-002` | Packer-controlled livestock contracts may not syst |
| `ANT-AGF-003` | `COR-AGF-003` | Seed, agricultural chemical, and farm technology c |
| `ANT-NMD-001` | `COR-NMD-001` | Further consolidation of local media ownership mus |
| `ANT-NMD-002` | `COR-NMD-002` | Digital platforms must negotiate in good faith wit |
| `ANT-NMD-003` | `COR-NMD-003` | News publishers may collectively negotiate with do |
| `ANT-PLT-001` | `COR-PLT-001` | Dominant digital platforms may not self-preference |
| `ANT-PLT-002` | `COR-PLT-002` | App store platforms with dominant market position  |
| `ANT-PLT-003` | `COR-PLT-003` | Dominant platforms must provide data portability a |
| `ANT-PLT-004` | `COR-PLT-004` | Dominant platform acquisitions of nascent competit |

### checks-and-balances.html (79 mismatches)

| div id | rule-id code | Title |
|--------|-------------|-------|
| `CHK-OVR-001` | `OVR-BRN-001` | Independent Oversight Boards for Each Branch |
| `CHK-OVR-002` | `OVR-BRN-002` | Oversight Board Independence |
| `CHK-OVR-003` | `OVR-FED-001` | Federal Independent Oversight Body |
| `CHK-OVR-004` | `OVR-FED-002` | Authority Over Federally Elected Officials |
| `CHK-OVR-005` | `OVR-FED-003` | Oversight Body Composition and Elected Component |
| `CHK-OVR-006` | `OVR-FED-004` | Subpoena and Deposition Powers |
| `CHK-OVR-007` | `OVR-FND-001` | Guaranteed Adequate Funding |
| `CHK-OVR-008` | `OVR-FND-002` | Automatic Extension if Funding Not Passed |
| `CHK-OVR-009` | `OVR-FND-003` | Automatic Extension Includes 10% Increase |
| `CHK-OVR-010` | `OVR-FND-004` | Funding Separate from Overseen Departments |
| `CHK-OVR-011` | `OVR-FND-005` | Protection from Political and External Influence |
| `CHK-OVR-012` | `OVR-JUR-001` | Jurisdiction Over State Officials |
| `CHK-OVR-013` | `OVR-JUR-002` | Jurisdiction Over Failed State Oversight |
| `CHK-OVR-014` | `OVR-STA-001` | State Oversight Boards Required |
| `CHK-OVR-015` | `OVR-STA-002` | Directly Elected Members |
| `CHK-OVR-016` | `OVR-STA-003` | Appointed Members Balance |
| `CHK-SYS-001` | `SYS-AI-001` | Prohibition on Asymmetrical AI Processes |
| `CHK-SYS-002` | `SYS-AI-002` | Independent Human Judgment Required for Material H |
| `CHK-SYS-003` | `SYS-AI-003` | Absence of AI Recommendation Not Evidence of Denia |
| `CHK-SYS-004` | `SYS-AI-004` | Equal and Timely Consideration Regardless of AI Sc |
| `CHK-SYS-005` | `SYS-AI-005` | AI Bias Detection and Mitigation |
| `CHK-SYS-006` | `SYS-AI-006` | Continuous Auditing for Bias and Disparate Impact |
| `CHK-SYS-007` | `SYS-AI-007` | Domain-Specific AI Rules |
| `CHK-SYS-008` | `SYS-FED-001` | High-Risk Systems Not Fully Centralized |
| `CHK-SYS-009` | `SYS-FED-002` | Elections Remain State/Local Administered |
| `CHK-SYS-010` | `SYS-FED-003` | Federal Standards for Elections |
| `CHK-SYS-011` | `SYS-FED-004` | Multiple Independent Oversight Layers Required |
| `CHK-SYS-012` | `SYS-FED-005` | Safeguards Against Both State and Federal Abuse |
| `CHK-SYS-013` | `SYS-GEO-001` | Geography Must Not Determine Rights Access |
| `CHK-SYS-014` | `SYS-GEO-002` | National Baseline Must Be Uniform |
| `CHK-SYS-015` | `SYS-GEO-003` | States May Not Degrade Federal Rights |
| `CHK-SYS-016` | `SYS-GEO-004` | Cross-State Access Guaranteed |
| `CHK-SYS-017` | `SYS-GEO-005` | Travel Support When Local Care Unavailable |
| `CHK-SYS-018` | `SYS-FND-001` | Platform as Policy and Strategy |
| `CHK-SYS-019` | `SYS-FND-002` | Restore Checks and Balances |
| `CHK-SYS-020` | `SYS-FND-003` | Modernize the Constitution |
| `CHK-SYS-021` | `SYS-FND-004` | Guarantee Universal Equal Rights |
| `CHK-SYS-022` | `SYS-FND-005` | Address Economic Inequality Structurally |
| `CHK-SYS-023` | `SYS-FND-006` | Address Modern Systemic Issues |
| `CHK-SYS-024` | `SYS-FND-007` | Make Technology Work for People |
| `CHK-SYS-025` | `SYS-FND-008` | Movement Not Left vs Right |
| `CHK-SYS-026` | `SYS-FND-009` | Movement Accessible to Everyone |
| `CHK-SYS-027` | `SYS-FND-010` | Includes Communication and Coalition Strategy |
| `CHK-SYS-028` | `SYS-FND-011` | Not a Political Party |
| `CHK-SYS-029` | `SYS-FND-012` | Origin Tied to Post-Trump Instability Concerns |
| `CHK-SYS-030` | `SYS-FND-013` | Address Ignored Working-Class Issues |
| `CHK-SYS-031` | `SYS-FND-014` | Address Rising Costs and Declining Quality |
| `CHK-SYS-032` | `SYS-FND-015` | Address Elite Detachment |
| `CHK-SYS-033` | `SYS-FND-016` | Address Wealth Concentration |
| `CHK-SYS-034` | `SYS-FND-017` | Address Declining Institutional Trust |
| `CHK-SYS-035` | `SYS-FND-018` | Core Values: Truth, Equality, Freedom, Dignity |
| `CHK-SYS-036` | `SYS-RUL-001` | System Rules Ensure Completeness and Alignment |
| `CHK-SYS-037` | `SYS-LAW-001` | Laws and system rules must be enforceable, clear |
| `CHK-SYS-038` | `SYS-LAW-002` | Laws should be written with definite terms, explic |
| `CHK-SYS-039` | `SYS-LAW-003` | Flexibility clauses must be bounded, reviewable, a |
| `CHK-SYS-040` | `SYS-REG-001` | Regulation must protect safety, quality, fairness |
| `CHK-SYS-041` | `SYS-REG-002` | Regulatory systems must distinguish between protec |
| `CHK-SYS-042` | `SYS-REG-003` | Removal or modification of regulations must be evi |
| `CHK-SYS-043` | `SYS-REG-004` | Regulations that protect safety, habitability, env |
| `CHK-SYS-044` | `SYS-REG-005` | Regulatory processes may not be structured to crea |
| `CHK-SYS-045` | `SYS-REG-006` | Regulatory systems must include safeguards against |
| `CHK-SYS-046` | `SYS-REG-007` | Regulation must be enforceable in practice; under- |
| `CHK-SYS-047` | `SYS-REG-008` | Regulatory frameworks must be periodically reviewe |
| `CHK-SYS-048` | `SYS-REG-009` | Mandatory compliance with oversight body findings  |
| `CHK-WPR-001` | `SYS-WPR-001` | Enforce the War Powers Resolution — automatic fund |
| `CHK-WPR-002` | `SYS-WPR-002` | Repeal and replace open-ended AUMFs with time-limi |
| `CHK-WPR-003` | `SYS-WPR-003` | Strict limits on domestic deployment of military f |
| `CHK-EMG-001` | `SYS-EMG-001` | Automatic 90-day sunset on national emergency decl |
| `CHK-EMG-002` | `SYS-EMG-002` | Prohibit use of emergency declarations to circumve |
| `CHK-EMG-003` | `SYS-EMG-003` | Fast-track judicial review for emergency declarati |
| `CHK-IMP-001` | `SYS-IMP-001` | Enforce the Impoundment Control Act — criminal pen |
| `CHK-IMP-002` | `SYS-IMP-002` | Automatic continuing resolutions — end government  |
| `CHK-AGN-001` | `SYS-AGY-001` | Restore removal-for-cause protection for heads of  |
| `CHK-AGN-002` | `SYS-AGY-002` | Civil service anti-politicization — prohibit recla |
| `CHK-AGN-003` | `SYS-AGY-003` | Protect state sovereignty — establish anti-preempt |
| `CHK-ACC-001` | `GOV-ACC-002` | Ban political firings |
| `CHK-ACC-002` | `GOV-SHD-001` | No pay during government shutdown |
| `CHK-ACC-003` | `GOV-SHD-002` | Permanent pay loss after 30 days shutdown |
| `CHK-WAR-001` | `GOV-WAR-002` | Require declared wars |

### consumer-rights.html (78 mismatches)

| div id | rule-id code | Title |
|--------|-------------|-------|
| `CON-CON-001` | `CON-GEN-001` | Prohibit deceptive and exploitative business pract |
| `CON-CON-002` | `CON-GEN-002` | Ban confusion-based and friction-based business mo |
| `CON-CON-003` | `CON-GEN-003` | Consumers have clear enforceable rights across key |
| `CON-CON-004` | `CON-GEN-004` | Adhesion contracts may not waive fundamental consu |
| `CON-CON-005` | `CON-GEN-005` | Restrict or ban mandatory arbitration in consumer  |
| `CON-CON-006` | `CON-GEN-006` | Fine print cannot substitute for substantive fairn |
| `CON-CON-007` | `CON-FEE-001` | Prohibit hidden fees, drip pricing, and junk fees |
| `CON-CON-008` | `CON-FEE-002` | Full upfront total price disclosure required |
| `CON-CON-009` | `CON-FEE-003` | Prohibit confusing billing and negative-option ren |
| `CON-CON-010` | `CON-FEE-004` | Easy subscription cancellation through same enroll |
| `CON-CON-011` | `CON-SUB-001` | Subscriptions may not replace feasible ownership |
| `CON-CON-012` | `CON-SUB-002` | Disclose ownership versus subscription status clea |
| `CON-CON-013` | `CON-SUB-003` | No degrading owned products to force subscription  |
| `CON-CON-014` | `CON-SUB-004` | Core device functions may not require subscription |
| `CON-CON-015` | `CON-SUB-005` | Legitimate ongoing services may use subscription m |
| `CON-CON-016` | `CON-SUB-006` | Disclose owned versus service-based features at po |
| `CON-CON-017` | `CON-OWN-001` | Purchase conveys full access to core functionality |
| `CON-CON-018` | `CON-OWN-002` | Ownership may not be converted to subscription dep |
| `CON-CON-019` | `CON-AUTO-002` | Core vehicle functions may not be subscription-loc |
| `CON-CON-020` | `CON-AUTO-003` | Hardware-enabled features at time of sale remain a |
| `CON-CON-021` | `CON-ELC-002` | Computing hardware performance may not be subscrip |
| `CON-CON-022` | `CON-ELC-003` | Basic device functions may not require subscriptio |
| `CON-CON-023` | `CON-CNS-001` | No required proprietary consumables where alternat |
| `CON-CON-024` | `CON-CNS-002` | No degrading functionality when third-party consum |
| `CON-CON-025` | `CON-FTR-001` | May not artificially disable available hardware fe |
| `CON-CON-026` | `CON-FTR-002` | Software feature restrictions require legitimate j |
| `CON-CON-027` | `CON-TRN-004` | Standardized disclosure of included versus paid fe |
| `CON-CON-028` | `CON-TRN-005` | Post-sale paywalling of previously included featur |
| `CON-CON-029` | `CON-ENF-001` | Violations require restoration, restitution, and p |
| `CON-CON-030` | `CON-ENF-002` | Private right of action for unlawful post-purchase |
| `CON-CON-031` | `CON-QLT-001` | Products must meet minimum durability and quality  |
| `CON-CON-032` | `CON-QLT-002` | Marketing claims must match actual product quality |
| `CON-CON-033` | `CON-QLT-003` | Systematic low-quality manufacturing practices sub |
| `CON-CON-034` | `CON-QLT-004` | Essential household goods need stronger baseline q |
| `CON-CON-035` | `CON-WAR-001` | Warranties must be understandable, fair, and enfor |
| `CON-CON-036` | `CON-WAR-002` | Manufacturers must disclose support timelines at p |
| `CON-CON-037` | `CON-WAR-003` | Early support withdrawal must trigger remedies |
| `CON-RPR-001` | `RPR-SYS-001` | Right to repair owned products without unreasonabl |
| `CON-RPR-002` | `RPR-SYS-002` | Manufacturers must provide repair access at fair a |
| `CON-RPR-003` | `RPR-SYS-003` | Products may not be designed to prevent repair |
| `CON-RPR-004` | `RPR-DES-001` | Products must be designed for reasonable disassemb |
| `CON-RPR-005` | `RPR-DES-002` | Wear components must be individually replaceable |
| `CON-RPR-006` | `RPR-DES-003` | Manufacturers must publish repairability scores |
| `CON-RPR-007` | `RPR-LIFE-001` | Products must meet minimum durability standards by |
| `CON-RPR-008` | `RPR-LIFE-002` | Manufacturers must support products for a minimum  |
| `CON-RPR-009` | `RPR-LIFE-003` | Artificial lifespan limitation through software is |
| `CON-RPR-010` | `RPR-AUTO-001` | Vehicles must provide independent diagnostic and r |
| `CON-RPR-011` | `RPR-AUTO-002` | Repair rights apply to all vehicles including agri |
| `CON-RPR-012` | `RPR-ELC-001` | Consumer electronics must allow component-level re |
| `CON-RPR-013` | `RPR-ENF-001` | Regulators may compel access to repair materials |
| `CON-RPR-014` | `RPR-ENF-002` | Violations carry penalties, private right of actio |
| `CON-RPR-015` | `RPR-ENF-003` | Safety claims blocking repair must be specifically |
| `CON-RPR-016` | `RPR-ENF-004` | Repair standards cover vehicles, electronics, farm |
| `CON-RPR-017` | `RPR-ENF-005` | Public procurement favors repairable and sustainab |
| `CON-RPR-018` | `RPR-AGR-001` | Full diagnostic access required for agricultural e |
| `CON-RPR-019` | `RPR-AGR-002` | Dealer-only repair access restriction is prohibite |
| `CON-RPR-020` | `RPR-AGR-003` | Software locks may not prevent lawful equipment re |
| `CON-RPR-021` | `RPR-AGR-004` | Unauthorized repair may not trigger equipment degr |
| `CON-RPR-022` | `RPR-AGR-005` | Time-sensitive equipment must be repairable withou |
| `CON-RPR-023` | `RPR-AGR-006` | Prevent repair bottlenecks during critical agricul |
| `CON-RPR-024` | `RPR-AGR-007` | Parts, tools, and manuals available at fair and re |
| `CON-RPR-025` | `RPR-AGR-008` | Equipment ownership may not be reduced to a licens |
| `CON-RPR-026` | `RPR-AGR-009` | Contractual repair restrictions on owned equipment |
| `CON-RPR-027` | `RPR-AGR-010` | No exclusive repair market control through technic |
| `CON-RPR-028` | `RPR-AGR-011` | Agricultural repair violations trigger accelerated |
| `CON-RPR-029` | `RPR-COM-001` | Repair rights apply fully to commercial equipment |
| `CON-RPR-030` | `RPR-COM-002` | Manufacturers may not restrict diagnostic informat |
| `CON-RPR-031` | `RPR-COM-003` | Error systems may not obscure faults or mislead op |
| `CON-RPR-032` | `RPR-COM-004` | Authorized-only repair restrictions are prohibited |
| `CON-RPR-033` | `RPR-COM-005` | Software-enforced service monopolies are prohibite |
| `CON-RPR-034` | `RPR-COM-006` | Equipment design may not predictably cause extende |
| `CON-RPR-035` | `RPR-COM-007` | Recurring failure states due to design lockout sub |
| `CON-RPR-036` | `RPR-COM-008` | Manufacturers may not obscure repair pathways or c |
| `CON-RPR-037` | `RPR-COM-009` | Third-party repair tools and interfaces may not be |
| `CON-RPR-038` | `RPR-COM-010` | Manufacturers may not interfere with third-party r |
| `CON-RPR-039` | `RPR-ANTI-001` | No restriction of repair to authorized service net |
| `CON-RPR-040` | `RPR-ANTI-002` | DRM and component pairing systems blocking repair  |
| `CON-RPR-041` | `RPR-ANTI-003` | Third-party repair may not void warranty unless ca |

### education.html (222 mismatches)

| div id | rule-id code | Title |
|--------|-------------|-------|
| `EDU-MISC-001` | `EDU-SYS-001` | Education systems must provide universal access to |
| `EDU-MISC-002` | `EDU-SYS-002` | Educational opportunity may not be determined by w |
| `EDU-MISC-003` | `EDU-SYS-003` | Education systems must be designed for long-term h |
| `EDU-MISC-004` | `EDU-SYS-004` | Access to education that is necessary for economic |
| `EDU-MISC-005` | `EDU-SYS-005` | Education is a public good and must be |
| `EDU-MISC-006` | `EDU-SYS-006` | Public education funding must be used to strengthe |
| `EDU-MISC-007` | `EDU-ACC-001` | All individuals must have access to free, high-qua |
| `EDU-MISC-008` | `EDU-ACC-002` | Access to higher education, vocational training, a |
| `EDU-MISC-009` | `EDU-ACC-003` | Educational systems must actively correct disparit |
| `EDU-MISC-010` | `EDU-ACC-004` | Students with disabilities must receive full acces |
| `EDU-MISC-011` | `EDU-ACC-005` | Students must have access to safe and reliable |
| `EDU-MISC-012` | `EDU-ACC-006` | Transportation systems may not be structured in wa |
| `EDU-MISC-013` | `EDU-ACC-007` | Publicly funded education must be subject to trans |
| `EDU-MISC-014` | `EDU-ACC-008` | Education systems receiving public funding may not |
| `EDU-MISC-015` | `EDU-FND-001` | Education funding systems may not rely on local |
| `EDU-MISC-016` | `EDU-FND-002` | Public funding must ensure baseline parity of educ |
| `EDU-MISC-017` | `EDU-FND-003` | Schools serving higher-need populations must recei |
| `EDU-MISC-018` | `EDU-QLT-001` | Education systems must provide high-quality instru |
| `EDU-MISC-019` | `EDU-QLT-002` | Curriculum must include literacy, numeracy, scienc |
| `EDU-MISC-020` | `EDU-QLT-003` | Education must prepare students for real-world ski |
| `EDU-MISC-021` | `EDU-QLT-004` | Education systems must avoid overreliance on stand |
| `EDU-MISC-022` | `EDU-WRK-001` | Teachers must be compensated at levels that reflec |
| `EDU-MISC-023` | `EDU-WRK-002` | Teachers must have access to training, continuing  |
| `EDU-MISC-024` | `EDU-WRK-003` | Teacher workloads must be reasonable and may not |
| `EDU-MISC-025` | `EDU-WRK-004` | Educators must have professional autonomy in instr |
| `EDU-MISC-026` | `EDU-STU-001` | Schools must support student physical, mental, and |
| `EDU-MISC-027` | `EDU-STU-002` | Students must have access to counseling, mental he |
| `EDU-MISC-028` | `EDU-STU-003` | Disciplinary systems must be fair, proportional, a |
| `EDU-MISC-029` | `EDU-EXT-001` | Educational systems may not be structured primaril |
| `EDU-MISC-030` | `EDU-EXT-002` | Predatory practices in student lending, for-profit |
| `EDU-MISC-031` | `EDU-EXT-003` | Students may not be burdened with excessive debt |
| `EDU-MISC-032` | `EDU-VOC-001` | Education systems must include strong vocational,  |
| `EDU-MISC-033` | `EDU-VOC-002` | Vocational and technical education must be treated |
| `EDU-MISC-034` | `EDU-VOC-003` | Partnerships between education and industry must p |
| `EDU-MISC-035` | `EDU-HED-001` | Higher education must be financially accessible an |
| `EDU-MISC-036` | `EDU-HED-002` | Public investment in higher education must priorit |
| `EDU-MISC-037` | `EDU-HED-003` | Student loan systems must include strong borrower  |
| `EDU-MISC-038` | `EDU-HED-004` | Public community colleges, technical schools, and  |
| `EDU-MISC-039` | `EDU-HED-005` | Tuition-free access must include core instructiona |
| `EDU-MISC-040` | `EDU-HED-006` | Tuition-free programs must include part-time stude |
| `EDU-MISC-041` | `EDU-HED-007` | Trade, vocational, and certification programs must |
| `EDU-MISC-042` | `EDU-HED-008` | Public investment in community and technical educa |
| `EDU-MISC-043` | `EDU-HED-010` | Higher education must function as a public-interes |
| `EDU-MISC-044` | `EDU-HED-011` | Admissions processes must be fair, transparent, an |
| `EDU-MISC-045` | `EDU-HED-012` | Institutions may not use admissions practices that |
| `EDU-MISC-046` | `EDU-HED-013` | Standardized testing may not be used as the |
| `EDU-MISC-047` | `EDU-HED-014` | Institutions must provide multiple pathways to adm |
| `EDU-MISC-048` | `EDU-HED-015` | Institutions receiving public funding must be acco |
| `EDU-MISC-049` | `EDU-HED-016` | Persistent failure to meet baseline outcome standa |
| `EDU-MISC-050` | `EDU-HED-017` | Institutions may not rely on enrollment growth or |
| `EDU-MISC-051` | `EDU-HED-018` | Institutions must demonstrate responsible use of t |
| `EDU-MISC-052` | `EDU-HED-019` | Excessive administrative cost growth that does not |
| `EDU-MISC-053` | `EDU-HED-020` | Tuition increases must be justified, transparent,  |
| `EDU-MISC-054` | `EDU-HED-021` | Institutions must maintain stable, fairly compensa |
| `EDU-MISC-055` | `EDU-HED-022` | Faculty must have academic freedom in research, te |
| `EDU-MISC-056` | `EDU-HED-023` | Academic labor practices must align with broader l |
| `EDU-MISC-057` | `EDU-HED-024` | Institutions must maintain strong standards for ac |
| `EDU-MISC-058` | `EDU-HED-025` | Research funding and partnerships may not compromi |
| `EDU-MISC-059` | `EDU-HED-026` | Conflicts of interest in research, funding, or pub |
| `EDU-MISC-060` | `EDU-HED-027` | Accreditation systems must ensure educational qual |
| `EDU-MISC-061` | `EDU-HED-028` | Accreditation must be based on outcomes, quality,  |
| `EDU-MISC-062` | `EDU-HED-029` | New or alternative education providers must have p |
| `EDU-MISC-063` | `EDU-HED-030` | Students must have rights to fair treatment, due |
| `EDU-MISC-064` | `EDU-HED-031` | Institutions must provide clear information on cos |
| `EDU-MISC-065` | `EDU-HED-032` | Students may not be misled about job placement |
| `EDU-MISC-066` | `EDU-HED-033` | Institutions must maintain safe campus environment |
| `EDU-MISC-067` | `EDU-HED-034` | Reporting systems must be accessible, fair, and no |
| `EDU-MISC-068` | `EDU-HED-035` | Students must be able to transfer credits between |
| `EDU-MISC-069` | `EDU-HED-036` | Public systems must establish standardized credit  |
| `EDU-MISC-070` | `EDU-HED-037` | Prior learning, work experience, and non-tradition |
| `EDU-MISC-071` | `EDU-HED-038` | Public higher education institutions must serve br |
| `EDU-MISC-072` | `EDU-HED-039` | Institutions may not prioritize rankings, exclusiv |
| `EDU-MISC-073` | `EDU-HED-040` | Higher education may not function primarily as a |
| `EDU-MISC-074` | `EDU-HED-041` | Financial models that depend on unsustainable stud |
| `EDU-MISC-075` | `EDU-LIF-001` | Individuals must have access to lifelong learning, |
| `EDU-MISC-076` | `EDU-LIF-002` | Public systems must support workers transitioning  |
| `EDU-MISC-077` | `EDU-CIV-001` | Education must include strong civic education cove |
| `EDU-MISC-078` | `EDU-CIV-002` | Students must be equipped to critically evaluate i |
| `EDU-MISC-079` | `EDU-CIV-003` | Education systems may not be used for political |
| `EDU-MISC-080` | `EDU-GOV-001` | Education systems must be transparent, accountable |
| `EDU-MISC-081` | `EDU-GOV-002` | Policies must be evaluated based on student outcom |
| `EDU-MISC-082` | `EDU-GOV-003` | Communities must have meaningful input into educat |
| `EDU-MISC-083` | `EDU-GOV-004` | Education systems must track and publicly report d |
| `EDU-MISC-084` | `EDU-GOV-005` | Persistent patterns of segregation or inequity mus |
| `EDU-MISC-085` | `EDU-GOV-006` | Policies that worsen segregation or inequity must  |
| `EDU-MISC-086` | `EDU-DEBT-001` | Broad federal student loan forgiveness must be imp |
| `EDU-MISC-087` | `EDU-DEBT-002` | Debt relief must prioritize borrowers most affecte |
| `EDU-MISC-088` | `EDU-DEBT-003` | Student loan systems must be restructured to preve |
| `EDU-MISC-089` | `EDU-DEBT-004` | Interest structures, repayment systems, and loan s |
| `EDU-MISC-090` | `EDU-DEBT-005` | Institutions with consistently poor student outcom |
| `EDU-MISC-091` | `EDU-DEBT-006` | Educational institutions may not shift financial r |
| `EDU-MISC-092` | `EDU-DEBT-007` | Predatory student lending practices, including dec |
| `EDU-MISC-093` | `EDU-DEBT-008` | Loan servicing must be regulated to ensure accurat |
| `EDU-MISC-094` | `EDU-DEBT-009` | Public education funding models should reduce reli |
| `EDU-MISC-095` | `EDU-DEBT-010` | Any alternative financing models must not replicat |
| `EDU-MISC-096` | `EDU-SEC-001` | Public education must remain religiously neutral,  |
| `EDU-MISC-097` | `EDU-SEC-002` | Public schools and their employees may not engage |
| `EDU-MISC-098` | `EDU-SEC-003` | School policies, curricula, and official activitie |
| `EDU-MISC-099` | `EDU-SEC-004` | Public resources, instructional time, and school-s |
| `EDU-MISC-100` | `EDU-SEC-005` | Students retain the right to individual religious  |
| `EDU-MISC-101` | `EDU-SEC-006` | Schools must protect students from discrimination  |
| `EDU-MISC-102` | `EDU-SEC-007` | Violations of religious neutrality or evidence-bas |
| `EDU-MISC-103` | `EDU-SEC-008` | Students and families must have accessible mechani |
| `EDU-MISC-104` | `EDU-SCI-001` | Science curricula in public education must be base |
| `EDU-MISC-105` | `EDU-SCI-002` | Non-scientific belief systems, including religious |
| `EDU-MISC-106` | `EDU-SCI-003` | Topics such as religion, philosophy, and cultural  |
| `EDU-MISC-107` | `EDU-SCI-004` | Concepts such as “Intelligent Design” or similar f |
| `EDU-MISC-108` | `EDU-STR-001` | Education systems must not structurally produce or |
| `EDU-MISC-109` | `EDU-STR-002` | School assignment systems must balance community a |
| `EDU-MISC-110` | `EDU-ZON-001` | School district boundaries and attendance zones ma |
| `EDU-MISC-111` | `EDU-ZON-002` | States must periodically review and adjust distric |
| `EDU-MISC-112` | `EDU-ZON-003` | Where local district structures produce persistent |
| `EDU-MISC-113` | `EDU-ZON-004` | Regional systems must include fair resource alloca |
| `EDU-MISC-114` | `EDU-INT-001` | Education systems must use lawful, evidence-based  |
| `EDU-MISC-115` | `EDU-INT-002` | School assignment systems may incorporate multiple |
| `EDU-MISC-116` | `EDU-INT-003` | Tracking, gifted programs, and selective admission |
| `EDU-MISC-117` | `EDU-CHO-001` | Public school choice systems must be designed to |
| `EDU-MISC-118` | `EDU-CHO-002` | Charter and alternative public schools must meet t |
| `EDU-MISC-119` | `EDU-CHO-003` | School choice policies may not be used to |
| `EDU-MISC-120` | `EDU-PRV-001` | Public funds used for private education must be |
| `EDU-MISC-121` | `EDU-PRV-002` | Voucher or subsidy programs may not enable segrega |
| `EDU-MISC-122` | `EDU-PRV-003` | Policies that functionally replicate vouchers, inc |
| `EDU-MISC-123` | `EDU-PRV-004` | Public education resources, including funding, fac |
| `EDU-MISC-124` | `EDU-AI-001` | AI systems used in education must preserve enough |
| `EDU-MISC-125` | `EDU-AI-002` | High-impact educational AI must undergo pre-deploy |
| `EDU-MISC-126` | `EDU-AI-003` | Educational AI may not silently shift from assisti |
| `EDU-MISC-127` | `EDU-DAT-001` | Student data, behavior, and learning activity must |
| `EDU-MISC-128` | `EDU-DAT-002` | Schools and educational systems may collect only t |
| `EDU-MISC-129` | `EDU-DAT-003` | Collection of biometric, behavioral, psychological |
| `EDU-MISC-130` | `EDU-DAT-004` | Student data may not be sold, traded, licensed |
| `EDU-MISC-131` | `EDU-DAT-005` | Educational technology providers may not use stude |
| `EDU-MISC-132` | `EDU-DAT-006` | Schools may not implement pervasive or continuous  |
| `EDU-MISC-133` | `EDU-DAT-007` | AI or automated systems may not be used |
| `EDU-MISC-134` | `EDU-DAT-008` | Students and families must have the right to |
| `EDU-MISC-135` | `EDU-DAT-009` | Students and families must be informed of what |
| `EDU-MISC-136` | `EDU-DAT-010` | Violations of student data protections must trigge |
| `EDU-MISC-137` | `EDU-DAT-011` | Educational systems must maintain audit logs and o |
| `EDU-MISC-138` | `EDU-ECE-001` | Early childhood education and childcare are essent |
| `EDU-MISC-139` | `EDU-ECE-002` | Access to high-quality early childhood education a |
| `EDU-MISC-140` | `EDU-ECE-003` | Universal access to high-quality pre-kindergarten  |
| `EDU-MISC-141` | `EDU-ECE-004` | Affordable, high-quality childcare must be broadly |
| `EDU-MISC-142` | `EDU-ECE-005` | Access systems must include full-time, part-time,  |
| `EDU-MISC-143` | `EDU-ECE-006` | Early childhood programs must meet strong developm |
| `EDU-MISC-144` | `EDU-ECE-007` | Early childhood education must prioritize language |
| `EDU-MISC-145` | `EDU-ECE-008` | Early childhood systems may not rely on low-qualit |
| `EDU-MISC-146` | `EDU-ECE-009` | Early childhood educators and childcare workers mu |
| `EDU-MISC-147` | `EDU-ECE-010` | Early childhood staffing systems must include trai |
| `EDU-MISC-148` | `EDU-ECE-011` | Childcare and early education systems may not rely |
| `EDU-MISC-149` | `EDU-ECE-012` | Early childhood systems must actively correct disp |
| `EDU-MISC-150` | `EDU-ECE-013` | Families in rural areas, lower-income communities, |
| `EDU-MISC-151` | `EDU-ECE-014` | Early childhood systems must include strong inclus |
| `EDU-MISC-152` | `EDU-ECE-015` | Childcare and early childhood systems must be desi |
| `EDU-MISC-153` | `EDU-ECE-016` | Families may not be forced out of work |
| `EDU-MISC-154` | `EDU-ECE-017` | Public funding models must reduce childcare costs  |
| `EDU-MISC-155` | `EDU-ECE-018` | Early childhood and childcare funding must priorit |
| `EDU-MISC-156` | `EDU-ECE-019` | Public funding may not be used to sustain |
| `EDU-MISC-157` | `EDU-ECE-020` | Governments must directly build, support, or coord |
| `EDU-MISC-158` | `EDU-ECE-021` | Early childhood providers must be subject to stron |
| `EDU-MISC-159` | `EDU-ECE-022` | Families must have access to clear information abo |
| `EDU-MISC-160` | `EDU-ECE-023` | Repeated safety, neglect, abuse, or quality failur |
| `EDU-MISC-161` | `EDU-ECE-024` | Early childhood systems should be coordinated with |
| `EDU-MISC-162` | `EDU-ECE-025` | Pre-K and childcare systems must include screening |
| `EDU-MISC-163` | `EDU-ECE-026` | Childcare and early childhood systems may not be |
| `EDU-MISC-164` | `EDU-ECE-027` | Families and providers must have clear, navigable  |
| `EDU-MISC-165` | `EDU-ECE-028` | Early childhood systems must be evaluated based on |
| `EDU-MISC-166` | `EDU-ECE-029` | Early childhood policy must recognize long-term de |
| `EDU-MISC-167` | `EDU-ECE-030` | Universal access to high-quality childcare must be |
| `EDU-MISC-168` | `EDU-ECE-031` | Childcare services must be provided at no cost |
| `EDU-MISC-169` | `EDU-ECE-031` | ALT — Childcare costs must be capped relative to h |
| `EDU-MISC-170` | `EDU-ECE-032` | Governments must ensure sufficient childcare capac |
| `EDU-MISC-171` | `EDU-ECE-033` | Where private markets fail to provide sufficient c |
| `EDU-MISC-172` | `EDU-ECE-034` | Childcare systems must provide hours and schedulin |
| `EDU-MISC-173` | `EDU-ECE-035` | Childcare access may not be restricted to limited |
| `EDU-MISC-174` | `EDU-ECE-036` | Universal childcare systems may not exclude childr |
| `EDU-MISC-175` | `EDU-ECE-037` | Universal childcare systems must maintain quality, |
| `EDU-MISC-176` | `EDU-SPD-001` | Children and students with disabilities have a rig |
| `EDU-MISC-177` | `EDU-SPD-002` | Special education rights may not be weakened by |
| `EDU-MISC-178` | `EDU-SPD-003` | Disability-related educational access must be trea |
| `EDU-MISC-179` | `EDU-SPD-004` | Schools must identify, evaluate, and support stude |
| `EDU-MISC-180` | `EDU-SPD-005` | Evaluation systems may not rely on delay, denial |
| `EDU-MISC-181` | `EDU-SPD-006` | Students must have access to re-evaluation and upd |
| `EDU-MISC-182` | `EDU-SPD-007` | Families must have clear rights to request evaluat |
| `EDU-MISC-183` | `EDU-SPD-008` | Students with disabilities must receive individual |
| `EDU-MISC-184` | `EDU-SPD-009` | Individualized education plans and equivalent supp |
| `EDU-MISC-185` | `EDU-SPD-010` | Schools may not offer generic, under-scoped, or mi |
| `EDU-MISC-186` | `EDU-SPD-011` | Accommodations, therapies, assistive technology, a |
| `EDU-MISC-187` | `EDU-SPD-012` | Students with disabilities must be educated in inc |
| `EDU-MISC-188` | `EDU-SPD-013` | Separate placements may be used only where clearly |
| `EDU-MISC-189` | `EDU-SPD-014` | Inclusion policy must not become a pretext for |
| `EDU-MISC-190` | `EDU-SPD-015` | Schools and education systems must maintain suffic |
| `EDU-MISC-191` | `EDU-SPD-016` | Staffing shortages may not be used as justificatio |
| `EDU-MISC-192` | `EDU-SPD-017` | Special-education personnel must receive strong tr |
| `EDU-MISC-193` | `EDU-SPD-018` | Families must have meaningful participation rights |
| `EDU-MISC-194` | `EDU-SPD-019` | Schools must provide families with clear explanati |
| `EDU-MISC-195` | `EDU-SPD-020` | Families must have access to advocacy, translation |
| `EDU-MISC-196` | `EDU-SPD-021` | Retaliation against families for asserting disabil |
| `EDU-MISC-197` | `EDU-SPD-022` | Special-education rights must be enforceable throu |
| `EDU-MISC-198` | `EDU-SPD-023` | Dispute-resolution systems may not be structured t |
| `EDU-MISC-199` | `EDU-SPD-024` | Where schools fail to provide required services, r |
| `EDU-MISC-200` | `EDU-SPD-025` | Repeated or systemic noncompliance with disability |
| `EDU-MISC-201` | `EDU-SPD-026` | Students with disabilities may not be disproportio |
| `EDU-MISC-202` | `EDU-SPD-027` | Disciplinary systems must account for disability,  |
| `EDU-MISC-203` | `EDU-SPD-028` | Seclusion, restraint, and related coercive practic |
| `EDU-MISC-204` | `EDU-SPD-029` | Educational materials, platforms, facilities, and  |
| `EDU-MISC-205` | `EDU-SPD-030` | Students who need assistive technology, accessible |
| `EDU-MISC-206` | `EDU-SPD-031` | Digital education systems and educational technolo |
| `EDU-MISC-207` | `EDU-SPD-032` | Special-education systems must monitor and correct |
| `EDU-MISC-208` | `EDU-SPD-033` | Disability rights in education apply equally to st |
| `EDU-MISC-209` | `EDU-SPD-034` | Special-education systems must include transition  |
| `EDU-MISC-210` | `EDU-SPD-035` | Transition services may not be treated as optional |
| `EDU-MISC-211` | `EDU-SPD-036` | Education systems must collect and publish standar |
| `EDU-MISC-212` | `EDU-SPD-037` | Special-education policy must be evaluated on real |
| `EDU-MISC-213` | `EDU-HSG-001` | Education policy must account for the relationship |
| `EDU-MISC-214` | `EDU-HSG-002` | Governments must coordinate housing and education  |
| `EDU-MISC-215` | `EDU-PUB-001` | Governments must ensure that all public schools me |
| `EDU-MISC-216` | `EDU-PUB-002` | Public education systems must be continuously eval |
| `EDU-MISC-217` | `EDU-PUB-003` | Public education must include diverse program offe |
| `EDU-MISC-218` | `EDU-VCH-001` | Public funds may not be used to subsidize |
| `EDU-MISC-219` | `EDU-VCH-002` | Education policy must prioritize strengthening pub |
| `EDU-MISC-220` | `EDU-VCH-003` | Limited exceptions may be permitted where necessar |
| `EDU-MISC-221` | `EDU-FIN-001` | EDU|FIN|Student loan debt forgiveness or large-sca |
| `EDU-MISC-222` | `EDU-STD-001` | EDU|STD|Education standards must include protectio |

### elections-and-representation.html (8 mismatches)

| div id | rule-id code | Title |
|--------|-------------|-------|
| `ELE-REP-001` | `ELE-FIN-001` | Equal campaign funding system |
| `ELE-REP-002` | `ELE-FIN-002` | Eliminate donation imbalance |
| `ELE-REP-003` | `ELE-FIN-003` | DISCLOSE Act — mandate real-time disclosure of all |
| `ELE-REP-004` | `ELE-PAR-001` | Remove two-party structural protections |
| `ELE-REP-005` | `ELE-REP-001` | Abolish Electoral College |
| `ELE-REP-006` | `ELE-REP-002` | National ballot initiatives |
| `ELE-REP-007` | `ELE-REP-003` | Territories get House representation |
| `ELE-REP-008` | `ELE-REP-004` | DC and Puerto Rico statehood — end taxation withou |

### environment-and-agriculture.html (83 mismatches)

| div id | rule-id code | Title |
|--------|-------------|-------|
| `ENV-AGR-001` | `AGR-REG-001` | Promote regenerative agriculture and sustainable f |
| `ENV-EDU-001` | `EDU-FIN-001` | Student loan debt forgiveness or large-scale restr |
| `ENV-EDU-002` | `EDU-STD-001` | Education standards must include protections again |
| `ENV-ENV-001` | `ENV-BIO-001` | Protect and restore migratory patterns for animals |
| `ENV-ENV-002` | `ENV-BIO-002` | Require wildlife crossings including bridges tunne |
| `ENV-ENV-003` | `ENV-BIO-003` | Protect wildlife, habitats, and national parks fro |
| `ENV-ENV-004` | `ENV-BIO-004` | Require urban green spaces with public access in c |
| `ENV-ENV-005` | `ENV-COR-001` | Establish general anti-greenwashing standards proh |
| `ENV-ENV-006` | `ENV-COR-002` | Require standardized verifiable environmental repo |
| `ENV-ENV-007` | `ENV-POL-001` | Establish stronger national standards to reduce an |
| `ENV-ENV-008` | `ENV-POL-002` | Establish stronger national standards to reduce an |
| `ENV-ENV-009` | `ENV-SPC-001` | Establish rules for orbital sanitation and removal |
| `ENV-ENV-010` | `ENV-SPC-002` | Require stronger regulation of private satellite d |
| `ENV-ENV-011` | `ENV-SPC-003` | Private satellite systems must meet environmental  |
| `ENV-LAB-001` | `LAB-WRK-001` | Establish a standard 4-day 32-hour work week witho |
| `ENV-LAB-002` | `LAB-WRK-002` | Productivity gains from AI and automation must ben |
| `ENV-LAB-003` | `LAB-WRK-003` | Guarantee overtime pay protections for all workers |
| `ENV-LAB-004` | `ENV-SYS-001` | Waste reduction, recyclability, repairability, and |
| `ENV-LAB-005` | `ENV-CLN-001` | Environmental policy must include active cleanup a |
| `ENV-LAB-006` | `ENV-CLN-002` | Polluters and responsible entities must bear the c |
| `ENV-LAB-007` | `ENV-CLN-003` | Liability rules for environmental contamination mu |
| `ENV-LAB-008` | `ENV-CLN-004` | Governments must have authority and dedicated fund |
| `ENV-LAB-009` | `ENV-CLN-005` | Cleanup funding mechanisms should include dedicate |
| `ENV-LAB-010` | `ENV-CLN-006` | Federal, state, and local governments must coordin |
| `ENV-LAB-011` | `ENV-CLN-007` | Environmental cleanup programs must prioritize are |
| `ENV-LAB-012` | `ENV-CLN-008` | Public agencies must fund research, monitoring, an |
| `ENV-LAB-013` | `ENV-CLN-009` | Cleanup and remediation standards must address per |
| `ENV-LAB-014` | `ENV-CLN-010` | Contaminated industrial, commercial, and waste sit |
| `ENV-LAB-015` | `ENV-CLN-011` | Brownfield and contaminated-site policy should pri |
| `ENV-LAB-016` | `ENV-CLN-012` | Cleanup policy must include restoration of habitat |
| `ENV-LAB-017` | `ENV-CLN-013` | Environmental restoration should prioritize biodiv |
| `ENV-LAB-018` | `ENV-CLN-014` | Communities affected by environmental contaminatio |
| `ENV-LAB-019` | `ENV-CLN-015` | Cleanup progress, contamination data, and remediat |
| `ENV-LAB-020` | `ENV-CLN-016` | Cleanup obligations may not be delayed indefinitel |
| `ENV-LAB-021` | `ENV-CLN-017` | Repeated failure to remediate known contamination  |
| `ENV-LAB-022` | `ENV-AUD-001` | Corporations must file standardized environmental  |
| `ENV-LAB-023` | `ENV-AUD-002` | Audits must include water use, emissions, pollutan |
| `ENV-LAB-024` | `ENV-AUD-003` | Audits must include both internal reporting and mu |
| `ENV-LAB-025` | `ENV-AUD-004` | Auditors, including individuals, are criminally li |
| `ENV-LAB-026` | `ENV-AUD-005` | Collusion, conspiracy, or coordinated fraud in env |
| `ENV-LAB-027` | `ENV-EPR-001` | Producers are responsible for the full lifecycle |
| `ENV-LAB-028` | `ENV-EPR-002` | Producers must fund and participate in systems |
| `ENV-LAB-029` | `ENV-EPR-003` | Products that are difficult to recycle, hazardous |
| `ENV-LAB-030` | `ENV-ESC-001` | Waste systems must be designed to prevent material |
| `ENV-LAB-031` | `ENV-ESC-002` | Entities responsible for production, transport, or |
| `ENV-LAB-032` | `ENV-ESC-003` | Release of plastics, microplastics, synthetic mate |
| `ENV-LAB-033` | `ENV-IND-001` | Industrial processes must minimize waste output an |
| `ENV-LAB-034` | `ENV-IND-002` | Facilities must monitor, report, and mitigate wast |
| `ENV-LAB-035` | `ENV-INF-001` | Waste management infrastructure must prevent leaka |
| `ENV-LAB-036` | `ENV-INF-002` | Landfills, transfer stations, and waste facilities |
| `ENV-LAB-037` | `ENV-INF-003` | Stormwater, wastewater, and drainage systems must  |
| `ENV-LAB-038` | `ENV-PKG-001` | Excessive packaging and non-essential materials mu |
| `ENV-LAB-039` | `ENV-PKG-002` | Reusable, refillable, or minimal packaging systems |
| `ENV-LAB-040` | `ENV-PLS-001` | Production and use of single-use plastics and non- |
| `ENV-LAB-041` | `ENV-PLS-002` | Microplastic generation from products, manufacturi |
| `ENV-LAB-042` | `ENV-PLS-003` | Synthetic materials that persist in ecosystems wit |
| `ENV-LAB-043` | `ENV-REC-001` | Recycling systems must be expanded, standardized,  |
| `ENV-LAB-044` | `ENV-REC-002` | Recycling infrastructure must be accessible, consi |
| `ENV-LAB-045` | `ENV-REC-003` | Materials placed into the market must be compatibl |
| `ENV-LAB-046` | `ENV-TRN-001` | Governments must track and publish data on waste |
| `ENV-LAB-047` | `ENV-TRN-002` | High-risk materials and sectors must be subject |
| `ENV-LAB-048` | `ENV-WST-001` | Waste generation must be minimized at the source |
| `ENV-LAB-049` | `ENV-DES-001` | Products and packaging must be designed for recycl |
| `ENV-LAB-050` | `ENV-DES-002` | Use of composite, bonded, or mixed materials that |
| `ENV-LAB-051` | `ENV-ENF-001` | Entities responsible for environmental contaminati |
| `ENV-LAB-052` | `ENV-ENF-002` | Repeated or large-scale violations of waste contai |
| `ENV-LAB-053` | `ENV-AI-001` | AI used in infrastructure, energy, water, transpor |
| `ENV-LAB-054` | `EWT-LIF-001` | Manufacturers are responsible for the full lifecyc |
| `ENV-LAB-055` | `EWT-LIF-002` | Producers must provide accessible take-back, recyc |
| `ENV-LAB-056` | `EWT-LIF-003` | Products may not be designed in ways that |
| `ENV-LAB-057` | `EWT-SUP-001` | Withdrawal of software support may not render hard |
| `ENV-LAB-058` | `EWT-SUP-002` | Devices must retain baseline usability after end-o |
| `ENV-ENV-012` | `ENV-REG-001` | Environmental Protection Agency must be constituti |
| `ENV-ENV-013` | `ENV-REG-002` | Baseline environmental protections must include li |
| `ENV-ENV-014` | `ENV-REG-003` | Carbon, water, and environmental offsets may not b |
| `ENV-EWT-001` | `EWT-SYS-001` | Products must be designed, manufactured, and suppo |
| `ENV-EWT-002` | `EWT-SYS-002` | Anti-waste, repairability, and anti-lock-in requir |
| `ENV-EWT-003` | `EWT-DES-001` | Products must be designed for long-term use, inclu |
| `ENV-EWT-004` | `EWT-DES-002` | Use of non-replaceable components in high-failure  |
| `ENV-EWT-005` | `EWT-TRN-001` | Products must disclose expected lifespan, support  |
| `ENV-EWT-006` | `EWT-WST-001` | Rapid product replacement cycles that drive unnece |
| `ENV-EWT-007` | `EWT-WST-002` | Marketing practices that encourage premature repla |
| `ENV-BIO-001` | `ENV-BIO-003` | Protect wildlife habitats and national parks from  |

### equal-justice-and-policing.html (31 mismatches)

| div id | rule-id code | Title |
|--------|-------------|-------|
| `JUS-WIT-006` | `JUS-DAT-001` | Criminal justice systems must collect and publish  |
| `JUS-WIT-007` | `JUS-DAT-002` | Data must be disaggregated to detect bias systemic |
| `JUS-WIT-008` | `JUS-DAT-003` | Public access to justice-system data must be free |
| `JUS-WIT-009` | `JUS-ERR-001` | Mechanisms must exist to identify correct and reme |
| `JUS-WIT-010` | `JUS-ERR-002` | Discovery of systemic error patterns must trigger  |
| `JUS-WIT-011` | `JUS-ERR-003` | Individuals wrongfully convicted must receive comp |
| `JUS-WIT-012` | `JUS-ERR-004` | People wrongfully convicted are entitled to compen |
| `JUS-WIT-013` | `JUS-ERR-005` | Compensation for wrongful conviction must increase |
| `JUS-WIT-014` | `JUS-ERR-006` | In cases of malicious, vindictive, or politically  |
| `JUS-WIT-015` | `JUS-ERR-007` | Wrongful-conviction remedies should include compen |
| `JUS-WIT-016` | `JUS-ETH-001` | Prosecutors and regulators must disclose conflicts |
| `JUS-WIT-017` | `JUS-ETH-002` | Cooling-off periods apply before and after public  |
| `JUS-WIT-018` | `JUS-PLB-001` | Plea bargaining systems may not be structured |
| `JUS-WIT-019` | `JUS-PLB-002` | Defendants must have access to all relevant eviden |
| `JUS-WIT-020` | `JUS-PLB-003` | Plea agreements must be reviewed for fairness |
| `JUS-WIT-021` | `JUS-PLB-004` | differential between plea offers and post-trial se |
| `JUS-WIT-022` | `JUS-PLB-005` | Defendants must receive full discovery and a minim |
| `JUS-WIT-023` | `JUS-PLB-006` | Courts must review pleas for fairness, proportiona |
| `JUS-WIT-024` | `JUS-PTL-001` | Monetary bail systems that condition pretrial libe |
| `JUS-WIT-025` | `JUS-PTL-002` | Pretrial conditions must be time-limited, reviewab |
| `JUS-WIT-026` | `JUS-SNT-001` | Sentencing must follow transparent, evidence-based |
| `JUS-WIT-027` | `JUS-SNT-002` | Sentencing data must be publicly reported and disa |
| `JUS-WIT-028` | `JUS-SNT-003` | Ability to pay may not reduce custodial accountabi |
| `JUS-WIT-029` | `JUS-SOL-001` | Statutes of limitations for violent assault sexual |
| `JUS-WIT-030` | `JUS-SOL-002` | Legal frameworks must allow reopening or continuat |
| `JUS-WIT-031` | `JUS-SOL-003` | Limitations rules must not function to shield perp |
| `JUS-WIT-032` | `JUS-TRN-001` | Ex parte communications with judges or prosecutors |
| `JUS-WIT-033` | `JUS-TRN-002` | Material meetings between defense and prosecutors  |
| `JUS-WIT-034` | `JUS-WHT-001` | Enforcement agencies must maintain specialized uni |
| `JUS-WIT-035` | `JUS-WHT-002` | Statutes of limitations for complex financial crim |
| `JUS-WIT-036` | `JUS-WHT-003` | Whistleblower protections and incentives must be r |

### executive-power.html (149 mismatches)

| div id | rule-id code | Title |
|--------|-------------|-------|
| `EXP-ACC-001` | `GOV-ACC-001` | President subject to law |
| `EXP-ACC-002` | `GOV-ACC-002` | Protect civil servants and oversight officials fro |
| `EXP-ACC-003` | `GOV-ACC-003` | Ban executive kill lists |
| `EXP-ACC-004` | `GOV-SHD-001` | No pay during government shutdown |
| `EXP-ACC-005` | `GOV-SHD-002` | Permanent pay loss after 30 days shutdown |
| `EXP-DIV-001` | `GOV-DIV-001` | Mandatory divestment enforcement |
| `EXP-EMR-001` | `GOV-EMR-001` | Time limits on executive actions |
| `EXP-EXO-001` | `GOV-EXO-001` | Limit executive orders to emergencies |
| `EXP-PDN-001` | `GOV-PDN-001` | Restrict pardon power |
| `EXP-REC-001` | `GOV-REC-001` | Constitutionalize presidential records |
| `EXP-WAR-001` | `GOV-WAR-001` | Ban open-ended AUMFs |
| `EXP-WAR-002` | `GOV-WAR-002` | Require declared wars |
| `EXP-WAR-003` | `GOV-WAR-003` | Limit military authority |
| `EXP-WAR-004` | `EXE-SYS-001` | Executive power shall be distributed across multip |
| `EXP-WAR-005` | `EXE-SYS-002` | executive branch shall consist of three primary of |
| `EXP-WAR-006` | `EXE-SYS-003` | All executive powers must be explicitly assigned |
| `EXP-WAR-007` | `EXE-SYS-004` | No executive authority may be exercised based |
| `EXP-WAR-008` | `EXE-SYS-005` | Executive design must minimize personalism, preven |
| `EXP-WAR-009` | `EXE-SYS-006` | Executive office titles and structures must be des |
| `EXP-WAR-010` | `EXE-SYS-007` | Head of Government may also be designated |
| `EXP-WAR-011` | `EXE-SYS-008` | Deputy Head of Government may be designated |
| `EXP-WAR-012` | `EXE-SYS-009` | Election cycles for executive offices must be stru |
| `EXP-WAR-013` | `EXE-SYS-010` | Staggered elections must not create persistent leg |
| `EXP-WAR-014` | `EXE-SYS-011` | Executive offices with overlapping timeframes must |
| `EXP-WAR-015` | `EXE-SYS-012` | Executive offices within the same functional lane |
| `EXP-WAR-016` | `EXE-SYS-013` | Staggered executive elections must reduce the risk |
| `EXP-WAR-017` | `EXE-PRES-001` | President shall serve as head of state |
| `EXP-WAR-018` | `EXE-PRES-002` | President shall retain limited veto, assent, and r |
| `EXP-WAR-019` | `EXE-PRES-003` | President’s role as commander-in-chief shall be li |
| `EXP-WAR-020` | `EXE-PRES-004` | President shall not exercise primary authority ove |
| `EXP-WAR-021` | `EXE-PRES-005` | President may participate in high-level diplomatic |
| `EXP-WAR-022` | `EXE-PRES-006` | Emergency powers exercised by the President must r |
| `EXP-WAR-023` | `EXE-VP-001` | Vice President shall be directly elected and hold |
| `EXP-WAR-024` | `EXE-VP-001` | vice president must be directly elected rather tha |
| `EXP-WAR-025` | `EXE-VP-002` | Vice President shall serve as primary continuity o |
| `EXP-WAR-026` | `EXE-VP-002` | vice presidency must have constitutionally defined |
| `EXP-WAR-027` | `EXE-VP-003` | Vice President shall participate in defined execut |
| `EXP-WAR-028` | `EXE-VP-003` | vice president’s authority and responsibilities mu |
| `EXP-WAR-029` | `EXE-VP-004` | Vice President shall have defined interbranch coor |
| `EXP-WAR-030` | `EXE-VP-004` | vice president may be assigned defined constitutio |
| `EXP-WAR-031` | `EXE-VP-005` | Direct election of the vice president must be |
| `EXP-WAR-032` | `EXE-VP-005` | Vice President shall not be a purely ceremonial |
| `EXP-WAR-033` | `EXE-VP-006` | Vice President’s authority must be structured to s |
| `EXP-WAR-034` | `EXE-VP-006` | vice president must hold constitutionally specifie |
| `EXP-WAR-035` | `EXE-VP-007` | Vice President shall be directly elected |
| `EXP-WAR-036` | `EXE-VP-008` | Vice President’s term must align with continuity |
| `EXP-WAR-037` | `EXE-VP-009` | Vice President shall have no routine authority |
| `EXP-WAR-038` | `EXE-VP-010` | Vice President may participate in executive confli |
| `EXP-WAR-039` | `EXE-HOG-001` | Head of Government shall be established as |
| `EXP-WAR-040` | `EXE-HOG-001` | head-of-government office, whether styled prime mi |
| `EXP-WAR-041` | `EXE-HOG-002` | head-of-state office, whether styled president or  |
| `EXP-WAR-042` | `EXE-HOG-002` | Head of Government shall oversee executive agencie |
| `EXP-WAR-043` | `EXE-HOG-003` | Executive design must prevent ambiguous overlap be |
| `EXP-WAR-044` | `EXE-HOG-003` | Head of Government shall be responsible for execut |
| `EXP-WAR-045` | `EXE-HOG-004` | Head of Government shall not derive authority from |
| `EXP-WAR-046` | `EXE-HOG-004` | head of government is the primary officer |
| `EXP-WAR-047` | `EXE-HOG-005` | method of selection and removal of the Head |
| `EXP-WAR-048` | `EXE-HOG-006` | Head of Government may be subject to legislative |
| `EXP-WAR-049` | `EXE-HOG-007` | Head of Government may be supported |
| `EXP-WAR-050` | `EXE-HOG-008` | Deputy Head of Government shall act under |
| `EXP-WAR-051` | `EXE-HOG-009` | Deputy Head of Government shall assume the duties |
| `EXP-WAR-052` | `EXE-HOG-010` | role of Deputy Head of Government must be |
| `EXP-WAR-053` | `EXE-HOG-011` | Deputy Head of Government shall not exercise indep |
| `EXP-WAR-054` | `EXE-HOG-012` | offices of Vice President and Deputy Head |
| `EXP-WAR-055` | `EXE-HOG-013` | Deputy Head of Government may be directly elected |
| `EXP-WAR-056` | `EXE-HOG-013` | Head of Government shall be nominated |
| `EXP-WAR-057` | `EXE-HOG-014` | Confirmation procedures must evaluate competence,  |
| `EXP-WAR-058` | `EXE-HOG-014` | term of the Deputy Head of Government |
| `EXP-WAR-059` | `EXE-HOG-015` | Head of Government may be removed through defined |
| `EXP-WAR-060` | `EXE-HOG-016` | Removal mechanisms must prevent arbitrary dismissa |
| `EXP-WAR-061` | `EXE-HOG-017` | Removal procedures must not allow indefinite reten |
| `EXP-WAR-062` | `EXE-HOG-018` | Head of Government shall be accountable for execut |
| `EXP-WAR-063` | `EXE-HOG-019` | Head of Government shall have primary authority ov |
| `EXP-WAR-064` | `EXE-HOG-020` | Cabinet officers shall be operationally accountabl |
| `EXP-WAR-065` | `EXE-HOG-021` | Conflicts between the President and Head of Govern |
| `EXP-WAR-066` | `EXE-HOG-022` | Head of Government shall be directly elected |
| `EXP-WAR-067` | `EXE-HOG-023` | Elections for the Head of Government shall occur |
| `EXP-WAR-068` | `EXE-HOG-024` | Head of Government shall serve a fixed term |
| `EXP-WAR-069` | `EXE-HOG-025` | term length of the Head of Government |
| `EXP-WAR-070` | `EXE-HOG-026` | Head of Government may not be removed unilaterally |
| `EXP-WAR-071` | `EXE-HOG-027` | Head of Government may be removed |
| `EXP-WAR-072` | `EXE-HOG-028` | Removal of the Head of Government must require |
| `EXP-WAR-073` | `EXE-HOG-029` | President may initiate formal review of the Head |
| `EXP-WAR-074` | `EXE-HOG-030` | In cases of severe executive deadlock, the Preside |
| `EXP-WAR-075` | `EXE-HOG-031` | Deputy Head of Government shall assume the duties |
| `EXP-WAR-076` | `EXE-HOG-032` | Temporary assumption of duties by the Deputy Head |
| `EXP-WAR-077` | `EXE-HOG-033` | Where the office of Head of Government becomes |
| `EXP-WAR-078` | `EXE-HOG-034` | If the legislature fails to designate a successor |
| `EXP-WAR-079` | `EXE-POW-001` | Emergency, military, administrative, and appointme |
| `EXP-WAR-080` | `EXE-POW-002` | Any executive action with significant national imp |
| `EXP-WAR-081` | `EXE-POW-003` | Executive authority may not be expanded through cu |
| `EXP-WAR-082` | `EXE-POW-004` | State/Continuity lane shall retain authority over  |
| `EXP-WAR-083` | `EXE-POW-005` | Authority between the two executive lanes must be |
| `EXP-WAR-084` | `EXE-25A-001` | Twenty-Fifth Amendment or successor constitutional |
| `EXP-WAR-085` | `EXE-25A-001` | constitutional framework governing executive incap |
| `EXP-WAR-086` | `EXE-25A-002` | Executive incapacity rules must be clear, enforcea |
| `EXP-WAR-087` | `EXE-25A-002` | Incapacity determinations must include defined rol |
| `EXP-WAR-088` | `EXE-25A-003` | Temporary transfer of authority, contested incapac |
| `EXP-WAR-089` | `EXE-25A-003` | Temporary transfer of power, contested incapacity, |
| `EXP-WAR-090` | `EXE-25A-004` | Incapacity and succession rules must separately ad |
| `EXP-WAR-091` | `EXE-25A-004` | Succession rules must specify transitions for Pres |
| `EXP-WAR-092` | `EXE-25A-005` | No single actor may unilaterally determine executi |
| `EXP-WAR-093` | `EXE-25A-006` | Succession and incapacity rules must separately de |
| `EXP-WAR-094` | `EXE-25A-007` | Succession chains must prevent ambiguity, overlapp |
| `EXP-WAR-095` | `EXE-25A-008` | Succession and incapacity rules must account for i |
| `EXP-WAR-096` | `EXE-25A-009` | Temporary transfer of authority must preserve cont |
| `EXP-WAR-097` | `EXE-25A-010` | Succession and incapacity rules must preserve cont |
| `EXP-WAR-098` | `EXE-25A-011` | Temporary transfer of authority must maintain stab |
| `EXP-WAR-099` | `EXE-25A-012` | Incapacity procedures for the President, Vice Pres |
| `EXP-WAR-100` | `EXE-25A-013` | Incapacity determinations must include medical, pr |
| `EXP-WAR-101` | `EXE-25A-014` | Succession within each executive lane must be auto |
| `EXP-WAR-102` | `EXE-25A-015` | Cross-lane succession may occur only under express |
| `EXP-WAR-103` | `EXE-CAB-001` | Cabinet appointment systems should be reworked to  |
| `EXP-WAR-104` | `EXE-CAB-001` | Cabinet officers shall not be appointed solely |
| `EXP-WAR-105` | `EXE-CAB-002` | Cabinet formation shall prioritize expertise, comp |
| `EXP-WAR-106` | `EXE-CAB-002` | Cabinet officers should be subject to stronger qua |
| `EXP-WAR-107` | `EXE-CAB-003` | Appointment mechanisms for major executive offices |
| `EXP-WAR-108` | `EXE-CAB-003` | Critical cabinet and national-governance offices m |
| `EXP-WAR-109` | `EXE-CAB-004` | Appointment design for major executive departments |
| `EXP-WAR-110` | `EXE-CAB-004` | Cabinet officers shall be accountable to the Head |
| `EXP-WAR-111` | `EXE-CAB-005` | Executive appointment systems must prevent capture |
| `EXP-WAR-112` | `EXE-CAB-005` | process for selecting cabinet officers must not al |
| `EXP-WAR-113` | `EXE-CAB-006` | Constitutionally established or high-risk executiv |
| `EXP-WAR-114` | `EXE-GRD-001` | Constitutional redesign of the executive must be t |
| `EXP-WAR-115` | `EXE-GRD-001` | executive system must be evaluated against risks |
| `EXP-WAR-116` | `EXE-GRD-002` | Constitutional design must include explicit mechan |
| `EXP-WAR-117` | `EXE-GRD-003` | Executive authority must remain subject to legisla |
| `EXP-WAR-118` | `EXE-GRD-004` | Executive design must ensure that no more than |
| `EXP-WAR-119` | `EXE-GRD-005` | executive system must include explicit tie-breakin |
| `EXP-WAR-120` | `EXE-GRD-006` | Systems with multiple directly elected executive o |
| `EXP-WAR-121` | `EXE-GRD-007` | No executive office may claim superior democratic  |
| `EXP-WAR-122` | `EXE-GRD-008` | Systems with staggered executive elections must in |
| `EXP-WAR-123` | `EXE-GRD-009` | No executive office may claim electoral mandate as |
| `EXP-WAR-124` | `EXE-GRD-010` | executive system must be stress-tested against sce |
| `EXP-WAR-125` | `EXE-GRD-011` | Where stress testing reveals ambiguity, constituti |
| `EXP-TRN-001` | `EXE-TRN-001` | Presidential transition cooperation made a legal o |
| `EXP-TRN-002` | `EXE-TRN-002` | Real-time preservation of presidential records — a |
| `EXP-TRN-003` | `EXE-TRN-003` | Continuity of government — clear operational succe |
| `EXP-ACT-001` | `EXE-ACT-001` | Strict 30-day limit on acting officers in Senate-c |
| `EXP-ACT-002` | `EXE-ACT-002` | Limit recess appointments to genuine recesses — cl |
| `EXP-ACT-003` | `EXE-ACT-003` | Restrict acting officials from exercising final au |
| `EXP-IMM-001` | `EXE-IMM-001` | Legislatively define narrow, bounded presidential  |
| `EXP-IMM-002` | `EXE-IMM-002` | Constitutional amendment to explicitly prohibit pr |
| `EXP-IMM-003` | `EXE-IMM-003` | Toll the statute of limitations for crimes committ |
| `EXP-CLS-001` | `EXE-CLS-001` | Codify the prohibition on classifying information  |
| `EXP-CLS-002` | `EXE-CLS-002` | Automatic declassification at 25 years with mandat |
| `EXP-CLS-003` | `EXE-CLS-003` | Criminal penalties for unlawful removal or retenti |
| `EXP-STF-001` | `EXE-STF-001` | Mandatory disclosure of all White House staff, adv |
| `EXP-STF-002` | `EXE-STF-002` | Require career security clearance process for Whit |

### foreign-policy.html (16 mismatches)

| div id | rule-id code | Title |
|--------|-------------|-------|
| `FPL-BRN-001` | `OVR-BRN-001` | Each branch of government and major constitutional |
| `FPL-BRN-002` | `OVR-BRN-002` | Oversight boards must be independent from the bodi |
| `FPL-FED-001` | `OVR-FED-001` | Establish a federal independent oversight and inve |
| `FPL-FED-002` | `OVR-FED-002` | Federal oversight body has authority to investigat |
| `FPL-FED-003` | `OVR-FED-003` | Federal oversight body includes one elected member |
| `FPL-FED-004` | `OVR-FED-004` | Federal oversight body has subpoena and deposition |
| `FPL-FND-001` | `OVR-FND-001` | Funding for oversight and investigation bodies mus |
| `FPL-FND-002` | `OVR-FND-002` | If funding is not passed oversight bodies automati |
| `FPL-FND-003` | `OVR-FND-003` | Automatic funding extension includes a 10 percent  |
| `FPL-FND-004` | `OVR-FND-004` | Oversight funding must be separate from the depart |
| `FPL-FND-005` | `OVR-FND-005` | Oversight funding must be protected from political |
| `FPL-JUR-001` | `OVR-JUR-001` | Federal oversight body may investigate governors a |
| `FPL-JUR-002` | `OVR-JUR-002` | Federal oversight body may investigate state overs |
| `FPL-STA-001` | `OVR-STA-001` | Each state must establish its own independent over |
| `FPL-STA-002` | `OVR-STA-002` | State oversight boards include directly elected me |
| `FPL-STA-003` | `OVR-STA-003` | State oversight boards include members appointed b |

### gun-policy.html (2 mismatches)

| div id | rule-id code | Title |
|--------|-------------|-------|
| `GUN-JUS-001` | `JUS-POL-006` | Ban police automatic weapons |
| `GUN-JUS-002` | `JUS-POL-007` | Ban police weapons of war |

### healthcare.html (59 mismatches)

| div id | rule-id code | Title |
|--------|-------------|-------|
| `HLT-AI-008` | `HLT-AI-007A` | Independent clinical judgment required |
| `HLT-AI-009` | `HLT-AI-007B` | AI for approval only, not denial |
| `HLT-AI-010` | `HLT-AI-007C` | Prior human review for denials |
| `HLT-AI-011` | `HLT-AI-007D` | Absence of AI approval not grounds for denial |
| `HLT-AI-012` | `HLT-AI-007E` | Independent evaluation required for denials |
| `HLT-AI-013` | `HLT-AI-007F` | No systemic bias from AI prioritization |
| `HLT-AI-014` | `HLT-AI-007G` | Equal human consideration for non-AI-flagged cases |
| `HLT-AI-015` | `HLT-AI-008` | No opaque triage decisions |
| `HLT-AI-016` | `HLT-AI-009` | AI may not prioritize cost over outcomes |
| `HLT-AI-017` | `HLT-AI-010` | Access to explanations and appeals |
| `HLT-AI-018` | `HLT-AI-011` | Right to human care |
| `HLT-AI-019` | `HLT-AI-012` | Informed consent and opt-out |
| `HLT-AI-020` | `HLT-AI-013` | Strict data protections |
| `HLT-AI-021` | `HLT-AI-014` | No commercial data exploitation |
| `HLT-AI-022` | `HLT-AI-015` | Training data ethical standards |
| `HLT-AI-023` | `HLT-AI-016` | Fail-safe design |
| `HLT-AI-024` | `HLT-AI-017` | No unwarranted certainty |
| `HLT-AI-025` | `HLT-AI-018` | Bias evaluation and mitigation |
| `HLT-AI-026` | `HLT-AI-019` | No disparity worsening |
| `HLT-AI-027` | `HLT-AI-020` | AI for research acceleration |
| `HLT-AI-028` | `HLT-AI-021` | Research funding for neglected conditions |
| `HLT-AI-029` | `HLT-AI-022` | Priority for underfunded diseases |
| `HLT-AI-030` | `HLT-AI-023` | Science-based AI policy |
| `HLT-AI-031` | `HLT-AI-024` | Safe AI integration |
| `HLT-AI-032` | `HLT-AI-025` | Interoperability with privacy protections |
| `HLT-COV-004` | `HLT-COV-005` | Tighter denial limits |
| `HLT-COV-005` | `HLT-COV-006` | Overhaul insurance to reduce denials |
| `HLT-COV-006` | `HLT-COV-007` | Faster coverage decision timelines |
| `HLT-COV-007` | `HLT-COV-008` | Expedited appeal processes |
| `HLT-COV-008` | `HLT-COV-009` | Increase required coverage |
| `HLT-COV-009` | `HLT-COV-010` | Protect pre-existing condition bans |
| `HLT-COV-010` | `HLT-COV-011` | Expand coverage for under-covered conditions |
| `HLT-COV-011` | `HLT-COV-012` | Require mental healthcare coverage |
| `HLT-COV-012` | `HLT-COV-013` | Psychedelic therapy coverage |
| `HLT-COV-013` | `HLT-COV-014` | Nationwide in-network care |
| `HLT-COV-014` | `HLT-COV-015` | Expand HSA-style tools |
| `HLT-COV-015` | `HLT-COV-016` | Ban high-deductible-only plans |
| `HLT-COV-016` | `HLT-COV-017` | Employers pay all premiums |
| `HLT-COV-017` | `HLT-COV-018` | Fair coverage processes |
| `HLT-COV-018` | `HLT-COV-019` | Clear standards for denials |
| `HLT-COV-019` | `HLT-COV-020` | Public reporting of denial rates |
| `HLT-COV-020` | `HLT-COV-021` | Penalties for repeated unjustified denials |
| `HLT-COV-021` | `HLT-COV-022` | Mandatory care floor |
| `HLT-COV-022` | `HLT-COV-023` | No vague exclusions |
| `HLT-COV-023` | `HLT-COV-024` | Clear language and pro-access interpretation |
| `HLT-COV-024` | `HLT-COV-025` | Evidence-based coverage inclusion |
| `HLT-COV-025` | `HLT-COV-026` | Permanent pre-existing condition protections |
| `HLT-COV-026` | `HLT-COV-027` | No indirect pre-existing condition exclusion |
| `HLT-COV-027` | `HLT-COV-028` | Expand historically under-covered conditions |
| `HLT-COV-028` | `HLT-COV-029` | Mental health parity |
| `HLT-COV-029` | `HLT-COV-030` | No mental health access discrimination |
| `HLT-COV-030` | `HLT-COV-031` | Emerging evidence-based therapies |
| `HLT-COV-031` | `HLT-COV-032` | Preventative care coverage mandate |
| `HLT-COV-032` | `HLT-COV-033` | Weight management as covered care |
| `HLT-COV-033` | `HLT-COV-034` | Preventative mental wellness visits |
| `HLT-COV-034` | `HLT-COV-035` | Cosmetic and reconstructive procedures for documen |
| `HLT-COV-035` | `HLT-COV-036` | Chronic pain as a covered primary condition |
| `HLT-COV-036` | `HLT-COV-037` | Functional medicine and quality-of-life care for c |
| `HLT-HLT-001` | `HLT-JUS-001` | Guarantee healthcare for incarcerated individuals  |

### housing.html (155 mismatches)

| div id | rule-id code | Title |
|--------|-------------|-------|
| `HOU-MISC-001` | `HOU-RGT-001` | Housing policy must prioritize stable, safe, habit |
| `HOU-MISC-002` | `HOU-RGT-002` | Access to housing must be practical in reality |
| `HOU-MISC-003` | `HOU-RGT-003` | Housing systems must be designed to reduce extract |
| `HOU-MISC-004` | `HOU-HAB-001` | All housing receiving public subsidy, public vouch |
| `HOU-MISC-005` | `HOU-HAB-002` | Housing policy must treat livability as a core |
| `HOU-MISC-006` | `HOU-HAB-003` | Repeated failure to maintain habitable housing mus |
| `HOU-MISC-007` | `HOU-HAB-004` | Residents must have accessible mechanisms to repor |
| `HOU-MISC-008` | `HOU-PUB-001` | Government-owned or publicly administered housing  |
| `HOU-MISC-009` | `HOU-PUB-002` | Public housing systems must receive stable mainten |
| `HOU-MISC-010` | `HOU-PUB-003` | Residents of public housing must have enforceable  |
| `HOU-MISC-011` | `HOU-PUB-004` | Public housing policy must prioritize long-term qu |
| `HOU-MISC-012` | `HOU-PUB-005` | Governments must directly develop, own, or support |
| `HOU-MISC-013` | `HOU-PUB-006` | Public or social housing must be integrated into |
| `HOU-MISC-014` | `HOU-PUB-007` | Public housing development must prioritize long-te |
| `HOU-MISC-015` | `HOU-PUB-008` | Public and social housing must be protected from |
| `HOU-MISC-016` | `HOU-PUB-009` | Public-housing management systems must be audited  |
| `HOU-MISC-017` | `HOU-PUB-010` | Public or social housing may not be neglected |
| `HOU-MISC-018` | `HOU-OWN-001` | Federal and state policy must address the long-ter |
| `HOU-MISC-019` | `HOU-OWN-002` | Housing policy must identify and reform legal, tax |
| `HOU-MISC-020` | `HOU-OWN-003` | The cost of homeownership must be evaluated as |
| `HOU-MISC-021` | `HOU-OWN-004` | Homeownership policy should prioritize long-term r |
| `HOU-MISC-022` | `HOU-OWN-005` | Housing policy must ensure that ordinary income ea |
| `HOU-MISC-023` | `HOU-OWN-006` | First-time homebuyers must have access to fair fin |
| `HOU-MISC-024` | `HOU-OWN-007` | Down payment assistance, public financing tools, o |
| `HOU-MISC-025` | `HOU-MKT-001` | Housing markets may not be structured so that |
| `HOU-MISC-026` | `HOU-MKT-002` | Government should limit speculative bulk acquisiti |
| `HOU-MISC-027` | `HOU-MKT-003` | Ownership concentration in residential housing mar |
| `HOU-MISC-028` | `HOU-MKT-004` | Corporate ownership of single-family homes and oth |
| `HOU-MISC-029` | `HOU-MKT-005` | Institutional and corporate ownership caps should  |
| `HOU-MISC-030` | `HOU-MKT-006` | Bulk acquisition of single-family homes, starter h |
| `HOU-MISC-031` | `HOU-MKT-007` | Shell-company, affiliate, and fragmented-title str |
| `HOU-MISC-032` | `HOU-MKT-008` | Ownership-concentration rules must distinguish bet |
| `HOU-MISC-033` | `HOU-MKT-009` | Housing policy may not prioritize asset appreciati |
| `HOU-MISC-034` | `HOU-MKT-010` | Tax, financing, and regulatory systems must not di |
| `HOU-MISC-035` | `HOU-MKT-011` | Residential housing must not be treated primarily  |
| `HOU-MISC-036` | `HOU-MKT-012` | Ownership concentration that enables coordinated p |
| `HOU-MISC-037` | `HOU-MKT-013` | Use of algorithmic or coordinated systems to artif |
| `HOU-MISC-038` | `HOU-MKT-014` | Residential housing markets are subject to heighte |
| `HOU-MISC-039` | `HOU-MKT-015` | Landlords, property managers, investors, and prici |
| `HOU-MISC-040` | `HOU-MKT-016` | Use of algorithmic rent-setting systems in concent |
| `HOU-MISC-041` | `HOU-MKT-017` | Large-scale residential ownership structures that  |
| `HOU-MISC-042` | `HOU-SUP-001` | Housing policy must expand the supply of affordabl |
| `HOU-MISC-043` | `HOU-SUP-002` | Restrictive zoning, exclusionary land-use rules, a |
| `HOU-MISC-044` | `HOU-SUP-003` | Housing supply reform should prioritize abundant,  |
| `HOU-MISC-045` | `HOU-SUP-004` | Inclusionary requirements, affordability set-aside |
| `HOU-MISC-046` | `HOU-SUP-005` | Zoning and land-use systems may not be structured |
| `HOU-MISC-047` | `HOU-SUP-006` | Permitting and approval processes must be time-bou |
| `HOU-MISC-048` | `HOU-SUP-007` | Discretionary approval systems that allow arbitrar |
| `HOU-MISC-049` | `HOU-PRS-001` | Housing policy must preserve existing affordable h |
| `HOU-MISC-050` | `HOU-PRS-002` | Anti-displacement protections must be built into r |
| `HOU-MISC-051` | `HOU-PRS-003` | Communities facing gentrification pressure must re |
| `HOU-MISC-052` | `HOU-ALT-001` | Housing policy should promote nonprofit housing, c |
| `HOU-MISC-053` | `HOU-ALT-002` | Public subsidy and land policy should favor owners |
| `HOU-MISC-054` | `HOU-ALT-003` | Social housing systems should include mixed-income |
| `HOU-MISC-055` | `HOU-ALT-004` | Community land trusts, cooperatives, and nonprofit |
| `HOU-MISC-056` | `HOU-TEN-001` | Tenants must have enforceable rights to habitabili |
| `HOU-MISC-057` | `HOU-TEN-002` | Administrative barriers, legal complexity, and cod |
| `HOU-MISC-058` | `HOU-TEN-003` | Housing code enforcement must be proactive, adequa |
| `HOU-MISC-059` | `HOU-TEN-004` | Tenants must have the right to clear, stable |
| `HOU-MISC-060` | `HOU-TEN-005` | Lease renewals and terminations must be governed b |
| `HOU-MISC-061` | `HOU-TEN-006` | Tenants must have protection from sudden or extrem |
| `HOU-MISC-062` | `HOU-TEN-007` | Tenants must have the right to organize, form |
| `HOU-MISC-063` | `HOU-OVR-001` | Federal, state, and local governments must collect |
| `HOU-MISC-064` | `HOU-OVR-002` | Repeated patterns of unsafe housing, speculative e |
| `HOU-MISC-065` | `HOU-OVR-003` | Housing regulators must track and publish standard |
| `HOU-MISC-066` | `HOU-OVR-004` | Repeated patterns of abuse, neglect, collusion, un |
| `HOU-MISC-067` | `HOU-VAC-001` | Purchase of homes in developing or supply-constrai |
| `HOU-MISC-068` | `HOU-VAC-002` | Vacancy taxes or equivalent anti-speculation tools |
| `HOU-MISC-069` | `HOU-VAC-003` | Housing policy should discourage land banking and  |
| `HOU-MISC-070` | `HOU-VAC-004` | Legitimate exceptions to vacancy restrictions may  |
| `HOU-MISC-071` | `HOU-VAC-005` | Policies must prevent speculative holding of resid |
| `HOU-MISC-072` | `HOU-VAC-006` | Rapid speculative turnover practices that destabil |
| `HOU-MISC-073` | `HOU-HOA-001` | Homeowner associations must be subject to strong l |
| `HOU-MISC-074` | `HOU-HOA-002` | HOA governance must include due process, transpare |
| `HOU-MISC-075` | `HOU-HOA-003` | HOA fines, liens, and enforcement powers must be |
| `HOU-MISC-076` | `HOU-HOA-004` | HOAs may not impose rules that violate protected |
| `HOU-MISC-077` | `HOU-HOA-005` | State law should provide oversight, complaint mech |
| `HOU-MISC-078` | `HOU-HOA-006` | HOA rules may not be used to block |
| `HOU-MISC-079` | `HOU-HOA-007` | HOAs may not use aesthetic rules to force |
| `HOU-MISC-080` | `HOU-GEN-001` | Housing policy must include proactive anti-gentrif |
| `HOU-MISC-081` | `HOU-GEN-002` | Redevelopment and upzoning policies must include a |
| `HOU-MISC-082` | `HOU-GEN-003` | Communities facing gentrification pressure should  |
| `HOU-MISC-083` | `HOU-GEN-004` | Public investment and infrastructure improvements  |
| `HOU-MISC-084` | `HOU-GEN-005` | Housing and development policy must prevent predic |
| `HOU-MISC-085` | `HOU-BLD-001` | Housing policy should expand investment in sustain |
| `HOU-MISC-086` | `HOU-BLD-002` | Residential construction incentives should priorit |
| `HOU-MISC-087` | `HOU-BLD-003` | Publicly supported housing development should favo |
| `HOU-MISC-088` | `HOU-BLD-004` | Housing production systems must incentivize constr |
| `HOU-MISC-089` | `HOU-BLD-005` | Regulatory frameworks must be evaluated to remove  |
| `HOU-MISC-090` | `HOU-BLD-006` | Housing construction and renovation policy must mi |
| `HOU-MISC-091` | `HOU-BLD-007` | Residential construction may not rely on materials |
| `HOU-MISC-092` | `HOU-BLD-008` | Publicly supported housing and large-scale residen |
| `HOU-MISC-093` | `HOU-QLT-001` | Residential construction must meet stronger qualit |
| `HOU-MISC-094` | `HOU-QLT-002` | Large-scale subdivision builders and mass resident |
| `HOU-MISC-095` | `HOU-QLT-003` | Housing policy should discourage construction patt |
| `HOU-MISC-096` | `HOU-QLT-004` | Historic housing districts and architecturally sig |
| `HOU-MISC-097` | `HOU-QLT-005` | Developers responsible for repeated quality failur |
| `HOU-MISC-098` | `HOU-SYS-001` | Federal and state housing policy must identify and |
| `HOU-MISC-099` | `HOU-SYS-002` | Housing reform should be based on root-cause analy |
| `HOU-MISC-100` | `HOU-SYS-003` | Housing, healthcare, employment, and social-servic |
| `HOU-MISC-101` | `HOU-SYS-004` | Systems must intervene early to prevent eviction a |
| `HOU-MISC-102` | `HOU-SYS-005` | Housing is an essential public-interest sector and |
| `HOU-MISC-103` | `HOU-SYS-006` | Housing policy must measure success by affordabili |
| `HOU-MISC-104` | `HOU-REG-001` | Housing regulations must prioritize safety, durabi |
| `HOU-MISC-105` | `HOU-REG-002` | Housing regulation may not be weakened in ways |
| `HOU-MISC-106` | `HOU-REG-003` | Land-use and zoning regulation may not be used |
| `HOU-MISC-107` | `HOU-REG-004` | Building and safety codes must be strengthened or |
| `HOU-MISC-108` | `HOU-REG-005` | Regulatory reform in housing must target unnecessa |
| `HOU-MISC-109` | `HOU-REG-006` | Industry influence over housing regulation must be |
| `HOU-MISC-110` | `HOU-EVI-001` | Evictions may only occur through a transparent leg |
| `HOU-MISC-111` | `HOU-EVI-002` | No eviction may occur without judicial review; adm |
| `HOU-MISC-112` | `HOU-EVI-003` | Tenants must have access to legal representation i |
| `HOU-MISC-113` | `HOU-EVI-004` | Eviction timelines must provide sufficient time fo |
| `HOU-MISC-114` | `HOU-EVI-005` | Evictions based on minor, technical, or non-materi |
| `HOU-MISC-115` | `HOU-EVI-006` | Retaliatory evictions for reporting code violation |
| `HOU-MISC-116` | `HOU-EVI-007` | Evictions may not be used as a tool |
| `HOU-MISC-117` | `HOU-EVI-008` | Serial eviction filings without legitimate cause m |
| `HOU-MISC-118` | `HOU-EVI-009` | Landlords may not use threats, lockouts, utility s |
| `HOU-MISC-119` | `HOU-EVI-010` | Eviction for nonpayment must include mandatory opp |
| `HOU-MISC-120` | `HOU-EVI-011` | Courts must consider temporary hardship, income di |
| `HOU-MISC-121` | `HOU-EVI-012` | Evictions for small or de minimis arrears that |
| `HOU-MISC-122` | `HOU-RNT-001` | Rent increases must be subject to reasonable limit |
| `HOU-MISC-123` | `HOU-RNT-002` | Sudden, excessive rent increases that displace ten |
| `HOU-MISC-124` | `HOU-RNT-003` | Rent-setting practices that rely on coordinated pr |
| `HOU-MISC-125` | `HOU-HML-001` | Housing policy must adopt a Housing First approach |
| `HOU-MISC-126` | `HOU-HML-002` | Access to housing may not be conditioned on |
| `HOU-MISC-127` | `HOU-HML-003` | Homelessness interventions must include access to  |
| `HOU-MISC-128` | `HOU-HML-004` | Emergency shelters must meet safety, sanitation, a |
| `HOU-MISC-129` | `HOU-HML-005` | Criminalization of homelessness through bans on sl |
| `HOU-MISC-130` | `HOU-RPR-001` | Residents and property owners have the right to |
| `HOU-MISC-131` | `HOU-RPR-002` | Manufacturers, builders, and contractors must not  |
| `HOU-MISC-132` | `HOU-RPR-003` | Housing systems must not rely on proprietary, lock |
| `HOU-MISC-133` | `HOU-RPR-004` | Policies must prevent forced full-system replaceme |
| `HOU-MISC-134` | `HOU-RPR-005` | Repairability must be considered a core design req |
| `HOU-MISC-135` | `HOU-RPR-006` | Tenants must have the right to request and |
| `HOU-MISC-136` | `HOU-RPR-007` | In cases of landlord failure to maintain habitable |
| `HOU-MISC-137` | `HOU-RPR-008` | Housing systems must prioritize long lifecycle dur |
| `HOU-MISC-138` | `HOU-RPR-009` | Core housing systems including HVAC, plumbing, ele |
| `HOU-MISC-139` | `HOU-RPR-010` | Manufacturers and service providers may not use so |
| `HOU-MISC-140` | `HOU-RPR-011` | Building systems installed in homes, apartments, a |
| `HOU-MISC-141` | `HOU-TAX-001` | Property tax systems must protect long-term owner- |
| `HOU-MISC-142` | `HOU-TAX-002` | Property tax increases for primary residences shou |
| `HOU-MISC-143` | `HOU-TAX-003` | Tax policy should distinguish between primary resi |
| `HOU-MISC-144` | `HOU-INS-001` | Homeownership affordability must account for insur |
| `HOU-MISC-145` | `HOU-INS-002` | Insurance markets may not withdraw or price-gouge  |
| `HOU-MISC-146` | `HOU-FIN-001` | Mortgage lending must prohibit predatory terms, de |
| `HOU-MISC-147` | `HOU-FIN-002` | Adjustable-rate, variable-risk, or complex mortgag |
| `HOU-MISC-148` | `HOU-FIN-003` | Lenders must retain accountability for long-term l |
| `HOU-MISC-149` | `HOU-LND-001` | Public land should be prioritized for development  |
| `HOU-MISC-150` | `HOU-LND-002` | Land-use policy must support long-term housing sta |
| `HOU-MISC-151` | `HOU-EXT-001` | Housing may not be treated primarily as an |
| `HOU-MISC-152` | `HOU-EXT-002` | Landlords, developers, and housing owners may not  |
| `HOU-MISC-153` | `HOU-EXT-003` | Publicly subsidized or publicly supported housing  |
| `HOU-MISC-154` | `HOU-SUB-001` | Housing subsidies may not be structured in ways |
| `HOU-MISC-155` | `HOU-SUB-002` | Public subsidies must be tied to measurable afford |

### information-and-media.html (20 mismatches)

| div id | rule-id code | Title |
|--------|-------------|-------|
| `MED-MED-001` | `MED-PRS-001` | Protect Journalists |
| `MED-MED-002` | `MED-PRS-002` | Protect Sources |
| `MED-MED-003` | `MED-PRS-003` | Limit Compelled Disclosure |
| `MED-MED-004` | `MED-PRS-004` | Ban Retaliation Against Journalists |
| `MED-MED-005` | `MED-PRS-005` | Prevent Misuse of Secrecy Laws |
| `MED-MED-006` | `MED-PRS-006` | Judicial Review Before Disclosure |
| `MED-MED-007` | `MED-PRS-007` | Limit Surveillance of Journalists |
| `MED-MED-008` | `MED-PRS-008` | Include Independent Journalists |
| `MED-MED-009` | `MED-PRS-009` | Transparency on Targeting Journalists |
| `MED-INF-001` | `INF-BLD-002` | Carbon-Neutral Infrastructure |
| `MED-INF-002` | `INF-ENR-004` | End Fossil Fuel Subsidies |
| `MED-INF-003` | `INF-ENR-005` | Guarantee Fossil Fuel Phaseout |
| `MED-INF-004` | `INF-GRD-003` | Carbon-Neutral Power Grid |
| `MED-INF-005` | `INF-RAIL-001` | Modernize Rail System |
| `MED-INF-006` | `INF-RAIL-002` | Expand High-Speed Rail |
| `MED-INF-007` | `INF-TRN-001` | Expand Public Transportation |
| `MED-INF-008` | `INF-TRN-002` | Prioritize Accessible Public Transit |
| `MED-INF-009` | `INF-TRN-003` | Phase Out Gasoline-Only Vehicles |
| `MED-INF-010` | `INF-TRN-004` | Require Hybrid Capability in Transition |
| `MED-INF-011` | `INF-TRN-005` | Strict Fuel Efficiency Standards |

### labor-and-workers-rights.html (159 mismatches)

| div id | rule-id code | Title |
|--------|-------------|-------|
| `LAB-MISC-001` | `LAB-SYS-001` | Labor systems must ensure fair compensation, safe  |
| `LAB-MISC-002` | `LAB-SYS-002` | Workers must share in the economic value they |
| `LAB-MISC-003` | `LAB-SYS-003` | Employment systems must not rely on coercion, depe |
| `LAB-MISC-004` | `LAB-RGT-001` | All workers are entitled to fair wages, safe |
| `LAB-MISC-005` | `LAB-RGT-002` | Workers must have access to clear, enforceable lab |
| `LAB-MISC-006` | `LAB-RGT-003` | Labor rights must apply equally to full-time, part |
| `LAB-MISC-007` | `LAB-PAY-001` | Workers must receive compensation sufficient to me |
| `LAB-MISC-008` | `LAB-PAY-002` | Wage systems must be transparent, predictable, and |
| `LAB-MISC-009` | `LAB-PAY-003` | Wage theft, misclassification, unpaid labor, and d |
| `LAB-MISC-010` | `LAB-PAY-004` | Extreme disparities between executive compensation |
| `LAB-MISC-011` | `LAB-PAY-005` | Firms must disclose compensation ratios between ex |
| `LAB-MISC-012` | `LAB-PAY-006` | Tax, regulatory, or governance mechanisms may be u |
| `LAB-MISC-013` | `LAB-PAY-007` | Compensation structures may not incentivize short- |
| `LAB-MISC-014` | `LAB-LVE-001` | Workers are entitled to paid leave, including vaca |
| `LAB-MISC-015` | `LAB-LVE-002` | Paid leave must be sufficient in duration and |
| `LAB-MISC-016` | `LAB-LVE-003` | Workers may not be penalized, retaliated against,  |
| `LAB-MISC-017` | `LAB-LVE-004` | Governments must ensure leave access for small-bus |
| `LAB-MISC-018` | `LAB-LVE-005` | Leave systems must account for caregiving, family  |
| `LAB-MISC-019` | `LAB-SUR-001` | Employers may not use invasive surveillance system |
| `LAB-MISC-020` | `LAB-SUR-002` | Continuous monitoring of workers through cameras,  |
| `LAB-MISC-021` | `LAB-SUR-003` | Worker data collection must be transparent, minima |
| `LAB-MISC-022` | `LAB-SUR-004` | Workers must have the right to know what |
| `LAB-MISC-023` | `LAB-SUR-005` | Surveillance systems may not be used to enforce |
| `LAB-MISC-024` | `LAB-HRS-001` | Work schedules must be predictable, reasonable, an |
| `LAB-MISC-025` | `LAB-HRS-002` | Excessive working hours that undermine health, saf |
| `LAB-MISC-026` | `LAB-HRS-003` | Workers must receive overtime compensation for hou |
| `LAB-MISC-027` | `LAB-HRS-004` | Workers must have scheduling protections that acco |
| `LAB-MISC-028` | `LAB-HRS-005` | Employers may not rely on unstable on-call schedul |
| `LAB-MISC-029` | `LAB-COE-001` | Employers may not use economic dependency, schedul |
| `LAB-MISC-030` | `LAB-COE-002` | Workers must have meaningful ability to leave empl |
| `LAB-MISC-031` | `LAB-CLS-001` | Worker classification must reflect actual working  |
| `LAB-MISC-032` | `LAB-CLS-002` | Misclassification of employees as independent cont |
| `LAB-MISC-033` | `LAB-COL-001` | Workers have the right to organize, unionize, and |
| `LAB-MISC-034` | `LAB-COL-002` | Employers may not engage in union-busting, intimid |
| `LAB-MISC-035` | `LAB-COL-003` | Workers must have a real, enforceable ability to |
| `LAB-MISC-036` | `LAB-COL-004` | Collective bargaining is a fundamental counterbala |
| `LAB-MISC-037` | `LAB-COL-005` | Collective bargaining rights must apply across all |
| `LAB-MISC-038` | `LAB-COL-006` | Legal barriers that prevent workers from organizin |
| `LAB-MISC-039` | `LAB-COL-007` | Public-sector workers must have the right to organ |
| `LAB-MISC-040` | `LAB-COL-008` | Restrictions on collective action in essential ser |
| `LAB-MISC-041` | `LAB-SFT-001` | Employers must provide safe working conditions and |
| `LAB-MISC-042` | `LAB-SFT-002` | Workers must have the right to report unsafe |
| `LAB-MISC-043` | `LAB-TRN-001` | Employers must disclose key employment conditions, |
| `LAB-MISC-044` | `LAB-TRN-002` | Economic transition systems must be designed to su |
| `LAB-MISC-045` | `LAB-TRN-003` | Employers and platforms that materially displace l |
| `LAB-MISC-046` | `LAB-ENF-001` | Labor law violations must be subject to meaningful |
| `LAB-MISC-047` | `LAB-ENF-002` | Workers must have accessible mechanisms to report  |
| `LAB-MISC-048` | `LAB-ENF-003` | Labor enforcement agencies must have sufficient au |
| `LAB-MISC-049` | `LAB-ENF-004` | Repeated violations of labor rights must trigger e |
| `LAB-MISC-050` | `LAB-ENF-005` | Workers must have private rights of action to |
| `LAB-MISC-051` | `LAB-ENF-006` | Labor enforcement agencies must have authority to  |
| `LAB-MISC-052` | `LAB-ENF-007` | Labor rights must be enforceable through public en |
| `LAB-MISC-053` | `LAB-ENF-008` | Repeat labor violators must be subject to escalati |
| `LAB-MISC-054` | `LAB-ENF-009` | Labor systems must be evaluated for real-world out |
| `LAB-MISC-055` | `LAB-UNN-001` | Union formation processes must be timely, transpar |
| `LAB-MISC-056` | `LAB-UNN-002` | Employers may not delay, challenge, or obstruct un |
| `LAB-MISC-057` | `LAB-UNN-003` | Where a majority of workers demonstrate support th |
| `LAB-MISC-058` | `LAB-UNN-004` | Workers must have the option to form unions |
| `LAB-MISC-059` | `LAB-UNN-005` | Employers may not engage in union-busting practice |
| `LAB-MISC-060` | `LAB-UNN-006` | Retaliation against workers for organizing activit |
| `LAB-MISC-061` | `LAB-UNN-007` | Violations of union rights must carry meaningful p |
| `LAB-MISC-062` | `LAB-UNN-008` | Employers may not fragment workforces, misclassify |
| `LAB-MISC-063` | `LAB-UNN-009` | Multi-entity corporate structures may not be used  |
| `LAB-MISC-064` | `LAB-UNN-010` | Workers must have access to communication channels |
| `LAB-MISC-065` | `LAB-UNN-011` | Employers may not restrict lawful communication am |
| `LAB-MISC-066` | `LAB-UNN-012` | Individuals who direct, authorize, or knowingly pa |
| `LAB-MISC-067` | `LAB-UNN-013` | Personal liability applies to executives, managers |
| `LAB-MISC-068` | `LAB-UNN-014` | Use of third-party firms, consultants, or intermed |
| `LAB-MISC-069` | `LAB-UNN-015` | Prohibited conduct includes retaliation, intimidat |
| `LAB-MISC-070` | `LAB-UNN-016` | Individuals found liable for union-busting may be  |
| `LAB-MISC-071` | `LAB-UNN-017` | Civil penalties must be scaled to deter misconduct |
| `LAB-MISC-072` | `LAB-UNN-018` | Willful, repeated, or egregious violations of labo |
| `LAB-MISC-073` | `LAB-UNN-019` | Criminal liability must require clear evidence of  |
| `LAB-MISC-074` | `LAB-UNN-020` | Individuals may not evade liability through corpor |
| `LAB-MISC-075` | `LAB-UNN-021` | Individuals found liable for serious labor violati |
| `LAB-MISC-076` | `LAB-UNN-022` | Financial penalties for union-busting violations m |
| `LAB-MISC-077` | `LAB-UNN-023` | Penalties must be tied to company size and |
| `LAB-MISC-078` | `LAB-UNN-024` | Large firms may not face reduced effective penalti |
| `LAB-MISC-079` | `LAB-UNN-025` | Each act of retaliation, interference, or unlawful |
| `LAB-MISC-080` | `LAB-UNN-026` | Ongoing violations must trigger daily or periodic  |
| `LAB-MISC-081` | `LAB-UNN-027` | Repeat or patterned violations must trigger enhanc |
| `LAB-MISC-082` | `LAB-UNN-028` | Persistent noncompliance may result in structural  |
| `LAB-MISC-083` | `LAB-UNN-029` | Workers harmed by union-busting must receive full  |
| `LAB-MISC-084` | `LAB-UNN-030` | Remedies must account for chilling effects on orga |
| `LAB-MISC-085` | `LAB-UNN-031` | Firms found to have engaged in serious or |
| `LAB-MISC-086` | `LAB-UNN-032` | Labor violations and penalties must be publicly di |
| `LAB-MISC-087` | `LAB-UNN-033` | Settlements may not eliminate accountability for s |
| `LAB-MISC-088` | `LAB-CBA-001` | Employers must engage in good-faith bargaining fol |
| `LAB-MISC-089` | `LAB-CBA-002` | Failure to reach a first contract within a |
| `LAB-MISC-090` | `LAB-CBA-003` | Collective bargaining systems should include secto |
| `LAB-MISC-091` | `LAB-CBA-004` | Sectoral agreements may set minimum standards for  |
| `LAB-MISC-092` | `LAB-CBA-005` | Sectoral bargaining structures must include repres |
| `LAB-MISC-093` | `LAB-CBA-006` | Collective bargaining must include wages, benefits |
| `LAB-MISC-094` | `LAB-CBA-007` | Workers must have the ability to bargain over |
| `LAB-MISC-095` | `LAB-CBA-008` | Collective agreements must be enforceable, with me |
| `LAB-MISC-096` | `LAB-CBA-009` | Violations of collective agreements must result in |
| `LAB-MISC-097` | `LAB-PLT-001` | Workers managed by algorithms, platforms, or autom |
| `LAB-MISC-098` | `LAB-PLT-002` | Platforms may not use algorithmic control, opacity |
| `LAB-MISC-099` | `LAB-PLT-003` | Workers must have the right to transparency and |
| `LAB-MISC-100` | `LAB-AI-001` | AI systems used in employment must preserve logs |
| `LAB-MISC-101` | `LAB-AI-002` | AI systems affecting hiring, pay, scheduling, prod |
| `LAB-MISC-102` | `LAB-AI-003` | Employment AI may not move from assistive use |
| `LAB-MISC-103` | `LAB-AUT-001` | Employers must provide meaningful notice, consulta |
| `LAB-MISC-104` | `LAB-AUT-002` | Workers and their representatives must have the ri |
| `LAB-MISC-105` | `LAB-AUT-003` | Automation may not be used as a pretext |
| `LAB-MISC-106` | `LAB-BEN-001` | Workers must have reliable access to core benefits |
| `LAB-MISC-107` | `LAB-BEN-002` | Essential worker protections and benefits may not  |
| `LAB-MISC-108` | `LAB-BEN-003` | Benefit systems must be designed to support contin |
| `LAB-MISC-109` | `LAB-BEN-004` | Portable benefit systems should allow workers to a |
| `LAB-MISC-110` | `LAB-BEN-005` | Employers and platforms must contribute proportion |
| `LAB-MISC-111` | `LAB-BEN-006` | Portable benefits may not be used as a |
| `LAB-MISC-112` | `LAB-BEN-007` | Benefit portability systems must be standardized,  |
| `LAB-MISC-113` | `LAB-BEN-008` | Access to healthcare should not depend on retainin |
| `LAB-MISC-114` | `LAB-BEN-009` | Employment transitions, layoffs, reduced hours, or |
| `LAB-MISC-115` | `LAB-BEN-010` | Labor policy should reduce coercive dependence on  |
| `LAB-MISC-116` | `LAB-GIG-001` | Workers performing labor through platforms or digi |
| `LAB-MISC-117` | `LAB-GIG-002` | Employment classification must reflect the reality |
| `LAB-MISC-118` | `LAB-GIG-003` | Workers must be classified as employees where the |
| `LAB-MISC-119` | `LAB-GIG-004` | Independent contractor classification is permitted |
| `LAB-MISC-120` | `LAB-GIG-005` | Misclassification to avoid wages, benefits, or pro |
| `LAB-MISC-121` | `LAB-GIG-006` | Platform workers must receive compensation that me |
| `LAB-MISC-122` | `LAB-GIG-007` | Pay calculations must include all working time, in |
| `LAB-MISC-123` | `LAB-GIG-008` | Workers must be reimbursed for necessary work-rela |
| `LAB-MISC-124` | `LAB-GIG-009` | Platforms must provide clear, real-time informatio |
| `LAB-MISC-125` | `LAB-GIG-010` | Workers must have access to detailed earnings reco |
| `LAB-MISC-126` | `LAB-GIG-011` | Workers subject to algorithmic management must hav |
| `LAB-MISC-127` | `LAB-GIG-012` | Algorithmic systems may not be used to impose |
| `LAB-MISC-128` | `LAB-GIG-013` | Workers must have the right to contest, appeal |
| `LAB-MISC-129` | `LAB-GIG-014` | Platforms may not suspend, deactivate, or restrict |
| `LAB-MISC-130` | `LAB-GIG-015` | Automated deactivations must be subject to human r |
| `LAB-MISC-131` | `LAB-GIG-016` | Platforms may not use behavioral nudges, gamificat |
| `LAB-MISC-132` | `LAB-GIG-017` | Workers must have the ability to reject work |
| `LAB-MISC-133` | `LAB-GIG-018` | Gig and platform workers have the right to |
| `LAB-MISC-134` | `LAB-GIG-019` | Platforms may not classify workers in ways that |
| `LAB-MISC-135` | `LAB-GIG-020` | Workers must have access to and control over |
| `LAB-MISC-136` | `LAB-GIG-021` | Workers must be able to transfer relevant work |
| `LAB-MISC-137` | `LAB-GIG-022` | Rating systems must be transparent, fair, and prot |
| `LAB-MISC-138` | `LAB-GIG-023` | Workers must have the ability to challenge inaccur |
| `LAB-MISC-139` | `LAB-GIG-024` | Platform workers must have access to benefits incl |
| `LAB-MISC-140` | `LAB-GIG-025` | Benefits systems must be designed to follow worker |
| `LAB-MISC-141` | `LAB-GIG-026` | Platforms may not manipulate availability, visibil |
| `LAB-MISC-142` | `LAB-GIG-027` | Platforms may not restructure, reclassify, or rede |
| `LAB-MISC-143` | `LAB-GIG-028` | Labor laws must be enforced against platforms with |
| `LAB-MISC-144` | `LAB-GIG-029` | Repeated violations by platforms may trigger opera |
| `LAB-MISC-145` | `LAB-GOV-001` | Workers should have meaningful representation in f |
| `LAB-MISC-146` | `LAB-GOV-002` | Large firms may be required to include worker |
| `LAB-MISC-147` | `LAB-GOV-003` | Worker governance mechanisms must be structured to |
| `LAB-MISC-148` | `LAB-OWN-001` | Labor policy should promote worker ownership, coop |
| `LAB-MISC-149` | `LAB-OWN-002` | Governments should support formation and scaling o |
| `LAB-MISC-150` | `LAB-OWN-003` | Workers should have pathways to ownership transiti |
| `LAB-MISC-151` | `LAB-OWN-004` | Workers should share in gains from productivity, a |
| `LAB-MISC-152` | `LAB-OWN-005` | Compensation systems may not allocate the overwhel |
| `LAB-MISC-153` | `LAB-OWN-006` | Public incentives, procurement, or tax benefits ma |
| `LAB-MISC-154` | `LAB-RET-001` | Workers must have access to retirement-saving syst |
| `LAB-MISC-155` | `LAB-RET-002` | Retirement systems must be designed to protect wor |
| `LAB-MISC-156` | `LAB-WRK-001` | LAB|WRK|Establish a standard 4-day 32-hour work we |
| `LAB-MISC-157` | `LAB-WRK-002` | LAB|WRK|Productivity gains from AI and automation  |
| `LAB-MISC-158` | `LAB-WRK-003` | LAB|WRK|Guarantee overtime pay protections for all |
| `LAB-LAB-001` | `ECO-LAB-004` | Government must subsidize or support paid parental |

### legislative-reform.html (34 mismatches)

| div id | rule-id code | Title |
|--------|-------------|-------|
| `LEG-LEG-001` | `LEG-SYS-001` | Legislature must reflect democracy with power safe |
| `LEG-LEG-002` | `LEG-SYS-002` | No persistent minority governance without democrat |
| `LEG-LEG-003` | `LEG-STR-001` | Bicameralism retained but each chamber needs disti |
| `LEG-LEG-004` | `LEG-HSE-001` | House must represent population proportionally as  |
| `LEG-LEG-005` | `LEG-HSE-002` | House must expand to restore representational accu |
| `LEG-LEG-006` | `LEG-HSE-003` | House is primary origin of fiscal and domestic leg |
| `LEG-LEG-007` | `LEG-SEN-001` | Senate may use population-weighted voting to reduc |
| `LEG-LEG-008` | `LEG-SEN-002` | Senate may include both state-based and population |
| `LEG-LEG-009` | `LEG-SEN-003` | Senate may serve as review body rather than co-equ |
| `LEG-LEG-010` | `LEG-SEN-004` | House may have final legislative authority after S |
| `LEG-LEG-011` | `LEG-PRO-001` | Filibuster and indefinite minority obstruction mus |
| `LEG-LEG-012` | `LEG-PRO-002` | Systems must resolve persistent deadlock between c |
| `LEG-LEG-013` | `LEG-PRO-003` | Discharge petition reform — lower threshold and au |
| `LEG-LEG-014` | `LEG-PRO-004` | Proxy voting prohibited for floor votes; remote vo |
| `LEG-LEG-015` | `LEG-EXE-001` | Legislature may select or remove head of governmen |
| `LEG-LEG-016` | `LEG-OVR-001` | Congress must have strong oversight and enforcemen |
| `LEG-LEG-017` | `LEG-OVR-002` | Oversight cannot be blocked by executive privilege |
| `LEG-LEG-018` | `LEG-DMJ-001` | Structural minority rule over national policy is p |
| `LEG-LEG-019` | `LEG-DMJ-002` | Representational systems require periodic democrat |
| `LEG-LEG-020` | `LEG-DB-001` | Establish searchable public federal law database |
| `LEG-LEG-021` | `LEG-DB-002` | Database includes judicial opinions and agency int |
| `LEG-LEG-022` | `LEG-DB-003` | Database allows structured public comment and anno |
| `LEG-LEG-023` | `LEG-DB-004` | Law database must be free, searchable, and accessi |
| `LEG-LEG-024` | `LEG-DRF-001` | Binding drafting standards required for all new fe |
| `LEG-LEG-025` | `LEG-DRF-002` | Each new law requires plain-language statement of  |
| `LEG-LEG-026` | `LEG-DRF-003` | Large sections require plain-language summaries |
| `LEG-LEG-027` | `LEG-DRF-004` | Each provision must be relevant to the law's state |
| `LEG-LEG-028` | `LEG-DRF-005` | Laws reviewed for loopholes and exploit paths befo |
| `LEG-LEG-029` | `LEG-DRF-006` | Conflicts with existing law reconciled before enac |
| `LEG-LEG-030` | `LEG-REV-001` | Permanent body annually reviews federal laws for o |
| `LEG-LEG-031` | `LEG-REV-002` | Review body recommends repeal, consolidation, or m |
| `LEG-LEG-032` | `LEG-REV-003` | Review process includes public reporting and clean |
| `LEG-LEG-033` | `LEG-RPL-001` | Repeal Alien Enemies Act and related emergency abu |
| `LEG-LEG-034` | `LEG-RPL-002` | Repeal Comstock Act and similar archaic morality l |

### rights-and-civil-liberties.html (13 mismatches)

| div id | rule-id code | Title |
|--------|-------------|-------|
| `RGT-BOD-007` | `RGT-BOD-008` | Forced sterilization is prohibited in all contexts |
| `RGT-BOD-008` | `RGT-BOD-009` | No government institution court agency or private  |
| `RGT-BOD-009` | `RGT-BOD-010` | Repeal the Comstock Act |
| `RGT-PRV-001` | `RGT-DET-001` | Ban indefinite detention |
| `RGT-PRV-002` | `RGT-DET-002` | Ban offshore incarceration |
| `RGT-PRV-003` | `RGT-PRV-001` | Explicit right to privacy |
| `RGT-PRV-004` | `RGT-PRV-002` | Medical privacy protections |
| `RGT-PRV-005` | `RGT-PRV-003` | Digital privacy protections |
| `RGT-VTL-001` | `CIV-VTL-001` | Vital records obtainable at any courthouse or reco |
| `RGT-VTL-002` | `CIV-VTL-002` | No requirement to travel to the issuing courthouse |
| `RGT-VTL-003` | `CIV-VTL-003` | Vital records access includes marriage licenses na |
| `RGT-VTL-004` | `CIV-VTL-004` | Certified vital records must be easily obtainable  |
| `RGT-VTL-005` | `CIV-VTL-005` | Mailed vital records must be sent by certified tra |

### taxation-and-wealth.html (157 mismatches)

| div id | rule-id code | Title |
|--------|-------------|-------|
| `TAX-ECO-001` | `ECO-AUT-001` | Automation Tax on Labor Displacement |
| `TAX-ECO-002` | `ECO-AUT-002` | Automation Tax Revenue for Public Benefit |
| `TAX-ECO-003` | `ECO-AUT-003` | Structure Tax to Discourage Irresponsible Displace |
| `TAX-ECO-004` | `ECO-EQT-001` | Equal Pay and Economic Opportunity |
| `TAX-IND-001` | `ECO-IND-001` | National Industrial Strategy |
| `TAX-IND-002` | `ECO-IND-002` | Strategic Sector Investment and Public Financing |
| `TAX-IND-003` | `ECO-IND-003` | Critical Supply Chain Resilience |
| `TAX-IND-004` | `ECO-IND-004` | Rare Earth and Critical Minerals Strategy |
| `TAX-IND-005` | `ECO-IND-005` | Buy America and Domestic Content Requirements |
| `TAX-IND-006` | `ECO-IND-006` | Regional Industrial Policy and Manufacturing Clust |
| `TAX-IND-007` | `ECO-IND-007` | Worker Ownership and Democratic Enterprise in Indu |
| `TAX-IND-008` | `ECO-IND-008` | Research and Development as Industrial Policy |
| `TAX-IND-009` | `ECO-IND-009` | Trade Policy Aligned with Industrial Strategy |
| `TAX-IND-010` | `ECO-IND-010` | Industrial Workforce Pipeline — Apprenticeships, V |
| `TAX-IND-011` | `ECO-IND-001` | Establish national manufacturing and industrial po |
| `TAX-ECO-005` | `ECO-INS-001` | AI Cannot Deny Insurance Without Human Review |
| `TAX-ECO-006` | `ECO-INS-002` | Independent Human Judgment Required |
| `TAX-ECO-007` | `ECO-LAB-004` | Government Support for Small Business Parental Lea |
| `TAX-ECO-008` | `ECO-SMB-001` | Small Business Healthcare Coverage Support |
| `TAX-SS-001` | `ECO-SS-001` | Eliminate the Social Security Payroll Tax Wage Cap |
| `TAX-SS-002` | `ECO-SS-002` | Supplement Social Security Funding with Automation |
| `TAX-SS-003` | `ECO-SS-003` | Substantially Increase the Social Security Minimum |
| `TAX-SS-004` | `ECO-SS-004` | Add Caregiver Credits to Social Security Benefit C |
| `TAX-SS-005` | `ECO-SS-005` | Study and Address Occupational Inequity in Retirem |
| `TAX-GBI-001` | `ECO-GBI-001` | Guaranteed Income Floor for All Residents |
| `TAX-GBI-002` | `ECO-GBI-002` | Universal Displacement-Triggered Income Support |
| `TAX-GBI-003` | `ECO-GBI-003` | Automation Gains Must Fund a Social Dividend |
| `TAX-GBI-004` | `ECO-GBI-004` | Phased Implementation: Strengthen Existing Program |
| `TAX-GBI-005` | `ECO-GBI-005` | Prohibit Welfare Cliffs in All Means-Tested Progra |
| `TAX-CTC-001` | `ECO-CTC-001` | Fully Refundable, Universal Child Tax Credit |
| `TAX-CTC-002` | `ECO-CTC-002` | Child Allowance Paid Monthly |
| `TAX-CTC-003` | `ECO-CTC-003` | Benefit Level Sufficient to Reduce Child Poverty;  |
| `TAX-CTC-004` | `ECO-CTC-004` | No Tax Filing Barrier; Automatic Enrollment |
| `TAX-CTC-005` | `ECO-CTC-005` | Child Allowance Through Age 17; Study Extension Th |
| `TAX-ECO-009` | `ECO-TAX-001` | Anti-Wealth Hoarding |
| `TAX-ECO-010` | `TAX-WTH-001` | Tax policy must more effectively reach concentrate |
| `TAX-ECO-011` | `TAX-WTH-002` | Tax rules may not systematically privilege wealth  |
| `TAX-ECO-012` | `TAX-WTH-003` | Extremely large accumulations of wealth may be sub |
| `TAX-ECO-013` | `TAX-WTH-004` | Tax systems must prevent extreme concentration of  |
| `TAX-ECO-014` | `TAX-WTH-005` | Extremely large concentrations of wealth may be su |
| `TAX-ECO-015` | `TAX-WTH-006` | Wealth-tax systems must include strong valuation,  |
| `TAX-ECO-016` | `TAX-WTH-007` | High-wealth individuals may not use trusts, pass-t |
| `TAX-ECO-017` | `TAX-WTH-008` | Tax systems must apply heightened reporting, audit |
| `TAX-ECO-018` | `TAX-WTH-009` | Artificial conversion of labor income into lower-t |
| `TAX-ECO-019` | `TAX-WTH-010` | Personal tax avoidance schemes that rely on entity |
| `TAX-ECO-020` | `TAX-CAP-001` | Income derived from capital, including dividends,  |
| `TAX-ECO-021` | `TAX-CAP-002` | Preferential treatment of capital income that disp |
| `TAX-ECO-022` | `TAX-CAP-003` | Long-term investment incentives may be preserved o |
| `TAX-ECO-023` | `TAX-CAP-004` | Capital gains must be taxed in a manner |
| `TAX-ECO-024` | `TAX-CAP-005` | Unrealized gains at extreme wealth levels may be |
| `TAX-ECO-025` | `TAX-CAP-006` | Step-up in basis rules that eliminate tax |
| `TAX-ECO-026` | `TAX-CAP-007` | Compensation or value derived from personal labor |
| `TAX-ECO-027` | `TAX-CAP-008` | Carried interest, performance allocation, and simi |
| `TAX-ECO-028` | `TAX-EST-001` | Large intergenerational wealth transfers must be t |
| `TAX-ECO-029` | `TAX-EST-002` | Estate and inheritance tax systems must be structu |
| `TAX-ECO-030` | `TAX-EST-003` | Trusts, foundations, and other structures may not  |
| `TAX-ECO-031` | `TAX-AI-001` | Economic value generated through automation and AI |
| `TAX-ECO-032` | `TAX-AI-002` | Organizations that replace or substantially displa |
| `TAX-ECO-033` | `TAX-AI-003` | AI taxation applies where automation materially re |
| `TAX-ECO-034` | `TAX-AI-004` | AI tax obligations must be based on measurable |
| `TAX-ECO-035` | `TAX-AI-005` | AI taxation systems must prevent avoidance through |
| `TAX-ECO-036` | `TAX-AI-006` | Companies may not evade AI taxation by shifting |
| `TAX-ECO-037` | `TAX-AI-007` | Revenue from AI-related taxation should support wo |
| `TAX-ECO-038` | `TAX-AI-008` | AI tax systems must balance innovation incentives |
| `TAX-ECO-039` | `TAX-AI-009` | Beneficial uses of AI that improve safety, accessi |
| `TAX-ECO-040` | `TAX-AI-010` | Companies deriving disproportionate economic power |
| `TAX-ECO-041` | `TAX-COR-001` | Corporations must pay meaningful taxes on real eco |
| `TAX-ECO-042` | `TAX-COR-002` | Corporate tax systems must be designed to prevent |
| `TAX-ECO-043` | `TAX-COR-003` | Corporations may not use shell entities, internal  |
| `TAX-ECO-044` | `TAX-COR-004` | Corporate tax systems must reflect real economic a |
| `TAX-ECO-045` | `TAX-COR-005` | Corporations must pay a minimum effective tax rate |
| `TAX-ECO-046` | `TAX-COR-006` | Effective tax rate calculations must account for g |
| `TAX-ECO-047` | `TAX-LOP-001` | Tax provisions that primarily enable avoidance, de |
| `TAX-ECO-048` | `TAX-LOP-002` | Corporate tax law must be regularly reviewed |
| `TAX-ECO-049` | `TAX-DED-001` | Deductions must be directly tied to legitimate bus |
| `TAX-ECO-050` | `TAX-DED-002` | Excessive executive compensation, stock-based comp |
| `TAX-ECO-051` | `TAX-DED-003` | Interest deductions may be limited where used |
| `TAX-ECO-052` | `TAX-DED-004` | Internal financial arrangements, including interco |
| `TAX-ECO-053` | `TAX-DED-005` | Transactions lacking economic substance beyond tax |
| `TAX-ECO-054` | `TAX-BEP-001` | Corporate income must be taxed based on real |
| `TAX-ECO-055` | `TAX-BEP-002` | Transfer pricing must reflect real market value |
| `TAX-ECO-056` | `TAX-BEP-003` | Artificial profit allocation to low-tax jurisdicti |
| `TAX-ECO-057` | `TAX-EXT-001` | Stock buybacks and similar financial extraction me |
| `TAX-ECO-058` | `TAX-EXT-002` | Tax policy may not incentivize financial engineeri |
| `TAX-ECO-059` | `TAX-INC-001` | Tax incentives must be tied to measurable public-g |
| `TAX-ECO-060` | `TAX-INC-002` | Tax incentives may not reward stock buybacks, fina |
| `TAX-ECO-061` | `TAX-INC-003` | Public subsidies and tax advantages should favor d |
| `TAX-ECO-062` | `TAX-INC-004` | Corporate tax structures should reward long-term i |
| `TAX-ECO-063` | `TAX-INC-005` | Corporate tax incentives may not reward offshoring |
| `TAX-ECO-064` | `TAX-TRN-001` | Beneficial ownership of companies, trusts, major a |
| `TAX-ECO-065` | `TAX-TRN-002` | High-risk tax structures and large offshore holdin |
| `TAX-ECO-066` | `TAX-TRN-003` | Secrecy structures designed to conceal effective c |
| `TAX-ECO-067` | `TAX-TRN-004` | Large corporations must publicly report revenue, p |
| `TAX-ECO-068` | `TAX-TRN-005` | Corporate structures, subsidiaries, and ownership  |
| `TAX-ECO-069` | `TAX-ENF-001` | Tax enforcement agencies must be well funded, tech |
| `TAX-ECO-070` | `TAX-ENF-002` | Repeated, willful, or large-scale tax evasion must |
| `TAX-ECO-071` | `TAX-ENF-003` | Tax audits and investigations must prioritize larg |
| `TAX-ECO-072` | `TAX-ENF-004` | Professional facilitators of tax fraud or abusive  |
| `TAX-ECO-073` | `TAX-ENF-005` | Tax enforcement must prioritize large corporations |
| `TAX-ECO-074` | `TAX-ENF-006` | Professional enablers of corporate tax avoidance,  |
| `TAX-ECO-075` | `TAX-ENF-007` | Repeated or large-scale corporate tax avoidance mu |
| `TAX-ECO-076` | `TAX-ENF-008` | Corporations may not indefinitely delay tax enforc |
| `TAX-ECO-077` | `TAX-ENF-009` | Simplification for ordinary taxpayers must be pair |
| `TAX-ECO-078` | `TAX-ENF-010` | Enforcement resources must be allocated according  |
| `TAX-ECO-079` | `TAX-GOV-001` | Tax policy and enforcement agencies must be protec |
| `TAX-ECO-080` | `TAX-GOV-002` | Revolving-door practices between regulators and re |
| `TAX-ECO-081` | `TAX-ENV-001` | Environmental tax policy must internalize environm |
| `TAX-ECO-082` | `TAX-ENV-002` | Environmental taxation must be structured to reduc |
| `TAX-ECO-083` | `TAX-ENV-003` | Environmental taxes and fees may not be used |
| `TAX-ECO-084` | `TAX-ENV-004` | Carbon-intensive activity may be subject to direct |
| `TAX-ECO-085` | `TAX-ENV-005` | Environmental tax systems must not rely on unverif |
| `TAX-ECO-086` | `TAX-ENV-006` | Carbon pricing or equivalent environmental taxatio |
| `TAX-ECO-087` | `TAX-ENV-007` | Environmental tax systems must distinguish between |
| `TAX-ECO-088` | `TAX-ENV-008` | Water extraction and intensive water use may be |
| `TAX-ECO-089` | `TAX-ENV-009` | Water-related taxation and pricing must account fo |
| `TAX-ECO-090` | `TAX-ENV-010` | Large-scale industrial water use may be subject |
| `TAX-ECO-091` | `TAX-ENV-011` | Water taxation and fee systems must not undermine |
| `TAX-ECO-092` | `TAX-ENV-012` | Polluting activities and persistent pollutants may |
| `TAX-ECO-093` | `TAX-ENV-013` | Tax and fee systems may be used |
| `TAX-ECO-094` | `TAX-ENV-014` | Environmental taxes must account for lifecycle har |
| `TAX-ECO-095` | `TAX-ENV-015` | Environmental tax policy should incentivize durabl |
| `TAX-ECO-096` | `TAX-ENV-016` | Tax advantages may be used to support repair |
| `TAX-ECO-097` | `TAX-ENV-017` | Tax policy may disfavor disposable, non-repairable |
| `TAX-ECO-098` | `TAX-ENV-018` | Environmental tax systems must include strong anti |
| `TAX-ECO-099` | `TAX-ENV-019` | Corporations may not reduce environmental tax obli |
| `TAX-ECO-100` | `TAX-ENV-020` | Imports and cross-border supply chains may be subj |
| `TAX-ECO-101` | `TAX-ENV-021` | Revenue from environmental taxation should support |
| `TAX-ECO-102` | `TAX-ENV-022` | Environmental tax revenue should also support hous |
| `TAX-ECO-103` | `TAX-ENV-023` | Environmental tax systems must be designed so that |
| `TAX-ECO-104` | `TAX-ENV-024` | Environmental tax systems must be transparent, pub |
| `TAX-ECO-105` | `TAX-ENV-025` | Entities subject to environmental taxes or fees |
| `TAX-ECO-106` | `TAX-ENV-026` | Environmental tax enforcement must coordinate with |
| `TAX-ECO-107` | `TAX-ENV-027` | Fraud, concealment, collusion, or knowing misrepor |
| `TAX-ECO-108` | `TAX-ENV-028` | Auditors, executives, officers, and responsible in |
| `TAX-ECO-109` | `TAX-ENV-029` | Repeated or systemic environmental tax violations  |
| `TAX-ECO-110` | `TAX-ENV-030` | Environmental taxation must be integrated with dir |
| `TAX-ECO-111` | `TAX-ENV-031` | Environmental taxes, fees, and incentives must be  |
| `TAX-ECO-112` | `TAX-ENV-032` | Small-business carveouts or proportional treatment |
| `TAX-ECO-113` | `TAX-HVN-001` | Individuals and corporations may not evade tax obl |
| `TAX-ECO-114` | `TAX-HVN-002` | United States should impose strong anti-haven rule |
| `TAX-ECO-115` | `TAX-HVN-003` | Tax liability must follow beneficial ownership, ef |
| `TAX-ECO-116` | `TAX-HVN-004` | Corporations claiming offshore residence or foreig |
| `TAX-ECO-117` | `TAX-HVN-005` | Ultra-wealthy individuals who move assets, tax dom |
| `TAX-ECO-118` | `TAX-HVN-006` | Anti-tax-haven rules must distinguish ordinary exp |
| `TAX-ECO-119` | `TAX-INT-001` | United States should pursue international agreemen |
| `TAX-ECO-120` | `TAX-INT-002` | Trade, banking, sanctions, and diplomatic tools ma |
| `TAX-ECO-121` | `TAX-INT-003` | Foreign-policy and treaty tools should support tra |
| `TAX-ECO-122` | `TAX-ADM-001` | Tax administration systems should use automation,  |
| `TAX-ECO-123` | `TAX-ADM-002` | Automated tax-administration systems must be trans |
| `TAX-ECO-124` | `TAX-ADM-003` | IRS modernization must prioritize public usability |
| `TAX-ECO-125` | `TAX-DMJ-001` | Tax policy must be written and administered so |
| `TAX-ECO-126` | `TAX-DMJ-002` | legitimacy of the tax system depends on visible |
| `TAX-ECO-127` | `TAX-DMJ-003` | tax system must be visibly fair in practice |
| `TAX-ECO-128` | `TAX-DMJ-004` | Simplicity, fairness, and enforceability are co-eq |
| `TAX-ANT-001` | `ECO-ANT-001` | Strengthen federal antitrust enforcement to preven |
| `TAX-ANT-002` | `ECO-ANT-002` | Require consumer goods to be designed for durabili |
| `TAX-ANT-003` | `ECO-ANT-003` | Algorithmic price coordination between competing m |

### technology-and-ai.html (141 mismatches)

| div id | rule-id code | Title |
|--------|-------------|-------|
| `TEC-INT-001` | `TEC-INT-004` | Common carrier treatment |
| `TEC-INT-002` | `TEC-INT-005` | Non-discrimination requirement |
| `TEC-INT-003` | `TEC-INT-006` | No blocking or throttling |
| `TEC-INT-004` | `TEC-INT-007` | Narrow technical exceptions |
| `TEC-INT-005` | `TEC-INT-008` | Transparent exceptions |
| `TEC-INT-006` | `TEC-INT-009` | Protection from rollback |
| `TEC-MIL-006` | `TEC-MIL-005A` | No target filtering or ranking |
| `TEC-MIL-007` | `TEC-MIL-006` | Identified human decision-maker |
| `TEC-MIL-008` | `TEC-MIL-007` | Logging and auditability |
| `TEC-MIL-009` | `TEC-MIL-008` | Transparency for human oversight |
| `TEC-MIL-010` | `TEC-MIL-009` | Testing and reliability |
| `TEC-MIL-011` | `TEC-MIL-010` | Ban mass intelligence fusion |
| `TEC-MIL-012` | `TEC-MIL-011` | No profiling for targeting |
| `TEC-MIL-013` | `TEC-MIL-012` | Compliance with laws of armed conflict |
| `TEC-MIL-014` | `TEC-MIL-013` | Clear attribution of responsibility |
| `TEC-MIL-015` | `TEC-MIL-014` | No evasion of accountability |
| `TEC-MIL-016` | `TEC-MIL-015` | Congressional authorization required |
| `TEC-MIL-017` | `TEC-MIL-016` | Limits on executive authority |
| `TEC-MIL-018` | `TEC-MIL-017` | Regular reporting to Congress |
| `TEC-MIL-019` | `TEC-MIL-018` | Controlled testing required |
| `TEC-MIL-020` | `TEC-MIL-019` | No real-world testing |
| `TEC-MIL-021` | `TEC-MIL-020` | Adversarial testing |
| `TEC-MIL-022` | `TEC-MIL-021` | Contractor accountability |
| `TEC-MIL-023` | `TEC-MIL-022` | No outsourcing of authority |
| `TEC-MIL-024` | `TEC-MIL-023` | Export controls |
| `TEC-MIL-025` | `TEC-MIL-024` | Defensive AI permitted |
| `TEC-MIL-026` | `TEC-MIL-025` | No repurposing defensive AI |
| `TEC-MIL-027` | `TEC-MIL-026` | AI for analysis not targeting |
| `TEC-MIL-028` | `TEC-MIL-027` | Ban offensive lethal AI |
| `TEC-MIL-029` | `TEC-MIL-028` | Limited guidance use |
| `TEC-MIL-030` | `TEC-MIL-029` | Guidance parameters strictly defined |
| `TEC-MIL-031` | `TEC-MIL-030` | No new target selection by guidance |
| `TEC-MIL-032` | `TEC-MIL-031` | Human responsibility for guidance outcomes |
| `TEC-MIL-033` | `TEC-MIL-032` | Defensive systems against non-human threats |
| `TEC-MIL-034` | `TEC-MIL-033` | Support international treaties |
| `TEC-MIL-035` | `TEC-MIL-034` | Treaty goal: ban autonomous weapons |
| `TEC-MIL-036` | `TEC-MIL-035` | Treaty goal: ban targeting AI |
| `TEC-MIL-037` | `TEC-MIL-036` | Treaty goal: ban nuclear AI |
| `TEC-MIL-038` | `TEC-MIL-037` | Treaty mechanisms |
| `TEC-MIL-039` | `TEC-MIL-038` | Prevent AI arms races |
| `TEC-MIL-040` | `TEC-MIL-039` | Export controls in treaties |
| `TEC-MIL-041` | `TEC-MIL-040` | Strong sanctions for violations |
| `TEC-MIL-042` | `TEC-MIL-041` | Sanctions for prohibited systems |
| `TEC-MIL-043` | `TEC-MIL-042` | Narrow reciprocal exceptions |
| `TEC-MIL-044` | `TEC-MIL-043` | Temporary reciprocal measures |
| `TEC-MIL-045` | `TEC-MIL-044` | Core prohibitions remain |
| `TEC-MIL-046` | `TEC-MIL-045` | Autonomous targeting as war crime |
| `TEC-MIL-047` | `TEC-MIL-046` | Target generation as unlawful |
| `TEC-MIL-048` | `TEC-MIL-047` | Violations of armed conflict principles |
| `TEC-MIL-049` | `TEC-MIL-048` | Precision guidance exception |
| `TEC-MIL-050` | `TEC-MIL-049` | Commanders remain liable |
| `TEC-MIL-051` | `TEC-MIL-050` | Dedicated cyber branch |
| `TEC-MIL-052` | `TEC-MIL-051` | Cyber defense mission |
| `TEC-MIL-053` | `TEC-MIL-052` | Offensive cyber limits |
| `TEC-MIL-054` | `TEC-MIL-053` | Minimize civilian cyber impact |
| `TEC-MIL-055` | `TEC-MIL-054` | Cyber branch oversight |
| `TEC-MIL-056` | `TEC-MIL-055` | No domestic cyber surveillance |
| `TEC-MIL-057` | `TEC-MIL-056` | Coordination with civilian agencies |
| `TEC-MIL-058` | `TEC-MIL-057` | International cyber norms |
| `TEC-MIL-059` | `TEC-MIL-005A` | AI systems may not be used to narrow, filter, or r |
| `TEC-SYN-016` | `TEC-CHD-001` | AI systems directed at children or likely |
| `TEC-SYN-017` | `TEC-CHD-002` | AI companion systems may not be designed |
| `TEC-SYN-018` | `TEC-CHD-003` | AI systems may not simulate friendship, romance, p |
| `TEC-SYN-019` | `TEC-CHD-004` | Child-directed AI systems may not use persuasive d |
| `TEC-SYN-020` | `TEC-CHD-005` | AI systems for children must minimize data collect |
| `TEC-SYN-021` | `TEC-CHD-006` | High-risk generative features for minors, includin |
| `TEC-SYN-022` | `TEC-CHD-007` | AI systems used by minors must include strong |
| `TEC-SYN-023` | `TEC-CHD-008` | Deepfake generation involving minors or school com |
| `TEC-SYN-024` | `TEC-CHD-009` | Schools and guardians must have transparent contro |
| `TEC-SYN-025` | `TEC-CHD-010` | AI systems may not replace qualified human support |
| `TEC-SYN-026` | `TEC-CHD-011` | Platforms hosting child-facing AI systems must mai |
| `TEC-SYN-027` | `TEC-CHD-012` | Research on child impacts of AI systems, including |
| `TEC-SYN-028` | `TEC-DEM-001` | AI systems may not be used to generate |
| `TEC-SYN-029` | `TEC-DEM-002` | Deepfakes and synthetic impersonation of candidate |
| `TEC-SYN-030` | `TEC-DEM-003` | AI-generated political advertising must carry clea |
| `TEC-SYN-031` | `TEC-DEM-004` | Platforms must maintain rapid-response systems for |
| `TEC-SYN-032` | `TEC-DEM-005` | AI systems may not be used to microtarget |
| `TEC-SYN-033` | `TEC-DEM-006` | Political campaigns, parties, PACs, and major advo |
| `TEC-SYN-034` | `TEC-DEM-007` | AI may not be used to impersonate voters |
| `TEC-SYN-035` | `TEC-DEM-008` | Election administration agencies may not rely on o |
| `TEC-SYN-036` | `TEC-DEM-009` | AI tools used in election administration must be |
| `TEC-SYN-037` | `TEC-DEM-010` | AI systems may not be used to suppress |
| `TEC-SYN-038` | `TEC-DEM-011` | Platforms and political advertisers may not use ge |
| `TEC-SYN-039` | `TEC-DEM-012` | Synthetic civic content affecting elections must b |
| `TEC-SYN-040` | `TEC-DEM-013` | Public repositories of detected election-related s |
| `TEC-SYN-041` | `TEC-DEM-014` | Journalists, researchers, and election monitors mu |
| `TEC-SYN-042` | `TEC-DEM-015` | AI moderation systems used in election contexts |
| `TEC-SYN-043` | `TEC-DEM-016` | Emergency election-content interventions by platfo |
| `TEC-SYN-044` | `TEC-DEM-017` | AI systems may not be used to fabricate |
| `TEC-SYN-045` | `TEC-INF-001` | AI systems deployed in critical infrastructure mus |
| `TEC-SYN-046` | `TEC-INF-002` | Critical infrastructure AI may not be deployed |
| `TEC-SYN-047` | `TEC-INF-003` | Human operators must retain real-time override aut |
| `TEC-SYN-048` | `TEC-INF-004` | AI systems in critical infrastructure must be test |
| `TEC-SYN-049` | `TEC-INF-005` | Critical infrastructure operators must maintain fa |
| `TEC-SYN-050` | `TEC-INF-006` | AI-enabled cybersecurity tools may assist detectio |
| `TEC-SYN-051` | `TEC-INF-007` | AI systems may not be used to optimize |
| `TEC-SYN-052` | `TEC-INF-008` | Procurement of AI for critical infrastructure must |
| `TEC-SYN-053` | `TEC-INF-009` | Critical infrastructure AI incidents must be repor |
| `TEC-SYN-054` | `TEC-INF-010` | Operators may not rely on vendor opacity |
| `TEC-SYN-055` | `TEC-INF-011` | Essential public infrastructure using AI must main |
| `TEC-SYN-056` | `TEC-INF-012` | Concentration of control over AI-enabled critical  |
| `TEC-SYN-057` | `TEC-MED-001` | AI-driven recommender systems may not be optimized |
| `TEC-SYN-058` | `TEC-MED-002` | Large platforms must audit recommender systems for |
| `TEC-SYN-059` | `TEC-MED-003` | Users must have meaningful control over recommenda |
| `TEC-SYN-060` | `TEC-MED-004` | Platforms must disclose major ranking objectives a |
| `TEC-SYN-061` | `TEC-MED-005` | AI-generated news summaries, civic explainers, or  |
| `TEC-SYN-062` | `TEC-MED-006` | Dominant platforms may not use AI systems |
| `TEC-SYN-063` | `TEC-SCI-001` | AI systems may not be used to fabricate |
| `TEC-SYN-064` | `TEC-SCI-002` | Use of AI in research writing, coding, data |
| `TEC-SYN-065` | `TEC-SCI-003` | Scientific publishing systems must prohibit undisc |
| `TEC-SYN-066` | `TEC-SCI-004` | Research institutions must maintain policies for p |
| `TEC-SYN-067` | `TEC-SCI-005` | AI may assist scientific analysis, but |
| `TEC-SYN-068` | `TEC-SCI-006` | Funding agencies and journals should require repro |
| `TEC-SYN-069` | `TEC-SCI-007` | Scientific databases and search systems must guard |
| `TEC-SYN-070` | `TEC-SCI-008` | Publicly funded research using AI should prioritiz |
| `TEC-SYN-071` | `TEC-SCI-009` | Institutions must maintain misconduct procedures s |
| `TEC-SYN-072` | `TEC-SCI-010` | AI systems may not be used to generate |
| `TEC-SYN-073` | `PAT-SYS-001` | patent system must promote genuine innovation, pub |
| `TEC-SYN-074` | `PAT-ANT-001` | Patent rights may not be used to justify |
| `TEC-SYN-075` | `PAT-ANT-002` | Patent enforcement strategies that function as ant |
| `TEC-SYN-076` | `PAT-LIC-001` | Compulsory licensing must be available where paten |
| `TEC-SYN-077` | `PAT-LIC-002` | Essential sectors including healthcare, agricultur |
| `TEC-SYN-078` | `PAT-RPR-001` | Repair, maintenance, and restoration of legally ow |
| `TEC-SYN-079` | `PAT-RPR-002` | Replacement parts, consumables, and repair process |
| `TEC-SYN-080` | `PAT-SCP-001` | Patent duration and scope must be calibrated |
| `TEC-SYN-081` | `PAT-SCP-002` | Extensions, evergreening, and minor modification s |
| `TEC-SYN-082` | `PAT-SFT-001` | Abstract software concepts, algorithms, and genera |
| `TEC-SYN-083` | `PAT-SFT-002` | Software patents must be narrowly defined, technic |
| `TEC-SYN-084` | `PAT-SFT-003` | Patent claims that would prevent independent imple |
| `TEC-SYN-085` | `PAT-THK-001` | Accumulation of large patent portfolios for the pr |
| `TEC-SYN-086` | `PAT-THK-002` | Patent thickets that create unreasonable barriers  |
| `TEC-SYN-087` | `PAT-THK-003` | Regulatory bodies must have authority to limit, un |
| `TEC-SYN-088` | `PAT-TR-001` | Patent enforcement may not be conducted |
| `TEC-SYN-089` | `PAT-TR-002` | Entities that do not produce, license in good |
| `TEC-SYN-090` | `PAT-TR-003` | Courts must have authority to require fee-shifting |
| `TEC-SYN-091` | `PAT-TR-004` | Patent-assertion entities may not use shell struct |
| `TEC-SYN-092` | `PAT-TRN-001` | Patent ownership, licensing structures, and enforc |
| `TEC-SYN-093` | `PAT-TRN-002` | Shell ownership structures used to obscure patent  |
| `TEC-PAT-001` | `PAT-INT-001` | Patent rights may not be used to block |
| `TEC-PAT-002` | `PAT-INT-002` | Circumvention of technical protections for the pur |
| `TEC-PAT-003` | `PAT-INT-003` | Patent enforcement may not be used to restrict |

</details>

---

## Cards with no ID

✅ All cards have IDs.

---

## Duplicate IDs in HTML

**103 IDs appear on more than one card.**

| ID | Files |
|----|-------|
| `CIV-VTL-001` | administrative-state.html, rights-and-civil-liberties.html |
| `CIV-VTL-002` | administrative-state.html, rights-and-civil-liberties.html |
| `CIV-VTL-003` | administrative-state.html, rights-and-civil-liberties.html |
| `CIV-VTL-004` | administrative-state.html, rights-and-civil-liberties.html |
| `CIV-VTL-005` | administrative-state.html, rights-and-civil-liberties.html |
| `COR-AGF-001` | antitrust-and-corporate-power.html, anti-corruption.html |
| `COR-ALG-001` | antitrust-and-corporate-power.html, anti-corruption.html |
| `COR-ANT-001` | antitrust-and-corporate-power.html, anti-corruption.html |
| `COR-AUD-001` | antitrust-and-corporate-power.html, anti-corruption.html |
| `COR-CAP-001` | antitrust-and-corporate-power.html, anti-corruption.html |
| `COR-CON-001` | antitrust-and-corporate-power.html, anti-corruption.html |
| `COR-ENF-001` | antitrust-and-corporate-power.html, anti-corruption.html |
| `COR-FIN-001` | antitrust-and-corporate-power.html, anti-corruption.html |
| `COR-FIN-002` | antitrust-and-corporate-power.html, anti-corruption.html |
| `COR-FIN-003` | antitrust-and-corporate-power.html, anti-corruption.html |
| `COR-FIN-004` | antitrust-and-corporate-power.html, anti-corruption.html |
| `COR-LAW-001` | antitrust-and-corporate-power.html, anti-corruption.html |
| `COR-MKT-001` | antitrust-and-corporate-power.html, anti-corruption.html |
| `COR-MPY-001` | antitrust-and-corporate-power.html, anti-corruption.html |
| `COR-NMD-001` | antitrust-and-corporate-power.html, anti-corruption.html |
| `COR-PEQ-001` | antitrust-and-corporate-power.html, anti-corruption.html |
| `COR-PIS-001` | antitrust-and-corporate-power.html, anti-corruption.html |
| `COR-TRN-001` | antitrust-and-corporate-power.html, anti-corruption.html |
| `ECO-IND-001` | taxation-and-wealth.html |
| `ECO-LAB-004` | taxation-and-wealth.html, labor-and-workers-rights.html |
| `EDU-ECE-031` | education.html |
| `EDU-FIN-001` | environment-and-agriculture.html, education.html |
| `EDU-STD-001` | environment-and-agriculture.html, education.html |
| `ENV-BIO-003` | environment-and-agriculture.html |
| `EXE-25A-001` | executive-power.html |
| `EXE-25A-002` | executive-power.html |
| `EXE-25A-003` | executive-power.html |
| `EXE-25A-004` | executive-power.html |
| `EXE-CAB-001` | executive-power.html |
| `EXE-CAB-002` | executive-power.html |
| `EXE-CAB-003` | executive-power.html |
| `EXE-CAB-004` | executive-power.html |
| `EXE-CAB-005` | executive-power.html |
| `EXE-GRD-001` | executive-power.html |
| `EXE-HOG-001` | executive-power.html |
| `EXE-HOG-002` | executive-power.html |
| `EXE-HOG-003` | executive-power.html |
| `EXE-HOG-004` | executive-power.html |
| `EXE-HOG-013` | executive-power.html |
| `EXE-HOG-014` | executive-power.html |
| `EXE-VP-001` | executive-power.html |
| `EXE-VP-002` | executive-power.html |
| `EXE-VP-003` | executive-power.html |
| `EXE-VP-004` | executive-power.html |
| `EXE-VP-005` | executive-power.html |
| `EXE-VP-006` | executive-power.html |
| `GOV-ACC-002` | executive-power.html, checks-and-balances.html |
| `GOV-SHD-001` | executive-power.html, checks-and-balances.html |
| `GOV-SHD-002` | executive-power.html, checks-and-balances.html |
| `GOV-WAR-002` | executive-power.html, checks-and-balances.html |
| `HOU-PUB-001` | housing.html |
| `HOU-TEN-001` | housing.html |
| `INF-BLD-002` | information-and-media.html, infrastructure-and-public-goods.html |
| `INF-ENR-004` | information-and-media.html, infrastructure-and-public-goods.html |
| `INF-ENR-005` | information-and-media.html, infrastructure-and-public-goods.html |
| `INF-GRD-003` | information-and-media.html, infrastructure-and-public-goods.html |
| `INF-RAIL-001` | information-and-media.html, infrastructure-and-public-goods.html |
| `INF-RAIL-002` | information-and-media.html, infrastructure-and-public-goods.html |
| `INF-TRN-001` | information-and-media.html, infrastructure-and-public-goods.html |
| `INF-TRN-002` | information-and-media.html, infrastructure-and-public-goods.html |
| `INF-TRN-003` | information-and-media.html, infrastructure-and-public-goods.html |
| `INF-TRN-004` | information-and-media.html, infrastructure-and-public-goods.html |
| `INF-TRN-005` | information-and-media.html, infrastructure-and-public-goods.html |
| `JUS-POL-006` | equal-justice-and-policing.html, gun-policy.html |
| `JUS-POL-007` | equal-justice-and-policing.html, gun-policy.html |
| `LAB-WRK-001` | environment-and-agriculture.html, labor-and-workers-rights.html |
| `LAB-WRK-002` | environment-and-agriculture.html, labor-and-workers-rights.html |
| `LAB-WRK-003` | environment-and-agriculture.html, labor-and-workers-rights.html |
| `LEG-RPL-001` | legislative-reform.html |
| `MED-PRS-001` | information-and-media.html |
| `MED-PRS-002` | information-and-media.html |
| `OVR-BRN-001` | foreign-policy.html, checks-and-balances.html |
| `OVR-BRN-002` | foreign-policy.html, checks-and-balances.html |
| `OVR-FED-001` | foreign-policy.html, checks-and-balances.html |
| `OVR-FED-002` | foreign-policy.html, checks-and-balances.html |
| `OVR-FED-003` | foreign-policy.html, checks-and-balances.html |
| `OVR-FED-004` | foreign-policy.html, checks-and-balances.html |
| `OVR-FND-001` | foreign-policy.html, checks-and-balances.html |
| `OVR-FND-002` | foreign-policy.html, checks-and-balances.html |
| `OVR-FND-003` | foreign-policy.html, checks-and-balances.html |
| `OVR-FND-004` | foreign-policy.html, checks-and-balances.html |
| `OVR-FND-005` | foreign-policy.html, checks-and-balances.html |
| `OVR-JUR-001` | foreign-policy.html, checks-and-balances.html |
| `OVR-JUR-002` | foreign-policy.html, checks-and-balances.html |
| `OVR-STA-001` | foreign-policy.html, checks-and-balances.html |
| `OVR-STA-002` | foreign-policy.html, checks-and-balances.html |
| `OVR-STA-003` | foreign-policy.html, checks-and-balances.html |
| `TAX-COR-001` | taxation-and-wealth.html |
| `TAX-ENF-001` | taxation-and-wealth.html |
| `TEC-CHD-001` | technology-and-ai.html |
| `TEC-DEM-001` | technology-and-ai.html |
| `TEC-INF-001` | technology-and-ai.html |
| `TEC-INT-007` | technology-and-ai.html |
| `TEC-INT-008` | technology-and-ai.html |
| `TEC-INT-009` | technology-and-ai.html |
| `TEC-MED-001` | technology-and-ai.html |
| `TEC-MIL-005A` | technology-and-ai.html |
| `TEC-SCI-001` | technology-and-ai.html |

---

## Markdown cross-reference

Policy IDs mentioned in `pillars/` markdown sources.

- Markdown files with policy IDs: 29
- Unique IDs mentioned in markdown: 2240
- Markdown IDs not found in HTML: 2
- Markdown IDs not found in DB: 787

---

## Required actions before Phase 2

1. **Fix ID mismatches**: Update all div `id` attributes to match their `<code class="rule-id">` value
   (1535 mismatches across all pillar files)
2. **Assign IDs to untagged cards**: {len(results['no_id_cards'])} cards have no ID — run `scripts/tag-policy-cards.py`
3. **Review divergences**: {len(results['diverge'])} items have mismatched text between HTML and DB — human decision required
4. **Backfill HTML-only items**: {len(results['html_only'])} HTML cards must be added to DB before DB becomes canonical
5. **Add DB-only items to HTML**: {len(results['db_only'])} DB items must appear as proposal cards in the correct pillar pages

Ali must sign off on this report before Phase 2 migration begins.
