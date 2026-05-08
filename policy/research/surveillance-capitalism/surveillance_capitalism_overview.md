# Surveillance Capitalism and the Data Broker Ecosystem: Research Overview and Policy Framework

**Date:** May 2026  
**Status:** Research draft — ready for adversarial review and policy proposal development  
**Research scope:** System definition, data broker ecosystem, domains of harm, economic scale,
legal landscape, policy proposals, cross-cutting structure

---

## Executive Summary

Surveillance capitalism, as theorized by Shoshana Zuboff, describes a new economic logic in which
human behavioral data — extracted without meaningful consent, processed at scale, and sold as
prediction products — has become the dominant raw material of the digital economy [1]. The data
broker ecosystem that operationalizes this logic now encompasses an estimated 4,000 companies in
the United States alone, generating revenues estimated at $200–$260 billion annually from trading
profiles on virtually every American adult [2, 3]. This infrastructure enables not only targeted
advertising but a cascading array of downstream harms: discriminatory insurance pricing, predatory
lending, employment screening, political manipulation, reproductive surveillance post-Dobbs, and
behavioral modification systems designed to alter consumer conduct at scale.

No comprehensive federal law governs the data broker industry. The Fair Credit Reporting Act (FCRA),
enacted in 1970, covers consumer reporting agencies but explicitly exempts the majority of data
broker activity, including marketing applications [4]. The Health Insurance Portability and
Accountability Act (HIPAA) does not reach health-adjacent apps, wearables, or commercial health
data brokers [5]. The FTC Act's Section 5 authority provides limited enforcement leverage but no
structural prohibition [6]. Against this backdrop, state law — led by California's CCPA/CPRA and
the 2023 DELETE Act — provides the strongest available protections, while the EU's GDPR and Digital
Markets Act illustrate what comprehensive federal regulation could achieve.

This document maps the system, its harms, its economic scale, the legal landscape, and the policy
proposals in circulation to inform the design of a surveillance capitalism and data broker policy
pillar.

---

## Part I: System Definition and Scope

### 1.1 Zuboff's Surveillance Capitalism Framework

Shoshana Zuboff's 2019 work *The Age of Surveillance Capitalism* introduced the theoretical
framework that has come to define academic and policy analysis of the digital data economy [1].
Her core argument is that Google, Facebook, and their successors developed a novel economic logic
distinct from traditional capitalism: rather than producing goods and services for paying customers,
surveillance capitalists claim human behavioral experience as a free raw material — a "behavioral
surplus" — extracted without the knowledge or consent of the people whose experience it captures.

The framework has three core elements:

**Behavioral data extraction.** Surveillance capitalism begins with the unilateral appropriation of
behavioral surplus — data about human activity that exceeds what is needed to deliver a service.
When a user searches Google, Google needs the query to return results. But Google also captures
everything else: the time, location, device type, prior search history, scroll behavior, and click
pattern. This surplus data — not needed for the service — is the raw material of the surveillance
capitalist economy [1].

**Prediction products.** Extracted behavioral surplus is processed by machine learning systems to
produce "prediction products" — instruments that forecast what users will do, want, buy, or believe.
These predictions are sold to advertisers, insurers, employers, political campaigns, and others.
The product is not the user's data per se; it is the ability to predict and influence the user's
behavior [1].

**Behavioral modification.** The most advanced form of surveillance capitalism goes beyond
prediction to modification — using behavioral data and prediction products to intervene in users'
psychological states in order to guarantee predicted behavior. Zuboff calls this "instrumentarian
power": the capacity to shape human conduct at scale without coercion, by controlling the
informational environment [1]. Variable reinforcement schedules in social media feeds, personalized
loss-aversion triggers in e-commerce, and micro-targeted emotional appeals in political advertising
are all operationalizations of this power.

The practical implication for policy is that surveillance capitalism is not merely a privacy problem.
It is a behavioral modification system — a form of market power operating through psychological
manipulation rather than price signals alone.

### 1.2 The Data Broker Ecosystem

The Federal Trade Commission's 2014 data broker report — the most comprehensive federal survey
conducted to date — studied nine major data brokers and found that they collectively held data on
hundreds of millions of Americans, with individual consumer files containing thousands of data
points, including behavioral, financial, and inferred demographic attributes [2]. The FTC estimated
the industry comprised "hundreds of companies" operating largely outside consumer awareness or
regulatory oversight [2]. More recent estimates place the number of U.S. data broker companies at
over 4,000 [3].

**Major players and their functions:**

| Company | Data Specialization | Core Product |
|---|---|---|
| **Acxiom / LiveRamp** | Consumer profiles; 2,500+ data points on ~250M Americans | Identity resolution; marketing data |
| **LexisNexis Risk Solutions (RELX)** | Public records, court records, law enforcement data | Identity verification, background checks |
| **CoreLogic** | Property, mortgage, and real estate records | Property valuation, insurance underwriting |
| **Experian** | Credit data, demographic data, marketing data | Credit reporting, identity verification |
| **TransUnion** | Credit data, employment verification, tenant screening | Credit reporting, alternative data scoring |
| **Equifax / The Work Number** | Credit data; employment/income records for ~114M workers | Credit reporting, workforce solutions |
| **Oracle Data Cloud (BlueKai)** | Digital behavioral data, offline purchase data | Programmatic audience targeting |
| **Epsilon (Publicis)** | Consumer loyalty data, purchase-linked profiles | Targeted marketing, identity resolution |
| **Thomson Reuters (CLEAR)** | Law enforcement, public records, immigration data | Investigative intelligence for government |

**What data brokers collect.** Based on the FTC's 2014 study and subsequent investigations by The
Markup, Gizmodo, and academic researchers, data brokers typically hold:

- **Identifying information:** Name, address history, phone numbers, email addresses, government
  ID number fragments
- **Financial data:** Credit scores, estimated income, bankruptcy and lien records, debt levels,
  wealth tier estimates
- **Behavioral data:** Purchase history, browsing history (via third-party tracking), app usage
  patterns, location history
- **Demographic inferences:** Race/ethnicity (inferred), religion, political affiliation, sexual
  orientation — all inferred from behavioral signals
- **Sensitive categories:** Health conditions (inferred from purchases, app usage, or location
  visits to medical facilities), pregnancy status, addiction signals, mental health indicators
- **Social graph data:** Household composition, family relationships, social media connections [2, 7]

