# Plan Page Rewrite Implementation Plan

> **For agentic workers:** REQUIRED: Use superpowers:subagent-driven-development (if subagents available) or superpowers:executing-plans to implement this plan. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Replace the negatively framed Plan page with an inspirational, open-door rewrite that speaks in an FDR/MLK register and removes the three-phase card grid entirely.

**Architecture:** Single Nunjucks source template (`src/pages/plan.njk`) is rewritten in place. The build system regenerates `docs/plan.html` from it. E2E tests are updated first (TDD) so the new assertions fail before the rewrite, then pass after.

**Tech Stack:** Nunjucks (template), Node.js (`scripts/build-site.js`), Playwright (e2e tests), Vitest (unit tests)

**Spec:** `docs/superpowers/specs/2026-05-11-plan-page-rewrite-design.md`

---

## Chunk 1: Tests and template rewrite

### Task 1: Update e2e tests for plan.html

**Files:**
- Modify: `tests/e2e/site.spec.js:960-968` (plan.html describe block, hero and phases tests)

- [ ] **Step 1: Update the hero statement test**

In `tests/e2e/site.spec.js`, find this test inside `test.describe('plan.html', ...)`:

```js
test('hero statement contains expected copy', async ({ page }) => {
  await expect(page.locator('.hero-statement')).toContainText('Voting matters');
});
```

Replace with:

```js
test('hero statement contains expected copy', async ({ page }) => {
  await expect(page.locator('.hero-statement')).toContainText('The promise of America is not yet kept');
});
```

- [ ] **Step 2: Replace the three-phase presence test with an absence test**

Find this test immediately after the one above:

```js
test('all three phase names are present', async ({ page }) => {
  await expect(page.locator('.policyos-layers')).toContainText('The Foundation');
  await expect(page.locator('.policyos-layers')).toContainText('The Campaign');
  await expect(page.locator('.policyos-layers')).toContainText('The Transformation');
});
```

Replace it entirely with:

```js
test('three-phase card grid is removed', async ({ page }) => {
  // .policyos-layers is fully deleted from this page
  await expect(page.locator('.policyos-layers')).toHaveCount(0);
});
```

- [ ] **Step 3: Add section heading assertions**

After the test added in step 2, add a new test:

```js
test('section headings match spec', async ({ page }) => {
  const headings = page.locator('h2');
  await expect(headings.filter({ hasText: 'The work of keeping a promise' })).toHaveCount(1);
  await expect(headings.filter({ hasText: 'Built together' })).toHaveCount(1);
  await expect(headings.filter({ hasText: 'The demands are the work' })).toHaveCount(1);
  await expect(headings.filter({ hasText: 'A work in progress, by design' })).toHaveCount(1);
});
```

- [ ] **Step 4: Build the site and verify the new tests fail**

```bash
node scripts/build-site.js
npx playwright test tests/e2e/site.spec.js --grep "plan.html" --reporter=list
```

Expected: the three modified/new tests fail against the old HTML. The `has correct title`, `renders h1`, `Get Involved CTA links correctly`, `nav shows aria-current on plan.html`, and `approach.html still loads after de-navving` tests should still pass (those assertions are unchanged).

---

### Task 2: Rewrite src/pages/plan.njk

**Files:**
- Modify: `src/pages/plan.njk` (full content replacement)

The current file is 79 lines. Replace the entire `{% block content %}` section and the metadata variables at the top. Keep `{% extends "_base.njk" %}`, `{% block og_url %}`, and `{% endblock %}` for the content block.

- [ ] **Step 1: Replace the metadata variables (lines 2, 4, 6)**

Change line 2 from:
```njk
{% set description = "Voting matters. Organizing matters. This is the plan that gives both something to build toward, from policy platform to structural constitutional reform." %}
```
To:
```njk
{% set description = "The policy platform built in the open, by everyone who has a stake in the outcome." %}
```

Change line 4 from:
```njk
{% block og_description %}Voting matters. Organizing matters. This is the plan that gives both something to build toward, from policy platform to structural constitutional reform.{% endblock %}
```
To:
```njk
{% block og_description %}The policy platform built in the open, by everyone who has a stake in the outcome.{% endblock %}
```

