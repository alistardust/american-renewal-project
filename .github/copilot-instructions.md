# Copilot Instructions

## Project context

This repository is reconstructing a document-first political/platform project from branch chat logs plus older markdown files. The policy corpus is centered on:

- `sources/chat-logs/main-branch.txt`
- `sources/chat-logs/brainstorm-branch.txt`
- `data/policy_catalog.sqlite`

The markdown under `pillars/` is useful, but may be outdated relative to the logs and database.

Read `overview/current-state.md` before making structural changes.

## Source of truth

Use this order when deciding what is current:

1. formal structured IDs in the main/brainstorm chat logs
2. later contextual summary blocks in those chats when earlier mappings conflict
3. `data/policy_catalog.sqlite`
4. legacy pillar markdown

Do **not** assume the current pillar files are complete.

## Working with IDs and the catalog

- The old numeric checkpoint items live in `policy_items`.
- The structured ID system lives in `rule_items`.
- Legacy-to-structured conversions live in `record_links`.
- Prose/context-only IDs live in `prose_rule_mentions`.
- Use `deduped_catalog_entries` when you want the canonical structured corpus without the legacy numeric duplicates.
- Use `unresolved_prose_rule_mentions` when auditing IDs that were mentioned in context but not promoted into the canonical rule corpus.

If chat-log sources change, rebuild the catalog with:

```bash
scripts/import_policy_catalog.py
```

Do not hand-edit `data/policy_catalog.sqlite`.

## Known context-sensitive edge cases

- Some migration-map rows in the chats are stale relative to later canonical IDs.
- Some IDs appear only as future placeholders or optional variants and should not be promoted automatically.
- Some structured IDs were identified only in prose and had to be seeded into the catalog from context (`ECO-TAX-001`, `ADM-CHV-001`, `ADM-AGY-001`, `HLT-TRL-001`).
- Some unresolved prose-only IDs may represent future work rather than canon; check the surrounding chat context before formalizing them.

## Editing guidance

- Prefer updating import logic and source-backed docs over manual data patching.
- Preserve provenance. If you convert or reconcile IDs, keep the relationship visible through the database rather than deleting history.
- When updating policy content, search both main and brainstorm logs first, then update the relevant pillar or overview docs.
- Keep changes surgical: this repo is a reconstruction project, so context and traceability matter as much as the final wording.
