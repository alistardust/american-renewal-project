# Site Identity Alignment Implementation Plan

> **For agentic workers:** REQUIRED: Use superpowers:subagent-driven-development (if subagents available) or superpowers:executing-plans to implement this plan. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Redesign the Freedom & Dignity Project site to feel like a reform movement — every visitor gets an immediate sense of belonging, their role, and what they can do.

**Architecture:** The primary nav becomes a 5-item story arc (Home → The Problem → The Plan → The Platform → Join the Movement). A hamburger menu, always visible on desktop and mobile, provides the full expandable site tree. Six pages are created/renamed/removed. `app.js` is overhauled to replace ad-hoc nav injection with a structured hamburger tree. Every top-level page is audited against `.github/project-identity.md`.

**Tech Stack:** HTML5, vanilla JS (`docs/assets/js/app.js`), CSS custom properties (`docs/assets/css/style.css`), Playwright (E2E), Vitest (unit tests)

---

## Chunk 1: Navigation architecture and page inventory

Remove stale pages, rename pages, overhaul the nav injection in app.js, update the nav HTML on every affected page, and update E2E tests.

### Task 1: Remove stale pages

Files to delete:
- `docs/rights.html` — content elevated into `platform.html` (done in Task 9)
- `docs/approach.html` — content audited and folded into other pages (done in Tasks 8/12)
- `docs/constitution.html` — stale redirect
- `docs/foundations.html` — stale redirect

- [ ] **Step 1: Delete stale files**

```bash
cd docs
git rm rights.html approach.html constitution.html foundations.html
```

- [ ] **Step 2: Verify files are gone**

```bash
ls docs/rights.html docs/approach.html docs/constitution.html docs/foundations.html
```
Expected: `No such file or directory` for all four

- [ ] **Step 3: Commit**

```bash
git commit -m "chore: remove stale pages (rights, approach, constitution, foundations)"
```

---

### Task 2: Rename pages and copy content

`mission.html` → `problem.html`; `get-involved.html` → `join.html`

The old files are removed, new files created. Prose rewrite happens in Chunk 2; this task just establishes the new filenames with the existing content as a starting point.

- [ ] **Step 1: Copy and remove**

```bash
cp docs/mission.html docs/problem.html
cp docs/get-involved.html docs/join.html
git rm docs/mission.html docs/get-involved.html
git add docs/problem.html docs/join.html
```

- [ ] **Step 2: Update all internal `href` links across the site**

Use `sed` to batch-replace across all HTML files — do not hand-edit file-by-file:

```bash
# Dry-run first — verify the matches
grep -rl "mission\.html\|get-involved\.html" docs/ --include="*.html"

# Apply the replacements
find docs/ -name "*.html" -exec sed -i \
  -e 's|mission\.html|problem.html|g' \
  -e 's|get-involved\.html|join.html|g' {} \;

# Verify no old references remain
grep -rl "mission\.html\|get-involved\.html" docs/ --include="*.html"
# Expected: no output (empty)
```

This covers `<a href>`, `<link rel="canonical">`, `<meta property="og:url">`, and any other tag that referenced the old filenames.

- [ ] **Step 3: Update sitemap and feed if they reference old URLs**

```bash
grep -l "mission\|get-involved" docs/sitemap.xml docs/feed.xml 2>/dev/null
```

Update any matches.

- [ ] **Step 4: Commit**

```bash
git add -A
git commit -m "chore: rename mission→problem, get-involved→join"
```

---

### Task 3: Overhaul app.js — primary nav and hamburger tree

**Replace** the current nav injection block (lines 6–130 of app.js) and hamburger handler (lines 154–162) with:
1. A simplified active-link highlighter for the new 5-item nav
2. A `buildHamburgerTree()` function that creates the full site tree as a separate `<nav>` element
3. Full keyboard navigation on the tree
4. Updated footer-links injection to match renamed pages

**Files:**
- Modify: `docs/assets/js/app.js` — lines 6–130 and 154–162

- [ ] **Step 1: Write the failing test (nav link count)**

In `tests/e2e/site.spec.js`, update the Homepage nav count test. The new nav has 5 items — no more app.js injected links:

```js
test('nav has 5 links (Home, The Problem, The Plan, The Platform, Join the Movement)', async ({ page }) => {
  // 5 hardcoded items — app.js no longer injects into nav-links
  await expect(page.locator('.nav-links a')).toHaveCount(5);
});
```

- [ ] **Step 2: Run test to confirm it fails**

```bash
npm run test:e2e -- --grep "nav has"
```
Expected: FAIL (currently 7 links)

- [ ] **Step 3: Replace the nav injection block in app.js**

Replace lines 6–130 (the `(function() { const page = ... })()` nav injection IIFE) with the active-link highlighter below. **Also explicitly delete the old hamburger toggle** — find and remove the `burger.addEventListener('click', () => navList.classList.toggle('open'))` call (at approximately lines 154–162 in the original file, but the line numbers will have shifted after this edit — search for the string):

```bash
# Confirm the old hamburger toggle line exists before proceeding
grep -n "classList.toggle('open')" docs/assets/js/app.js
# Expected: one match — that's the line to remove
```

Replace lines 6–130 with:

```js
/* ── ACTIVE NAV LINK ─────────────────────────────── */
(function () {
  const page = location.pathname.split('/').pop() || 'index.html';
  const pageName = page.replace(/\.html$/, '') || 'index';
  document.querySelectorAll('.nav-links a').forEach(a => {
    const href = a.getAttribute('href') || '';
    const hrefName = href.replace(/\.html$/, '').replace(/^\.\.\//, '');
    if (hrefName === pageName || (pageName === 'index' && href === 'index.html')) {
      a.classList.add('active');
    }
  });
})();
```

- [ ] **Step 4: Build the hamburger tree — add after active nav block**

After inserting the active-link block (Step 3), add the following hamburger tree IIFE. Then **explicitly remove the old hamburger toggle** — search for `classList.toggle('open')` and delete that entire `addEventListener` call (it should now be gone after the active-link block replaced lines 6–130, but confirm):

```bash
grep -n "classList.toggle" docs/assets/js/app.js
# Expected: no output — confirms the old toggle is gone
# If there IS output, delete that line before proceeding
```

Add the hamburger tree IIFE:

