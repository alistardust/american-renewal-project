# Design Spec: PolicyOS Site Exposure

**Date:** 2026-05-04
**Status:** Approved
**Author:** Sam (GitHub Copilot)

---

## Problem Statement

PolicyOS is the meta-layer governing how all policy on this platform is designed, scoped, and enforced. It has three locked layers (Platform Values, System Principles, Authoring OS) and 11 rule families covering 25 pillars. The site currently exposes only a 3-row summary table on `classification.html` with stale "Under review" status badges. The actual rules, intent, and pillar-specific overlay mappings are not accessible to visitors.

---

## Goal

Expose PolicyOS fully on the site:

1. A dedicated `policyos.html` page with the full three-layer rule system
2. Each pillar page showing the domain-specific PolicyOS overlay families that apply to it
3. `classification.html` updated with correct status and a link to the new page
4. PolicyOS added to the "The Platform" nav dropdown
5. Hard-coded policy position counts removed from prose throughout the site

---

## Approach

**Option B — Static `policyos.html` + data-injected pillar sections**

`policyos.html` is hand-authored HTML (following the pattern of `constitution.html` and `approach.html`). The pillar-to-families mapping lives in `data.js` and is injected into each pillar page at runtime by `app.js`. This matches the site's existing architecture: unique reference pages are hand-authored; repeated patterns across pages are data-driven.

---

## Architecture

### New file

- `docs/policyos.html` — standalone PolicyOS reference page, hand-authored HTML

### Modified files

| File | Change |
|------|--------|
| `docs/assets/js/data.js` | Add `siteData.policyosFamilies` (11 family metadata objects) + `policyosOverlays` field on each of the 25 pillar entries |
| `docs/assets/js/app.js` | Inject PolicyOS nav link under "The Platform" dropdown; inject `#pil-policyos` section into pillar pages |
| `docs/classification.html` | Update status badges to "Locked"; add link to `policyos.html` |
| `docs/pillars/*.html` | No manual edits — overlay section is injected by `app.js` |
| `tests/unit/data.test.js` | Tests for new overlay data structure |
| `tests/e2e/site.spec.js` | Tests for `policyos.html`, nav link, per-pillar injection, classification.html badges |
| Various `docs/*.html` | Remove hard-coded policy position counts from prose |

### Data flow

```
data.js (policyosOverlays + per-pillar mappings)
  → app.js (reads pillar slug from URL, injects overlay section)
    → pillar pages (shows applicable families with links to policyos.html#anchor)
```

---

## `policyos.html` Page Structure

Follows the same HTML shell as `constitution.html` and `approach.html`. Sections in order:

1. **Hero** — "PolicyOS: The Rules Behind the Rules" — short intro; PolicyOS is the operating logic that governs how all policy on this platform is designed, scoped, and enforced
2. **How it fits** — brief prose on the relationship between PolicyOS and the five foundations; why a meta-layer exists
3. **Layer 1: Platform Values** — intro to the floor/duty model; each value with its floor prohibition and positive duty
4. **Layer 2: System Principles** — intro explaining overlays and the inheritance model; each of the 11 families as its own named subsection with: what it governs, when it applies, and all rules with IDs (e.g., `PLOS-KERN-0001`)
5. **Layer 3: Authoring OS** — same treatment for NORM, AUTH, TEST, ENFC, PLAC, MAINT families; rules with IDs (e.g., `PAOS-NORM-0001`)
6. **Governance** — the amendment process; how PolicyOS rules are proposed, reviewed, and locked
7. **Pillar compliance** — brief note that all pillars must satisfy applicable families; link to `classification.html`

Each family section has a stable lowercase anchor: `#kern`, `#geog`, `#fedr`, `#regd`, `#enfa`, `#aigv`, `#ecol`, `#thrv`, `#demo`, `#priv`, `#econ`, `#norm`, `#auth`, `#test`, `#enfc`, `#plac`, `#maint`.

---

## `data.js` Additions

### `siteData.policyosFamilies`

An object keyed by family code, each entry having:

```js
{
  label: string,    // Human-readable name, e.g., 'Core Kernel'
  anchor: string,   // Page anchor on policyos.html, e.g., 'kern'
  summary: string,  // One-sentence description
}
```

Families:

| Code | Label | When it applies |
|------|-------|-----------------|
| KERN | Core Kernel | Universal — all pillars |
| GEOG | Geography & Access | Equal access regardless of location |
| FEDR | Federalism | Power distribution and intergovernmental design |
| REGD | Regulatory Design | Anti-capture and structural safeguards |
| ENFA | Enforcement Architecture | All pillars with enforcement, penalties, or eligibility |
| AIGV | AI Governance | Automated systems affecting rights or access |
| ECOL | Ecological Habitability | Environmental preconditions for rights |
| THRV | Material Security | Health, shelter, and material preconditions for freedom |
| DEMO | Democratic Participation | Anti-entrenchment and participation design |
| PRIV | Privacy & Surveillance | Data collection, retention, and surveillance limits |
| ECON | Economic Domination | Anti-extraction, anti-monopoly, structural fairness |

