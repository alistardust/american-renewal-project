# Design: Rename "Pillars" to "Policy Areas" — Full Codebase Migration

**Date:** 2026-05-12
**Status:** Approved for implementation

---

## Overview

The concept of a "pillar" is retired. Individual policy sections are now "policy areas" — unremarkable parts of each foundation, not a special structural concept. This migration removes the word "pillar" and all related identifiers from every layer of the codebase: URLs, file paths, CSS classes, JavaScript identifiers, prose content, navigation labels, test files, and generator scripts.

The migration is implemented via a single Node.js script (`scripts/migrate-policy-areas.js`) that handles all mechanical changes in one pass, followed by a verify pass that flags any remaining occurrences for manual review. All changes land in one feature branch as one PR.

---

## Goals

- Remove "pillar/pillars" from all user-visible content (prose, headings, labels, nav, meta)
- Remove "pillar/pillars" from all code identifiers (CSS classes, JS variables, HTML IDs, test constants)
- Rename URL paths from `/pillars/` to `/policy/`
- Rename source templates from `src/pages/pillars/` to `src/pages/policy/`
- Rename `siteData.pillars` to `siteData.policyAreas` throughout
- Remove the `completion-status` development status block from all policy area pages
- Remove all pillar count badges and `data-dynamic="pillar-count"` spans
- Update all tests to use the new paths, class names, and data property names
- Leave old `/pillars/` URLs as broken links (site is early-stage; no redirect stubs needed)

---

## Out of scope

- Policy position IDs (`HLTH-COVR-0001` etc.) — do not contain "pillar"
- SQLite database schema column names — separate migration concern
- Git history
- GitHub Issues and PR text

---

## 1. File structure changes

### Moves
| From | To |
|---|---|
| `docs/pillars/*.html` (27 files: 26 policy area pages + `index.html`) | `docs/policy/*.html` |
| `src/pages/pillars/*.njk` (27 files: 26 policy area pages + `index.njk`) | `src/pages/policy/*.njk` |

The script uses `fs.renameSync` / `fs.mkdirSync` to move all files. The old directories are removed after all files are moved.

### Generator scripts
| Old | New |
|---|---|
| `scripts/new-pillar.js` | `scripts/new-policy-area.js` |
| `scripts/build_pillar_pages.py` | *(removed)* |

**`scripts/build_pillar_pages.py` is removed in the same PR.** It hardcodes `out_dir = os.path.join(REPO, 'docs', 'pillars')` and will recreate `docs/pillars/` if executed after the migration, undoing the rename entirely. It is not referenced by `npm run build` but any manual invocation would be destructive. The file is deleted (not renamed) in Phase 1.

`new-compare.js` is updated in-place. Specific changes:
- Two nav link hrefs: `../pillars/index.html` → `../policy/index.html`
- Template comment referencing `.cov-pillar` class updated to `.cov-area`
- Prose strings "pillar" → "policy area" in any generated comments or labels
- **Three additional targeted replacements (C2):** `// Pillar link` comment → `// Policy area link`; `// pillar card` comment → `// policy area card`; `// Connected pillars` comment → `// Connected policy areas` (exact strings; do not rely on Phase 5 prose pass — Phase 5 does not run on JS files)

`new-pillar.js` is renamed to `new-policy-area.js` and updated throughout. Specific changes:
- Script docblock: "new-pillar.js — Scaffold a new pillar HTML page" → "new-policy-area.js — Scaffold a new policy area HTML page"
- Usage comment: `--id my-pillar-name` → `--id my-policy-area-name`, `--title "My Pillar Title"` → `--title "My Policy Area Title"`
- `outputDir` path: `'../docs/pillars'` → `'../docs/policy'`
- Inline comment in src reference: `src/pages/pillars/<id>.njk` → `src/pages/policy/<id>.njk`
- Template HTML: nav label `<a href="index.html" class="active">Pillars</a>` → `Policy Areas`; footer nav `<a href="index.html">Pillars</a>` → `Policy Areas`
- Template HTML: `<!-- ═══ PILLAR SECTION NAV ═══ -->` → `<!-- ═══ POLICY AREA SECTION NAV ═══ -->`; `<!-- Per-pillar accent color -->` → `<!-- Per-area accent color -->`
- Template HTML: `<h2>What This Pillar Covers</h2>` → `<h2>What This Policy Area Covers</h2>`; `<p class="eyebrow">Connected Pillars</p>` → `Connected Policy Areas`; `<!-- Add links to related pillars here -->` → `related policy areas`
- `console.log` output: "Add pillar to docs/assets/js/data.js — pillars array + foundation .pillars list" → "Add policy area to ... — policyAreas array + foundation .policyAreas list"; stale `PILLAR_COUNT` reference removed from step 2 message

---

## 2. URL and path replacements

Applied across all HTML, njk, JS, test, and XML files:

| Old pattern | New pattern |
|---|---|
| `/pillars/` (in href, src, goto, page.goto) | `/policy/` |
| `'pillars'` (bare string in `path.join` calls — `backfill-rule-notes.js`, `strip-card-status.js`) | `'policy'` |
| `pillars/` (relative paths — applies globally across all source files, not only build.test.js) | `policy/` |
| `/(pillars\|compare)/` (app.js path detection regex) | `/(policy\|compare)/` |

**Explicit exception — regex literal in `site.spec.js:593`:** The string `/pillars\/` does not appear literally in the file (the slash is escaped). The migration script must include a targeted replacement: replace `/pillars\//` with `/policy\//` on this line explicitly, separate from the general string-replacement pass.

**XML files in scope:** `docs/sitemap.xml` and `docs/feed.xml` are included in Phase 2 replacement scope. `sitemap.xml` contains 26 `/pillars/` URL entries; `feed.xml` contains "pillars" prose. Both would advertise dead URLs on the live site after migration if left unchanged.

---

## 3. CSS class renames

Applied in `docs/assets/css/style.css`, all HTML files, all njk files, `docs/assets/js/app.js`, and `tests/**/*.js`. Including test files in Phase 3 prevents Phase 5's word-boundary replacement from mangling selector strings that appear as quoted JS strings in test files. Replacements are applied longest-match-first to avoid partial collisions. The migration script sorts ALL classes from both tables together by descending string length in a single pass — not table-by-table.

### .pil-* prefix renames
| Old class | New class |
|---|---|
| `.pil-pillar-card` | `.area-card` |
| `.pil-pillar-title` | `.area-card-title` |
| `.pil-pillar-desc` | `.area-card-desc` |
| `.pil-pillar-link` | `.area-link` |
| `.pil-pillar-grid` | `.area-grid` |
| `.pil-pillar-count` | *(removed — see Section 6)* |
| `.pil-foundation-accordion` | `.area-foundation-accordion` |
| `.pil-foundation-bar-left` | `.area-foundation-bar-left` |
| `.pil-foundation-bar-right` | `.area-foundation-bar-right` |
| `.pil-foundation-bar-text` | `.area-foundation-bar-text` |
| `.pil-foundation-bar` | `.area-foundation-bar` |
| `.pil-foundation-name` | `.area-foundation-name` |
| `.pil-foundation-num` | `.area-foundation-num` |
| `.pil-foundation-teaser` | `.area-foundation-teaser` |
| `.pil-fv-pill` | `.pi-fv-area-pill` |
| `.pil-grid-closing` | `.area-grid-closing` |
| `.pil-idx-wrap` | `.area-idx-wrap` |
| `.pil-chevron` | `.area-chevron` |
| `.pil-hero` | `.area-hero` |
| `.pil-intro` | `.area-intro` |
| `.pil-summary` | `.area-summary` |
| `.pil-snav` | `.area-snav` |
| `.pil-title` | `.area-title` |

### Other pillar-named classes
| Old class | New class |
|---|---|
| `.adv-pillar-header` | `.adv-area-header` |
| `.adv-pillar-title` | `.adv-area-title` |
| `.adv-pillar-badge` | `.adv-area-badge` |
| `.adv-pillar-body` | `.adv-area-body` |
| `.adv-pillar` | `.adv-area` |
| `.cov-pillar` | `.cov-area` |
| `.f-pillar-grid` | `.f-area-grid` |
| `.f-pillar-card` | `.f-area-card` |
| `.f-pillars-header` | `.f-areas-header` |
| `.mission-pillars-grid` | `.mission-areas-grid` |
| `.mission-pillar-card` | `.mission-area-card` |
| `.pi-fv-pillars` | `.pi-fv-areas` |
| `.pfc-pillars` | `.pfc-areas` |
| `.pillar-filter-btn` | `.policy-area-filter-btn` |
| `.pillar-filters` | `.policy-area-filters` |
| `.pillar-grid` | `.policy-area-grid` |
| `.pillar-index-section` | `.policy-area-index-section` |
| `.pillar-card` | `.policy-area-card` |
| `.pillar-status-pill` | `.policy-area-status-pill` |
| `.roadmap-pillar-table` | `.roadmap-area-table` |
| `.cmp-th-pillar` | `.cmp-th-area` |
| `.cmp-td-pillar` | `.cmp-td-area` |
| `.fd-pillars` | `.fd-policy-areas` |
| `.fd-pillar-tag` | `.fd-policy-area-tag` |

**Note:** `.policy-card` already exists as the class for policy rule/position cards. `.policy-area-card` is used for area index cards to avoid collision.

**Note:** `.pillar-hero` appears in one responsive override block in `style.css` but is unused in all HTML and njk files (dead selector). Remove it rather than rename.