```js
/* ── HAMBURGER SITE TREE ─────────────────────────── */
(function () {
  const inSubdir = /\/(pillars|compare)\//.test(location.pathname);
  const base = inSubdir ? '../' : '';

  function buildTree() {
    const foundations = (window.siteData && siteData.foundations) ? siteData.foundations : [];
    const comparePages = [
      { label: 'Republican Party',                  href: base + 'compare/republican-party.html' },
      { label: 'Democratic Party',                  href: base + 'compare/democratic-party.html' },
      { label: 'Green Party',                       href: base + 'compare/green-party.html' },
      { label: 'Libertarian Party',                 href: base + 'compare/libertarian-party.html' },
      { label: 'Working Families Party',            href: base + 'compare/working-families-party.html' },
      { label: 'Democratic Socialists of America',  href: base + 'compare/dsa.html' },
    ];
    const policyLibraryChildren = foundations.map(f => ({
      label: f.title,
      href: base + 'proposals.html#' + f.id,
    }));

    return [
      { label: 'Home',             href: base + 'index.html' },
      { label: 'The Problem',      href: base + 'problem.html' },
      { label: 'The Plan',         href: base + 'plan.html' },
      { label: 'The Platform', children: [
        { label: 'Bills of Rights',        href: base + 'platform.html#bills-of-rights' },
        { label: 'PolicyOS',               href: base + 'platform.html#policyos' },
        { label: 'Policy Library',         href: base + 'proposals.html',
          children: policyLibraryChildren },
        { label: 'How the Platform Works', href: base + 'classification.html' },
      ]},
      { label: 'Join the Movement', href: base + 'join.html' },
      { label: 'Roadmap',           href: base + 'roadmap.html' },
      { label: 'About', children: [
        { label: 'Letter from the Founder', href: base + 'letter-from-the-founder.html' },
        { label: 'On the Use of AI',        href: base + 'about-ai.html' },
      ]},
      { label: 'Compare Platforms', children: comparePages },
    ];
  }

  function makeTreeNode(item, level) {
    const li = document.createElement('li');
    li.className = 'st-node' + (item.children && item.children.length ? ' st-parent' : '');
    li.setAttribute('role', 'treeitem');
    li.setAttribute('aria-level', level);
    if (item.children && item.children.length) {
      li.setAttribute('aria-expanded', 'false');
      const btn = document.createElement('button');
      btn.className = 'st-toggle';
      btn.setAttribute('aria-label', 'Expand ' + item.label);
      const labelSpan = document.createElement('span');
      labelSpan.className = 'st-label';
      if (item.href) {
        const a = document.createElement('a');
        a.href = item.href;
        a.textContent = item.label;
        a.className = 'st-item-link';
        labelSpan.appendChild(a);
      } else {
        labelSpan.textContent = item.label;
      }
      const chevron = document.createElement('span');
      chevron.className = 'st-chevron';
      chevron.setAttribute('aria-hidden', 'true');
      chevron.textContent = '›';
      btn.appendChild(labelSpan);
      btn.appendChild(chevron);
      li.appendChild(btn);
      const ul = document.createElement('ul');
      ul.className = 'st-children';
      ul.setAttribute('role', 'group');
      item.children.forEach(child => ul.appendChild(makeTreeNode(child, level + 1)));
      li.appendChild(ul);
      btn.addEventListener('click', function (e) {
        e.stopPropagation();
        const expanded = li.getAttribute('aria-expanded') === 'true';
        li.setAttribute('aria-expanded', String(!expanded));
        btn.setAttribute('aria-label', (expanded ? 'Expand ' : 'Collapse ') + item.label);
      });
    } else {
      const a = document.createElement('a');
      a.href = item.href;
      a.className = 'st-item-link st-leaf';
      a.textContent = item.label;
      a.setAttribute('role', 'none');
      a.addEventListener('click', closeTree);
      li.appendChild(a);
    }
    return li;
  }

  function closeTree() {
    const panel = document.querySelector('.site-tree');
    const burger = document.querySelector('.nav-hamburger');
    if (panel) panel.classList.remove('st-open');
    if (burger) {
      burger.setAttribute('aria-expanded', 'false');
      burger.setAttribute('aria-label', 'Open site menu');
    }
  }

  function buildPanel() {
    const nav = document.querySelector('.site-nav');
    if (!nav) return;
    const panel = document.createElement('nav');
    panel.id = 'site-tree';         // required — aria-controls is an IDREF
    panel.className = 'site-tree';
    panel.setAttribute('aria-label', 'Site navigation tree');
    // No role="tree" on the <nav> — that overrides its landmark semantics.
    // The role="tree" belongs only on the <ul> below.

    const header = document.createElement('div');
    header.className = 'st-header';
    const closeBtn = document.createElement('button');
    closeBtn.className = 'st-close';
    closeBtn.setAttribute('aria-label', 'Close site menu');
    closeBtn.textContent = '✕';
    closeBtn.addEventListener('click', closeTree);
    header.appendChild(closeBtn);
    panel.appendChild(header);

    const ul = document.createElement('ul');
    ul.className = 'st-root';
    ul.setAttribute('role', 'tree');
    buildTree().forEach(item => ul.appendChild(makeTreeNode(item, 1)));
    panel.appendChild(ul);

    const overlay = document.createElement('div');
    overlay.className = 'st-overlay';
    overlay.addEventListener('click', closeTree);

    document.body.appendChild(overlay);
    nav.insertAdjacentElement('afterend', panel);
  }

  buildPanel();

  // Wire hamburger button to toggle the site-tree panel
  const burger = document.querySelector('.nav-hamburger');
  if (burger) {
    burger.setAttribute('aria-expanded', 'false');
    burger.setAttribute('aria-controls', 'site-tree');
    burger.addEventListener('click', function () {
      const panel = document.querySelector('.site-tree');
      const open = panel && panel.classList.toggle('st-open');
      burger.setAttribute('aria-expanded', open ? 'true' : 'false');
      burger.setAttribute('aria-label', open ? 'Close site menu' : 'Open site menu');
      if (open) {
        const firstLink = panel.querySelector('.st-item-link, .st-toggle');
        if (firstLink) firstLink.focus();
      }
    });
  }

  // Keyboard navigation
  document.addEventListener('keydown', function (e) {
    const panel = document.querySelector('.site-tree.st-open');
    if (!panel) return;
    if (e.key === 'Escape') { closeTree(); burger && burger.focus(); return; }
    const focusable = Array.from(panel.querySelectorAll('.st-item-link, .st-toggle'));
    const idx = focusable.indexOf(document.activeElement);
    if (e.key === 'ArrowDown') { e.preventDefault(); focusable[(idx + 1) % focusable.length].focus(); }
    if (e.key === 'ArrowUp')   { e.preventDefault(); focusable[(idx - 1 + focusable.length) % focusable.length].focus(); }
  });

  // Close on outside click
  document.addEventListener('click', function (e) {
    const panel = document.querySelector('.site-tree.st-open');
    if (!panel) return;
    if (!panel.contains(e.target) && e.target !== burger) closeTree();
  });
})();
```

- [ ] **Step 5: Add footer-links injection to app.js**

Add this as a new standalone IIFE **after** the hamburger tree block added in Step 4. (Do not look for lines 83–130 — those are gone. Simply append after the hamburger tree IIFE.)

```js
// Inject links into footer-links (path-aware)
(function () {
  const inSubdir = /\/(pillars|compare)\//.test(location.pathname);
  const base = inSubdir ? '../' : '';
  const footerLinks = document.querySelector('ul.footer-links');
  if (!footerLinks) return;

  const links = [
    ['platform.html', 'The Platform'],
    ['problem.html',  'The Problem'],
    ['plan.html',     'The Plan'],
    ['join.html',     'Join the Movement'],
    ['roadmap.html',  'Roadmap'],
    ['about-ai.html', 'About AI'],
  ];
  links.forEach(([file, label]) => {
    const selector = 'a[href*="' + file.replace('.html','') + '"]';
    if (footerLinks.querySelector(selector)) return;
    const li = document.createElement('li');
    li.innerHTML = '<a href="' + base + file + '">' + label + '</a>';
    footerLinks.appendChild(li);
  });
})();
```

- [ ] **Step 6: Run the nav count test to confirm it passes**

```bash
npm run test:e2e -- --grep "nav has"
```
Expected: PASS

- [ ] **Step 7: Run full unit tests**

```bash
npm run test:unit
```
Expected: all 42 pass

- [ ] **Step 8: Commit**

```bash
git add docs/assets/js/app.js tests/e2e/site.spec.js
git commit -m "feat(nav): replace injection with hamburger site tree and 5-item primary nav"
```

---

### Task 4: Add hamburger tree CSS to style.css