### Per-pillar overlay field

Each pillar entry in `siteData.pillars` receives:

```js
policyosOverlays: {
  mandatory: ['KERN'],
  conditional: ['GEOG', 'REGD', 'ENFA', 'AIGV'],  // varies per pillar
}
```

Source: `policy/policyos/policyos_1_0_inheritance_matrix.csv` — all 25 pillars are already mapped.

> **Naming note:** The global family metadata lives at `siteData.policyosFamilies` (11 entries, keyed by code). The per-pillar field is named `policyosOverlays` and has a different shape (`{ mandatory, conditional }`). These are intentionally distinct names to avoid ambiguity in `app.js`.

---

## `app.js` Injection

### Nav injection

Add "PolicyOS" as the fourth item in the "The Platform" dropdown (after "Rights", "Policy Library", and "Platform Overview"). Follows the same path-resolution pattern used for existing injected links.

### Per-pillar section injection

On pillar pages (detected by the presence of `#pil-snav` in the DOM — the established signal already used by `app.js` for scrollspy and other pillar-page logic):

**Injection position:** The `#pil-policyos` section is appended after `#pil-related` (the final section on all pillar pages), making it the last section on the page. A corresponding nav item ("PolicyOS") is also injected into `#pil-snav` as the final list item.

**Empty conditional overlay case:** If a pillar's `policyosOverlays.conditional` list is empty, the section still renders showing only the KERN baseline note — it is never suppressed entirely, since KERN always applies.

1. Derive the pillar slug from `location.pathname`: take the filename without extension (e.g., `executive-power` from `executive-power.html`), then replace all hyphens with underscores (`executive_power`). This normalizes to the format used in `siteData.pillars[].id`.
2. Find the current pillar in `siteData.pillars` by matching the normalized slug against `pillar.id`
2. Read `pillar.policyosOverlays`
3. Inject `<section id="pil-policyos">` into the page

**Rendered section structure:**

- Heading: "PolicyOS Overlays"
- Subhead or note: "This pillar is governed by the following PolicyOS rule families. [KERN applies to all pillars.](policyos.html#kern)"
- List of conditional families: each rendered as a card/pill showing family code, label, summary, and a "View rules →" link to `policyos.html#anchor`

KERN is shown as a universal baseline note rather than in the conditional list, keeping the displayed list focused on the domain-specific overlays.

**Path resolution:** Pillar pages are served from `docs/pillars/`, so links to the PolicyOS page must use the `base` variable already established in `app.js` (e.g., `base + 'policyos.html#kern'`), which resolves correctly as `../policyos.html#kern` from a pillar page context.

**Error handling:** If a pillar slug has no matching entry in `siteData.pillars` (e.g., a pillar added before `data.js` is updated), the injection is silently skipped — no broken page, no console error.

---

## `classification.html` Changes

1. Update the two "Under review" status badges (Layer 2: System Principles and Layer 3: Authoring OS) to "Locked". Layer 1 (Platform Values) is already "Locked" and requires no change.
2. Add after the summary table: `For the full PolicyOS documentation, including all rule families and individual rules, see <a href="policyos.html">PolicyOS</a>.`

---

## Hard-Coded Count Removal

Scan `docs/*.html` and `docs/pillars/*.html` for hard-coded policy position counts in prose (patterns like `\d[,\d]+ positions`, `\d+ subdomains`, `\d+ policy cards`). `docs/compare/*.html` is excluded — those pages describe party platforms, not this project's catalog. Remove or replace with neutral phrasing:

- Where the count was the substance: remove the sentence or replace with "the full policy catalog"
- Where the count was incidental color: drop the number

Dynamic `[data-dynamic]` spans (pillar count, family count, policy count on current page) are unaffected.

---

## Testing

### Unit tests (`data.test.js`)

- All 25 pillar entries have `policyosOverlays` with at least `mandatory: ['KERN']`
- `siteData.policyosFamilies` has exactly 11 keys
- Each family object has `label`, `anchor`, and `summary`

### E2E tests (`site.spec.js`)

- `policyos.html` loads; has correct title; nav and footer visible
- All 11 System Principles family anchors exist on `policyos.html`
- At least the 6 Authoring OS family anchors exist on `policyos.html`
- A sample pillar page (e.g., `healthcare.html`) has `#pil-policyos` section injected after load
- PolicyOS nav link appears in the "The Platform" dropdown
- `classification.html` status badges read "Locked", not "Under review"

---

## Out of Scope

- Generating `policyos.html` dynamically from the database
- Making PolicyOS rules editable through the site
- Linking individual policy positions to the specific PLOS/PAOS rules that shaped them
- Pillar compliance audit or scoring
