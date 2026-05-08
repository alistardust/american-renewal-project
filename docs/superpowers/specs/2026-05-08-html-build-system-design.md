# HTML Build System Design

**Date:** 2026-05-08
**Status:** Approved for implementation
**Scope:** Phase 1 — shell migration (nav, head, footer) into a Nunjucks base template; pillar page content unchanged

---

## Problem

The site's ~45 HTML pages were hand-authored. Over time, three different nav authoring patterns diverged, producing:

- One page (`policyos.html`) with a text-only nav and no logo SVG
- One page (`policy-library.html`) with 4 hamburger buttons (hand-coded nav plus `app.js` injection on top)
- Inconsistent footer structures across compare pages
- No enforced single source of truth for the nav/footer shell

Every new page is at risk of diverging again. The current `app.js` nav-injection pattern is a footgun: it assumes the page shell is already correct and fails silently when it isn't.

---

## Decision

Introduce a Nunjucks-based static build system. A canonical base template (`_base.njk`) owns the entire shell. Per-page source files extend it and supply only their content. The build script renders everything into `docs/`. GitHub Pages deploys from the built output via the official Actions artifact workflow.

This is Phase 1 only. Pillar page content (policy cards, hero sections, etc.) stays as-is in Nunjucks blocks. No content is rewritten.

---

## Architecture

### Directory layout

```
src/
  templates/
    _base.njk          # canonical shell (nav, head, footer, scripts)
  pages/
    index.njk
    policy-library.njk
    get-involved.njk
    about-ai.njk
    pillars/
      healthcare.njk
      ...
    compare/
      republican-party.njk
      ...
    policyos.njk       # content block only; generator writes this file
  data/
    nav.json           # shared nav item list

scripts/
  build-site.js        # Nunjucks renderer: src/ → docs/
  migrate-to-njk.js    # one-time migration script
  check-html.js        # conformance assertions on docs/
  check-parity.js      # diffs regenerated vs original during migration

docs/                  # build output; committed; GH Pages deploys from here
tests/
  visual/
    baselines/         # committed reference screenshots (10 files)
```

---

## Section 1: Base template (`_base.njk`)

```nunjucks
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{% block title %}Freedom and Dignity Project{% endblock %}</title>
  {% if description %}
  <meta name="description" content="{{ description | escape }}">
  {% endif %}
  {# OG/Twitter meta, favicon, stylesheet defined once here #}
  {% block head_extra %}{% endblock %}
</head>
<body class="{{ body_class | default('') }}">
<a href="#main-content" class="skip-link sr-only focusable">Skip to main content</a>

<nav class="site-nav" aria-label="Site navigation">
  <div class="nav-inner">
    <a href="{{ base }}index.html" class="nav-brand">
      <img src="{{ base }}assets/img/logo.svg"
           alt="Freedom and Dignity Project seal" width="36" height="36">
      <span class="nav-wordmark">Freedom and Dignity<span>Project</span></span>
    </a>
    <ul class="nav-links">
      {% for item in nav %}
      <li>
        <a href="{{ base }}{{ item.href }}"
           {% if currentPage == item.href %}aria-current="page"{% endif %}>
          {{ item.label }}
        </a>
      </li>
      {% endfor %}
    </ul>
    <button type="button" class="nav-hamburger" aria-label="Open site menu"
            aria-expanded="false" aria-controls="site-tree">&#9776;</button>
  </div>
</nav>

<div id="site-tree" hidden></div>

<main id="main-content">
  {% block content %}{% endblock %}
</main>

<footer class="site-footer">
  {# standard footer defined once here #}
</footer>

<script src="{{ base }}assets/js/data.js" defer></script>
<script src="{{ base }}assets/js/app.js" defer></script>
</body>
</html>
```

### Key decisions

- **Nav links are rendered statically** from `src/data/nav.json`. `app.js` handles behavior only (hamburger toggle, active-link `aria-current`, mobile tree menu). This eliminates the runtime injection footgun.
- **`aria-current="page"`** is set at build time by comparing `currentPage` to each nav item's `href`. No JS timing issues.
- **`#site-tree` is a static placeholder** in the shell. `app.js` populates and toggles it rather than injecting it from scratch, keeping `aria-controls` valid from initial parse.
- **`<main id="main-content">`** wraps the content block in the shell so skip links always work and pages cannot omit it.
- **`base` is computed from output path depth** in `build-site.js` (empty string for root pages, `../` for one-level subdirs). Computed generically so a third directory level does not break it.
- **`description` is conditional** — the meta tag is omitted rather than rendered empty. The build script emits a warning for any public page missing a description.
- **`defer`** on both script tags.

### Page file pattern

```nunjucks
{% extends "_base.njk" %}
{% set description = "Our healthcare policy positions." %}
{% set body_class = "pillar pillar-healthcare" %}
{% block title %}Healthcare — Freedom and Dignity Project{% endblock %}
{% block content %}
  ... existing page HTML, unchanged ...
{% endblock %}
```

### Intermediate templates

`_pillar.njk` and `_compare.njk` extending `_base.njk` are **deferred to Phase 2**. In Phase 1, all pages extend `_base.njk` directly. Intermediate templates will be added when the first cross-pillar structural change requires them.

---

## Section 2: Build script (`scripts/build-site.js`)

Responsibilities:

1. Load `src/data/nav.json`
2. For each `src/pages/**/*.njk`:
   - Compute output path under `docs/`
   - Compute `base` from output path depth
   - Compute `currentPage` from the output filename relative to `docs/`
   - Render with Nunjucks, passing `{ nav, base, currentPage }`
   - Write to `docs/`
3. Emit a warning (non-fatal) for any page where `description` is not set
4. Exit non-zero if any render fails