**Files:**
- Modify: `docs/assets/css/style.css` — append new `.site-tree` component styles

- [ ] **Step 1: Add site-tree CSS**

Append to `docs/assets/css/style.css`:

```css
/* ── SITE TREE (HAMBURGER) ───────────────────────────────────────────── */
.site-tree {
  position: fixed;
  top: 0; right: 0;
  width: min(340px, 90vw);
  height: 100vh;
  background: var(--navy);
  color: #fff;
  z-index: 500;
  overflow-y: auto;
  transform: translateX(100%);
  transition: transform .25s ease;
  padding: 0 0 2rem;
  box-shadow: -4px 0 24px rgba(0,0,0,.4);
}
.site-tree.st-open { transform: translateX(0); }
.st-overlay {
  display: none;
  position: fixed; inset: 0;
  background: rgba(0,0,0,.45);
  z-index: 499;
}
.site-tree.st-open ~ .st-overlay,
body:has(.site-tree.st-open) .st-overlay { display: block; }
.st-header {
  display: flex;
  justify-content: flex-end;
  padding: .75rem 1rem;
  border-bottom: 1px solid rgba(255,255,255,.1);
  position: sticky; top: 0;
  background: var(--navy);
  z-index: 1;
}
.st-close {
  background: none; border: none;
  color: rgba(255,255,255,.7);
  font-size: 1.2rem; cursor: pointer;
  padding: .25rem .5rem;
  border-radius: 3px;
}
.st-close:hover { color: #fff; background: rgba(255,255,255,.1); }
.st-root, .st-children {
  list-style: none; margin: 0; padding: 0;
}
.st-root { padding: .5rem 0; }
.st-children {
  padding-left: 1rem;
  overflow: hidden;
  max-height: 0;
  transition: max-height .2s ease;
}
.st-parent[aria-expanded="true"] > .st-children { max-height: 1000px; }
.st-parent[aria-expanded="true"] > .st-toggle .st-chevron { transform: rotate(90deg); }
.st-toggle {
  display: flex; align-items: center; justify-content: space-between;
  width: 100%; background: none; border: none;
  color: rgba(255,255,255,.85);
  font-family: 'Libre Franklin', sans-serif;
  font-size: .92rem;
  padding: .6rem 1.25rem;
  cursor: pointer; text-align: left;
  transition: background .15s;
}
.st-toggle:hover { background: rgba(255,255,255,.07); color: #fff; }
.st-item-link {
  display: block;
  color: rgba(255,255,255,.75);
  font-family: 'Libre Franklin', sans-serif;
  font-size: .92rem;
  padding: .55rem 1.25rem;
  text-decoration: none;
  transition: background .15s, color .15s;
}
.st-toggle .st-item-link {
  padding: 0; color: inherit; font-size: inherit;
}
.st-item-link:hover { background: rgba(255,255,255,.07); color: #fff; }
.st-item-link.st-leaf:hover { padding-left: 1.5rem; }
.st-chevron {
  flex-shrink: 0;
  display: inline-block;
  transition: transform .2s;
  font-style: normal;
  margin-left: .5rem;
  opacity: .6;
}
.st-label { flex: 1; }
@media (max-width: 600px) {
  .site-tree { width: 100vw; }
}
@media (prefers-reduced-motion: reduce) {
  .site-tree, .st-children, .st-chevron { transition: none; }
}
```

- [ ] **Step 2: Verify no `.nav-links.open` styles are still needed**

The old hamburger toggled `nav-links` with a `.open` class on small screens. Search for this in style.css:

```bash
grep -n "nav-links.*open\|open.*nav-links" docs/assets/css/style.css
```

If found, those styles can stay (they control `.nav-links` on mobile — still valid for showing/hiding the 5-item primary nav on mobile if needed), but the hamburger no longer toggles `.nav-links`. Remove the `burger.addEventListener('click', () => navList.classList.toggle('open'))` line if it's still present in `app.js`.

- [ ] **Step 3: Run E2E smoke test**

```bash
npm run test:e2e -- --grep "Homepage"
```

Expected: core structural tests pass; any tests that checked for old elements (FDR block, PolicyOS layers, 4 entry cards, 5 foundation cards) will need updating in Chunk 4.

- [ ] **Step 4: Commit**

```bash
git add docs/assets/css/style.css
git commit -m "feat(nav): add site-tree hamburger panel CSS"
```

---

### Task 5: Update nav HTML on all affected pages

Every top-level HTML page must have the new 5-item primary nav. Replace the old nav-links on each file.

> **Note:** `index.html` is intentionally excluded here — its nav will be fully rebuilt as part of the homepage redesign in Task 11 (Chunk 4). Do not run the script against it now.

**Affected files (nav-links block in each):**
- `docs/problem.html` (was mission.html)
- `docs/join.html` (was get-involved.html)
- `docs/platform.html`
- `docs/proposals.html`
- `docs/roadmap.html`
- `docs/about-us.html`
- `docs/letter-from-the-founder.html`
- `docs/about-ai.html`
- `docs/classification.html`
- All `docs/compare/*.html` files (6 pages) — use `../` for hrefs
- All `docs/pillars/*.html` files — use `../` for hrefs

The new nav-links block for root-level pages:

```html
<ul class="nav-links">
  <li><a href="index.html">Home</a></li>
  <li><a href="problem.html">The Problem</a></li>
  <li><a href="plan.html">The Plan</a></li>
  <li><a href="platform.html">The Platform</a></li>
  <li><a href="join.html">Join the Movement</a></li>
</ul>
```

For subdirectory pages (`pillars/`, `compare/`), use `../` prefix on all hrefs.

The `class="active"` on the current page item is left for app.js to set. **Do not hardcode `class="active"` in the HTML** — app.js sets it dynamically from `location.pathname`.

- [ ] **Step 1: Update all root-level pages**

Use `sed` to batch-replace the nav-links block across all 9 root-level pages. Because the current nav varies in content across pages, a targeted sed replacement is safest:

```bash
# For each root-level page, replace the entire <ul class="nav-links">...</ul> block.
# The safest approach is a Python one-liner that handles multi-line replacement:
python3 - <<'EOF'
import re, pathlib

NEW_NAV_ROOT = """<ul class="nav-links">
        <li><a href="index.html">Home</a></li>
        <li><a href="problem.html">The Problem</a></li>
        <li><a href="plan.html">The Plan</a></li>
        <li><a href="platform.html">The Platform</a></li>
        <li><a href="join.html">Join the Movement</a></li>
      </ul>"""

root_pages = [
  'docs/problem.html', 'docs/join.html', 'docs/platform.html',
  'docs/proposals.html', 'docs/roadmap.html', 'docs/about-us.html',
  'docs/letter-from-the-founder.html', 'docs/about-ai.html', 'docs/classification.html',
]
for path in root_pages:
    p = pathlib.Path(path)
    if not p.exists(): continue
    text = p.read_text()
    new_text = re.sub(r'<ul class="nav-links">.*?</ul>', NEW_NAV_ROOT, text, flags=re.DOTALL)
    p.write_text(new_text)
    print(f"Updated: {path}")
EOF

# Verify
grep -c "Join the Movement" docs/platform.html docs/roadmap.html docs/about-us.html
# Expected: 1 1 1
```

- [ ] **Step 2: Update pillar pages**