Change line 6 from:
```njk
{% block twitter_description %}Voting matters. Organizing matters. This is the plan that gives both something to build toward.{% endblock %}
```
To:
```njk
{% block twitter_description %}The policy platform built in the open, by everyone who has a stake.{% endblock %}
```

The `{% block title %}` line (line 3) is **unchanged** — it already contains the correct title with the real em-dash: `The Plan — Freedom and Dignity Project`.

- [ ] **Step 2: Replace the hero statement**

Find inside `<header class="page-hero-standard">`:

```njk
<p class="hero-statement">Voting matters. Organizing matters. This is the plan that gives both something to build toward.</p>
```

Replace with:

```njk
<p class="hero-statement">The promise of America is not yet kept. This is the plan to keep it.</p>
```

- [ ] **Step 3: Replace the opening section**

Replace the entire `<!-- WHY NOTHING ELSE IS ENOUGH -->` section (from `<section class="bg-cream ruled" aria-labelledby="why-heading">` through its closing `</section>`) with:

```html
<!-- THE WORK OF KEEPING A PROMISE -->
<section class="bg-cream ruled" aria-labelledby="opening-heading">
<div class="wrap">
  <h2 id="opening-heading">The work of keeping a promise</h2>
  <p>This country was founded on a set of promises: that every person is born with rights, that government exists to secure those rights, that no one is above the law and no one is beneath its protection.</p>
  <p>Those promises have never been fully kept. That work remains. It belongs to all of us.</p>
</div>
</section>
```

- [ ] **Step 4: Replace the three-phase section**

Replace the entire `<!-- THE THREE PHASES -->` section (from `<section class="bg-dark on-dark ruled" aria-labelledby="phases-heading">` through its closing `</section>`) with:

```html
<!-- BUILT TOGETHER -->
<section class="bg-dark on-dark ruled" aria-labelledby="built-together-heading">
<div class="wrap">
  <h2 id="built-together-heading">Built together</h2>
  <p>This platform is built in the open, because policy that belongs to everyone has to be built by everyone. Anyone can read it, question it, challenge it, improve it. The research is cited so you can check it. The positions are argued so you can disagree with them. Nothing here is handed down from on high.</p>
  <p>Coalition means intellectual participation, not just political support. This platform runs on a rule system (PolicyOS) that governs how policy is written, how evidence is evaluated, how positions are structured and tested. Those rules are designed to make open participation produce quality rather than noise. The review system, in development, is how anyone will be able to formally challenge a position, submit research, or contest a claim, not as commentary, but as structured input that enters the record.</p>
  <p>A coalition too large to be ignored cannot be built from the top. It has to be built from everywhere, by everyone who has a stake in the outcome. That is every one of us.</p>
</div>
</section>

<!-- THE DEMANDS ARE THE WORK -->
<section class="bg-cream ruled" aria-labelledby="demands-heading">
<div class="wrap">
  <h2 id="demands-heading">The demands are the work</h2>
  <p>The policy positions on this platform are live and arguable now. Building them and building the coalition around them are the same ongoing work, not sequential phases. Every person who reads a position, challenges it, or helps refine it is part of the coalition taking shape around it.</p>
  <p>A coalition organized around specific demands is one that every candidate and institution has to answer directly. They either stand for the demands or they do not. There is no room for vague agreement. That is how electoral and legislative pressure flows toward structural reform: by having demands too specific to misrepresent and a coalition too large to ignore.</p>
</div>
</section>
```

- [ ] **Step 5: Replace the WIP section**

Replace the entire `<!-- WHERE WE ARE NOW -->` section (from `<section class="bg-parchment ruled" aria-labelledby="now-heading">` through its closing `</section>`) with:

```html
<!-- WORK IN PROGRESS -->
<section class="bg-parchment ruled" aria-labelledby="wip-heading">
<div class="wrap">
  <h2 id="wip-heading">A work in progress, by design</h2>
  <p>Everything here is a work in progress, by design. The policy pillars are live, citable, and open to challenge. The research is ongoing. The platform grows as more people engage with it.</p>
  <p>The review system is in development. It is how formal challenge enters the record, and how the platform, over time, is held to its own standards.</p>
  <ul style="list-style:none;padding:0;display:flex;gap:1rem;flex-wrap:wrap;margin-top:1rem">
    <li><a href="get-involved.html">Get involved</a></li>
  </ul>
</div>
</section>
```