**Note:** `id="pil-snav"` is renamed alongside its class. The HTML attribute `id="pil-snav"` → `id="area-snav"` is handled in Phase 3 (HTML/njk files). The corresponding `app.js` call `getElementById('pil-snav')` → `getElementById('area-snav')` is added to the Phase 4 explicit rename table. Test selectors `#pil-snav` are renamed via Phase 3's `tests/**/*.js` scope. After migration the element consistently has `id="area-snav"` and `class="area-snav"`.

**Note:** `id="pil-related"` and `id="pil-policyos"` also use the "pil-" abbreviation of "pillar" and are renamed by the same logic. `id="pil-related"` → `id="area-related"` in Phase 3 (all 26 policy area HTML/njk files). The dynamically generated `section.id = 'pil-policyos'` and the nav anchor `href="#pil-policyos"` are renamed to `area-policyos` in Phase 4 (app.js). These IDs do not contain the word "pillar" and will not be caught by the Phase 7 verify pass — they must be in the explicit rename tables.

---

## 4. JavaScript identifier renames

Applied in `docs/assets/js/data.js` and `docs/assets/js/app.js`:

| Old identifier | New identifier | File |
|---|---|---|
| `siteData.pillars` (array) | `siteData.policyAreas` | data.js |
| `foundation.pillars: [...]` | `foundation.policyAreas: [...]` | data.js (all 5 foundations) |
| `siteData.getPillarsByFoundation` | `siteData.getPolicyAreasByFoundation` | data.js |
| `siteData.pillars` (consumers) | `siteData.policyAreas` | app.js |
| `pillarCount` variable | `policyAreaCount` | app.js |
| `case 'pillar-count':` | *(removed — see Section 6)* | app.js |
| `pillarGrid` / `#pillar-grid` | `policyAreaGrid` / `#policy-area-grid` | app.js only (no current HTML has these IDs) |
| `getElementById('pillar-filters')` → `getElementById('policy-area-filters')` | (ID renamed; `filterBar` variable name stays as-is) | app.js |
| `getElementById('pil-snav')` | `getElementById('area-snav')` | app.js |
| `getElementById('pil-related')` | `getElementById('area-related')` | app.js |
| `section.id = 'pil-policyos'` | `section.id = 'area-policyos'` | app.js |
| `href="#pil-policyos"` (in `li.innerHTML` string) | `href="#area-policyos"` | app.js |
| `.pillar-filter-btn` (in JS querySelector) | `.policy-area-filter-btn` | app.js |
| `.pillar-card` (in JS-generated HTML) | `.policy-area-card` | app.js |
| `pillarOverlays` | `policyAreaOverlays` | app.js |
| `"apply to this pillar"` (string literal) | `"apply to this policy area"` | app.js |
| `'All Pillars'` (filter button label, line 196) | `'All Policy Areas'` | app.js |
| `/* ── PILLAR FILTER + RENDER ─── */` (comment) | `/* ── POLICY AREA FILTER + RENDER ─── */` | app.js |
| `/(pillars\|compare)/` (regex) | `/(policy\|compare)/` | app.js |
| `"summary": "Universal rules that apply to every pillar."` (in `policyosFamilies`) | `"...every policy area."` | data.js |
| `renderPillars` | `renderPolicyAreas` | app.js |
| `/* ── PILLAR FILTER + RENDER ─── */` (comment) | `/* ── POLICY AREA FILTER + RENDER ─── */` | app.js |
| `/* ── POLICYOS PILLAR OVERLAY */` (comment) | `/* ── POLICYOS POLICY AREA OVERLAY */` | app.js |
| `// Injects a PolicyOS design-rules section after #pil-related on pillar pages.` | `// Injects a PolicyOS design-rules section after #area-related on policy area pages.` | app.js |
| `/* ── PILLAR SECTION SCROLLSPY */` (comment) | `/* ── POLICY AREA SECTION SCROLLSPY */` | app.js |
| `// Highlights the active section in the sticky pillar sub-nav.` | `// Highlights the active section in the sticky policy area sub-nav.` | app.js |
| `/* ── PILLARS INDEX ACCORDION ANIMATION ─────────────── */` (comment) | `/* ── POLICY AREAS INDEX ACCORDION ANIMATION ─────────────── */` | app.js |
| `'System design rules that apply to this pillar under the PolicyOS framework.'` (line 542) | `'System design rules that apply to this policy area under the PolicyOS framework.'` | app.js |
| `// Usage: <span data-dynamic="pillar-count">23</span>  ← fallback shown if JS disabled` (line 350) | *(remove this comment line — the `pillar-count` case is removed in Phase 6)* | app.js |

**Generator prose strings (Phase 4):** The `console.log` string literals in `scripts/new-pillar.js` (lines 284-285) reference "pillar/pillars" and `PILLAR_COUNT`. These are covered by the Phase 1 rename of the file to `new-policy-area.js` and its internal rewrite per Section 1's specific-changes list, which Phase 4 implements. The `PILLAR_COUNT` reference in the step-2 message is removed entirely — that constant is eliminated by the migration.

---

## 5. Content and prose replacements