`npm run build` invokes this script. It is idempotent.

---

## Section 3: CI workflow

### Trigger

```yaml
on:
  push:
    branches: [main]
  pull_request:
    branches: [main]
```

### Concurrency

```yaml
concurrency:
  group: pages-${{ github.ref }}
  cancel-in-progress: true
```

### Jobs

**`build` job:**

1. `actions/checkout@v4`
2. `actions/setup-node@v4` with npm cache
3. `npm ci`
4. `npm run build` — renders `src/` to `docs/`
5. `npm run check:html` — conformance assertions (see below); gates the build
6. `actions/upload-pages-artifact@v3` with `path: docs/`

**`deploy` job** (runs only on push to `main`, not on PRs):

1. `needs: build`
2. `environment: github-pages`
3. `actions/deploy-pages@v4`

### Required one-time repo change

GitHub Pages source must be switched from "Deploy from a branch" to "GitHub Actions" in repository Settings > Pages. The `docs/` directory remains committed as a last-known-good snapshot for local development and diff history, but CI deploys from the artifact, not the branch.

### Conformance check (`npm run check:html`)

Scans every `.html` file in `docs/` and asserts:

- Exactly 1 `<nav class="site-nav">`
- Exactly 1 `<main id="main-content">`
- Exactly 1 `<footer class="site-footer">`
- Exactly 1 `<button class="nav-hamburger">`
- Exactly 1 `<div id="site-tree">`
- `<ul class="nav-links">` is not empty (nav was rendered)
- No `<meta name="description" content="">` (empty description not permitted)

Any violation exits non-zero and prints the offending file and assertion. This is the enforcement layer that makes the template guarantee durable — a hand-edited or malformed page cannot be deployed.

---

## Section 4: Visual regression testing

### Baseline pages

Ten screenshots are captured at two viewports each (desktop 1280px, mobile 390px):

| Page | Template type |
|---|---|
| `index.html` | Root |
| `pillars/healthcare.html` | Pillar |
| `compare/republican-party.html` | Compare |
| `policyos.html` | Generated |
| `policy-library.html` | Multi-section root |

### Tool

Playwright (`tests/visual/visual.spec.js`), using the existing Playwright install and Firefox configuration. Playwright's built-in `toHaveScreenshot()` handles pixel diffing with a configurable threshold.

### Threshold

0.1% pixel difference. Tight enough to catch real regressions (layout collapse, missing logo, invisible text), tolerant enough to survive minor antialiasing differences between CI and local environments.

### Workflow

- Baselines are committed at `tests/visual/baselines/`. They are the reference images.
- On every PR, the CI build step spins up the built site and runs `npm run test:visual`. Screenshots are diffed against baselines.
- If any diff exceeds threshold, the check fails. The diff image is uploaded as a CI artifact.
- To intentionally update baselines (after a real design change), run `npm run test:visual:update` locally, which overwrites the baseline files. Commit the new baselines in the same PR as the design change.

### What it catches

Layout breakage, missing logo, footer structure changes, hero section collapse, text going invisible (contrast failures). It does not check content accuracy or policy text.

---

## Section 5: Migration strategy

### Approach

A one-time migration script (`scripts/migrate-to-njk.js`) does the mechanical conversion:

1. For each `.html` file in `docs/`:
   - Strip the `<html>`, `<head>`, `<nav>`, `<footer>`, and `<script>` boilerplate
   - Extract `<title>` content into `{% block title %}`
   - Extract any description meta into `{% set description %}`
   - Wrap remaining body content in `{% extends "_base.njk" %}` and `{% block content %}`
   - Write to the corresponding path under `src/pages/` with a `.njk` extension
2. Run `npm run build` to regenerate `docs/`
3. Run `npm run check:parity` to diff each regenerated file against the original and flag structural differences

### Migration order

1. Root pages (`index.html`, `policy-library.html`, `get-involved.html`, etc.) — highest traffic, easiest to verify
2. Compare pages — structurally uniform, easy to batch
3. Pillar pages (~22) — most numerous, also structurally uniform
4. Generated pages — update generators to write content blocks only

### Generator scripts

`scripts/generate-policyos.py` and similar scripts currently write complete HTML files. After migration, they write only the `{% block content %}` body for their corresponding `.njk` file. The base template owns the shell. This requires a small targeted change to each generator.

### Atomicity

The live site never breaks during migration. `docs/` is always either the old hand-authored files or the freshly built files. The switch happens in a single commit that adds all `src/` source files and replaces all `docs/` output files simultaneously. There is no intermediate state where `docs/` is partially migrated.

### `app.js` changes

After migration, `app.js` loses its nav-injection and footer-injection responsibilities. It retains:

- Hamburger toggle (sets `aria-expanded`, populates and shows `#site-tree`)
- Active-link visual highlight (reads `aria-current` from the static markup, adds `.is-active` class for CSS)
- Mobile tree menu behavior
- Dynamic value rendering (policy counts, pillar counts via `data-dynamic` spans)
- Any other page-behavior logic unrelated to shell structure

All nav-injection and footer-injection code in `app.js` is removed. The conformance check will catch any page that still relies on it.

---

## Out of scope (Phase 1)

- Intermediate templates (`_pillar.njk`, `_compare.njk`)
- Generating policy card HTML from the database
- Changing pillar page content structure
- CSS changes beyond what migration requires

---

## Success criteria

- Every HTML file in `docs/` passes the conformance check
- Visual regression baselines established for all 5 page types at 2 viewports
- CI build + conformance + visual regression run on every PR
- GH Pages deploys from Actions artifact
- No hand-authored nav, footer, or script tags in any page source file
- All existing unit and e2e tests continue to pass