- [ ] **Step 6: Replace the CTA block**

Replace the inner content of `<div class="page-nav-cta">` (keep the outer wrapper and `.wrap` div, replace only their contents):

Old inner content:
```html
<p>The coalition gets built one person at a time. Here's your role in this.</p>
<a href="get-involved.html" class="btn-primary">Get Involved →</a>
```

New inner content:
```html
<p>The promise of this country is not kept by any one person, or any one party, or any one platform. It is kept by a generation that decides to keep it.</p>
<p>Come be part of this work.</p>
<ul style="display:flex;gap:1rem;flex-wrap:wrap;margin-top:1.5rem;list-style:none;padding:0">
  <li><a href="get-involved.html" class="btn-primary">Get Involved</a></li>
  <li><a href="https://github.com/alistardust/freedom-and-dignity-project" class="btn-outline" target="_blank" rel="noopener noreferrer">GitHub</a></li>
</ul>
```

- [ ] **Step 7: Verify the final file matches the spec**

Open `src/pages/plan.njk` and confirm:
- No `data-dynamic` spans anywhere in the file
- No `.policyos-layers` or `.layer-card` markup
- No `.arch-intro`, `.arch-item`, or `.pullquote` markup
- Hero statement reads: "The promise of America is not yet kept. This is the plan to keep it."
- All four new sections are present with the correct `aria-labelledby` ids: `opening-heading`, `built-together-heading`, `demands-heading`, `wip-heading`
- No em-dashes (`—`) in body copy (title line is the only permitted exception)
- No double-dashes (`--`) in body copy

---

### Task 3: Build and verify

**Files:**
- Generated: `docs/plan.html` (do not edit)

- [ ] **Step 1: Build the site**

```bash
node scripts/build-site.js
```

Expected: completes without errors. `docs/plan.html` is regenerated.

- [ ] **Step 2: Run unit tests**

```bash
npm run test:unit
```

Expected: all tests pass (no unit tests touch plan.html content).

- [ ] **Step 3: Run e2e tests for plan.html**

```bash
npx playwright test tests/e2e/site.spec.js --grep "plan.html" --reporter=list
```

Expected: all 8 tests in the `plan.html` describe block pass:
- `has correct title`
- `renders h1`
- `hero statement contains expected copy` (now checks for "The promise of America is not yet kept")
- `three-phase card grid is removed`
- `section headings match spec`
- `Get Involved CTA links correctly`
- `nav shows aria-current on plan.html`
- `approach.html still loads after de-navving`

- [ ] **Step 4: Run the full e2e suite**

```bash
npm run test:e2e
```

Expected: all tests pass. If any test outside the `plan.html` describe block fails, investigate before committing.

---

### Task 4: Commit

- [ ] **Step 1: Update policy/briefing-pack.md**

Open `policy/briefing-pack.md` and remove or update any references to the three-phase roadmap (Phase 1 / Phase 2 / Phase 3 framing), "We're in Phase 1," and the `.policyos-layers` card grid. This is a platform-state change: the phase framing has been dropped entirely. Update the Plan page description to reflect the new structure (affirmative framing, five sections, no phase roadmap).

- [ ] **Step 2: Stage files**

```bash
git add src/pages/plan.njk docs/plan.html tests/e2e/site.spec.js policy/briefing-pack.md
```

- [ ] **Step 3: Commit**

```bash
git commit -m "feat(plan): rewrite plan page with affirmative framing

Replace negative/diagnostic framing with FDR/MLK register.
Remove three-phase card grid and phase-number framing.
Add 'The demands are the work' section.
Remove hardcoded dynamic counts from WIP section.
Update e2e tests to match new content.

Co-authored-by: Copilot <223556219+Copilot@users.noreply.github.com>"
```

---

## Success criteria

Per spec `docs/superpowers/specs/2026-05-11-plan-page-rewrite-design.md`:

1. No comparison language referencing other platforms, parties, or movements
2. No negative framing as the headline or section heading
3. Hero statement, opening, "Built together," WIP, and CTA copy all match approved text in this spec
4. Three-phase card grid is fully removed
5. No hardcoded counts or `data-dynamic` count spans in the WIP section
6. Page builds cleanly, all tests pass
7. No em-dashes in body copy (title block only exception, using real `—` U+2014)