Applied in all HTML, njk, and XML files **only**. **Phase 5 must never run on JS files or test files.** JS string literals (including CSS selector strings in `app.js` and Playwright test files) are handled exclusively by Phase 3 (class renames, which includes `tests/**/*.js`) and Phase 4 (explicit JS identifier renames). Running word-boundary `\bpillar\b` on JS files would corrupt selector strings before Phase 6 can remove them — e.g., `'.pillar-intro p'` would become `'.policy area-intro p'` (a descendant selector with a space, causing a Playwright parse error). **Phase 5 replacements are case-sensitive** — use literal string matching, not case-insensitive flags, to avoid inadvertently replacing identifiers or code in `<code>` elements. Case variants handled explicitly:

| Old text | New text |
|---|---|
| `Policy Pillar` | `Policy Area` |
| `Policy Pillars` | `Policy Areas` |
| `policy pillar` | `policy area` |
| `policy pillars` | `policy areas` |
| `Pillar` (standalone title case) | `Policy Area` |
| `Pillars` (standalone title case) | `Policy Areas` |
| `pillar` (standalone lowercase) | `policy area` |
| `pillars` (standalone lowercase) | `policy areas` |
| Navigation labels referencing "Pillars" | "Policy Areas" |

**Targeted exception for `about-ai.html`:** `about-ai.html` contains a `<code>SAMPLE_PILLARS</code>` element referencing the test constant by name. This is a code identifier reference in contributor docs — it must be updated to `<code>SAMPLE_POLICY_AREAS</code>` as a targeted explicit replacement **before** Phase 5 runs, to prevent Phase 5's word-boundary match from producing `<code>SAMPLE_POLICY AREAS</code>` (broken identifier with space). Add this as an explicit pre-Phase-5 targeted replacement in the migration script.

The script applies word-boundary replacements (`\bpillar\b`, `\bpillars\b`) to avoid corrupting identifiers in mid-replacement. After all replacements, a verify pass scans for any remaining "pillar" occurrences across all source files and prints them for manual review.

| Old text | New text |
|---|---|
| `Policy Pillar` | `Policy Area` |
| `Policy Pillars` | `Policy Areas` |
| `policy pillar` | `policy area` |
| `policy pillars` | `policy areas` |
| `Pillar` (standalone title case) | `Policy Area` |
| `Pillars` (standalone title case) | `Policy Areas` |
| `pillar` (standalone lowercase) | `policy area` |
| `pillars` (standalone lowercase) | `policy areas` |
| Navigation labels referencing "Pillars" | "Policy Areas" |

The script applies word-boundary replacements (`\bpillar\b`, `\bpillars\b`) to avoid corrupting identifiers in mid-replacement. After all replacements, a verify pass scans for any remaining "pillar" occurrences across all source files and prints them for manual review.

---

## 6. Elements removed entirely

These are deleted, not renamed:

- `<div class="completion-status">...</div>` — development status block with progress bar, present on all 26 area pages and their njk counterparts. Removed entirely. These blocks contain deeply nested `<div>` elements; a naive regex terminating on `</div>` will stop at the first inner close tag and produce malformed HTML. **The migration script must use `parse5`** to locate the `div.completion-status` node. (`parse5` is already a dev dependency at `^6.0.1`.) The sentinel approach is not specified and must not be used. **Serialization strategy differs by file type:** For `.html` files, parse the full document tree, remove the node, and serialize back to string. For `.njk` files, **do not serialize the parse5 tree** — Nunjucks tags (`{% ... %}`, `{{ ... }}`) are not HTML and can be mangled or escaped by an HTML serializer. Instead, use `parse5`'s `sourceCodeLocation` offsets on the `div.completion-status` node to identify the byte range in the original file, then splice that range out of the original source string, leaving everything else byte-for-byte unchanged. **If `div.completion-status` is not found in a file that is expected to contain one** (capture the expected file list from `docs/pillars/*.html` and `src/pages/pillars/*.njk` *before* Phase 1 moves them — the fail-loudly check uses pre-move paths to build its list, then runs post-move on the new locations), **the script must throw an error rather than silently skip — silent skip would produce an undetectable incomplete migration.**
- `<span class="pil-pillar-count">N pillars</span>` — per-foundation count badges on the index page (5 instances in HTML + njk). Removed entirely.
- `<span data-dynamic="pillar-count">25</span> pillars` — in `policy-library.html` and `policy-library.njk`. The `data-dynamic="pillar-count"` attribute and the surrounding sentence are removed. Replace the sentence "25 pillars of specific, evidence-grounded policy, each with a canonical ID..." with: "Specific, evidence-grounded policy across five foundations, each position with a canonical ID..." (preserving the rest of the original sentence after "ID"). Do not leave the replacement text to implementer discretion.
- `case 'pillar-count':` branch in app.js dynamic counts block — no remaining consumers.
- `.pil-pillar-count` CSS rule in `style.css` — no remaining HTML consumers after the span removal above. Remove the CSS rule as well.
- `.pillar-hero` rule in `style.css` responsive override block — dead selector (no matching HTML). The selector appears mid-list in a comma-separated rule (`style.css:1823`); the script must remove the entire `.pillar-hero,\n` line (including trailing comma and newline), not just the class name token, to avoid a dangling-comma CSS parse error.
- `.pillar-tags` and `.pillar-tag` CSS rules in `style.css` (lines 2201-2202) — dead selectors, no matching HTML or njk. Remove entirely.
- `.pillar-intro p` and `.pillar-summary` string literals in the `SELECTORS` constant in `app.js` (lines 243-244) — dead selectors that match no HTML or CSS classes in the codebase. Remove from the array.
- Prose sentences referencing "25 pillars" or "N pillars" in meta descriptions and body text — reworded to describe content without counting policy areas.