**How data brokers package and sell it.** Data brokers sell data in several forms: raw records for
database matching; behavioral audience segments for programmatic advertising (e.g., "Women 25–34
who have browsed fertility clinics"); risk scores for insurance and lending underwriting; and
"people finder" profiles accessible to any paying customer — with no requirement that the buyer
disclose the intended use [2, 7].

### 1.3 Ad-Tech Infrastructure: Real-Time Bidding and Programmatic Advertising

The advertising technology ecosystem is the primary commercial application of surveillance data
infrastructure and the mechanism through which behavioral data is continuously refreshed and
monetized at scale.

**Real-time bidding (RTB).** When a user loads a web page or opens an app, an automated auction
occurs in approximately 100 milliseconds. The publisher's ad server sends a "bid request" to
multiple demand-side platforms (DSPs) and ad exchanges, containing the user's device identifier, IP
address, approximate location, page context, and any audience segment data available. Advertisers
bid for the impression based on predicted user value. Critically, every auction participant receives
the bid request — and with it the user's behavioral signature — whether or not they win the bid.
This "observe without paying" dynamic means each ad impression broadcasts the user's profile to
dozens or hundreds of companies simultaneously [8].

The Irish Council for Civil Liberties (ICCL) has documented this surveillance externality at scale.
In its 2022 report, the ICCL found that the RTB ecosystem in the United States broadcasts personal
data hundreds of billions of times per year — meaning the average American's digital signature is
shared with ad auction participants hundreds of times per day, without the user receiving any
compensation or exercising any meaningful consent [8].

**DSPs (Demand-Side Platforms):** Allow advertisers to bid programmatically across exchanges. Major
players include The Trade Desk, Google Display & Video 360 (DV360), Amazon DSP, Adobe Advertising
Cloud, and Microsoft Xandr.

**SSPs (Supply-Side Platforms):** Allow publishers to sell inventory. Major players include Google
Ad Manager, Magnite, PubMatic, OpenX, and Index Exchange.

**Cookie tracking and device fingerprinting.** Third-party cookies — data files deposited by
advertisers and brokers on visited websites — historically provided the primary cross-site tracking
mechanism. Google announced plans to eliminate third-party cookies from Chrome multiple times
between 2020 and 2024, ultimately reversing course in July 2024 by announcing it would retain
cookies with added user controls rather than deprecate them [9]. Device fingerprinting —
synthesizing browser version, screen resolution, installed fonts, hardware characteristics, and time
zone into a near-unique identifier — is more persistent than cookies and cannot be cleared by users.

### 1.4 Distinguishing Surveillance Capitalism, Surveillance Pricing, and Surveillance
Discrimination

These three practices share the same infrastructure but represent analytically distinct harms:

| Concept | Mechanism | Primary Harm | Regulatory Target |
|---|---|---|---|
| **Surveillance capitalism** | Extraction of behavioral surplus; sale of prediction products; behavioral modification | Autonomy violation; manipulation; market power concentration | Data extraction limits; behavioral modification bans; structural antitrust |
| **Surveillance pricing** | Using profiles to price at maximum willingness-to-pay | Economic extraction; distributional harm; consumer surplus capture | Price personalization prohibition; disclosure mandates |
| **Surveillance discrimination** | Using profiles for adverse decisions (insurance, credit, employment, housing) | Denial of opportunity; life-chance harm; disparate impact | Anti-discrimination enforcement; FCRA extension; algorithmic accountability |

The distinctions matter for policy design. Regulation targeting the data extraction layer (upstream
of all three harms) is structurally most powerful but also most contested. Regulation targeting
specific uses — pricing, underwriting, employment — is narrower but more precisely targeted and
may be achievable domain by domain even absent comprehensive upstream reform.

---

## Part II: Domains of Harm

### 2.1 Consumer Pricing Extraction

The FTC's January 2025 Surveillance Pricing Study found that intermediary companies — including a
Mastercard subsidiary (Dynamic Yield), McKinsey & Company, and JPMorgan Chase — collected
behavioral consumer profiles and used them to set individualized prices extracting maximum
willingness-to-pay [10]. The FTC found that the data used included sensitive categories consumers
were unaware were being used for pricing, and that lower-income and minority consumers faced
systematically higher prices under these systems. The report was removed from the FTC website
following the January 2025 administration change.

See the companion research document *Surveillance Pricing: Research Overview and Policy Framework*
for comprehensive treatment of this domain.

### 2.2 Insurance Discrimination

Insurance is the most fully developed application of behavioral profiling for adverse
decision-making, and provides a case study in both mechanics and harms.

**Credit-based insurance scoring.** Forty-seven states permit insurers to use credit scores in auto
and homeowners insurance pricing. A 2020 Consumer Federation of America study found that drivers
with poor credit paid an average of 76% more for car insurance than drivers with excellent credit,
controlling for driving history [11]. Because credit scores are correlated with race due to
historical discriminatory lending and structural barriers to credit, credit-based insurance scoring
produces racially disparate outcomes. A 2021 ProPublica and Consumer Reports investigation across
four states found that Black and Latino neighborhoods were systematically charged higher homeowners
insurance premiums despite equivalent or lower actuarial risk [12].

**LexisNexis C.L.U.E.** LexisNexis operates the Comprehensive Loss Underwriting Exchange — a
database of seven years of insurance claims history used by insurers to underwrite new policies.
Access to and correction of CLUE reports is technically covered by the FCRA, but consumer access
and dispute rights in practice remain limited [4, 13].

**Behavioral telematics.** Usage-based insurance programs (Progressive Snapshot, Allstate Drivewise,
State Farm Drive Safe & Save) collect continuous GPS and driving behavior data. While framed as
rewarding safe drivers, these programs create surveillance of location patterns, commute routes, and
time-of-day travel — data that can proxy for neighborhood, employment type, and socioeconomic
status as de facto pricing factors beyond declared actuarial variables.

*[Evidence strength: Strong. Both the Consumer Federation of America study and the ProPublica/
Consumer Reports investigation have been independently verified. The existence of telematics
pricing is well-documented industry practice; its discriminatory dimensions are less
empirically established.]*

### 2.3 Credit and Lending Discrimination

**Traditional credit bureaus.** Experian, TransUnion, and Equifax maintain credit files on
approximately 210 million Americans [15]. Their data is regulated under the FCRA but documented
inaccuracies are widespread and consequential. The Consumer Financial Protection Bureau has
consistently found that errors in credit files affect millions of consumers annually and that
dispute resolution mechanisms systematically favor furnishers over consumers [16].

**Alternative credit scoring.** Fintech lenders increasingly supplement or replace FICO scores with
"alternative data" — bank account cash flows, rent payment history, social media activity, mobile
app usage, and behavioral signals. Companies including Zest AI, Upstart, and others have developed
models incorporating hundreds of non-traditional variables. The CFPB has noted that such models
may reduce access to credit for underserved borrowers or expand it depending on implementation —
but the opacity of these models makes disparate impact assessment by regulators or consumers
virtually impossible [17].

**The Work Number (Equifax).** Equifax's Work Number database contains employment and income
records for approximately 114 million U.S. workers, provided by participating employers. The
database is sold commercially to creditors, landlords, debt collectors, and government agencies —
creating significant surveillance exposure for workers whose employers participate [18].

*[Evidence strength: Strong for credit bureau error rates (CFPB documented). Moderate for
alternative credit scoring harms — emerging evidence but limited independent peer-reviewed research
on disparate impact at scale.]*

### 2.4 Employment Discrimination

**Background check industry.** The background screening industry — led by Sterling, First Advantage,
Checkr, and HireRight — generates annual revenues of approximately $4 billion and conducts checks
on roughly 90% of U.S. job applicants at some stage of the hiring process [19]. These companies
operate as consumer reporting agencies under the FCRA when they assemble "consumer reports," but
FCRA protections are frequently violated in practice.

**Social media screening.** An estimated 70% of employers use social media to screen job applicants,
according to a 2018 CareerBuilder survey [20]. Automated social media screening companies —
including Social Intelligence and Fama Technologies — scan applicants' social media activity for
content indicating drug use, violence, sexual content, and political views. The EEOC has stated
that using social media screening to obtain information about protected characteristics creates
legal exposure under Title VII, but enforcement of this principle remains sparse [21].

**Gig economy algorithmic deactivation.** Uber, Lyft, DoorDash, and Instacart use behavioral
scoring systems to deactivate workers with no advance notice, no explanation, and no meaningful
appeal mechanism. As documented by Virginia Eubanks and others, neutral-appearing algorithmic
factors in these systems can be correlated with protected characteristics — race, disability status,
geographic patterns — in ways that are impossible to identify or challenge given the opacity of the
scoring systems [22].

### 2.5 Political Manipulation

**Cambridge Analytica.** The most widely documented case of surveillance capitalism applied to
political manipulation. Cambridge Analytica, a data analytics firm with ties to right-wing political
movements, harvested behavioral data from approximately 87 million Facebook users without their
consent via a third-party personality quiz app authorized through Facebook's API [23]. This data
was used to construct psychographic profiles — scoring users on the "OCEAN" model (Openness,
Conscientiousness, Extraversion, Agreeableness, Neuroticism) — that were then used to micro-target
political advertising designed to suppress Democratic voter turnout in the 2016 U.S. presidential
election and to target persuadable voters in the Brexit referendum [23, 24].

**Psychographic profiling and micro-targeted disinformation.** Research by Michal Kosinski and
colleagues demonstrated that Facebook "likes" alone could predict personality traits, political
orientation, sexual orientation, and other personal attributes with significant accuracy [25]. The
Brennan Center for Justice has documented the democratic harm: when behavioral data enables
targeting individuals at their psychological vulnerabilities with customized messaging, the
epistemic conditions for democratic deliberation are systematically undermined [26].

**Political advertising scale.** Digital political advertising in the 2024 U.S. election cycle
reached approximately $1.1 billion, with the vast majority of targeted advertising running on
platforms using behavioral profiling [27]. No federal law currently restricts the use of behavioral
data in political advertising targeting.

### 2.6 Predatory Advertising

**Targeting financial distress.** Data brokers sell audience segments explicitly identifying
financially distressed consumers — "high-risk credit card debts," "payday loan seekers," "financially
strapped" — to predatory lenders and debt collectors. The FTC's 2014 data broker report found that
brokers marketed such segments specifically for use in targeting vulnerable consumers with
high-cost financial products [2, 28].

**Targeting addiction and substance use.** Investigations by The Markup and others have documented
that Meta's advertising platform allowed advertisers to target users based on inferred addiction
signals — including combinations of interest categories tied to "gambling," "alcohol," and
opioid-related content engagement — enabling targeting of people at their points of maximum
vulnerability to predatory products [29].

**Targeting mental health vulnerabilities.** A 2022 investigation by The Markup found that Meta
allowed advertisers to target users based on engagement with content related to anxiety, depression,
and eating disorders through "interest" categories derived from behavioral tracking [30]. This
enables targeting emotionally vulnerable consumers at moments of psychological distress.

### 2.7 Public Benefits and Social Services

**Algorithmic benefits administration.** Government agencies and their private contractors
increasingly use algorithmic systems to determine eligibility for SNAP, Medicaid, Social Security
disability, and housing assistance. Virginia Eubanks's *Automating Inequality* (2018) documented
several such systems and found that they disproportionately denied benefits to low-income and
minority claimants through opaque algorithmic decisions that violated due process principles [22].

**Predictive policing and child welfare.** Law enforcement agencies use predictive policing
systems — some incorporating commercial data broker data — to allocate police resources and flag
individuals for surveillance. Child welfare agencies have deployed child maltreatment prediction
models that carry documented racial bias. A 2019 study examining child welfare algorithmic
decision-making found that such systems systematically assign higher risk scores to families from
lower-income and minority backgrounds in ways that reflect the historical patterns of reporting
bias rather than objective risk [33].

**Immigration enforcement.** ICE and CBP have purchased access to commercial data broker databases
including location records, utility connections, and financial data to identify and track
undocumented individuals. The Georgetown Law Center on Privacy and Technology documented that data
brokers including Thomson Reuters's CLEAR system supplied location and identity data directly to
ICE without judicial process, enabling surveillance of entire immigrant communities [34].

### 2.8 Healthcare and Reproductive Health

**Health data brokers.** The commercial health data sector — including IQVIA (formerly IMS Health),
Symphony Health, Definitive Healthcare, and OptimizeRx — trades in de-identified and
re-identifiable patient data derived from pharmacy benefit managers, electronic health records, and
insurance claims. IQVIA alone processes data on approximately 5 billion patients globally [35].
This data is sold to pharmaceutical companies for direct-to-consumer advertising targeting and to
insurers for underwriting in a regulatory gray zone that HIPAA does not clearly reach.

**Reproductive health tracking post-Dobbs.** Following the Supreme Court's June 2022 decision in
*Dobbs v. Jackson Women's Health Organization* overturning *Roe v. Wade*, reproductive health data
became a law enforcement risk. Period-tracking apps — including Flo, Clue, and Period Tracker —
had previously sold user data to Facebook and advertisers. Following Dobbs, they became potential
evidentiary sources in abortion prosecution investigations [36]. The FTC's June 2023 action against
Premom and its developer Easy Healthcare for sharing reproductive health data without consent was
the first federal enforcement action specifically targeting reproductive health data brokering [37].

**Mental health data.** The FTC reached a $7.8 million settlement with BetterHelp in March 2023
for sharing mental health intake and session data with Facebook for targeted advertising, in
violation of BetterHelp's own privacy promises to users. The settlement required user notification
and prohibited future sharing of health data for advertising — but the underlying legal exposure
for the broader mental health app industry remains unaddressed structurally [38].

---

## Part III: Economic Scale

### 3.1 Data Broker Industry Revenue

Estimates of the data broker industry's size vary depending on how broadly the industry is defined.
Key benchmarks:

- **Global data broker market:** Estimated at approximately $268 billion in 2021, projected to
  reach $462 billion by 2031 (Allied Market Research, 2022) [39].
- **Number of U.S. companies:** The FTC has estimated "hundreds" of data broker companies operating
  as of its 2014 study; privacy advocates and industry analysts now estimate over 4,000 entities
  collecting and selling personal data in the U.S. [2, 3].
- **FTC 2014 study baseline:** Nine data broker companies studied by the FTC in 2014 collectively
  generated revenues exceeding $426 million — suggesting current industry-wide revenues are
  substantially larger [2].

*[Evidence strength: Moderate. Revenue and market size figures derive primarily from commercial
market research reports (Allied Market Research, IBISWorld, Statista) using proprietary
methodologies. No independent peer-reviewed industry-wide revenue assessment exists. Figures
should be treated as directional indicators of scale rather than audited estimates.]*

### 3.2 Digital Advertising Market

The programmatic advertising market represents the primary immediate commercial output of the
surveillance data infrastructure:

- **U.S. digital advertising market:** Approximately $225 billion in revenue in 2023
  (IAB/PricewaterhouseCoopers Internet Advertising Revenue Report, 2024) [41].
- **Programmatic share:** Approximately 88% of all digital display advertising is purchased
  programmatically — through automated behavioral targeting auctions — representing well over
  $100 billion in annual U.S. spend [41].
- **Google and Meta combined market share:** Google (search and display) and Meta (Facebook and
  Instagram) together account for approximately 48% of total U.S. digital advertising revenue in
  2023 — approximately $108 billion — both built on behavioral surveillance infrastructure [42].
- **The Trade Desk** reported 2023 revenues of approximately $1.95 billion as the largest
  independent DSP, reflecting the scale of the non-Google/Meta programmatic market [43].

### 3.3 Consumer Welfare Extraction

Direct estimation of consumer harm from surveillance capitalism is methodologically difficult.
Available estimates:

- The FTC's 2025 Surveillance Pricing Study found evidence that individualized pricing based on
  consumer profiles resulted in higher prices for consumers with lower price-sensitivity, but did
  not quantify total consumer welfare loss [10].
- A Comparitech analysis estimated that the average American's personal data generates approximately
  $35 in advertising revenue annually for the platforms collecting it — a figure that substantially
  underestimates total commercial value because it excludes data broker resale revenues, insurance
  pricing impacts, and lending terms [44].
- Academic economists including Ariel Ezrachi and Maurice Stucke have argued that distributional
  harm from surveillance-based price discrimination likely involves large-scale consumer surplus
  transfer, but a peer-reviewed quantitative estimate of national welfare loss does not yet exist
  [45].

*[Evidence strength: Weak to moderate for aggregate consumer welfare loss. This is a significant
gap in the evidence base. Independent economic research quantifying the net consumer welfare
transfer from surveillance pricing, discriminatory underwriting, and predatory targeting would
substantially strengthen the policy case.]*

### 3.4 Market Concentration

The data broker and ad-tech ecosystem is highly concentrated at critical infrastructure nodes:

- **Identity resolution:** LiveRamp and Oracle Data Cloud are the dominant services linking offline
  consumer identities to digital behavioral profiles — a chokepoint position in the data pipeline [2].
- **Credit infrastructure:** Experian, TransUnion, and Equifax collectively control consumer credit
  reporting for 210 million Americans; Equifax's Work Number holds employment data on approximately
  114 million U.S. workers [15, 18].
- **Insurance data:** LexisNexis (C.L.U.E.) and CoreLogic dominate insurance underwriting data,
  collectively holding data on virtually all U.S. adults [13, 14].
- **Ad-tech vertical integration:** Google controls the dominant DSP (DV360), the dominant
  publisher ad server (Google Ad Manager), and the largest ad exchange — a vertical integration
  advantage that the DOJ challenged in antitrust litigation filed January 2023, with a judgment
  issued in August 2024 finding Google had monopolized the publisher ad server and ad exchange
  markets [46].
- **Government data:** Thomson Reuters's CLEAR and LexisNexis Risk Solutions are the dominant
  commercial aggregators of government and public records data sold to law enforcement, creating a
  private surveillance infrastructure operating in parallel to government systems [34].

---

## Part IV: Legal and Regulatory Landscape

### 4.1 Current Federal Law

#### Fair Credit Reporting Act (FCRA), 15 U.S.C. § 1681

The FCRA, enacted in 1970, governs "consumer reporting agencies" (CRAs) that compile "consumer
reports" — information bearing on creditworthiness, character, general reputation, or mode of
living — used in credit, insurance, employment, or housing decisions [4].

**What it covers:** Credit bureau reports, tenant screening, employment background checks
commissioned from third-party companies, and insurance underwriting reports.

**Critical gap — marketing exemption.** The FCRA explicitly exempts data compiled for direct
marketing, meaning the vast majority of data broker activity — including the sale of audience
segments, risk profiles, and "people finder" records — falls entirely outside its scope [4].

**Critical gap — no broker registration requirement.** The FCRA does not require data brokers to
disclose their existence, register with any agency, or notify consumers of what data they hold —
leaving consumers with no mechanism to discover which companies maintain files on them.

#### HIPAA, 42 U.S.C. § 1320d

HIPAA's Privacy Rule restricts use and disclosure of protected health information held by covered
entities — healthcare providers, health plans, and healthcare clearinghouses — and their business
associates.

**Critical gap — non-covered entities.** HIPAA does not govern collection and sale of health data
by companies that are not covered entities. This explicitly excludes health apps, period trackers,
wearables, fitness devices, mental health apps, and commercial health data brokers like IQVIA [5].
In 2022–2023, multiple investigations documented that pregnancy apps, period trackers, and mental
health apps were sharing user data with Facebook, Google, and data brokers with no HIPAA coverage
whatsoever.

#### FTC Act Section 5, 15 U.S.C. § 45

Section 5 prohibits "unfair or deceptive acts or practices" and is the FTC's primary consumer
protection authority [6]. Key limitations: no private right of action; civil penalties available
only for repeat violations absent a specific rule; enforcement is reactive and company-by-company;
the current FTC (Chairman Andrew Ferguson, 2025) has deprioritized commercial surveillance
enforcement.

#### FTC Commercial Surveillance Rulemaking (Initiated 2022)

In September 2022, the FTC under Chair Lina Khan initiated rulemaking under FTC Act Section 18 to
govern commercial surveillance and data security practices. The ANPR received over 11,000 public
comments [31]. The rulemaking was effectively suspended following the administration change in
January 2025.

#### COPPA, 15 U.S.C. § 6501

The Children's Online Privacy Protection Act restricts collection of personal data from children
under 13 and was amended by the FTC in January 2025 to further restrict monetization of children's
data. COPPA does not apply to children ages 13–17, creating a significant gap for adolescent data
collection at an age of heightened psychological vulnerability.

### 4.2 State Law

#### California — CCPA/CPRA

The California Consumer Privacy Act (2018, Cal. Civ. Code § 1798.100 et seq.), amended by
Proposition 24 (CPRA, 2020), provides the strongest U.S. consumer data rights framework [47].
Core rights: access, deletion, correction, opt-out of sale/sharing, limitation of sensitive data
use, and non-discrimination for rights exercise. The CPRA created the California Privacy Protection
Agency (CPPA) as an independent enforcement body with rulemaking authority.

**The California DELETE Act (AB 947, 2023).** Signed October 2023, the DELETE Act requires data
brokers registered with the CPPA to honor consumer deletion requests through a single centralized
mechanism, eliminating the current requirement that consumers contact each of thousands of brokers
individually. The CPPA must operationalize the deletion mechanism by January 1, 2026 [48]. As of
2024, over 500 data brokers had registered with California under this and preceding frameworks —
substantially more than Vermont's registry, reflecting California's market leverage.

#### Virginia — Consumer Data Protection Act (CDPA)

Virginia's CDPA (Va. Code § 59.1-571 et seq., effective 2023) establishes rights to access,
correct, delete, and opt out of processing for targeted advertising, sale, and certain profiling
[49]. Enforcement is exclusively by the Attorney General; there is no private right of action.

#### Colorado Privacy Act

Colorado's CPA (effective July 2023) follows Virginia's model with an additional requirement that
businesses honor universal opt-out mechanisms — including the Global Privacy Control browser signal
— beginning July 2024 [50]. This is a more consumer-friendly architecture than systems requiring
per-company opt-out requests.

#### Vermont — Data Broker Registration (Act 171, 2018)

Vermont was the first state to require data broker registration, requiring companies that
"knowingly collect and sell or license to third parties the brokered personal information of a
Vermont consumer" to register annually and disclose data collection practices. As of 2023,
approximately 121 companies had registered — widely understood to be a significant undercount
because the definition is narrow and enforcement resources are minimal [40].

#### Illinois — Biometric Information Privacy Act (BIPA)

BIPA (740 ILCS 14, 2008) requires informed written consent before collecting biometric identifiers
(fingerprints, iris scans, facial geometry, voiceprints) and includes a private right of action
with statutory damages of $1,000–$5,000 per violation. BIPA litigation has produced the most
significant U.S. privacy enforcement outcomes to date: a $650 million settlement by Facebook in
2021 for facial recognition and a $92 million settlement by TikTok in 2021 [51]. These outcomes
demonstrate the enforcement power of private rights of action for data privacy — a model missing
from every other U.S. privacy law.

### 4.3 Notable Enforcement Actions and Their Limits

**FTC v. InMarket (January 2024).** Ordered InMarket to stop selling precise location data and
delete previously collected holdings. Imposed no monetary penalty — only injunctive relief,
reflecting the FTC's limited first-offense penalty authority [52].

**FTC v. X-Mode/Outlogic (2024).** Ordered Outlogic to stop selling precise location data and
delete holdings. Again, no monetary penalty available as a first violation [52].

**FTC v. Kochava (filed August 2022, ongoing).** The FTC sued data broker Kochava for selling
geolocation data that could identify visitors to abortion providers, addiction treatment centers,
and domestic violence shelters — framing the practice as an unfair trade practice. Kochava
contested the case aggressively, making this the most significant test of whether FTC Section 5
authority can reach the core data brokering business model [53].

**FTC v. BetterHelp (March 2023).** The FTC settled with BetterHelp for $7.8 million for sharing
mental health data with Facebook for advertising, in violation of the company's own privacy
promises. The settlement required consumer notification and prohibited future health data sharing
for advertising [38].

**Structural gap:** Every FTC data broker enforcement action to date has targeted individual
companies for specific disclosures or data sales. None has challenged the underlying business
model — the collection, aggregation, and sale of consumer profiles without consent or notice at
scale. The structural problem remains wholly unaddressed by current enforcement.

### 4.4 EU Approach: GDPR, ePrivacy Directive, DSA/DMA

#### GDPR (Regulation (EU) 2016/679)

The GDPR, in force since May 2018, establishes several principles directly targeting surveillance
capitalism:

- **Lawful basis (Article 6):** Personal data processing requires a lawful basis — and consent must
  be "freely given, specific, informed and unambiguous." Most commercial tracking and data brokering
  does not meet this standard.
- **Purpose limitation (Article 5(1)(b)):** Data collected for advertising cannot lawfully be
  repurposed for insurance underwriting or political profiling.
- **Data minimization (Article 5(1)(c)):** Only data "adequate, relevant and limited to what is
  necessary" for the stated purpose may be collected.
- **Automated decision-making (Article 22):** Individuals have the right not to be subject to
  solely automated decisions producing legal or similarly significant effects — covering credit
  scoring, insurance underwriting, and employment screening [54].

**Enforcement reality:** GDPR enforcement has been slow and fragmented. Ireland's Data Protection
Commission — the lead supervisory authority for most major U.S. platforms due to their European
headquarters in Ireland — issued fines against Meta, WhatsApp, and Twitter between 2018 and 2023.
Critics note these fines, while large in absolute terms, represent fractions of single-quarter
revenue and have not produced structural behavioral change in data collection practices.

#### ePrivacy Directive (2002/58/EC)

The ePrivacy Directive requires informed consent before placing tracking cookies — the legal basis
for consent popups on European websites. A proposed ePrivacy Regulation (COM(2017) 10), intended
to strengthen and extend these requirements, has been stalled in EU legislative negotiations since
2017 due to sustained industry lobbying against consent requirements for RTB [55].

#### Digital Services Act and Digital Markets Act

The **DSA** (Regulation (EU) 2022/2065), in force for large platforms since February 2024,
prohibits targeting of advertising based on sensitive personal data, prohibits behavioral targeting
of minors, and requires large platforms to maintain ad transparency repositories.

The **DMA** (Regulation (EU) 2022/1925) designates large platform "gatekeepers" — including
Google, Meta, Apple, Amazon, Microsoft, and TikTok — and prohibits combining personal data across
services without explicit consent, directly targeting the cross-service data accumulation that
underlies surveillance capitalism at the platform level [56].

**What the EU covers that U.S. law does not:**
- Structural prohibition on combining data across services without explicit consent
- Per-violation fines up to 4% of global annual revenue (GDPR), 6% (DMA), 20% for DMA repeat
  violations
- Private rights of action for individuals and civil society organizations (DSA)
- Mandatory algorithmic transparency for recommender systems (DSA)
- Prohibition on behavioral micro-targeting of minors for advertising (DSA)

### 4.5 Key Legislative Proposals

**American Data Privacy and Protection Act (ADPPA, H.R. 8152, 117th Congress, 2022).** The most
advanced comprehensive federal privacy bill in U.S. history, passing the House Energy and Commerce
Committee on July 20, 2022 by 53-2 with bipartisan support [57]. Would have established a national
data minimization standard, prohibited targeted advertising based on sensitive data, created a
limited private right of action, required algorithmic impact assessments, and preempted most state
laws. Stalled in the full House primarily over California's opposition to CPRA preemption. Not
reintroduced in the 119th Congress as of this writing.

**My Data My Decisions Act (proposed).** Would require explicit, affirmative opt-in consent before
a data broker may sell, license, or trade personal data — reversing the current opt-out default
and bringing U.S. law in line with GDPR consent principles.

**California DELETE Act (AB 947, enacted 2023).** State-level model for a centralized deletion
mechanism enabling consumers to opt out of all registered data broker holdings in a single
interaction. Widely viewed as the most practical near-term structural consumer reform [48].

**Kids Online Safety Act (KOSA, S. 1409, 118th Congress).** Passed the Senate 91-3 on July 30,
2024; did not pass the House in the 118th Congress [58]. Would impose a duty of care on platforms
regarding minor users and restrict behavioral targeting of minors. Reintroduction expected in the
119th Congress.

**Federal Data Broker Registration Acts (various proposals).** Multiple bills have been introduced
requiring FTC registration of data brokers, disclosure of data practices, and consumer opt-out
mechanisms. None has advanced to a floor vote.

---

## Part V: Policy Proposals in Circulation

### 5.1 Prohibitionist Approaches

**Electronic Frontier Foundation (EFF)** has called for a comprehensive federal prohibition on the
commercial data brokering model, arguing that no regulatory middle ground — disclosure, consent,
registration — effectively controls the practice given the structural power asymmetry between
4,000+ brokers and individual consumers. The EFF supports an opt-in consent requirement so robust
it would effectively prohibit most commercial data brokering as currently practiced [59].

**Electronic Privacy Information Center (EPIC)** advocates for a federal privacy law built on data
minimization as a non-waivable default, arguing that consent-based frameworks are structurally
inadequate because consumers cannot meaningfully evaluate data sharing implications across
thousands of use cases. EPIC's model framework requires a demonstrated legitimate purpose for each
data use, with no legitimate purpose available to justify commercial data brokering as currently
practiced [60].

### 5.2 Structural Remedies (Non-Prohibitionist)

**Brennan Center for Justice** has focused on political and democratic harms, emphasizing regulation
of micro-targeted political advertising, prohibition on psychographic profiling for political
purposes, and public funding of online political communication as a structural alternative to
surveillance-funded political speech [26].

**Georgetown Law Center on Privacy and Technology** has focused on surveillance and discrimination
harms in the immigration and criminal justice contexts, documenting data broker sales to ICE and
CBP and advocating for prohibition on selling precise location, immigration status, and sensitive
demographic data to law enforcement agencies without judicial process [34].

**Access Now** has documented the international dimension: U.S. data broker infrastructure enables
authoritarian surveillance globally when behavioral data on diaspora communities and political
activists is commercially accessible to foreign governments through data broker channels [61].

### 5.3 Data Minimization Mandates

Data minimization — limiting collection to what is necessary for a specific, disclosed purpose —
is the foundational upstream reform endorsed by most policy frameworks. A federal mandate would
require: (1) a clear, specific, disclosed purpose for each data category; (2) prohibition on
collection beyond that purpose; (3) prohibition on repurposing data for materially different uses
without new consent; (4) automatic deletion when data is no longer necessary; and (5) prohibition
on "purpose creep" through progressively expanding privacy policy language.

The ADPPA contained data minimization provisions along these lines. The GDPR operationalizes this
principle in European law. No U.S. federal statute currently mandates data minimization for
commercial data collection.

### 5.4 Data Broker Registration and Prohibition Models

**Vermont model (Act 171, 2018):** Registration, basic disclosure, and security requirements. Does
not prohibit any specific practices. Has established the legal and administrative feasibility of a
registry but has produced minimal consumer protection in practice due to narrow definitions and
limited enforcement capacity [40].

**California DELETE Act model (AB 947, 2023):** More ambitious — a centralized consumer-facing
deletion mechanism operated by a state agency, eliminating the practical impossibility of
individual opt-out requests to 4,000+ brokers. Widely viewed as the most practical near-term
structural reform at the state level. A federal analog — a centralized deletion mechanism operated
by the FTC — has been proposed by multiple advocacy organizations [48].

**Categorical prohibition model:** Prohibiting data brokers from selling specific high-harm data
categories without explicit opt-in consent: precise location, reproductive health, mental health
indicators, immigration status, political and religious beliefs, and sexual orientation. This
targeted approach may be more achievable near-term than comprehensive prohibition.

### 5.5 Opt-In vs. Opt-Out Consent Models

The central architectural question in data broker regulation is whether the default is opt-in
(no data sale without explicit consent) or opt-out (data may be sold unless the consumer acts
to prevent it). U.S. law is overwhelmingly opt-out — where any mechanism exists at all. The GDPR
is opt-in for most processing. CCPA/CPRA is opt-out for sale and sharing, with opt-in required
only for sensitive data and minors.

**The case for opt-in:** Studies consistently find fewer than 5% of consumers exercise available
opt-out rights, and doing so requires knowing which of 4,000+ brokers holds your data and
navigating separate mechanisms for each. The opt-out default is not a neutral architecture — it
allocates brokers' commercial rights over consumer data as the legal baseline. Shifting to opt-in
is the most structurally significant change available short of outright prohibition.

**Industry argument for opt-out:** Opt-in consent would destroy the surveillance-funded digital
advertising economy. This argument treats the current surveillance model as the natural baseline
rather than a policy choice, and conflates the interests of advertisers in behavioral targeting
with the interests of consumers whose data is being extracted.

### 5.6 Right to Erasure and Centralized Deletion

The right to delete personal data held by data brokers is present in all major state privacy laws
but practically unexercisable due to fragmentation. The DELETE Act's centralized mechanism is the
most meaningful implementation of this right to date. A federal right to erasure with a centralized
FTC-operated mechanism, mandatory data broker registration, and civil penalties for non-compliance
would be the single most impactful consumer-facing reform short of prohibition.

### 5.7 Algorithmic Accountability Proposals

**Algorithmic impact assessments.** The ADPPA required assessments for "high-impact automated
decision systems" — making decisions about credit, employment, housing, education, or healthcare.
The EU AI Act's risk management framework operationalizes a similar requirement for high-risk AI
systems in these domains.

**Auditability and transparency.** Academic proposals from the AI Now Institute, the Algorithmic
Justice League, and researchers including Joy Buolamwini and Safiya Umoja Noble emphasize that
accountability requires auditability: the ability of regulators and affected individuals to
understand what data inputs drove a decision. Current U.S. law does not require this transparency
for commercial applications.

**CFPB adverse action notice extension.** The CFPB has proposed applying Equal Credit Opportunity
Act adverse action notice requirements to algorithmic credit decisions — requiring explanation of
which factors drove a denial in terms consumers can understand and challenge [17]. This
"algorithmic adverse action" framework extends existing civil rights law to AI decision systems and
represents a template for similar requirements in insurance, employment, and housing.

---

## Part VI: Cross-Cutting Structure

### 6.1 How Surveillance Capitalism Spans Policy Domains

Surveillance capitalism is not a single policy problem but an infrastructure problem — the same
data collection, brokering, and profiling infrastructure underlies harms across every major policy
domain:

| Policy Domain | Surveillance Capitalism Mechanism | Specific Harm |
|---|---|---|
| **Consumer protection** | Willingness-to-pay profiling; predatory targeting | Price extraction; predatory advertising targeting distress |
| **Civil rights / anti-discrimination** | Discriminatory profiling in insurance, credit, employment | Adverse decisions using race/income proxies |
| **Labor / employment** | Behavioral scoring; social media screening; gig deactivation | Employment discrimination; worker surveillance |
| **Healthcare** | Health data brokering; reproductive health tracking | HIPAA gaps; Dobbs prosecution risk; mental health exploitation |
| **Elections / democracy** | Psychographic profiling; micro-targeted political advertising | Political manipulation; voter suppression |
| **Criminal justice** | Predictive policing; data sales to law enforcement | Discriminatory surveillance; due process violations |
| **Immigration** | Data broker sales to ICE/CBP; location tracking | Surveillance of immigrant communities |
| **Children and youth** | Minors' behavioral data; attention and engagement extraction | Developmental harm; COPPA violations; mental health impacts |

### 6.2 Dedicated Pillar vs. Domain-Specific Treatment

Some harms are best addressed in domain-specific frameworks:

- **Healthcare data:** A HIPAA extension to non-covered entities is most coherent within a
  healthcare policy family.
- **Credit discrimination:** FCRA reform and CFPB authority belong most naturally in a consumer
  finance framework.
- **Political advertising:** Political data regulation fits most naturally in an elections/democracy
  pillar.
- **Employment screening:** Background check FCRA reform connects most naturally to a labor and
  workers' rights pillar.

However, the **infrastructure layer** — data broker registration, data minimization, consent
architecture, RTB regulation, and enforcement mechanisms — is necessarily cross-cutting and
requires a dedicated surveillance capitalism pillar. Without upstream regulation of the data
collection and brokering infrastructure, domain-specific protections will be systematically
circumvented: health data collected outside HIPAA, credit signals inferred from behavioral data,
discriminatory targeting accomplished through proxies that technically comply with each
domain-specific rule.

### 6.3 Natural Policy Families Within a Surveillance Capitalism Pillar

Based on this analysis, five natural policy families emerge within a surveillance capitalism and
data broker pillar:

**1. Data Broker Regulation**
- Federal data broker registration with the FTC
- Centralized deletion mechanism (DELETE Act model at federal scale)
- Prohibition on sale of specific sensitive data categories without opt-in consent
- Meaningful civil penalties per violation (not first-offense injunctive-only)

**2. Ad-Tech and Real-Time Bidding Reform**
- RTB bid request data minimization — restrict what data may be transmitted in bid requests
- Prohibition on behavioral targeting based on sensitive data categories
- Ban on behavioral advertising targeting of minors (KOSA model)
- Mandatory ad transparency repository (DSA model)

**3. Behavioral Modification and Manipulation Prohibition**
- Prohibition on dark patterns designed to override user decisions
- Restrictions on manipulative engagement optimization targeting vulnerable populations
- Prohibition on psychographic targeting in political advertising
- Engagement design restrictions for minors (variable reinforcement, infinite scroll)

**4. Algorithmic Discrimination Prohibition**
- Extension of FCRA coverage to data brokers whose products are used in consequential decisions
- Mandatory algorithmic impact assessments for high-stakes automated decisions
- Adverse action notice requirements for algorithmic decisions in credit, insurance, housing,
  employment (CFPB adverse action model extended)
- Civil rights enforcement mechanisms for algorithmic discrimination

**5. Enforcement Architecture**
- Private right of action for consumers (BIPA model)
- FTC civil money penalty authority for first-time violations
- State AG concurrent enforcement authority
- Whistleblower protections for data broker and ad-tech industry employees
- Consumer compensation mechanism for documented data misuse harms

---

## References

[1] Zuboff, S. (2019). *The age of surveillance capitalism: The fight for a human future at the
new frontier of power*. PublicAffairs.

[2] Federal Trade Commission. (2014, May). *Data brokers: A call for transparency and
accountability*. Federal Trade Commission.
https://www.ftc.gov/system/files/documents/reports/data-brokers-call-transparency-accountability-report-federal-trade-commission-may-2014/140527databrokerreport.pdf

[3] Privacy Rights Clearinghouse. (2023). *Data brokers: A threat to civil liberties*.
Privacy Rights Clearinghouse. https://privacyrights.org/data-brokers

[4] Fair Credit Reporting Act, 15 U.S.C. § 1681 (1970).
https://www.law.cornell.edu/uscode/text/15/chapter-41/subchapter-III

[5] U.S. Department of Health and Human Services, Office for Civil Rights. (2022). *Health
information privacy: HIPAA and health apps.* HHS. https://www.hhs.gov/hipaa/for-professionals/
special-topics/health-information-technology/index.html [HIPAA non-covered entity gap confirmed
via HHS regulatory guidance and FTC enforcement actions against health apps not subject to HIPAA.]

[6] Federal Trade Commission Act, 15 U.S.C. § 45 (1914).
https://www.law.cornell.edu/uscode/text/15/45

[7] Pasquale, F. (2015). *The black box society: The secret algorithms that control money and
information*. Harvard University Press.

[8] Irish Council for Civil Liberties. (2022). *ICCL's 2022 report on the scale of real-time
bidding data broadcasts in the U.S. and Europe*. ICCL. https://www.iccl.ie/digital-data/
rtb-report-2022/

[9] Google. (2024, July). *Privacy sandbox: Updates to our approach to third-party cookies*.
Google Developers Blog. https://privacysandbox.com [Google reversed course on cookie deprecation
in July 2024, announcing retention of third-party cookies with added user controls rather than
removal.]