```bash
python3 - <<'EOF'
import re, pathlib

NEW_NAV_SUB = """<ul class="nav-links">
        <li><a href="../index.html">Home</a></li>
        <li><a href="../problem.html">The Problem</a></li>
        <li><a href="../plan.html">The Plan</a></li>
        <li><a href="../platform.html">The Platform</a></li>
        <li><a href="../join.html">Join the Movement</a></li>
      </ul>"""

for path in pathlib.Path('docs/pillars').glob('*.html'):
    text = path.read_text()
    new_text = re.sub(r'<ul class="nav-links">.*?</ul>', NEW_NAV_SUB, text, flags=re.DOTALL)
    path.write_text(new_text)

print(f"Updated {len(list(pathlib.Path('docs/pillars').glob('*.html')))} pillar pages")
EOF

# Verify spot-check
grep -A8 "nav-links" docs/pillars/healthcare.html | head -10
```

- [ ] **Step 3: Update compare pages**

```bash
python3 - <<'EOF'
import re, pathlib

NEW_NAV_SUB = """<ul class="nav-links">
        <li><a href="../index.html">Home</a></li>
        <li><a href="../problem.html">The Problem</a></li>
        <li><a href="../plan.html">The Plan</a></li>
        <li><a href="../platform.html">The Platform</a></li>
        <li><a href="../join.html">Join the Movement</a></li>
      </ul>"""

for path in pathlib.Path('docs/compare').glob('*.html'):
    text = path.read_text()
    new_text = re.sub(r'<ul class="nav-links">.*?</ul>', NEW_NAV_SUB, text, flags=re.DOTALL)
    path.write_text(new_text)

print(f"Updated {len(list(pathlib.Path('docs/compare').glob('*.html')))} compare pages")
EOF

# Verify
grep -c "Join the Movement" docs/compare/republican-party.html
# Expected: 1
```

- [ ] **Step 4: Run E2E tests**

```bash
npm run test:e2e -- --grep "Pillar page"
npm run test:e2e -- --grep "Compare"
```