---

## 7. Test updates

### tests/e2e/shared.js
- `SAMPLE_PILLARS` → `SAMPLE_POLICY_AREAS`
- Comment updated: "slug matches the filename at `docs/policy/<slug>.html`"

### tests/e2e/site.spec.js
- `const { SAMPLE_PILLARS }` → `const { SAMPLE_POLICY_AREAS }`
- `PILLAR_COUNT` constant removed. The two affected assertions become:
  - Line 131-132 (index accordion links): `await expect(page.locator('a.area-link')).toHaveCount(siteData.policyAreas.length)`
  - Line 596-598 (foundation cards): `await expect(page.locator('a.f-area-card')).toHaveCount(siteData.policyAreas.length + 1)` (comment updated to explain the +1 is for the rights cross-area card)
- All `/pillars/` paths → `/policy/`
- All `.pil-pillar-link`, `.pil-pillar-card`, `.f-pillar-card` selectors updated to new class names
- Regex literal at line 593 (`/pillars\//`) → `/policy\//` (explicit targeted replacement — the escaped slash makes this immune to the general Phase 2 string pass)
- Test descriptions updated: "pillar page" → "policy area page", "Pillars index" → "Policy areas index", etc.
- Line 85 comment updated: the existing assertion that nav does NOT contain "pillars" becomes a clean correctness check; the caveat comment is removed
- "pillar PolicyOS overlay" describe block renamed to "policy area PolicyOS overlay"

### tests/e2e/mobile.spec.js
- All `/pillars/` paths → `/policy/`
- `SAMPLE_PILLARS` → `SAMPLE_POLICY_AREAS`
- `SPOT_PILLARS` → `SPOT_POLICY_AREAS`
- Test descriptions updated: "pillar page" → "policy area page", "pillar sub-nav" → "area sub-nav"
- Path detection comment updated: `/(pillars|compare)/` → `/(policy|compare)/`

### tests/unit/data.test.js
- `siteData.pillars` → `siteData.policyAreas` throughout
- `f.pillars` → `f.policyAreas`
- `PILLAR_COUNT` → `POLICY_AREA_COUNT` (derived dynamically: `siteData.policyAreas.length`)
- `siteData.getPillarsByFoundation` → `siteData.getPolicyAreasByFoundation`
- All describe/test descriptions and inline `expect()` failure message strings: "pillar" → "policy area" throughout
- `policyosOverlays` test: description changes from "has exactly 25 pillar entries" → "has 25 entries (not all policy areas have an overlay)". The `toHaveLength(25)` literal stays — `policyosOverlays` currently has 25 keys because one policy area does not have a PolicyOS overlay, so `siteData.policyAreas.length` (26) would be wrong here.

### tests/unit/build.test.js
- Example paths: `docs/pillars/healthcare.html` → `docs/policy/healthcare.html`
- `pillars/healthcare.html` → `policy/healthcare.html`

### tests/unit/scripts/ (new)

**`tests/unit/scripts/migrate-phase3-sort.test.js`** — new file, validates Phase 3 rename table before the script runs on real files.

```js
import { CLASS_RENAMES } from '../../scripts/migrate-policy-areas.js';
// (Phase 3 rename map must be exported for testability)

test('Phase 3 class renames are sorted longest-first', () => {
  const names = CLASS_RENAMES.map(([from]) => from);
  for (let i = 0; i < names.length - 1; i++) {
    expect(names[i].length).toBeGreaterThanOrEqual(names[i + 1].length);
  }
});

test('No class name in the rename list is a prefix of a longer class name that appears later', () => {
  const names = CLASS_RENAMES.map(([from]) => from);
  for (let i = 0; i < names.length; i++) {
    for (let j = i + 1; j < names.length; j++) {
      expect(names[j].startsWith(names[i])).toBe(false);
    }
  }
});
```

**Requires:** The migration script must export `CLASS_RENAMES` as a named export. No other script internals need to be exported.

