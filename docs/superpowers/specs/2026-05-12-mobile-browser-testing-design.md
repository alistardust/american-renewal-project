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

// Each entry: { slug: string, title: string }
// slug matches the filename at docs/pillars/<slug>.html
const SAMPLE_PILLARS = [
  { slug: 'executive-power',               title: 'Executive Power' },
  { slug: 'elections-and-representation',  title: 'Elections' },
  { slug: 'anti-corruption',               title: 'Anti-Corruption' },
  { slug: 'equal-justice-and-policing',    title: 'Equal Justice' },
  { slug: 'rights-and-civil-liberties',    title: 'Rights' },
  { slug: 'courts-and-judicial-system',    title: 'Courts' },
  { slug: 'checks-and-balances',           title: 'Checks' },
  { slug: 'taxation-and-wealth',           title: 'Taxation' },
  { slug: 'healthcare',                    title: 'Healthcare' },
  { slug: 'antitrust-and-corporate-power', title: 'Antitrust' },
  { slug: 'information-and-media',         title: 'Information' },
  { slug: 'gun-policy',                    title: 'Gun Policy' },
  { slug: 'term-limits-and-fitness',       title: 'Term Limits' },
  { slug: 'administrative-state',          title: 'Administrative' },
  { slug: 'technology-and-ai',             title: 'Technology' },
  { slug: 'immigration',                   title: 'Immigration' },
  { slug: 'environment-and-agriculture',   title: 'Environment' },
  { slug: 'education',                     title: 'Education' },
  { slug: 'labor-and-workers-rights',      title: 'Labor' },
  { slug: 'housing',                       title: 'Housing' },
  { slug: 'consumer-rights',               title: 'Consumer' },
  { slug: 'data-rights-and-privacy',       title: 'Data Rights' },
  { slug: 'legislative-reform',            title: 'Legislative' },
  { slug: 'foreign-policy',                title: 'Foreign Policy' },
  { slug: 'science-technology-space',      title: 'Science Technology Space' },
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
    // Playwright has no Firefox mobile device preset — only Desktop Firefox and Desktop Firefox HiDPI
    // exist in the registry. Use a custom narrow viewport with Firefox instead.
    // Note: isMobile and hasTouch are not supported in Playwright's Firefox implementation;
    // click-based interactions (including the hamburger nav) work correctly.
    use: {
      browserName: 'firefox',
      viewport: { width: 390, height: 844 },
    },
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

- `.nav-links` links are hidden via `display: none` at ≤600px (confirmed in `style.css`); use `toBeHidden()` which correctly handles `display: none` without the `opacity:0` false-pass risk
- `.nav-hamburger` button is visible and has `aria-expanded="false"` on load
- Clicking the burger sets `aria-expanded="true"` and adds `.st-open` to `.site-tree`
- Clicking the burger a second time toggles it closed (`st-open` removed, `aria-expanded="false"`)
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

Uses `locator.boundingBox()` and asserts `box.width >= 44 && box.height >= 44` (both dimensions, per WCAG 2.5.5).

#### 4. Mobile layout spot checks

- **Homepage:** `.foundations-grid` resolves to a single column at ≤640px. Assert via:
  ```js
  const cols = await page.evaluate(() =>
    getComputedStyle(document.querySelector('.foundations-grid')).gridTemplateColumns
  );
  // Single column resolves to one space-separated value (a pixel measurement)
  expect(cols.trim().split(/\s+/).length).toBe(1);
  ```
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

`npm run test:e2e` currently runs `playwright test --project=firefox`. This will be updated to `playwright test` (no project filter) so all four projects run by default on every commit, matching the agreed behaviour. This will increase per-run time roughly 4x — acceptable given the suite is fast.

`npm run test:e2e:mobile` will also be added as a convenience alias to run only the three mobile projects when debugging mobile-specific failures.

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
