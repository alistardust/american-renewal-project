# Mobile Browser Testing — Design Spec

**Date:** 2026-05-12
**Status:** Approved

---

## Problem

The existing Playwright E2E suite runs exclusively on Desktop Firefox. The site has responsive CSS (breakpoints at 480px, 540px, 600px, 640px, 700px, 860px, 900px) and a JavaScript-driven hamburger nav, but none of this behaviour is verified by automated tests. Mobile layout regressions and touch interaction failures are invisible until a user reports them.

---

## Goal

Add full mobile browser test coverage across Android Chrome, iOS Safari, and Firefox Mobile. Mobile tests run on every commit alongside the existing desktop suite. A one-time bug sweep follows the initial test run to fix any layout or interaction failures the new tests surface.

---

## Architecture

### Approach

Shared constants module + separate mobile spec file.

- Shared constants (`PILLAR_COUNT`, `SAMPLE_PILLARS`) extracted from `site.spec.js` into `tests/e2e/shared.js`
- `site.spec.js` imports from `shared.js` — no behaviour change
- New `tests/e2e/mobile.spec.js` imports from `shared.js` and contains mobile-specific tests
- Playwright `testMatch` per project controls which spec files each project runs

### Why not a single spec file with guards?

`test.skip(!isMobile)` guards scattered through `site.spec.js` make it hard to see what the mobile surface area is. A dedicated `mobile.spec.js` keeps the mobile-specific contract explicit and independently readable.

---

## File Changes

### `tests/e2e/shared.js` (new)

Exports two constants currently duplicated or at risk of diverging between spec files:

```js
const PILLAR_COUNT = 26;

const SAMPLE_PILLARS = [
  // ... slug/title objects currently in site.spec.js
];

module.exports = { PILLAR_COUNT, SAMPLE_PILLARS };
```

### `tests/e2e/site.spec.js` (updated)

Replace inline constant declarations with:

```js
const { PILLAR_COUNT, SAMPLE_PILLARS } = require('./shared');
```

No other changes. All existing tests remain exactly as-is.

### `playwright.config.js` (updated)

Add three mobile projects and scope `testMatch` on all projects:

```js
projects: [
  {
    name: 'firefox',
    use: { ...devices['Desktop Firefox'] },
    testMatch: ['**/site.spec.js'],
  },
  {
    name: 'mobile-chrome',
    use: { ...devices['Pixel 5'] },
    testMatch: ['**/site.spec.js', '**/mobile.spec.js'],
  },
  {
    name: 'mobile-safari',
    use: { ...devices['iPhone 14'] },
    testMatch: ['**/site.spec.js', '**/mobile.spec.js'],
  },
  {
    name: 'mobile-firefox',
    use: { ...devices['Firefox Mobile'] },
    testMatch: ['**/site.spec.js', '**/mobile.spec.js'],
  },
  {
    name: 'visual-firefox',
    testDir: './tests/visual',
    use: { ...devices['Desktop Firefox'] },
  },
],
```

`visual-firefox` is unchanged — its `testDir` override already isolates it.

### `tests/e2e/mobile.spec.js` (new)

Four describe blocks:

#### 1. Hamburger nav

Runs on homepage. Verifies:

- `.nav-links` links are hidden (not visible) at mobile viewport
- `.nav-hamburger` button is visible and has `aria-expanded="false"` on load
- Clicking the burger sets `aria-expanded="true"` and adds `.st-open` to `.site-tree`
- Clicking the `.st-overlay` closes the panel (`st-open` removed, `aria-expanded="false"`)
- Pressing Escape closes an open panel

#### 2. No horizontal overflow

Runs on homepage, pillars index, and one sample pillar page. For each:

```js
const overflow = await page.evaluate(
  () => document.body.scrollWidth > window.innerWidth
);
expect(overflow).toBe(false);
```

This is the most common mobile layout regression and the most invisible to desktop testing.

#### 3. Tap target sizes

Checks that key interactive controls meet the WCAG 2.5.5 minimum of 44 × 44 CSS pixels in at least one dimension. Scoped to:

- `.nav-hamburger` button
- Primary CTA buttons on the homepage (`.entry-card a`, `.f-card a`)
- Nav links (`.nav-links a`)

Uses `locator.boundingBox()` and asserts `Math.max(box.width, box.height) >= 44`.

#### 4. Mobile layout spot checks

- **Homepage:** `.foundations-grid` computed `grid-template-columns` resolves to a single column track at ≤640px viewport
- **Sample pillar page:** `.pil-snav` (sub-nav) does not overflow its container (`scrollWidth <= offsetWidth`); policy section (`#pil-policy`) is attached

---

## Mobile Bug Sweep

After the initial test run, triage all failures. Expected areas of risk based on the CSS:

- Pillar sub-nav (`.pil-snav`) — multiple breakpoints, likely to overflow on narrow screens
- Compare pages — complex grid layout, several breakpoints down to 480px
- Foundation cards — grid collapse to single column

Fixes go to `docs/assets/css/style.css` and/or `docs/assets/js/app.js`. Each distinct layout bug gets its own atomic commit (`fix(mobile): ...`).

---

## npm Scripts

No changes needed. `npm run test:e2e` runs all projects via `playwright test --project=firefox`, which will need to be updated to run all four projects. Options:

- Change `test:e2e` to `playwright test` (runs all projects)
- Or add `test:e2e:mobile` as a separate script

Decision deferred to implementation — confirm with Ali before changing the default `test:e2e` command, since adding three more profiles will increase runtime significantly.

---

## Out of Scope

- Visual regression snapshots on mobile (separate concern, can be added later under `visual-firefox`-equivalent mobile projects)
- Real-device testing (Playwright emulation is sufficient for layout and interaction)
- Performance testing on mobile

---

## Success Criteria

1. `npm run test:e2e` passes all four browser projects with zero failures
2. The horizontal overflow check passes on all tested pages
3. The hamburger nav open/close/escape cycle passes on all three mobile profiles
4. No regressions introduced to the existing desktop Firefox suite