### tests/visual/visual.spec.js
- `{ name: 'pillar-healthcare', path: '/pillars/healthcare.html' }` → `{ name: 'policy-area-healthcare', path: '/policy/healthcare.html' }`
- Comment "pillar pages exceed the 32767px CDP screenshot limit" → "policy area pages exceed..."
- Visual baselines must be refreshed after the migration (see Section 9)

---

## 8. Migration script design

**File:** `scripts/migrate-policy-areas.js`

**Usage:**
```bash
node scripts/migrate-policy-areas.js          # dry run (prints changes, no writes)
node scripts/migrate-policy-areas.js --apply  # apply all changes
node scripts/migrate-policy-areas.js --verify # scan for remaining "pillar" occurrences
```

**Phases (in order):**

1. **Move files** — `docs/pillars/` → `docs/policy/`, `src/pages/pillars/` → `src/pages/policy/`. Renames `scripts/new-pillar.js` → `scripts/new-policy-area.js`. Deletes `scripts/build_pillar_pages.py`.
2. **URL/path replacements** — `/pillars/` and `pillars/` → `/policy/` and `policy/` across all HTML, njk, JS, test, and XML files. Includes `docs/sitemap.xml` and `docs/feed.xml`. Includes a targeted explicit replacement for the regex literal `/pillars\//` → `/policy\//` in `tests/e2e/site.spec.js:593`.
3. **CSS class renames** — longest-match-first to prevent partial collisions (e.g., `.pil-pillar-card` before `.pil-pillar-grid`). Applied in CSS, HTML, njk, `app.js`, and **`tests/**/*.js`**. Also renames `id="pil-snav"` → `id="area-snav"` in HTML/njk files.
4. **JS identifier renames** — `siteData.pillars`, `pillarCount`, `renderPillars`, `getElementById('pil-snav')`, section-header comments, and all other explicit identifiers per Section 4 table. Applied in JS files only.
5. **Content/prose replacements** — word-boundary aware (`\bpillar\b`, `\bpillars\b`), case variants per Section 5 table. Applied to **HTML, njk, and XML files only — never JS or test files**.
6. **Element removals** — `completion-status` divs (via parse5 or sentinel), count spans, dead `case 'pillar-count':` branch, dead CSS rules (`.pillar-hero,\n` line, `.pillar-tags`, `.pillar-tag`, `.pil-pillar-count`).
7. **Verify pass** — scan all in-scope files for: (a) remaining "pillar" occurrences (case-insensitive — catches `PILLAR`, `Pillar`, `pillars`), (b) remaining `pil-` prefix patterns (`\bpil-` and `#pil-`) that signal un-migrated identifiers (these do not contain the word "pillar" and are not caught by check (a)), and (c) remaining `completion-status` class names (confirming Phase 6 removal was complete). The migration script itself (`scripts/migrate-policy-areas.js`) and its unit test (`tests/unit/scripts/migrate-phase3-sort.test.js`) are explicitly excluded from the verify scan via an allowlist. This is a **hard pass/fail gate**: zero occurrences of all three patterns (outside the allowlist) required before the PR can merge.

**Scope of files processed:** `docs/**/*.html`, `docs/**/*.xml`, `src/pages/**/*.njk`, `docs/assets/js/*.js`, `docs/assets/css/style.css`, `tests/**/*.js`, `scripts/*.js`

**`path.join` audit (required before applying Phase 2):** Before running Phase 2 replacements, the migration script must scan all `scripts/*.js` files for any `path.join(...)` or template-literal path constructions containing `'pillars'` as a path segment — not just the two named in the Phase 2 table (`backfill-rule-notes.js`, `strip-card-status.js`). Any unaccounted instance in a build script (e.g., `build-site.js`) would cause `npm run build` to regenerate `docs/pillars/` after migration, silently undoing the file moves. The audit must be run during the dry-run phase and halt with a clear error if unaccounted path.join instances are found.

**Exclusions:** `node_modules/`, `.git/`, `*.png`, `*.sqlite`, `policy/catalog/`, `policy/policyos/`, `policy/foundations/` (markdown content), `docs/superpowers/` (spec/plan docs)

**Python scripts excluded from automated migration — but require manual path updates:** `scripts/*.py` files are excluded from the automated migration script (their internal naming is outside the UI migration scope). However, 12 Python scripts hardcode `docs/pillars/` file paths and will throw `FileNotFoundError` at runtime after migration. These must be updated before the PR merges:

| Script | Path reference | Risk |
|---|---|---|
| `add-proposals-econ.py` | hardcoded dict `'docs/pillars/...'` | FileNotFoundError |
| `add-proposals-imm-hlt.py` | hardcoded dict `'docs/pillars/...'` | FileNotFoundError |
| `add-proposals-rest.py` | hardcoded dict `'docs/pillars/...'` | FileNotFoundError |
| `add-proposals-tec.py` | `HTML_PATH = 'docs/pillars/...'` | FileNotFoundError |
| `backfill_cnsr_plain_language.py` | `REPO_ROOT / "docs" / "pillars" / ...` | FileNotFoundError |
| `backfill_hlth_plain_language.py` | `REPO / "docs/pillars/..."` | FileNotFoundError |
| `complete-missing-cards.py` | `Path("docs/pillars/...")` | FileNotFoundError |
| `complete-policy-cards.py` | `REPO_ROOT / "docs/pillars/..."` (2 files) | FileNotFoundError |
| `fix-html-plain-language.py` | `ROOT / "docs/pillars/..."` | FileNotFoundError |
| `rewrite_antr_proposals.py` | `Path("docs/pillars/...")` | FileNotFoundError |
| `transform-healthcare-cards.py` | `Path("docs/pillars/...")` | FileNotFoundError |
| `update-briefing-pack.py` | `(REPO_ROOT / 'docs' / 'pillars').glob(...)` | FileNotFoundError |

Two additional scripts (`add-proposals-justice.py`, `import_policy_catalog.py`) contain `docs/pillars/` in docstrings or comments only — they will not break at runtime but should be updated for consistency. The verify pass does not scan `.py` files; this is an intentional exclusion. The checklist includes a required manual audit step. `build_pillar_pages.py` is deleted in Phase 1 (not updated).

**`scripts/build-site.js` is in scope.** It is a `scripts/*.js` file and contains "pillar" prose and path references that will be caught by Phases 2, 4, and 5.

**Verify pass scope:** `--verify` scans the same file globs as `--apply`. It does NOT scan `*.py`, `*.md`, `*.sqlite`, or `*.png`. Markdown files are intentionally out of scope for this UI migration — they are updated as part of the repo documentation commit included in the same PR. `scripts/migrate-policy-areas.js` and `tests/unit/scripts/migrate-phase3-sort.test.js` are explicitly excluded from the verify scan via allowlist (they contain the word "policy-areas" and valid `pil-` references in test fixture strings). The verify pass is a **hard pass/fail gate**: the PR cannot merge until zero occurrences of all three patterns are reported outside the allowlist.

After the script runs, the implementer commits with `refactor(site): rename pillars to policy areas`.

---

## 9. Visual regression baselines

After the rename, visual regression baselines in `tests/visual/visual.spec.js-snapshots/` will need refreshing because:
- Class names on the policy areas index page changed
- The `completion-status` block is removed from all area pages

Run `npx playwright test --project=visual-firefox --update-snapshots` after verifying the site renders correctly.

---

## 10. Verification checklist

Before merging:

- [ ] `npm run test:unit` passes
- [ ] `npm run build` (run after migration to verify `src/pages/` → `docs/` regeneration)
- [ ] Re-run `node scripts/migrate-policy-areas.js --verify` against freshly built output — still zero occurrences
- [ ] `npm run test:e2e` passes across all browser projects (run against freshly built output)
- [ ] `node scripts/migrate-policy-areas.js --verify` reports zero remaining "pillar", `\bpil-`, and `#pil-` occurrences in source files (outside allowlist)
- [ ] **Python scripts updated:** the 12 scripts with hardcoded `docs/pillars/` file paths updated to `docs/policy/` (see Section 8 table). Also update `add-proposals-justice.py` and `import_policy_catalog.py` comments for consistency. Verify with: `grep -rn "docs/pillars" scripts/*.py`
- [ ] `/policy/healthcare.html` loads correctly in browser
- [ ] `/policy/index.html` loads correctly in browser
- [ ] Nav links point to `/policy/` paths
- [ ] Foundation page policy area cards (on platform page) link to `/policy/` paths
- [ ] PolicyOS overlay still appears on policy area pages
- [ ] `completion-status` block is absent from all policy area pages
- [ ] No "pillar" text visible anywhere on the live site
- [ ] `scripts/new-policy-area.js` exists and `scripts/new-pillar.js` has been removed
- [ ] `scripts/build_pillar_pages.py` has been removed
- [ ] `docs/sitemap.xml` and `docs/feed.xml` contain no `/pillars/` URLs
- [ ] Visual regression baselines refreshed: `npx playwright test --project=visual-firefox --update-snapshots` (run after site renders correctly — see Section 9)
- [ ] `package.json` `description` field updated manually to remove "pillar docs"
- [ ] Repo documentation updated in same commit: `README.md`, `.github/current-state.md`, `.github/copilot-instructions.md`, `CODING_STANDARDS.md` (any pillar references), `.github/ai-repo-context.md`

---

## 11. Review history

**Rounds 1-5 (2026-05-12, Claude Sonnet 4.6):** Automated spec review; approved with two advisory notes — both fixed and committed.

**Section 11 findings (2026-05-12/13, GPT-5.2 + Claude Sonnet 4.6):** Two parallel reviews evaluated Critical/High/Medium/Low findings. All confirmed issues have been incorporated into Sections 1-10. Resolved:

