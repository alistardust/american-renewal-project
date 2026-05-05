# Design Spec: PolicyOS Site Exposure

**Date:** 2026-05-04
**Revised:** 2026-05-05
**Status:** Under review (revised)
**Author:** Sam (GitHub Copilot)

---

## Problem Statement

PolicyOS is the meta-layer governing how all policy on this platform is designed, scoped, and enforced. It has three locked layers (Platform Values, System Principles, Authoring OS) and 11 rule families covering 25 pillars. The site currently exposes only a 3-row summary table on `classification.html` with stale "Under review" status badges. The actual rules, intent, and pillar-specific overlay mappings are not accessible to visitors.

The PolicyOS rules currently live in `.md` files under `policy/policyos/`. The policy catalog DB is the established source of truth for structured content. PolicyOS rules should live there too — and `docs/policyos.html` should be generated from the DB, consistent with how policy cards are generated from the catalog.

---

## Goal

Expose PolicyOS fully on the site:

1. A dedicated `docs/policyos.html` page with the full three-layer rule system, generated from the DB
2. Each pillar page showing the domain-specific PolicyOS overlay families that apply to it
3. `classification.html` updated with correct status and a link to the new page
4. PolicyOS added to "The Platform" nav dropdown
5. Hard-coded policy position counts removed from prose throughout the site

---

## Approach

**DB-sourced generation**

PolicyOS rules are added to `policy_catalog_v2.sqlite` under a new schema. A generation script (`scripts/generate-policyos.py`) reads from the DB and writes `docs/policyos.html` as committed static HTML — consistent with how `scripts/generate-pillar-cards.py` works. The same script also updates the PolicyOS sections of `docs/assets/js/data.js` (family metadata and per-pillar overlay mappings), so all PolicyOS data flows from a single source.

The `.md` source files in `policy/policyos/` are retained as the migration source and for provenance, but are no longer the authoritative source after migration.

---

## Architecture

### New files

- `docs/policyos.html` — generated output; do not hand-edit; re-run `scripts/generate-policyos.py` to update
- `scripts/generate-policyos.py` — reads PolicyOS rules and overlay mappings from the DB; writes `docs/policyos.html` and updates PolicyOS sections in `data.js`

### Modified files

| File | Change |
|------|--------|
| `policy/catalog/policy_catalog_v2.sqlite` | New tables: `policyos_layers`, `policyos_families`, `policyos_rules`, `policyos_pillar_overlays` |
| `docs/assets/js/data.js` | `siteData.policyosFamilies` and per-pillar `policyosOverlays` fields added/updated by generation script |
| `docs/assets/js/app.js` | Inject PolicyOS nav link under "The Platform" dropdown; inject `#pil-policyos` section into pillar pages |
| `docs/classification.html` | Update two "Under review" badges to "Locked"; remove stale "not yet canonicalized" prose; add link to `policyos.html` |
| `docs/pillars/*.html` | No manual edits — overlay section is injected by `app.js` at runtime |
| `tests/unit/data.test.js` | Tests for new overlay data structure in `siteData` |
| `tests/e2e/site.spec.js` | Tests for `policyos.html`, nav link, per-pillar injection, classification.html badges |
| Various `docs/*.html` | Remove hard-coded aggregate policy position counts from prose |

### Data flow

```
policy_catalog_v2.sqlite
  (policyos_layers, policyos_families, policyos_rules, policyos_pillar_overlays)
  → scripts/generate-policyos.py
    → docs/policyos.html          (committed static HTML)
    → data.js policyosFamilies    (11 family metadata objects)
    → data.js pillar[].policyosOverlays  (per-pillar overlay mappings)
      → app.js (reads pillar slug, injects #pil-policyos section at runtime)
        → pillar pages (shows applicable families, links to policyos.html#anchor)
```

---

## DB Schema

Four new tables in `policy_catalog_v2.sqlite`:

### `policyos_layers`

```sql
CREATE TABLE policyos_layers (
    id          TEXT PRIMARY KEY,   -- 'values', 'principles', 'authoring'
    title       TEXT NOT NULL,      -- 'Platform Values', 'System Principles', 'Authoring OS'
    description TEXT,
    sort_order  INTEGER NOT NULL
);
```

### `policyos_families`

```sql
CREATE TABLE policyos_families (
    code        TEXT PRIMARY KEY,   -- 'KERN', 'GEOG', 'NORM', etc.
    layer_id    TEXT NOT NULL REFERENCES policyos_layers(id),
    label       TEXT NOT NULL,      -- 'Core Kernel', 'Geography & Access', etc.
    anchor      TEXT NOT NULL,      -- page anchor on policyos.html, e.g., 'kern'
    summary     TEXT NOT NULL,      -- one-sentence description for UI use
    sort_order  INTEGER NOT NULL
);
```

Platform Values rows in `policyos_rules` have `family_code = NULL` and are associated with the `values` layer by joining through a `layer_id` column added to `policyos_rules`:

```sql
ALTER TABLE policyos_rules ADD COLUMN layer_id TEXT REFERENCES policyos_layers(id);
```

