# Project Overview

## Core idea

This project is a **Third Bill of Rights** — completing Franklin Roosevelt's unfinished 1944 Second Bill of Rights and extending it into the 21st century.

The First Bill of Rights (1791) told government what it could not do to you. FDR's Second Bill recognized that political freedom is meaningless without material security. This project completes that work and adds what a new century demands: digital rights, bodily autonomy, algorithmic accountability, climate rights, and immigration dignity.

> *"You can't be free if you're sick, homeless, or in debt."*

See [`overview/third-bill-of-rights.md`](third-bill-of-rights.md) for the full framing declaration.

Beyond the rights framing, this project is building a complete system: a structured policy corpus, a narrative, and an implementation path organized from values to enforceable rules.

## Structural layers

The project has two primary public layers, plus internal working infrastructure:

1. **Foundations** (5 core values, `foundations/` directory) — The moral and political commitments that define what the project believes. Written to be public-facing, accessible, and resonant. Each foundation explains *why* the work matters before getting into *what* must change. See [`foundations/README.md`](../foundations/README.md) for the full index.
2. **Pillars** — domain-by-domain policy design (17 pillars, `pillars/` directory). Each pillar is anchored to one of the five foundations and contains `overview.md` (purpose and design logic) and `policy.md` (all canonical rules).
3. **System rules** — cross-domain constraints and design invariants
4. **Strategy** — communication, rollout, and coalition work
5. **Catalog data** — structured IDs for policy items and rules (`data/policy_catalog.sqlite`)

### The Five Foundations

The foundations layer sits above the pillars — it is the "why" that the pillars translate into "how." Each foundation is a short, plain-language statement of a core value, grounded in the reasoning developed across the source logs.

| Foundation | Core Belief |
|---|---|
| [Accountable Power](../foundations/accountable_power/values.md) | No one is above the law or beyond accountability |
| [Clean Democracy](../foundations/clean_democracy/values.md) | Government must answer to people, not money or corporations |
| [Equal Justice](../foundations/equal_justice/values.md) | The law applies equally to everyone, fairly and humanely |
| [Real Freedom](../foundations/real_freedom/values.md) | Rights must be explicit, enforceable, and protected |
| [Freedom to Thrive](../foundations/freedom_to_thrive/values.md) | Material security is a prerequisite for real freedom |

## The 17 Pillars

Each pillar has `overview.md` (purpose, design logic, research synthesis) and `policy.md` (all canonical DB rules):

1. **Executive Power** (`executive_power/`) — Limits on presidential authority, emergency powers, pardon reform
2. **Elections and Representation** (`elections_and_representation/`) — Voting rights, redistricting, campaign finance
3. **Anti-Corruption** (`anti_corruption/`) — Lobbying bans, conflicts of interest, emoluments, dark money
4. **Equal Justice and Policing** (`equal_justice_and_policing/`) — Criminal justice reform, policing, qualified immunity
5. **Rights and Civil Liberties** (`rights_and_civil_liberties/`) — Bodily autonomy, privacy, equality, speech
6. **Courts and Judicial System** (`courts_and_judicial_system/`) — Judicial ethics, Supreme Court reform, venue
7. **Checks and Balances** (`checks_and_balances/`) — Separation of powers, congressional oversight, federalism
8. **Taxation and Wealth** (`taxation_and_wealth/`) — Progressive taxation, automation tax, economic equity
9. **Healthcare** (`healthcare/`) — Universal coverage, drug pricing, mental health, AI in healthcare
10. **Antitrust and Corporate Power** (`antitrust_and_corporate_power/`) — Monopoly reform, platform regulation
11. **Information and Media** (`information_and_media/`) — Press freedom, public infrastructure, broadband
12. **Gun Policy** (`gun_policy/`) — Weapons regulation, background checks, red flag laws
13. **Term Limits and Fitness** (`term_limits_and_fitness/`) — Congressional term limits, fitness for office
14. **Administrative State** (`administrative_state/`) — Agency authority, Chevron deference, constitutional departments
15. **Technology and AI** (`technology_and_ai/`) — AI governance, surveillance, data privacy, platform regulation
16. **Immigration** (`immigration/`) — Legal pathways, asylum, due process, enforcement limits
17. **Environment and Agriculture** (`environment_and_agriculture/`) — Climate, biodiversity, regenerative farming

## Working principles

- Limit concentrated power.
- Protect rights as usable realities, not abstractions.
- Make core access less dependent on geography, wealth, or gatekeeping.
- Prefer enforceable structure over soft norms.
- Preserve source traceability as the project is reconstructed.

## Scope of the catalog

As of July 2025: **1,095 canonical rules** across **20 scope codes** in `data/policy_catalog.sqlite`. The three largest domains are Technology/AI (361 rules), Immigration (222 rules), and Healthcare (184 rules). See `overview/current-state.md` for the full breakdown and source-of-truth ordering.