- C1: Phase 2 URL table now applies `pillars/` pattern globally (not only build.test.js)
- C2: Phase 3 scope extended to include `tests/**/*.js`; Phase 5 explicitly restricted to HTML/njk/XML
- C3: Explicit targeted replacement added for regex literal `/pillars\//` in `site.spec.js:593`
- C4: Generator script prose strings assigned to Phase 4 / Section 1 rewrite
- H1: `build_pillar_pages.py` deleted in Phase 1 (not excluded from scope)
- H2: `id="pil-snav"` brought into scope; renamed to `id="area-snav"` in Phase 3; `getElementById` rename added to Phase 4
- H3: `docs/*.xml` added to Phase 2 scope and verify pass
- H4: `completion-status` removal requires parse5 or sentinel approach (not naive regex)
- M1: Phase 5 explicitly scoped to HTML/njk/XML only; never runs on JS or test files
- M2: `.pillar-hero` removal specifies full `.pillar-hero,\n` line deletion
- M3: `.pillar-tags` and `.pillar-tag` added to dead-selector removal list
- M4: Finding rejected by both reviewers — existing test comment is already accurate; no change
- M5: Exact replacement sentence specified in Section 6
- M6: `npm run build` step added to checklist
- M7: `.pil-fv-pill` → `.pi-fv-area-pill` for `pi-fv-` naming family consistency
- L1: `SPOT_PILLARS` → `SPOT_POLICY_AREAS` (matching `SAMPLE_POLICY_AREAS` convention)
- L2: `package.json` description update added to manual checklist
- NEW-1: `renderPillars` → `renderPolicyAreas` added to Phase 4
- NEW-2: Two app.js section-header comments added to Phase 4
- GPT-new: `scripts/build-site.js` explicitly noted as in scope (`scripts/*.js` glob)

**plan-eng-review (2026-05-13, Claude Sonnet 4.6):** Interactive engineering review. Findings resolved:

- A1: `id="pil-related"` and `id="pil-policyos"` brought into scope (same logic as pil-snav). Added to Section 3 note and Section 4 rename table. The comment at app.js:502 corrected (new text had retained "#pil-related"; now "#area-related").
- A2: Phase 6 committed to parse5 exclusively; sentinel option dropped as underspecified. Fail-loudly requirement added: script must throw if `div.completion-status` is not found in an expected file.
- CQ1: Three missing Phase 4 entries added: `PILLARS INDEX ACCORDION ANIMATION` comment, JS prose string at line 542, and removal of stale `pillar-count` usage comment at line 350.
- T1: New unit test added to Section 7: `tests/unit/scripts/migrate-phase3-sort.test.js` validates Phase 3 class rename array is sorted longest-first with no prefix collisions. Requires `CLASS_RENAMES` exported from migration script.
- PF1: Fail-loudly requirement added to Phase 6 parse5 spec (covered by A2).
- Checklist: Visual baseline refresh added as explicit checklist item (Section 10).

**Final parallel review (2026-05-13, GPT-5.2 + Claude Opus):** Second parallel adversarial review completed. All Critical/High/Medium findings applied:

- G1 CRITICAL: Migration script renamed from `migrate-pillars-to-policy.js` → `migrate-policy-areas.js` throughout spec (script containing "pillars" in its name would cause verify pass to always fail or require allowlist exemption).
- G2 CRITICAL: Verify pass expanded to three-check gate: (a) "pillar" word occurrences, (b) `\bpil-` / `#pil-` identifier patterns, (c) `completion-status` class names. Script and test file excluded via explicit allowlist.
- G3/C1 HIGH: Python scripts with hardcoded `docs/pillars/` paths explicitly called out; 12 scripts confirmed with runtime-breaking paths, 2 more with comment-only references (full table in Section 8 — initial spec named 3 wrong script names, corrected after codebase verification). Verify pass intentionally does not scan `.py`; manual update required before merge.
- G4 HIGH: parse5 serialization strategy split by file type. HTML files: full tree serialize. `.njk` files: sourceCodeLocation offset splicing on original source string (full serialization mangled Nunjucks tags).
- G5 HIGH: `path.join(...)` audit added as pre-Phase-2 required dry-run step; migration script must halt if unaccounted `'pillars'` path segments found in `scripts/*.js` beyond the two named files.
- C2 MEDIUM: Three additional targeted replacements for `new-compare.js` template comments added to Section 1 (cannot be caught by Phase 5 — Phase 5 never runs on JS files).
- C3/G7 MEDIUM: Phase 5 explicitly marked case-sensitive. `about-ai.html` `<code>SAMPLE_PILLARS</code>` added as targeted pre-Phase-5 replacement to prevent word-boundary match producing broken `SAMPLE_POLICY AREAS` identifier.
- G6 MEDIUM: Section 6 fail-loudly rule updated to specify that expected file list is captured from pre-Phase-1 `docs/pillars/*.html` and `src/pages/pillars/*.njk` paths before Phase 1 moves them.