For System Principles and Authoring OS rules: `layer_id = NULL`, `family_code` is set (derivable from the family's own `layer_id`). For Platform Values rules: `layer_id = 'values'`, `family_code = NULL`.

### `policyos_rules`

```sql
CREATE TABLE policyos_rules (
    id          TEXT PRIMARY KEY,   -- 'PLOS-KERN-0001', 'PAOS-NORM-0001', etc.
    family_code TEXT REFERENCES policyos_families(code),   -- NULL for Platform Values rows
    rule_text   TEXT NOT NULL,
    rule_subtype TEXT,              -- 'floor' or 'duty' for Platform Values rows; NULL otherwise
    sort_order  INTEGER NOT NULL
);
```

`family_code` is nullable to accommodate Platform Values rules, which belong to a layer (`values`) but have no family codes. `rule_subtype` is only populated for rows in the `values` layer; System Principles and Authoring OS rows leave it NULL.

### `policyos_pillar_overlays`

```sql
CREATE TABLE policyos_pillar_overlays (
    pillar_id      TEXT NOT NULL,   -- matches siteData.pillars[].id, e.g., 'healthcare'
    family_code    TEXT NOT NULL REFERENCES policyos_families(code),
    overlay_type   TEXT NOT NULL,   -- 'mandatory' or 'conditional'
    notes          TEXT,
    PRIMARY KEY (pillar_id, family_code)
);
```

---

## DB Migration

Source data:
- Rules and family content: `policy/policyos/policyos_1_0_rules_proposal.md`, `policy/policyos/policyos_authoring_os_v1.md`, `policy/policyos/policyos_platform_values_v1.md`
- Pillar overlay mappings: `policy/policyos/policyos_1_0_inheritance_matrix.csv` (pipe-delimited `mandatory_families` and `conditional_families` columns; split on `|` to get arrays)

A migration script (`scripts/migrate-policyos-to-db.py`) parses the source files and populates the four new tables. The migration is idempotent — it uses `INSERT OR REPLACE` so it can be re-run safely if source content changes before the `.md` files are fully retired.

**Platform Values migration:** Each Platform Values statement is stored with `family_code = NULL` and `layer_id = 'values'`. The `rule_subtype` column distinguishes `'floor'` statements (negative prohibitions) from `'duty'` statements (positive obligations). The migration script parses the floor/duty structure from the markdown — each value section has clearly labeled floor and duty statements.

**Sentinel initialization:** As part of migration, the script also inserts the two sentinel comment blocks into `data.js` if they are not already present. It appends them to the end of the file, before the closing `</script>` or at the end of the `siteData` block as appropriate. The sentinels must exist before `generate-policyos.py` can run.

```js
/* POLICYOS-FAMILIES-START */
/* POLICYOS-FAMILIES-END */

/* POLICYOS-OVERLAYS-START */
/* POLICYOS-OVERLAYS-END */
```

After migration is verified, the `.md` files are retained for provenance but marked in their headers as superseded by the DB.

---

## `scripts/generate-policyos.py`

Reads from the DB and produces two outputs:

**1. `docs/policyos.html`**

The page uses the same HTML shell as `approach.html` and `platform.html` (doctype, `<html lang="en">`, shared CSS/JS, injected nav and footer). Sections:

1. **Hero** — "PolicyOS: The Rules Behind the Rules" — one-paragraph intro
2. **How it fits** — relationship between PolicyOS and the five foundations; why a meta-layer exists
3. **Layer 1: Platform Values** — intro to the floor/duty model; each value with its floor prohibition and positive duty statement
4. **Layer 2: System Principles** — intro on the overlay inheritance model; each of the 11 families as its own subsection with label, summary, applicability note, and all rules listed with IDs
5. **Layer 3: Authoring OS** — same treatment for NORM, AUTH, TEST, ENFC, PLAC, MAINT
6. **Governance** — the amendment process from `policyos_governance_v1.md` (governance rules are not in the DB — this section is templated inline in the script, or read from a separate governance markdown file)
7. **Pillar compliance** — brief note that all pillars must satisfy applicable families; link to `classification.html`

Each family section has a stable lowercase anchor derived from `policyos_families.anchor`: `#kern`, `#geog`, `#fedr`, etc.

**2. PolicyOS sections of `docs/assets/js/data.js`**

The script locates two delimited regions in `data.js` using sentinel comments (initialized by `migrate-policyos-to-db.py`). If either sentinel block is absent, the script exits non-zero and writes nothing.

```js
/* POLICYOS-FAMILIES-START */
siteData.policyosFamilies = { ... };
/* POLICYOS-FAMILIES-END */
```

```js
/* POLICYOS-OVERLAYS-START */
// per-pillar policyosOverlays populated below
/* POLICYOS-OVERLAYS-END */
```

On each run, the script replaces the content between the sentinels with freshly generated data from the DB. This allows the rest of `data.js` to be maintained by hand while keeping PolicyOS data DB-authoritative.

**`siteData.policyosFamilies` filter:** The script populates this object from `policyos_families WHERE layer_id = 'principles'` only (the 11 System Principles families). Authoring OS families are rendered on `policyos.html` but are not needed in the runtime JS — they are not used by `app.js` for pillar injection.

**`siteData.policyosFamilies` format:**

```js
siteData.policyosFamilies = {
  'KERN': { label: 'Core Kernel', anchor: 'kern', summary: '...' },
  'GEOG': { label: 'Geography & Access', anchor: 'geog', summary: '...' },
  // ... 9 more entries
};
```

**Per-pillar overlay format:** For each pillar with overlay rows in `policyos_pillar_overlays`, the script emits:

```js
(function() {
  const p = siteData.pillars.find(x => x.id === 'healthcare');
  if (p) p.policyosOverlays = { mandatory: ['KERN'], conditional: ['GEOG', 'REGD', 'ENFA'] };
})();
```

One IIFE per pillar, emitted inside the POLICYOS-OVERLAYS sentinel block. Using `find` keeps this independent of array index and safe across future pillar reorderings.

**Governance section:** The Governance section of `policyos.html` reads from `policyos_governance_v1.md` at generation time. The script converts the markdown to HTML using the `markdown2` Python library (`pip install markdown2`). This is the only markdown-to-HTML conversion in the script; all other content comes from the DB as plain text and is HTML-escaped before insertion.

The script exits with a non-zero code and writes no output if the DB tables are missing, empty, or if either sentinel block is absent from `data.js`.

---

## `app.js` Injection

### Nav injection

Add "PolicyOS" as the fourth item in the "The Platform" dropdown (after "Rights", "Policy Library", "Platform Overview"). Follows the same path-resolution pattern used for existing injected links.

### Per-pillar section injection

On pillar pages (detected by the presence of `#pil-snav` in the DOM):

**Injection position:** `#pil-policyos` is appended after `#pil-related` (the final section on all pillar pages), making it the last section. A "PolicyOS" nav item is also injected into `#pil-snav` as the final list item.

**Empty conditional overlay case:** If `policyosOverlays.conditional` is empty, the section still renders with only the KERN baseline note — it is never suppressed.

1. Derive the pillar slug from `location.pathname`: take the filename without extension, replace hyphens with underscores (e.g., `executive-power` → `executive_power`). This matches `siteData.pillars[].id`.
2. Find the current pillar in `siteData.pillars` by matching the normalized slug against `pillar.id`.
3. Read `pillar.policyosOverlays`.
4. Inject `<section id="pil-policyos">` into the page.

**Rendered section structure:**

- Heading: "PolicyOS Overlays"
- Note: "KERN applies to all pillars. [View KERN rules →](policyos.html#kern)"
- List of conditional families: each as a card showing family code, label, summary, and a "View rules →" link to `base + 'policyos.html#' + anchor`

**Path resolution:** Links use the `base` variable already established in `app.js`, resolving correctly from both root pages and `docs/pillars/` subdirectory.

**Error handling:** If the pillar slug has no matching entry in `siteData.pillars`, injection is silently skipped — no broken page, no console error.

---

## `classification.html` Changes

1. Update the two "Under review" status badges (Layer 2: System Principles; Layer 3: Authoring OS) to "Locked". Layer 1 is already "Locked".
2. Remove the full paragraph containing that stale sentence — both sentences: "PolicyOS rules will not be canonicalized into the main platform until the structural review is complete. For the current status and working files, see the `policyos/` directory in the project repository."
3. Add after the summary table: `For the full PolicyOS documentation, including all rule families and individual rules, see <a href="policyos.html">PolicyOS</a>.`

---

## Hard-Coded Count Removal

Scan `docs/*.html` and `docs/pillars/*.html` for aggregate policy position counts in prose. `docs/compare/*.html` is excluded.

**Scope:** Pre-implementation scan identified approximately 5 files with aggregate counts (catalog-level totals like "3,810 positions" and per-pillar totals like "362 policy positions across 22 distinct family codes"). Per-family inline annotations within pillar design sections (e.g., "COV (Coverage, 30 positions)") are structural descriptions of family composition — leave them unchanged.

- Where the count was the substance: remove the sentence or replace with "the full policy catalog"
- Where the count was incidental: drop the number

Dynamic `[data-dynamic]` spans are unaffected.

---

## Testing

### Unit tests (`data.test.js`)

- All 25 pillar entries have `policyosOverlays` with at least `mandatory: ['KERN']`
- `siteData.policyosFamilies` has exactly 11 keys
- Each family object has `label`, `anchor`, and `summary`

### E2E tests (`site.spec.js`)

- `policyos.html` loads; has correct title; nav and footer visible
- All 11 System Principles family anchors exist on `policyos.html`
- All 6 Authoring OS family anchors exist on `policyos.html`
- A sample pillar page (e.g., `healthcare.html`) has `#pil-policyos` section injected after load
- PolicyOS nav link appears in "The Platform" dropdown
- `classification.html` status badges read "Locked", not "Under review"

---

## Out of Scope

- Making PolicyOS rules editable through the site
- Linking individual policy positions to the specific PLOS/PAOS rules that shaped them
- Pillar compliance audit or scoring
- Migrating Platform Values governance prose to the DB (governance section of `policyos.html` reads from `policyos_governance_v1.md` directly, or is templated inline)

