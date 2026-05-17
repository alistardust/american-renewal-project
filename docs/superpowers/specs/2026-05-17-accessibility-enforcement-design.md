# Accessibility Enforcement Design

**Date:** 2026-05-17
**Issue:** [#18 — Improve accessibility and address accessibility audit](https://github.com/alistardust/freedom-and-dignity-project/issues/18)
**Status:** Approved for implementation

---

## Problem

The repository has strong written accessibility standards (WCAG 2.1 AA, CODING_STANDARDS.md, .github/copilot-instructions.md) and several good shared implementation patterns (skip link, `lang="en"`, hamburger ARIA attributes, focus utilities, reduced motion overrides). However, enforcement is incomplete:

- `scripts/check-html.js` enforces shell structure only — no a11y rules
- No automated a11y engine (axe, pa11y, or equivalent) is configured or runs in CI
- E2E tests cover `aria-current` and tap targets but not behavioral a11y flows (skip link activation, keyboard nav, focus return, reduced motion)
- Localization state is implicit rather than documented

---

## Approach

Option B: layered enforcement from day one.

- Static rules in `check-html.js` hard-fail immediately — they are deterministic and written to be clean on merge
- New behavioral E2E tests hard-fail immediately — written against current passing behavior
- Axe scanning starts report-only — violation backlog is unknown; graduates to hard-fail once clean
- i18n intent documented in the same body of work

---

## Section 1: `check-html.js` static rule extensions

**File:** `scripts/check-html.js`
**Enforcement:** hard-fail from day one
**New rules added to `checkFile()`:**

### 1.1 `lang` attribute
- `<html>` must have a non-empty `lang` attribute
- The `_base.njk` template already emits `lang="en"` — this rule should pass everywhere on merge

### 1.2 Heading hierarchy
- Collect all `h1`–`h6` elements in document order
- Fail if: (a) there is not exactly one `h1`, or (b) any heading jumps down more than one level (e.g., `h1` → `h3` with no `h2` between them)
- Jumps upward (e.g., `h3` → `h1`) are allowed — that is valid HTML section structure

### 1.3 Image alt text
- Every `<img>` must have an `alt` attribute present
- Empty string (`alt=""`) is valid for decorative images — the attribute must simply exist
- Missing `alt` attribute entirely is a failure

### 1.4 Form label coverage
- Every `<input>` (except `type="hidden"`), `<select>`, and `<textarea>` must be associated with a label via one of:
  - A `<label for="...">` referencing the element's `id`
  - Being a descendant of a `<label>` element
  - Having an `aria-label` attribute (non-empty)
  - Having an `aria-labelledby` attribute referencing an existing element id

---

## Section 2: Playwright + axe integration

**New file:** `tests/e2e/a11y.spec.js`
**New dependency:** `@axe-core/playwright` (dev)
**New npm script:** `npm run test:a11y` → `playwright test --project=firefox tests/e2e/a11y.spec.js`
**Enforcement:** report-only to start; graduates to hard-fail once violation count reaches zero

### Page coverage
A representative cross-section, not all 40+ pages:

| Page | Why |
|---|---|
| `index.html` | Homepage — most complex DOM, hero, foundation cards |
| `plan.html` | Primary nav destination |
| `policy/healthcare.html` | Representative policy area page |
| `compare/republican-party.html` | Representative compare page |
| `about-ai.html` | Non-policy root page |
| `get-involved.html` | Contribution page, contains lists and links |

### Violation handling
- Each test calls `checkA11y()` from `@axe-core/playwright`
- Violations are collected and logged with: impact level, rule ID, affected element selector, help URL
- Tests do **not** call `expect()` on violations — they pass regardless of violation count
- A prominent comment in the file marks the graduation point:
  ```js
  // TODO: once violation count is zero across all pages, remove the try/catch
  // and replace with: expect(violations).toHaveLength(0);
  ```

### CI integration
Added as a named step in `.github/workflows/build-and-deploy.yml` after the existing e2e step:
```yaml
- name: Run accessibility audit (report-only)
  run: npm run test:a11y
```
Never blocks the build in this phase. Violation output is visible in CI logs.

---

## Section 3: E2E behavioral tests

**File:** `tests/e2e/a11y-behavior.spec.js` (new, separate from `site.spec.js`)
**Enforcement:** hard-fail from day one
**Added to CI:** runs as part of `npm run test:e2e` via the existing playwright config

### 3.1 Skip link — focus and activation
- Navigate to homepage
- Press Tab once
- Assert the skip link is focused and visible (not sr-only-clipped)
- Press Enter
- Assert that `document.activeElement` is `#main-content` or a child of it
- Repeat on a policy area page (`policy/healthcare.html`)

### 3.2 Keyboard tree navigation
- Navigate to a policy area page
- Tab into `#site-tree`
- Assert a toggle button is reachable without mouse
- Press Enter/Space on a parent toggle
- Assert `aria-expanded` switches from `false` to `true`
- Assert the child list becomes visible (`.st-children` has height > 0 or `.visible` class)
- Press Enter/Space again and assert it collapses back

### 3.3 Hamburger focus return
- Set mobile viewport (375px wide)
- Press Tab to reach `.nav-hamburger` button, press Enter to open
- Assert `aria-expanded="true"`
- Press Escape
- Assert `aria-expanded="false"` and `document.activeElement` is the `.nav-hamburger` button

### 3.4 Reduced motion preference
- Emulate `prefers-reduced-motion: reduce` via `page.emulateMedia({ reducedMotion: 'reduce' })`
- Navigate to a policy area page
- Scroll a `.section-reveal` element into view
- Assert it receives the `.visible` class (content still reveals — behavior is not suppressed)
- Assert the computed `transition-duration` on the element resolves to `0s` (the `@media (prefers-reduced-motion)` override in `style.css` is applied)

---

## Section 4: i18n intent documentation

**No code changes. Two doc file updates only.**

### 4.1 `.github/ai-repo-context.md`
Add a "Localization" section:
- The site is currently English-only
- All shell text (nav, footer, WIP banner) is hard-coded in English in `app.js` and `_base.njk`
- `lang="en"` is declared on every page via the base template
- i18n is a planned future capability but has no implementation, no locale config, no translation bundles, and no language switcher
- Contributors adding shell text should write in English and note that strings will need extraction when i18n is implemented

### 4.2 `CODING_STANDARDS.md`
In the existing accessibility section, add a paragraph under the `<html lang="en">` rule clarifying:
- The site intentionally declares English and is monolingual for now
- i18n is planned but unscoped — no implementation timeline
- This absence is intentional, not an oversight

---

## Testing plan

| Test | Location | Mode | Passes today? |
|---|---|---|---|
| `lang` attribute present | `check-html.js` | hard-fail | yes — template always emits it |
| Heading hierarchy valid | `check-html.js` | hard-fail | verify on merge |
| All `<img>` have `alt` | `check-html.js` | hard-fail | verify on merge |
| Form controls have labels | `check-html.js` | hard-fail | yes — no bare form controls in shell |
| Axe scan — homepage | `a11y.spec.js` | report-only | n/a — violations logged, not blocked |
| Axe scan — 5 other pages | `a11y.spec.js` | report-only | n/a |
| Skip link focus + activation | `a11y-behavior.spec.js` | hard-fail | yes — skip link already implemented |
| Keyboard tree nav | `a11y-behavior.spec.js` | hard-fail | yes — tree ARIA already implemented |
| Hamburger focus return | `a11y-behavior.spec.js` | hard-fail | verify on merge |
| Reduced motion respected | `a11y-behavior.spec.js` | hard-fail | yes — `@media` override exists |

---

## Files changed

| File | Action |
|---|---|
| `scripts/check-html.js` | Extend `checkFile()` with 4 new rules |
| `tests/e2e/a11y.spec.js` | New — axe scan, report-only |
| `tests/e2e/a11y-behavior.spec.js` | New — behavioral tests, hard-fail |
| `.github/workflows/build-and-deploy.yml` | Add `test:a11y` step |
| `package.json` | Add `@axe-core/playwright` dev dep + `test:a11y` script |
| `.github/ai-repo-context.md` | Add Localization section |
| `CODING_STANDARDS.md` | Add i18n intent note under `lang` rule |

---

## Graduation path for axe (report-only → hard-fail)

Once CI logs show zero violations across all scanned pages:
1. In `a11y.spec.js`, replace the report-only pattern with `expect(violations).toHaveLength(0)`
2. Remove the TODO comment
3. Update the CI step label from "report-only" to the standard label
4. Update this doc to reflect hard-fail status

This is a one-line change per test. No structural changes needed.
