# Current State

## Source-of-truth order

1. Formal structured IDs in `sources/branch_political_project_brainstorm.txt` and `sources/branch_branch_political_project_main.txt` (primary sources)
2. Later contextual summary blocks in those chats when earlier mappings conflict
3. `data/policy_catalog.sqlite`
4. Pillar markdown under `pillars/` (rebuilt July 2025 — now current with the DB)

## Pillar structure

The `pillars/` directory was fully rebuilt in July 2025. Each of the 17 pillars now has two files:

- `overview.md` — purpose, core principle, design logic, research synthesis
- `policy.md` — all canonical rules from the DB for that pillar's scope codes

### The 17 pillars

| # | Directory | Scope Codes | Rule Count |
|---|-----------|-------------|-----------|
| 1 | `executive_power/` | GOV | 13 |
| 2 | `elections_and_representation/` | ELE | 22 |
| 3 | `anti_corruption/` | COR | 15 |
| 4 | `equal_justice_and_policing/` | JUS | 136 |
| 5 | `rights_and_civil_liberties/` | RGT | 26 |
| 6 | `courts_and_judicial_system/` | JUD | 8 |
| 7 | `checks_and_balances/` | SYS, OVR | 52 |
| 8 | `taxation_and_wealth/` | ECO | 10 |
| 9 | `healthcare/` | HLT | 184 |
| 10 | `antitrust_and_corporate_power/` | COR-FIN, MED (prose + cross-scope) | 4+ |
| 11 | `information_and_media/` | MED, INF | 20 |
| 12 | `gun_policy/` | (prose; JUS-POL-006, JUS-POL-007) | 2+ |
| 13 | `term_limits_and_fitness/` | TRM | 8 |
| 14 | `administrative_state/` | ADM | 3 |
| 15 | `technology_and_ai/` | TEC | 361 |
| 16 | `immigration/` | IMM | 222 |
| 17 | `environment_and_agriculture/` | ENV, AGR, LAB, EDU | 15 |

**Total:** ~1,095 rules across 20 scope codes

## Catalog state

The current importer reconstructs four layers from the main and brainstorm chats:

1. **Canonical numeric checkpoint items** in `policy_items`
2. **Canonical structured rules** in `rule_items`
3. **Legacy-to-structured conversions** in `record_links`
4. **Contextual/prose-only ID mentions** in `prose_rule_mentions`

### Current totals (as of July 2025 rebuild)

- 101 `policy_items`
- 1,095 `rule_items` (across 20 scope codes)
- 138 `record_links`
- 888 `prose_rule_mentions`

### IDs promoted from context

These structured IDs were identified in the chats but had been missed by the first importer because they never appeared as canonical pipe-delimited rows:

- `ECO-TAX-001`
- `ADM-CHV-001`
- `ADM-AGY-001`
- `HLT-TRL-001`

### Why contextual mentions matter

Some IDs appear only in prose or summary sections. Context shows they are not all equally authoritative:

- some are **future split placeholders** like `ADM-CON-001A` / `ADM-CON-001B`
- some are **optional/procedural variants** like `ADM-OVR-001`
- some are **older families later replaced or reframed** like `SYS-STR-*` or `HLT-DRG-*`
- some may be **real but still-unformalized candidates** such as `RGT-LAB-001`, `ECO-WRK-001`, `JUS-CRJ-001`, `JUS-CRJ-002`, and `RGT-DET-003`

Those are intentionally preserved in `unresolved_prose_rule_mentions` instead of being silently promoted into the canonical rule corpus.

### Pillars with prose-only or partially formalized rules

- **gun_policy**: No GUN- scope code yet. Two cross-scope rules (JUS-POL-006, JUS-POL-007) are the only formalized entries. The policy.md lists proposed GUN- rules as placeholders pending formal DB seeding.
- **antitrust_and_corporate_power**: No dedicated scope code. Rules cross-reference COR-FIN and MED families. The policy.md documents the formal rules plus prose-level reform descriptions.

## Important context from the chats

- The migration map embedded in the chats is useful, but not always final. Later summary blocks and later formal rule rows sometimes supersede earlier ID assignments.
- The main and brainstorm branches currently contain the same structured corpus, but the brainstorm branch includes important contextual explanations about duplication, provisional IDs, and when not to split an item yet.
- Some policy areas are much more developed in the database than in the pillar markdown, especially healthcare governance (184 HLT rules), AI/tech (361 TEC rules), immigration (222 IMM rules), and justice/drug policy (136 JUS rules).
- If chat-log sources change, rebuild the catalog with `scripts/import_policy_catalog.py`, then the pillar docs should be reviewed against the new DB state.
