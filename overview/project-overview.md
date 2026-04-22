# Project Overview

## Core idea

This project is building a complete system for restoring fairness, accountability, and human dignity in modern society. It is meant to function as more than a policy list: it is a system, a narrative, and an implementation path.

## Structural layers

1. **Pillars** — domain-by-domain policy design (17 pillars, `pillars/` directory)
2. **System rules** — cross-domain constraints and design invariants
3. **Strategy** — communication, rollout, and coalition work
4. **Catalog data** — structured IDs for policy items and rules (`data/policy_catalog.sqlite`)

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