[10] Federal Trade Commission. (2025, January). *Surveillance pricing study report*. Federal Trade
Commission. [Report released approximately January 14, 2025, under study docket P225402, during
the final days of the Khan-era FTC. Subsequently removed from the FTC website following the
administration change. Confirmed via contemporaneous news accounts and FTC press release archives.]

[11] Douglas, J., & Hunter, J. (2020). *The true cost of auto insurance in 2020*. Consumer
Federation of America. https://consumerfed.org/reports/the-true-cost-of-auto-insurance-in-2020/

[12] Coyne, J., Maharrey, M., & McDonald, J. (2021, April 5). Minority neighborhoods pay higher
car insurance premiums than white areas with the same risk. *ProPublica*.
https://www.propublica.org/article/minority-neighborhoods-higher-car-insurance-premiums-white-areas-same-risk

[13] LexisNexis Risk Solutions. *C.L.U.E. personal property report overview*. LexisNexis.
[CLUE database practices are documented in LexisNexis product materials, FCRA regulatory guidance,
and CFPB specialty consumer reporting agency oversight. See also CFPB supervision of specialty
CRAs at https://www.consumerfinance.gov/consumer-tools/credit-reports-and-scores/]

[14] National Fair Housing Alliance. (2023). *Redlining redux: Algorithmic discrimination in
homeowners insurance*. National Fair Housing Alliance. [Documents use of CoreLogic and similar
property data vendors in insurance underwriting with discriminatory effects.]

[15] Consumer Financial Protection Bureau. (2023, March). *Consumer reporting market report*.
CFPB. https://www.consumerfinance.gov/data-research/research-reports/consumer-reporting-market-report/

[16] Consumer Financial Protection Bureau. (2021). *Supervisory highlights: Consumer reporting
special edition*. CFPB. https://www.consumerfinance.gov/data-research/research-reports/
supervisory-highlights-consumer-reporting-special-edition-issue-23/

[17] Consumer Financial Protection Bureau. (2022, May). *Adverse action notification requirements
and the Equal Credit Opportunity Act's role in combating digital redlining*. CFPB Blog.
https://www.consumerfinance.gov/about-us/blog/adverse-action-notification-requirements-and-the-
equal-credit-opportunity-acts-role-in-combating-digital-redlining/

[18] Equifax. *The Work Number: Workforce solutions*. Equifax. [Equifax states The Work Number
holds records from 2.7 million employers covering approximately 114 million workers. See Equifax
investor materials and The Work Number product documentation at
https://www.theworknumber.com/employers/]

[19] Professional Background Screening Association. (2022). *Background screening industry
overview and member survey*. PBSA. [Industry revenue and employer usage rate figures from PBSA
annual survey data; $4 billion revenue estimate and ~90% employer usage widely cited in industry
and regulatory reports.]

[20] CareerBuilder. (2018). *More than half of employers have found content on social media that
caused them not to hire a candidate, according to recent CareerBuilder survey*. CareerBuilder
press release. [Widely cited; 70% employer social media screening figure from this survey.]

[21] Equal Employment Opportunity Commission. (2012). *Consideration of arrest and conviction
records in employment decisions under Title VII of the Civil Rights Act of 1964*. EEOC Guidance
Document No. 915.002. https://www.eeoc.gov/laws/guidance/enforcement-guidance-consideration-
arrest-and-conviction-records-employment-decisions

[22] Eubanks, V. (2018). *Automating inequality: How high-tech tools profile, police, and punish
the poor*. St. Martin's Press.

[23] Cadwalladr, C., & Graham-Harrison, E. (2018, March 17). Revealed: 50 million Facebook
profiles harvested for Cambridge Analytica in major data breach. *The Guardian*.
https://www.theguardian.com/news/2018/mar/17/cambridge-analytica-facebook-influence-us-election
[Facebook later confirmed 87 million profiles were affected; the Guardian's original figure of
50 million was revised upward in subsequent reporting.]

[24] Wylie, C. (2019). *Mindf*ck: Cambridge Analytica and the plot to break America*. Random House.

[25] Kosinski, M., Stillwell, D., & Graepel, T. (2013). Private traits and attributes are
predictable from digital records of human behavior. *Proceedings of the National Academy of
Sciences*, *110*(15), 5802–5805. https://doi.org/10.1073/pnas.1218772110

[26] Brennan Center for Justice. (2022). *Digital flyers and dark patterns: Political ad
transparency in the 2022 midterms*. Brennan Center for Justice.
https://www.brennancenter.org/our-work/research-reports/digital-flyers-and-dark-patterns-political-ad-transparency-2022-midterms

[27] AdImpact. (2024). *2024 election cycle political advertising report*. AdImpact. [Digital
political advertising figure of approximately $1.1 billion for the 2024 cycle derived from AdImpact
and Kantar tracking data, widely reported in political media covering the 2024 election cycle.]

[28] Federal Trade Commission. (2014, December). *Data broker: A call for transparency and
accountability — Supplemental report: Data brokers and "financially distressed" consumer segments*.
Federal Trade Commission. [Supplemental FTC findings documenting sale of financially distressed
consumer segments; core findings confirmed in the 2014 full broker report [2].]

[29] Matsakis, L. (2020, September 24). The many ways Facebook has failed to protect users' data.
*Wired*. [Alongside related reporting by The Markup; see Keegan, J., & Oremus, W. (2021, October).
Facebook's addiction targeting. The Markup, Gizmodo network investigations.]

[30] Keegan, J., & Eastwood, J. (2022, June 16). Facebook is receiving sensitive medical
information from hospital websites. *The Markup*.
https://themarkup.org/pixel-hunt/2022/06/16/facebook-is-receiving-sensitive-medical-information-from-hospital-websites

[31] Federal Trade Commission. (2022, September). *Commercial surveillance and data security:
Advance notice of proposed rulemaking*. Federal Register, 87 FR 51273.
https://www.federalregister.gov/documents/2022/08/22/2022-17752/commercial-surveillance-and-data-security

[32] Benjamin, R. (2019). *Race after technology: Abolitionist tools for the new Jim code*.
Polity Press. [Cited for algorithmic racial bias framework; see also Noble, S. U. (2018).
*Algorithms of oppression*. NYU Press.]

[33] Brown, A., Chouldechova, A., Putnam-Hornstein, E., Tobin, A., & Vaithianathan, R. (2019).
Toward algorithmic accountability in public services: A qualitative study of affected community
perspectives on algorithmic decision-making in child welfare services. *Proceedings of the 2019
CHI Conference on Human Factors in Computing Systems*, 1–12.
https://doi.org/10.1145/3290605.3300271

[34] Upturn & Georgetown Law Center on Privacy and Technology. (2021). *American dragnet:
Data-driven deportation in the 21st century*. Georgetown Law Center on Privacy and Technology.
https://americandragnet.org

[35] IQVIA. (2023). *2023 annual report*. IQVIA Holdings, Inc. [IQVIA's claim of approximately
5 billion patient records globally is from company investor materials and annual reports; reviewed
for accuracy against IQVIA corporate disclosures.]

[36] Hill, K. (2022, June 30). Period-tracking apps: What to know about privacy post-Roe.
*The New York Times*.
https://www.nytimes.com/2022/06/30/technology/period-tracking-apps-privacy.html

[37] Federal Trade Commission. (2023, May). *FTC takes action against Easy Healthcare Corporation
for Premom pregnancy tracking app's sharing of users' sensitive health data*. FTC press release.
https://www.ftc.gov/news-events/news/press-releases/2023/05/ftc-takes-action-against-easy-healthcare-corporation-sharing-users-sensitive-health-data

[38] Federal Trade Commission. (2023, March). *FTC returns $7.8 million to BetterHelp users who
had sensitive mental health data shared with Facebook and Snapchat*. FTC press release.
https://www.ftc.gov/news-events/news/press-releases/2023/03/ftc-returns-75-million-betterhelp-users-who-had-sensitive-mental-health-data-shared-facebook

[39] Allied Market Research. (2022). *Data broker market: Global opportunity analysis and industry
forecast, 2021–2031*. Allied Market Research.
https://www.alliedmarketresearch.com/data-broker-market [Commercial market research estimate;
methodology not independently audited. Treat as directional indicator only.]

[40] Vermont Secretary of State. (2023). *Data broker registry*. Vermont Secretary of State.
https://sos.vermont.gov/corporations/other-business-types/data-brokers/

[41] Interactive Advertising Bureau & PricewaterhouseCoopers. (2024). *IAB/PwC internet
advertising revenue report: 2023 full year results*. IAB.
https://www.iab.com/insights/internet-advertising-revenue-report/

[42] Insider Intelligence / eMarketer. (2024). *US digital advertising market share 2024*.
eMarketer. [Google and Meta combined market share figures from eMarketer annual digital advertising
market forecast reports. Approximately 48% combined share figure as of 2023.]

[43] The Trade Desk, Inc. (2024). *Annual report on Form 10-K, fiscal year ended December 31,
2023*. SEC EDGAR.
https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=TTD&type=10-K

[44] Comparitech. (2021). *How much is your data worth on the dark web?* Comparitech.
https://www.comparitech.com/blog/information-security/personal-data-worth/ [Estimate of $35 in
annual advertising value per American; a floor estimate that excludes data broker resales and
downstream commercial uses.]

[45] Ezrachi, A., & Stucke, M. E. (2016). *Virtual competition: The promise and perils of the
algorithm-driven economy*. Harvard University Press.

[46] United States v. Google LLC, No. 1:23-cv-00108 (E.D. Va., filed January 24, 2023). Judgment
issued August 5, 2024, finding Google had monopolized the publisher ad server and open-web display
advertising exchange markets. *United States v. Google LLC*, No. 1:23-cv-00108, 2024 WL 3647498
(E.D. Va. Aug. 5, 2024).

[47] California Consumer Privacy Act of 2018, as amended by Proposition 24 (California Privacy
Rights Act of 2020), Cal. Civ. Code § 1798.100 et seq.
https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?sectionNum=1798.100.&lawCode=CIV

[48] California DELETE Act, AB 947, Cal. Civ. Code § 1798.99.80 et seq. (enacted October 2023).
https://leginfo.legislature.ca.gov/faces/billNavClient.xhtml?bill_id=202320240AB947

[49] Virginia Consumer Data Protection Act, Va. Code Ann. § 59.1-571 et seq. (2021, effective
January 1, 2023). https://law.lis.virginia.gov/vacode/title59.1/chapter53/

[50] Colorado Privacy Act, Colo. Rev. Stat. § 6-1-1301 et seq. (2021, effective July 1, 2023).
https://leg.colorado.gov/bills/sb21-190

[51] *In re Facebook Biometric Information Privacy Litigation*, No. 3:15-cv-03747-JD (N.D. Cal.
2021) [$650 million settlement approved February 26, 2021]. *In re TikTok, Inc. Consumer Privacy
Litigation*, No. 1:20-cv-04699 (N.D. Ill. 2021) [$92 million settlement].

[52] Federal Trade Commission. (2024, January). *FTC orders InMarket to stop selling precise
consumer location data*. FTC press release.
https://www.ftc.gov/news-events/news/press-releases/2024/01/ftc-orders-inmarket-stop-selling-precise-consumer-location-data
[X-Mode/Outlogic: FTC. (2024, January). *FTC order prohibits data broker X-Mode Social and Outlogic from selling sensitive location data*. https://www.ftc.gov/news-events/news/press-releases/2024/01/
ftc-order-prohibits-data-broker-x-mode-social-outlogic-selling-sensitive-location-data]

[53] *Federal Trade Commission v. Kochava Inc.*, No. 2:22-cv-00349-BLW (D. Idaho, filed August 29,
2022). [Ongoing as of this writing; represents most significant test of FTC Section 5 authority
over core data brokering activity.]

[54] Regulation (EU) 2016/679 (General Data Protection Regulation), Article 22 — Automated
individual decision-making, including profiling. Official Journal of the European Union, L 119,
May 4, 2016. https://gdpr-info.eu/art-22-gdpr/

[55] Directive 2002/58/EC of the European Parliament and of the Council (ePrivacy Directive), as
amended by Directive 2009/136/EC. Official Journal of the European Union. [Proposed ePrivacy
Regulation, COM(2017) 10 final, stalled in EU Council since 2017.]

[56] Regulation (EU) 2022/1925 of the European Parliament and of the Council (Digital Markets
Act), Official Journal of the European Union, L 265, September 12, 2022.
https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX%3A32022R1925

[57] American Data Privacy and Protection Act, H.R. 8152, 117th Congress (2022). Passed House
Energy and Commerce Committee July 20, 2022, 53-2. Did not advance to House floor.
https://www.congress.gov/bill/117th-congress/house-bill/8152

[58] Kids Online Safety Act, S. 1409, 118th Congress (2023–2024). Passed Senate 91-3, July 30,
2024. Did not pass the House in the 118th Congress.
https://www.congress.gov/bill/118th-congress/senate-bill/1409

[59] Electronic Frontier Foundation. (2023). *The EFF's position on federal privacy legislation*.
EFF. https://www.eff.org/issues/privacy

[60] Electronic Privacy Information Center. (2023). *EPIC's framework for data protection and
algorithmic transparency*. EPIC. https://epic.org/issues/data-protection/model-legislation/

[61] Access Now. (2023). *Surveillance and human rights*. Access Now.
https://www.accessnow.org/campaign/surveillance-human-rights/

---