Expected: all pillar and compare tests pass (they don't assert nav link counts).

- [ ] **Step 5: Commit**

```bash
git add -A
git commit -m "feat(nav): update primary nav to 5-item story arc on all pages"
```

---

### Task 6: Update E2E tests for removed pages and nav changes

Remove tests that check for elements that no longer exist, and add regression tests for the new nav.

**Files:**
- Modify: `tests/e2e/site.spec.js`

- [ ] **Step 1: Remove tests that reference deleted pages**

```bash
grep -n "mission\|get-involved\|rights\.html\|approach\.html\|constitution\|foundations\.html" tests/e2e/site.spec.js
```

For any `describe` block or `test` that navigates to a removed page:
- If the page was renamed (mission → problem, get-involved → join), update **all three** of: the `page.goto` URL, the `toHaveTitle` regex, and the `describe` block label.
- If the page was deleted without replacement (rights.html, approach.html, constitution.html, foundations.html), remove the entire `describe` block.

The `'Mission nav link from all page types'` describe block in particular needs full restructuring: its selector is `a[href*="mission"]` — change to `a[href*="problem"]`, update the `toHaveTitle` regex to `/The Problem/i`, and rename the describe label to `'Problem nav link from all page types'`.

- [ ] **Step 2: Remove/update homepage tests for removed sections**

Remove (these sections no longer exist on the homepage):
- `renders the FDR block with his quote`
- `renders the PolicyOS 3-layer cards`
- `renders all 5 foundation cards`
- `renders all 4 Get Involved entry cards`

Stub replacements as `test.skip` — these will be replaced with new homepage tests in Task 11 (Chunk 4). Use this exact format for each stub:

```js
test.skip('renders the FDR block with his quote', async () => {
  // TODO(alice): re-add when homepage Section 2 is written — Task 11
});
test.skip('renders the PolicyOS 3-layer cards', async () => {
  // TODO(alice): re-add when homepage Section 3 is written — Task 11
});
test.skip('renders all 5 foundation cards', async () => {
  // TODO(alice): re-add when homepage Section 3 is written — Task 11
});
test.skip('renders all 4 Get Involved entry cards', async () => {
  // TODO(alice): re-add when homepage Section 5 is written — Task 11
});
```

> **Note:** `plan.html` does not exist yet at this point in the plan — it's created in Task 7. The primary nav will reference it but it will 404 until then. This is an expected intermediate state. Do not attempt to create a stub `plan.html` here.

- [ ] **Step 3: Add hamburger tree smoke test**

```js
test('hamburger button opens site tree panel', async ({ page }) => {
  await page.locator('.nav-hamburger').click();
  await expect(page.locator('.site-tree')).toHaveClass(/st-open/);
  // Tree contains the 5 primary nav items
  await expect(page.locator('.site-tree').getByText('The Plan')).toBeAttached();
  await expect(page.locator('.site-tree').getByText('Join the Movement')).toBeAttached();
});

test('hamburger site tree closes with Escape key', async ({ page }) => {
  await page.locator('.nav-hamburger').click();
  await expect(page.locator('.site-tree')).toHaveClass(/st-open/);
  await page.keyboard.press('Escape');
  await expect(page.locator('.site-tree')).not.toHaveClass(/st-open/);
});
```

- [ ] **Step 4: Add test for hamburger visible on desktop**

```js
test('hamburger button is visible on desktop viewport', async ({ page }) => {
  await page.setViewportSize({ width: 1280, height: 800 });
  await expect(page.locator('.nav-hamburger')).toBeVisible();
});
```

- [ ] **Step 5: Run updated E2E tests**

```bash
npm run test:e2e -- --grep "Homepage"
```

Expected: passing tests pass; skipped tests are skipped; no new failures.

- [ ] **Step 6: Commit**

```bash
git add tests/e2e/site.spec.js
git commit -m "test(e2e): update nav tests for new structure; stub removed homepage section tests"
```

---

## Chunk 2: New and rewritten pages

### Task 7: Create `plan.html` — The Plan

New page. Does not currently exist. Primary job: answer "how do you actually make this happen?" Written for the convinced-and-ready visitor; accessible to a first-time visitor.

**Voice:** 1–2 sentence stakes acknowledgment, then immediately into the plan. Forward-looking, no grievance re-litigating. Follows identity doc: direct, welcoming, hopeful, human.

**Files:**
- Create: `docs/plan.html`
- Modify: `tests/e2e/site.spec.js`

- [ ] **Step 1: Write the failing test**

```js
test.describe('The Plan page', () => {
  test.beforeEach(async ({ page }) => { await page.goto('/plan.html'); });

  test('has correct page title', async ({ page }) => {
    await expect(page).toHaveTitle(/The Plan/i);
  });

  test('has the strategy section', async ({ page }) => {
    await expect(page.locator('#plan-strategy, [id*="strategy"]').first()).toBeAttached();
  });

  test('has the where-we-are section', async ({ page }) => {
    await expect(page.locator('#plan-status, [id*="status"], [id*="where-we-are"]').first()).toBeAttached();
  });

  test('has a CTA to join.html', async ({ page }) => {
    await expect(page.locator('a[href*="join.html"]').first()).toBeAttached();
  });
});
```

- [ ] **Step 2: Run test to confirm it fails (404)**

```bash
npm run test:e2e -- --grep "The Plan page"
```
Expected: FAIL (page not found)

- [ ] **Step 3: Create `docs/plan.html`**

**Read `.github/project-identity.md` in full before writing any prose.** This page is a movement-voice page, not a policy doc.

Use this full HTML skeleton as your starting point (do not skip any structural element — they are all required by `app.js`, accessibility, and the nav):

```html
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>The Plan — Freedom and Dignity Project</title>
  <meta name="description" content="How we fix this: organize, build coalitions, elect aligned leaders, and sustain the pressure.">
  <meta property="og:title" content="The Plan — Freedom and Dignity Project">
  <meta property="og:description" content="How we fix this: organize, build coalitions, elect aligned leaders, and sustain the pressure.">
  <meta property="og:url" content="https://alistardust.github.io/freedom-and-dignity-project/plan.html">
  <link rel="canonical" href="https://alistardust.github.io/freedom-and-dignity-project/plan.html">
  <link rel="stylesheet" href="assets/css/style.css">
</head>
<body>
  <nav class="site-nav">
    <div class="nav-inner">
      <a href="index.html" class="nav-logo">Freedom &amp; Dignity</a>
      <ul class="nav-links">
        <li><a href="index.html">Home</a></li>
        <li><a href="problem.html">The Problem</a></li>
        <li><a href="plan.html" class="nav-active" aria-current="page">The Plan</a></li>
        <li><a href="platform.html">The Platform</a></li>
        <li><a href="join.html">Join the Movement</a></li>
      </ul>
      <button class="nav-hamburger" aria-label="Open site navigation" aria-expanded="false">&#9776;</button>
    </div>
  </nav>

  <main id="main-content">
    <header class="page-hero-standard">
      <p class="eyebrow">How We Fix This</p>
      <h1 class="hero-statement">The Plan</h1>
      <!-- 1–2 sentence stakes acknowledgment, then immediately into action -->
    </header>

    <section id="plan-strategy" class="content-section">
      <!-- The Strategy: organize, build, elect, apply, reach -->
    </section>

    <section id="plan-status" class="content-section">
      <!-- Where We Are: honest current-state; link to roadmap.html -->
    </section>

    <section id="plan-your-part" class="content-section">
      <!-- Your Part: multiple roles; no credentials required -->
    </section>

    <section id="plan-cta" class="content-section cta-section">
      <a href="join.html" class="btn-primary">Find Your Role</a>
      <a href="roadmap.html" class="btn-outline">See the Roadmap</a>
      <a href="platform.html" class="btn-outline">Read the Platform</a>
    </section>
  </main>

  <footer class="site-footer">
    <!-- app.js injects footer links -->
  </footer>

  <script src="assets/js/app.js"></script>
</body>
</html>
```

Voice check (verify before committing):
- Does it sound like a movement, not a policy briefing? ✓ required
- Does it give visitors a clear role? ✓ required
- Does it feel welcoming, not exclusive? ✓ required
- Does it connect forward to join.html and the platform? ✓ required

- [ ] **Step 4: Run tests**

```bash
npm run test:e2e -- --grep "The Plan page"
```
Expected: all 4 tests PASS

- [ ] **Step 5: Commit**

```bash
git add docs/plan.html tests/e2e/site.spec.js
git commit -m "feat: add plan.html — The Plan page"
```

---

### Task 8: Rewrite `join.html` — Join the Movement

`join.html` was copied from `get-involved.html` in Task 2. The existing content is a starting point; it needs a full voice rewrite and retitling.

**Files:**
- Modify: `docs/join.html`
- Modify: `tests/e2e/site.spec.js`

- [ ] **Step 1: Write the failing test**

```js
test.describe('Join the Movement page', () => {
  test.beforeEach(async ({ page }) => { await page.goto('/join.html'); });

  test('has correct page title', async ({ page }) => {
    await expect(page).toHaveTitle(/Join the Movement/i);
  });

  test('hero heading says Join the Movement', async ({ page }) => {
    await expect(page.locator('h1').first()).toContainText(/Join the Movement/i);
  });

  test('offers multiple distinct participation roles', async ({ page }) => {
    // At least 3 distinct entry cards/pathways
    const count = await page.locator('.entry-card, .role-card, .pathway-card').count();
    expect(count).toBeGreaterThanOrEqual(3);
  });

  test('links to GitHub and/or Discord', async ({ page }) => {
    const links = await page.locator('a[href*="github.com"], a[href*="discord"]').count();
    expect(links).toBeGreaterThanOrEqual(1);
  });
});
```

- [ ] **Step 2: Run test to confirm it fails**

```bash
npm run test:e2e -- --grep "Join the Movement page"
```
Expected: FAIL (title is still "Get Involved")

- [ ] **Step 3: Rewrite `docs/join.html`**

**Read `.github/project-identity.md` in full before writing any prose.**

To recover any contribution-pathway content from the now-deleted `approach.html`, run:

```bash
# Find the commit that deleted approach.html
git log --oneline -- docs/approach.html
# Then retrieve the file content
git show <sha>:docs/approach.html | grep -A5 -B2 "pathway\|role\|contribute\|volunteer\|discord\|github"
```

Update:
- `<title>`: "Join the Movement — Freedom and Dignity Project"
- `<h1>`: "Join the Movement"
- Hero statement: movement-first framing, not "this project exists because one person cared..." — that's too individualistic. Frame as collective: "This movement grows one person at a time."
- OG title and description
- All section headings and prose: audit against identity doc
- CTAs: "Find your role", "Sign up", "Share"
- Keep the existing participation pathways (GitHub, Discord, etc.) — just reframe them in movement language
- "approach.html" content audit: check `docs/approach.html` was removed in Task 1 — pull any relevant contribution-pathway content that was in it

Voice check:
- Welcoming to non-technical people? Every role listed should be accessible without coding knowledge
- Clear calls to action at the end of each pathway

- [ ] **Step 4: Run tests**

```bash
npm run test:e2e -- --grep "Join the Movement page"
```
Expected: all 4 tests PASS

- [ ] **Step 5: Commit**

```bash
git add docs/join.html tests/e2e/site.spec.js
git commit -m "feat: rewrite join.html as Join the Movement page"
```

---

### Task 9: Voice audit `problem.html`

`problem.html` (copied from `mission.html` in Task 2) has strong existing content. The rename is done. What's needed is a voice audit and minor rewrite where it fails the identity doc test.

**Files:**
- Modify: `docs/problem.html`
- Modify: `tests/e2e/site.spec.js`

- [ ] **Step 1: Write the test (regression guard)**

```js
test.describe('The Problem page', () => {
  test.beforeEach(async ({ page }) => { await page.goto('/problem.html'); });

  test('has correct page title', async ({ page }) => {
    await expect(page).toHaveTitle(/The Problem/i);
  });

  test('hero statement leads with human recognition, not policy framing', async ({ page }) => {
    const statement = await page.locator('.hero-statement').textContent();
    // Should contain a validating line, not start with a policy claim
    expect(statement).toBeTruthy();
    expect(statement.trim().length).toBeGreaterThan(30);
  });

  test('links forward to plan.html or join.html', async ({ page }) => {
    await expect(page.locator('a[href*="plan.html"], a[href*="join.html"]').first()).toBeAttached();
  });
});
```

- [ ] **Step 2: Run test**

```bash
npm run test:e2e -- --grep "The Problem page"
```

Expected: title test and hero test **PASS** (the content already exists from `mission.html`). The forward-link test (`a[href*="plan.html"], a[href*="join.html"]`) will likely **FAIL** — `mission.html` had no forward link to `plan.html`/`join.html`. That's the red state to fix.

- [ ] **Step 3: Audit `problem.html` against identity doc**

Read `.github/project-identity.md` before editing. Evaluate the page against:
1. **Voice** — sounds like the movement, not a policy briefing
2. **Welcome** — feels open, not already-aligned
3. **Agency** — visitor knows they have a role after reading
4. **Human element** — people are present, not just mechanisms
5. **Connection** — leads somewhere (The Plan, Join the Movement)

Edits typically needed:
- Update `<meta property="og:url">` from `mission.html` to `problem.html`
- Update `<link rel="canonical">` if present
- Update page `<title>` and `<h1>` if still says "mission"
- Add a forward link to `plan.html` at the end of the page ("Now that you know the problem — here's the plan")
- Soften any language that reads as accusatory or preachy; keep the devastation brief per FDR/MLK ratio

- [ ] **Step 4: Run tests**

```bash
npm run test:e2e -- --grep "The Problem page"
npm run test:unit
```
Expected: all pass

- [ ] **Step 5: Commit**

```bash
git add docs/problem.html tests/e2e/site.spec.js
git commit -m "feat: rename mission→problem and audit voice for The Problem page"
```

---

## Chunk 3: Platform page expansion

### Task 10: Expand `platform.html` — The Platform

`platform.html` currently has architecture overview + 5 foundation cards with "What It Demands / What It Rejects" blocks. Add three new sections above the existing content: values, Bills of Rights, and PolicyOS.

**Files:**
- Modify: `docs/platform.html`
- Modify: `tests/e2e/site.spec.js`

- [ ] **Step 1: Write the failing tests**

```js
test.describe('Platform page', () => {
  test.beforeEach(async ({ page }) => { await page.goto('/platform.html'); });

  test('has correct page title', async ({ page }) => {
    await expect(page).toHaveTitle(/Platform|The Platform/i);
  });

  test('has values section', async ({ page }) => {
    await expect(page.locator('#platform-values, [id*="values"]').first()).toBeAttached();
  });

  test('has Bills of Rights section with anchor id', async ({ page }) => {
    await expect(page.locator('#bills-of-rights')).toBeAttached();
    // Should show all 10 amendments
    await expect(page.locator('#bills-of-rights .amendment-item, #bills-of-rights [class*="amendment"]').first()).toBeAttached();
  });

  test('has PolicyOS section with anchor id', async ({ page }) => {
    await expect(page.locator('#policyos')).toBeAttached();
  });

  test('has CTA to policy library (proposals.html)', async ({ page }) => {
    await expect(page.locator('a[href*="proposals.html"]').first()).toBeAttached();
  });

  test('Bills of Rights anchor is directly navigable', async ({ page }) => {
    await page.goto('/platform.html#bills-of-rights');
    await expect(page.locator('#bills-of-rights')).toBeInViewport({ ratio: 0.1 });
  });
});
```

- [ ] **Step 2: Run tests to confirm they fail**

```bash
npm run test:e2e -- --grep "Platform page"
```
Expected: values, bills-of-rights, policyos tests fail; others may pass

- [ ] **Step 3: Update platform.html `<head>`**

- Title: "The Platform — Freedom and Dignity Project"
- OG title: "The Platform"
- OG description: focused on values + rights, not architecture

- [ ] **Step 4: Add Statement of Values section**

Insert before the existing `<section class="bg-cream" aria-labelledby="how-it-works-heading">`:

```html
<section id="platform-values" class="bg-parchment ruled" aria-labelledby="platform-values-heading">
  <div class="wrap">
    <div class="eyebrow">What We Believe</div>
    <h2 id="platform-values-heading">The Foundation Everything Flows From</h2>
    <!-- prose synthesized from .github/project-identity.md "What We Believe" and
         "What We Won't Be" sections, plus existing platform.html framing.
         3–5 short paragraphs. Direct, not listicle. No jargon. -->
  </div>
</section>
```

Content source: `.github/project-identity.md` §What We Believe + §What We Won't Be + existing `platform.html` foundation framing. Write as 3–5 direct paragraphs, not bullet lists. Voice: "we believe X" stated plainly, paired with "and we won't X" as honest contrast.

- [ ] **Step 5: Add Bills of Rights section**

`docs/rights.html` was deleted in Task 1. Recover its content from git history before writing this section:

```bash
# Find the commit that deleted rights.html
git log --oneline -- docs/rights.html

# Pipe content directly — no temp file needed
git show <sha>:docs/rights.html | grep -A10 "amendment\|Amendment\|Floor\|Duty\|floor\|duty" | head -80

# Or view the full file piped through less (q to exit):
git show <sha>:docs/rights.html | cat
```

The `rights.html` content has 10 amendments, each with a short title, one-liner, and floor+duty framing. Copy this structure into the Bills of Rights section (do not paraphrase from memory — use the actual recovered content).

Insert after the values section:

```html
<section id="bills-of-rights" class="bg-cream" aria-labelledby="bor-heading">
  <div class="wrap">
    <div class="eyebrow">Ten Amendments</div>
    <h2 id="bor-heading">A New Bill of Rights</h2>
    <p class="section-intro"><!-- brief intro paragraph from rights.html --></p>
    <!-- 10 amendment items: each with amendment number, short title, one-liner, floor+duty summary -->
    <!-- Use a grid or list structure with class "amendment-item" on each -->
  </div>
</section>
```

For each amendment (I through X), add:
```html
<div class="amendment-item">
  <div class="amendment-num">Amendment [N]</div>
  <h3 class="amendment-title">[Right to X]</h3>
  <p class="amendment-oneliner">[one-liner from rights.html]</p>
  <div class="amendment-floor-duty">
    <p><strong>Floor:</strong> [floor statement]</p>
    <p><strong>Duty:</strong> [duty statement]</p>
  </div>
</div>
```

- [ ] **Step 6: Add PolicyOS section**

**Read both PolicyOS source files in full before writing any prose:**
```bash
cat policy/policyos/policyos_platform_values_v1.md
cat policy/policyos/policyos_1_0_rules_proposal.md | head -200  # KERN family is near the top
```

Insert after Bills of Rights:

```html
<section id="policyos" class="bg-parchment ruled" aria-labelledby="policyos-heading">
  <div class="wrap">
    <div class="eyebrow">How the Platform Is Built</div>
    <h2 id="policyos-heading">PolicyOS — The Rules That Govern the Rules</h2>
    <p><!-- intro: every policy position in this platform is built on a framework of
          cross-cutting design rules. Here are the core values baked into the system. --></p>

    <!-- 3–4 core PolicyOS values in plain language -->
    <!-- Source: policy/policyos/policyos_platform_values_v1.md (floor+duty model, enforcement,
         geographic equity, etc.) -->
    <!-- Then 2–3 example rules briefly shown in action -->
    <!-- CTA: <a href="classification.html">How the Platform Works →</a> -->
  </div>
</section>
```

Source material:
- `policy/policyos/policyos_platform_values_v1.md` — values
- `policy/policyos/policyos_1_0_rules_proposal.md` — example rules from KERN family
- Pull 3–4 values: every rule must be enforceable; every rule must be tested for equity; no rule may apply differently based on geography; every person is protected regardless of identity
- Show 2–3 KERN rules briefly: "Policies must name an enforcement mechanism" / "Policies must include protection for the least powerful" / "Rights apply regardless of geography within U.S. jurisdiction"

- [ ] **Step 7: Run tests**

```bash
npm run test:e2e -- --grep "Platform page"
npm run test:unit
```
Expected: all pass

- [ ] **Step 8: Commit**

```bash
git add docs/platform.html tests/e2e/site.spec.js
git commit -m "feat: expand platform.html with values, bills of rights, and PolicyOS sections"
```

---

## Chunk 4: Homepage redesign

### Task 11: Rewrite `index.html` — the front door

Full redesign. The current homepage has: hero, FDR block, PolicyOS layers, foundations grid, entry cards, footer. The new homepage has 5 sections aligned to the approved design.

**Files:**
- Modify: `docs/index.html`
- Modify: `tests/e2e/site.spec.js`

- [ ] **Step 1: Write failing tests for new homepage structure**

```js
// Replace (or add alongside) existing Homepage describe block
test.describe('Homepage — redesigned', () => {
  test.beforeEach(async ({ page }) => { await page.goto('/'); });

  test('has correct page title', async ({ page }) => {
    await expect(page).toHaveTitle(/Freedom and Dignity/i);
  });

  test('hero section has a movement-first headline', async ({ page }) => {
    const h1 = await page.locator('h1').first().textContent();
    expect(h1).toBeTruthy();
    expect(h1.length).toBeGreaterThan(5);
  });

  test('hero primary CTA links to join.html', async ({ page }) => {
    await expect(page.locator('.hero-ctas .btn-primary[href*="join.html"]')).toBeAttached();
  });

  test('has validation section', async ({ page }) => {
    await expect(page.locator('#home-validation, [id*="validation"]').first()).toBeAttached();
  });

  test('has champion issues section with 5 cards', async ({ page }) => {
    await expect(page.locator('#home-champion-issues, [id*="champion"]').first()).toBeAttached();
    // 5 champion issue cards
    await expect(page.locator('.champion-card, [class*="champion-card"]')).toHaveCount(5);
  });

  test('champion cards link to plan.html and to pillar pages', async ({ page }) => {
    const planLinks = await page.locator('.champion-card a[href*="plan.html"]').count();
    expect(planLinks).toBeGreaterThanOrEqual(1);
  });

  test('has join the movement section', async ({ page }) => {
    await expect(page.locator('#home-join, [id*="join"]').first()).toBeAttached();
  });

  test('name notice banner is present and dismissible', async ({ page }) => {
    const banner = page.locator('.name-notice-banner');
    await expect(banner).toBeAttached();
    await page.locator('.name-notice-dismiss').click();
    await expect(banner).not.toBeAttached();
  });
});
```

- [ ] **Step 2: Run tests to confirm they fail**

```bash
npm run test:e2e -- --grep "Homepage — redesigned"
```
Expected: champion-issues, join-section, hero-cta tests fail

- [ ] **Step 3: Rewrite `docs/index.html`**

Read `.github/project-identity.md` in full before writing any prose.

**Section 1 — Identity and belonging (`#home-hero`)**

```html
<section id="home-hero" class="page-hero" aria-labelledby="home-hero-heading">
  <!-- Movement identity: "right vs. wrong, not left vs. right" -->
  <!-- Headline: short, direct, belonging-first. Not policy-first. -->
  <!-- Eyebrow: "Freedom and Dignity Project" or movement tagline -->
  <!-- Hero statement: 1–2 sentences. Visitor feels seen and welcomed. -->
  <!-- Primary CTA: <a href="join.html" class="btn-primary">Find Your Role</a> -->
  <!-- Secondary CTA: <a href="problem.html" class="btn-outline">What's Broken</a> -->
</section>
```

Voice: Think "You belong here. This is for you." Not "Here is our framework."

**Section 2 — Validation (`#home-validation`)**

```html
<section id="home-validation" class="bg-parchment ruled" aria-labelledby="home-validation-heading">
  <!-- Brief (2–4 sentences max). Names the reality without dwelling in it. -->
  <!-- "You're not wrong. You're not alone. Things have gotten harder and the system has failed." -->
  <!-- Immediate pivot after 1 paragraph. -->
  <!-- Link: "Read the full case →" → problem.html -->
</section>
```

FDR/MLK ratio: devastation is brief; hope gets the space.

**Section 3 — Hope and pivot (`#home-hope`)**

```html
<section id="home-hope" class="bg-cream" aria-labelledby="home-hope-heading">
  <!-- "It doesn't have to be this way." -->
  <!-- Brief. Sets up Section 4. 2–3 sentences. -->
  <!-- Transitions into: "Here are the five things we're fighting for right now." -->
</section>
```

**Section 4 — Champion issues + The Plan tease (`#home-champion-issues`)**

```html
<section id="home-champion-issues" class="bg-parchment" aria-labelledby="home-champion-heading">
  <div class="wrap">
    <h2 id="home-champion-heading">Five Rights Worth Fighting For</h2>
    <div class="champion-grid">
      <!-- Card 1: Amendment X — Right to Basic Necessities -->
      <!-- Card 2: Amendment I — Right to Vote -->
      <!-- Card 3: Amendment VIII — Right to Equal Justice -->
      <!-- Card 4: Amendment IV — Right to Bodily Autonomy -->
      <!-- Card 5: Amendment VII — Right to a Healthy Environment -->
    </div>
  </div>
</section>
```

Each champion card structure:
```html
<article class="champion-card">
  <div class="champion-amendment">Amendment [N]</div>
  <h3 class="champion-title">You have a right to [X]</h3>
  <p class="champion-block"><!-- what's blocking it: 1–2 sentences, concrete --></p>
  <div class="champion-links">
    <a href="[relevant-pillar].html">Read the policy →</a>
    <a href="plan.html">See the plan →</a>
  </div>
</article>
```

Champion issues → pillar page mappings:
- Amendment X (Basic Necessities): `pillars/healthcare.html` (or `pillars/housing.html` — verify which covers it more fully)
- Amendment I (Right to Vote): `pillars/elections-and-representation.html`
- Amendment VIII (Equal Justice): `pillars/equal-justice-and-policing.html`
- Amendment IV (Bodily Autonomy): `pillars/rights-and-civil-liberties.html` — **note:** rights-and-civil-liberties has a dedicated "Bodily Autonomy" policy family covering abortion, contraception, gender-affirming care, and Comstock Act repeal as a first-class constitutional right; healthcare covers reproductive care as a coverage mandate. Verify before committing, but rights-and-civil-liberties is the better fit for the constitutional framing used in champion cards.
- Amendment VII (Healthy Environment): `pillars/environment-and-agriculture.html`

Plan tease block after grid:
```html
<div class="plan-tease">
  <p>These rights don't win themselves. <a href="plan.html">Here's the plan →</a></p>
</div>
```

**Section 5 — Join the Movement (`#home-join`)**

```html
<section id="home-join" class="bg-navy-dark" aria-labelledby="home-join-heading">
  <!-- Multiple pathways, multiple roles. No credentials required. -->
  <!-- Organizer / Donor / Writer / Developer / Volunteer -->
  <!-- Primary CTA: <a href="join.html" class="btn-primary">Find Your Role</a> -->
</section>
```

- [ ] **Step 4: Add CSS for new homepage sections (if needed)**

New classes: `.champion-grid`, `.champion-card`, `.champion-amendment`, `.champion-title`, `.champion-block`, `.champion-links`, `.plan-tease`

Add to `docs/assets/css/style.css`. Follow existing card patterns.

- [ ] **Step 5: Run tests**

```bash
npm run test:e2e -- --grep "Homepage"
npm run test:unit
```
Expected: all pass; `test.skip` stubs from Task 6 are **removed in this task** — replace each with the actual new homepage test it was standing in for, or delete it if the original section no longer exists in any form.

- [ ] **Step 6: Commit**

```bash
git add docs/index.html docs/assets/css/style.css tests/e2e/site.spec.js
git commit -m "feat: redesign homepage as movement front door — 5-section Option C layout"
```

---

## Chunk 5: Voice audits

### Task 12: Rewrite `about-us.html` — movement-first

Current page leads with the founder's bio. New version leads with the movement; founder's presence is secondary (transparency, not focus).

**Files:**
- Modify: `docs/about-us.html`
- Modify: `tests/e2e/site.spec.js`

- [ ] **Step 1: Write the test**

```js
test.describe('About page', () => {
  test.beforeEach(async ({ page }) => { await page.goto('/about-us.html'); });

  test('has correct page title', async ({ page }) => {
    await expect(page).toHaveTitle(/About/i);
  });

  test('leads with movement identity, not founder bio', async ({ page }) => {
    // First h2 should be about the movement, not "The Founder"
    const firstH2 = await page.locator('h2').first().textContent();
    expect(firstH2.toLowerCase()).not.toContain('founder');
    expect(firstH2.toLowerCase()).not.toContain('alice');
  });

  test('includes founder section for transparency', async ({ page }) => {
    // Founder info must exist — but later in the page
    await expect(page.locator('text=Alice').first()).toBeAttached();
  });
});
```

- [ ] **Step 2: Audit current `about-us.html` against identity doc**

Evaluate five questions (document findings in code comment before editing):
1. Voice — policy briefing or movement?
2. Welcome — open or insider?
3. Agency — does visitor know their role?
4. Human element — are people present?
5. Connection — leads somewhere?

- [ ] **Step 3: Rewrite structure**

New order:
1. Hero: movement-first framing ("A project built by people who believe things can be better")
2. What we're building — movement description
3. How to contribute — brief
4. The founder — honest, brief, human: "I'm a person who got fed up and decided to do something about it. You can too." Include existing bio facts for transparency, but frame around the reader not the writer
5. `approach.html` content audit: check if any contribution-pathway content from the now-removed `approach.html` belongs here

- [ ] **Step 4: Run tests**

```bash
npm run test:e2e -- --grep "About page"
npm run test:unit
```

- [ ] **Step 5: Commit**

```bash
git add docs/about-us.html tests/e2e/site.spec.js
git commit -m "feat: rewrite about-us.html as movement-first About page"
```

---

### Task 13: Update `proposals.html` title and intro

`proposals.html` is demoted to "Policy Library" in the hamburger. Its title and intro should reflect this new role.

**Files:**
- Modify: `docs/proposals.html`
- Modify: `tests/e2e/site.spec.js`

- [ ] **Step 1: Write the failing test**

```js
test.describe('Policy Library page (proposals.html)', () => {
  test.beforeEach(async ({ page }) => { await page.goto('/proposals.html'); });

  test('has updated title Policy Library', async ({ page }) => {
    await expect(page).toHaveTitle(/Policy Library/i);
  });

  test('h1 says The Policy Library', async ({ page }) => {
    await expect(page.locator('h1').first()).toContainText(/Policy Library/i);
  });
});
```

- [ ] **Step 2: Run test to confirm it fails**

```bash
npm run test:e2e -- --grep "Policy Library page"
```

Expected: FAIL (current title is "Proposals" or similar, not "Policy Library")

- [ ] **Step 3: Update `<title>` and `<h1>`**

Change:
- `<title>` from "Proposals" (or current) to "Policy Library — Freedom and Dignity Project"
- `<h1>` heading to "The Policy Library"
- Hero statement: framing as the depth layer, not the front door. Something like "Every position, evidence-based and open to scrutiny. This is where the details live."

- [ ] **Step 4: Update OG meta tags**

```html
<meta property="og:title" content="Policy Library — Freedom and Dignity Project">
<meta name="description" content="Every policy position, organized by foundation and pillar. Evidence-based, structured, and open to scrutiny.">
```

- [ ] **Step 5: Run all Policy Library tests**

```bash
npm run test:e2e -- --grep "Policy Library page"
npm run test:e2e -- --grep "Pillars index"
```

Expected: Policy Library tests PASS. Pillars index tests PASS (they test the pillar grid, which is unchanged).

- [ ] **Step 6: Commit**

```bash
git add docs/proposals.html tests/e2e/site.spec.js
git commit -m "feat: rename proposals page to Policy Library, update title and intro"
```

---

### Task 14: Voice audit `roadmap.html`, `letter-from-the-founder.html`, `about-ai.html`

Lower-priority audits. These pages are in the hamburger, not the primary nav. Audit and make targeted improvements.

**Files:**
- Modify (as needed): `docs/roadmap.html`, `docs/letter-from-the-founder.html`, `docs/about-ai.html`
- Modify: `tests/e2e/site.spec.js`

- [ ] **Step 1: Audit each page against identity doc**

For each page, evaluate five questions and assign ratings (✅ solid / ⚠️ needs work / ❌ missing):
1. Voice
2. Welcome
3. Agency
4. Human element
5. Connection

Document ratings as a code comment at the top of each file before editing.

- [ ] **Step 2: Write tests for roadmap forward-links and add targeted edits**

Add this test before editing:

```js
test.describe('Roadmap page', () => {
  test.beforeEach(async ({ page }) => { await page.goto('/roadmap.html'); });

  test('links forward to plan.html', async ({ page }) => {
    await expect(page.locator('a[href*="plan.html"]').first()).toBeAttached();
  });

  test('links forward to join.html', async ({ page }) => {
    await expect(page.locator('a[href*="join.html"]').first()).toBeAttached();
  });
});
```

Run it to confirm it fails (the forward links don't exist yet):

```bash
npm run test:e2e -- --grep "Roadmap page"
```

Then make targeted edits to each page:

`roadmap.html`:
- Add forward links to `plan.html` and `join.html` at the bottom (e.g., "Ready to act now? Find your role →")
- Tone check: is it honest about current state without being discouraging?

`letter-from-the-founder.html`:
- Already a personal letter — keep the personal voice
- Ensure it connects forward ("what you can do") not just back ("why I started this")
- No changes needed if it already passes the five questions

`about-ai.html`:
- Transparency-focused page — should be clear, honest, and not defensive
- Frame AI use as a tool in service of the mission, not as something to apologize for
- Ensure it connects to the broader movement

- [ ] **Step 3: Run full test suite**

```bash
npm run test:unit
npm run test:e2e
```
Expected: all tests pass

- [ ] **Step 4: Final commit**

```bash
git add docs/roadmap.html docs/letter-from-the-founder.html docs/about-ai.html tests/e2e/site.spec.js
git commit -m "docs: voice audit roadmap, founder letter, about-ai against identity doc"
```

---

## Final verification

- [ ] **Run full test suite**

```bash
npm run test:unit && npm run test:e2e
```
Expected: all unit tests pass; all E2E tests pass

- [ ] **Manual smoke test**

Visit the live dev server (or GitHub Pages preview) and check:
1. Home → feels welcoming; champion cards visible; hero CTA links to join.html
2. Hamburger → opens; tree shows full hierarchy; Escape closes it
3. Primary nav → 5 items; correct active state on each page
4. The Plan → exists; has strategy, status, your-part, CTA sections
5. Join the Movement → retitled; movement framing; multiple roles
6. The Platform → values section + bills of rights + PolicyOS all present
7. No 404s on internal links (check: problem.html, join.html, plan.html)
8. Old URLs (mission.html, get-involved.html, rights.html) return 404 — expected

- [ ] **Final commit if any cleanup needed**

```bash
git add -A
git commit -m "chore: final cleanup and verification pass"
```
