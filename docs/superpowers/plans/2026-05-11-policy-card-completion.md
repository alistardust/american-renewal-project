# Policy Card Completion Implementation Plan

> **For agentic workers:** REQUIRED: Use superpowers:subagent-driven-development (if subagents available) or superpowers:executing-plans to implement this plan. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Convert all 1,201 proposal-status policy cards to a unified canonical format with `rule-stmt` and `rule-notes`, sync the DB, and strip all card status markers site-wide.

**Architecture:** Four serial phases: (1) DB schema migration, (2) mechanical HTML cleanup via script, (3) DB backfill of existing rule_notes, (4) per-pillar content conversion via one subagent per pillar run serially. Source of truth is `src/pages/pillars/*.njk` (Nunjucks, compiled to `docs/pillars/*.html` via `npm run build`).

**Tech Stack:** Node.js (HTML scripts via regex + fs), Python 3 + sqlite3 (DB scripts), SQLite (`policy/catalog/policy_catalog_v2.sqlite`), Nunjucks source files, Vitest (unit tests), Playwright Firefox (e2e tests).

---

## Chunk 1: Phases 1 and 2 -- DB migration and HTML cleanup

### Task 1.1: Add rule_notes column to the positions table

**Files:**
- Modify: `policy/catalog/policy_catalog_v2.sqlite` (binary, committed to git)

- [ ] **Step 1: Verify the column does not exist**

```bash
sqlite3 policy/catalog/policy_catalog_v2.sqlite ".schema positions"
```

Expected: no `rule_notes` column in the output.

- [ ] **Step 2: Add the column**

```bash
sqlite3 policy/catalog/policy_catalog_v2.sqlite \
  "ALTER TABLE positions ADD COLUMN rule_notes TEXT;"
```

Expected: no error output.

- [ ] **Step 3: Verify the column was added**

```bash
sqlite3 policy/catalog/policy_catalog_v2.sqlite ".schema positions"
```

Expected: `rule_notes TEXT` appears in the schema.

- [ ] **Step 4: Commit**

```bash
git add policy/catalog/policy_catalog_v2.sqlite
git commit -m "chore(db): add rule_notes column to positions table

Co-authored-by: Copilot <223556219+Copilot@users.noreply.github.com>"
```

---

### Task 1.2: Install better-sqlite3

better-sqlite3 is needed for Phases 3 and 4 DB scripts.

**Files:**
- Modify: `package.json` (devDependencies)

- [ ] **Step 1: Install**

```bash
npm install --save-dev better-sqlite3
```

Expected: `package.json` devDependencies now includes `better-sqlite3`.

- [ ] **Step 2: Verify**

```bash
node -e "const db = require('better-sqlite3'); console.log('ok');"
```

Expected: prints `ok`.

- [ ] **Step 3: Commit**

```bash
git add package.json package-lock.json
git commit -m "chore(deps): add better-sqlite3 for DB scripts

Co-authored-by: Copilot <223556219+Copilot@users.noreply.github.com>"
```

---

### Task 1.3: Write scripts/strip-card-status.js

This script removes all card status markers from every `.njk` source file. It must be idempotent (safe to run multiple times).

**Files:**
- Create: `scripts/strip-card-status.js`

- [ ] **Step 1: Create the script**

```js
'use strict';

const fs   = require('fs');
const path = require('path');

const SRC_DIR = path.join(__dirname, '..', 'src', 'pages', 'pillars');

/**
 * Returns the file content with all card status markers removed:
 *   - class="policy-card STATUS"  ->  class="policy-card"
 *   - <span class="rule-badge">...</span>  ->  (removed)
 *   - <div class="rule-status">...</div>   ->  (removed)
 */
function stripStatusMarkersFromContent(content) {
  // Remove status modifier from policy-card class attribute.
  // Handles: status-included, status-updated, status-partial, status-missing,
  //          status-proposed, proposal, and any other status-* variant.
  let result = content.replace(
    /class="policy-card (?:status-[a-z-]+|proposal)"/g,
    'class="policy-card"'
  );

  // Remove <span class="rule-badge">...</span> (single line, no nesting).
  result = result.replace(/<span class="rule-badge">[^<]*<\/span>\n?/g, '');

  // Remove <div class="rule-status">...</div> (single line, no nesting).
  result = result.replace(/<div class="rule-status">[^<]*<\/div>\n?/g, '');

  return result;
}

function main() {
  const files = fs.readdirSync(SRC_DIR).filter(f => f.endsWith('.njk'));
  let totalFiles = 0;
  let totalChanges = 0;

  for (const file of files) {
    const filePath = path.join(SRC_DIR, file);
    const original = fs.readFileSync(filePath, 'utf8');
    const updated  = stripStatusMarkersFromContent(original);

    if (updated !== original) {
      fs.writeFileSync(filePath, updated, 'utf8');
      totalFiles++;
      // Count replacements (approximate: lines changed).
      const origLines = original.split('\n');
      const updLines  = updated.split('\n');
      totalChanges += Math.abs(origLines.length - updLines.length);
      console.log(`  updated: ${file}`);
    } else {
      console.log(`  no change: ${file}`);
    }
  }

  console.log(`\nDone. Modified ${totalFiles} files, ~${totalChanges} lines removed.`);
}

main();
```

- [ ] **Step 2: Run the script**

```bash
node scripts/strip-card-status.js
```

Expected: output lists all 26 pillar files as `updated:` or `no change:`.

- [ ] **Step 3: Verify all 26 files are clean**

```bash
grep -rn "status-included\|rule-badge\|rule-status\|policy-card proposal\|policy-card status-" \
  src/pages/pillars/
```

Expected: no output (all markers removed across all pillar files).

```bash
grep -rn "policy-card" src/pages/pillars/ | grep -v 'class="policy-card"' | grep -v '<!--'
```

Expected: no output (every `policy-card` occurrence has no trailing status modifier).

- [ ] **Step 4: Run it a second time to verify idempotency**

```bash
node scripts/strip-card-status.js
```

Expected: all 26 files show `no change:`.

---

### Task 1.4: Remove status-related CSS rules from style.css

**Files:**
- Modify: `docs/assets/css/style.css` (lines 1500-1517 approximately)

Remove the following blocks. Locate each by searching for the comment/pattern; exact line numbers may shift.

- [ ] **Step 1: Remove the five status border rules and the .rule-status rule**

Find and delete these lines (they appear as a block, approximately lines 1500-1506):

```css
.policy-card.status-included { border-left: 4px solid #1e8449; }
.policy-card.status-updated  { border-left: 4px solid #2471a3; }
.policy-card.status-partial  { border-left: 4px solid #c9952a; }
.policy-card.status-missing  { border-left: 4px solid #ccc; opacity: .72; }
.policy-card.proposal        { border-left: 4px solid #1a6b8a; }
.proposal .rule-badge        { background: #d0eaf5; color: #1a6b8a; }
.rule-status                 { font-size: .78rem; color: #1a6b8a; margin: .25rem 0 .5rem; font-style: italic; }
```

- [ ] **Step 2: Remove the .rule-badge base rule and all per-status badge rules**

Find and delete these lines (approximately lines 1510-1517):

```css
.rule-badge   {
  /* ... the full rule block ... */
}
.status-included .rule-badge { background: #d4edda; color: #155724; }
.status-updated  .rule-badge { background: #cce5ff; color: #004085; }
.status-partial  .rule-badge { background: #fff3cd; color: #856404; }
.status-missing  .rule-badge { background: #f0f0f0; color: #666; }
```

- [ ] **Step 3: Verify no remaining status badge or rule-status CSS**

```bash
grep -n "rule-badge\|\.status-included\|\.status-updated\|\.status-partial\|\.status-missing\|\.proposal.*badge\|\.rule-status" \
  docs/assets/css/style.css
```

Expected: no output. (The `.fdr-status-partial` class on line ~2441 is unrelated and must be left intact.)

---

### Task 1.5: Build, test, and commit Phase 2

- [ ] **Step 1: Build the site**

```bash
npm run build
```

Expected: exits 0, no errors. Output HTML files regenerated in `docs/pillars/`.

- [ ] **Step 2: Run unit tests**

```bash
npm run test:unit
```

Expected: all tests pass (currently 42).

- [ ] **Step 3: Run e2e tests**

```bash
npm run test:e2e
```

Expected: all tests pass.

- [ ] **Step 4: Commit everything**

```bash
git add src/pages/pillars/ docs/assets/css/style.css scripts/strip-card-status.js docs/pillars/
git commit -m "refactor(cards): strip status classes and badges from all policy cards

Removes status modifier classes (status-included, status-updated, status-partial,
status-missing, proposal) and all rule-badge / rule-status elements from all 26
pillar source files. Removes corresponding CSS rules. Proposal cards remain in
an intermediate state with rule-body and rule-citations (Phase 4 converts them).

Co-authored-by: Copilot <223556219+Copilot@users.noreply.github.com>"
```

---

## Chunk 2: Phase 3 -- Backfill existing rule_notes to DB

### Task 2.1: Write scripts/backfill-rule-notes.js

This script reads all 26 source files, finds cards that already have a `rule-notes` paragraph (these are the formerly `status-included` cards), and writes their text content to the new `rule_notes` DB column. Proposal cards (identified by having `rule-body`) are skipped -- they are handled in Phase 4.

The script is idempotent: re-running it will overwrite the same values with the same values.

**Files:**
- Create: `scripts/backfill-rule-notes.js`

- [ ] **Step 1: Create the script**

```js
'use strict';

const fs   = require('fs');
const path = require('path');
const Database = require('better-sqlite3');

const SRC_DIR = path.join(__dirname, '..', 'src', 'pages', 'pillars');
const DB_PATH = path.join(__dirname, '..', 'policy', 'catalog', 'policy_catalog_v2.sqlite');

/**
 * Parse all policy cards from a .njk file.
 * Returns an array of { id, ruleNotes } objects.
 * Only returns cards that have a rule-notes paragraph AND no rule-body paragraph
 * (rule-body presence = proposal card, handled in Phase 4, not here).
 */
/**
 * Extract all policy-card div blocks from content.
 * Uses nesting depth counting to correctly handle nested divs inside cards
 * (e.g. rule-header, rule-body). A naive regex would stop at the first
 * nested </div>, capturing only the rule-header fragment.
 */
function extractCardBlocks(content) {
  const blocks = [];
  let searchFrom = 0;

  while (true) {
    const startIdx = content.indexOf('<div class="policy-card"', searchFrom);
    if (startIdx === -1) break;

    let depth = 0;
    let i = startIdx;

    while (i < content.length) {
      if (content.startsWith('<div', i) && (content[i + 4] === ' ' || content[i + 4] === '>' || content[i + 4] === '\n' || content[i + 4] === '\t')) {
        depth++;
        i += 4;
      } else if (content.startsWith('</div>', i)) {
        depth--;
        if (depth === 0) {
          blocks.push(content.slice(startIdx, i + 6));
          searchFrom = i + 6;
          break;
        }
        i += 6;
      } else {
        i++;
      }
    }

    if (depth !== 0) break; // malformed HTML, stop searching
  }

  return blocks;
}

function parseCards(content) {
  const cards = [];

  for (const block of extractCardBlocks(content)) {
    const idMatch = block.match(/id="([^"]+)"/);
    if (!idMatch) continue;
    const cardId = idMatch[1];

    // Skip proposal cards (have rule-body, regardless of any additional classes).
    if (block.includes('class="rule-body')) continue;

    // Extract rule-notes text (may span multiple lines).
    const notesMatch = block.match(/<p class="rule-notes">([\s\S]*?)<\/p>/);
    if (!notesMatch) continue;

    cards.push({ id: cardId, ruleNotes: notesMatch[1].trim() });
  }

  return cards;
}

function main() {
  const db = new Database(DB_PATH);

  const files = fs.readdirSync(SRC_DIR).filter(f => f.endsWith('.njk'));
  const unmatched = [];
  let totalUpdated = 0;

  try {
    // Prepare inside try so any schema error (e.g. Phase 1 not run) closes the DB cleanly.
    const updateStmt = db.prepare('UPDATE positions SET rule_notes = ? WHERE id = ?');

    for (const file of files) {
      const filePath = path.join(SRC_DIR, file);
      const content  = fs.readFileSync(filePath, 'utf8');
      const cards    = parseCards(content);

      for (const { id, ruleNotes } of cards) {
        const result = updateStmt.run(ruleNotes, id);
        if (result.changes === 0) {
          unmatched.push({ file, id });
        } else {
          totalUpdated++;
        }
      }
    }
  } finally {
    db.close();
  }

  console.log(`\nUpdated ${totalUpdated} rows in DB.`);

  if (unmatched.length > 0) {
    console.warn(`\nWARNING: ${unmatched.length} card IDs found in HTML with no matching DB row:`);
    for (const { file, id } of unmatched) {
      console.warn(`  [${file}] ${id}`);
    }
    console.warn('\nThese IDs should be investigated and backfilled into the DB manually,');
    console.warn('or tracked as known gaps before Phase 4 begins.');
  } else {
    console.log('All IDs matched successfully.');
  }
}

main();
```

- [ ] **Step 2: Run the script**

```bash
node scripts/backfill-rule-notes.js
```

Expected: prints a count of updated rows. May print warnings for unmatched IDs -- review these before Phase 4. An unmatched ID here means a `status-included` card whose ID is not in the `positions` table; this should not happen for well-formed v2 IDs.

- [ ] **Step 3: Verify a sample row was written**

```bash
sqlite3 policy/catalog/policy_catalog_v2.sqlite \
  "SELECT id, substr(rule_notes,1,80) FROM positions WHERE rule_notes IS NOT NULL LIMIT 5;"
```

Expected: several rows with rule_notes text.

- [ ] **Step 4: Check total rows updated**

```bash
sqlite3 policy/catalog/policy_catalog_v2.sqlite \
  "SELECT COUNT(*) FROM positions WHERE rule_notes IS NOT NULL;"
```

Record this number. It should equal the number of cards with a `rule-notes` paragraph in the source files, minus any unmatched IDs.

- [ ] **Step 5: Commit**

```bash
git add policy/catalog/policy_catalog_v2.sqlite scripts/backfill-rule-notes.js
git commit -m "chore(db): backfill rule_notes from existing status-included cards

status-included cards only. Proposal cards (rule-body/rule-citations)
are out of scope here and handled in Phase 4.

Co-authored-by: Copilot <223556219+Copilot@users.noreply.github.com>"
```

---

## Chunk 3: Phase 4 -- Per-pillar subagent template

### Task 3.1: Phase 4 subagent prompt template

**Phase 4 overview:** One subagent per pillar, run serially in the priority order below. Each subagent converts all `rule-body` cards in its assigned pillar to canonical format (`rule-stmt` + `rule-notes`), writes the DB, and commits per family. Subagents must run one at a time -- parallel execution is prohibited (SQLite single-writer, git merge conflicts).

**For the agent spawning Phase 4 subagents:** Use the prompt template below. Replace `{{PILLAR_SLUG}}`, `{{PILLAR_TITLE}}`, and `{{PROPOSAL_COUNT}}` with values from the priority table. Spawn the next subagent only after the current one completes successfully.

---

#### Phase 4 subagent prompt template

```
You are a policy writing subagent. Your job is to convert all proposal-format cards
in the {{PILLAR_TITLE}} pillar to canonical format, with full research, adversarial
review, and DB sync.

**Pillar:** {{PILLAR_TITLE}}
**Source file:** src/pages/pillars/{{PILLAR_SLUG}}.njk
**DB file:** policy/catalog/policy_catalog_v2.sqlite
**Proposal cards to convert:** {{PROPOSAL_COUNT}}

---

## Your task

Work through every policy family in this pillar sequentially. For each family,
complete the full 6-step process below before moving to the next family.

A policy family is a group of cards inside a `<div class="policy-family">` element
with a `<div class="family-header">` heading.

---

## Card format

After conversion, every card must have EXACTLY this structure (no other classes,
no rule-badge, no rule-status, no rule-body, no rule-citations):

```html
<div class="policy-card" id="XXXX-YYYY-0000">
  <div class="rule-header">
    <code class="rule-id">XXXX-YYYY-0000</code>
  </div>
  <p class="rule-title">Specific, descriptive title in plain language</p>
  <p class="rule-plain">1-3 sentences, roughly 8th-grade reading level.
  What does this rule do and why does it matter to an ordinary person?</p>
  <p class="rule-stmt">Formal, precise policy statement with thresholds,
  definitions, and enforcement detail. This is the operative legal text.</p>
  <p class="rule-notes">Research-backed rationale including: legal basis
  (statutes, case law), empirical evidence with inline citations, enforcement
  mechanisms, implementation notes, and the adversarial review findings below.</p>
</div>
```

---

## REQUIRED: Read the PolicyOS framework before writing any card (PAOS-AUTH-0010)

Before writing a single word of policy content, you must read all three PolicyOS
framework files in order:

1. `policy/policyos/policyos_platform_values_v1.md` -- the moral anchor; values
   that no rule may violate
2. `policy/policyos/policyos_1_0_rules_proposal.md` -- cross-platform design
   constraints; identify which KERN rules and overlays apply to this pillar
3. `policy/policyos/policyos_authoring_os_v1.md` -- structural requirements every
   rule must satisfy (NORM/AUTH/TEST/ENFC/PLAC/MAINT checklists)

These files are locked and authoritative. Every `rule-notes` field you write must
include a `rule-notes` line documenting: (a) which PolicyOS rules were applied, and
(b) which primary sources were reviewed. Policy written without this step is not
eligible for adoption per PAOS-AUTH-0010.

---

## Adversarial review requirement (PAOS-TEST-0008)

Every rule-notes paragraph MUST address all four of the following. If a category
has no findings, document that the review was conducted and explain why:

- **Gap:** What the rule fails to cover or whom it fails to protect.
- **Loophole:** How a bad-faith actor could technically comply while defeating
  the rule's purpose.
- **Unintended consequence:** Perverse incentives, burden-shifting, or
  foreseeable second-order harms.
- **Abuse path:** How government, institutions, or employers could exploit the rule.

---

## Research requirements

All rule-notes content must be grounded in primary sources and academic research:

- **Primary sources:** federal statutes (cite by U.S.C. section), court opinions
  (cite by case name and reporter), official government data (Census, BLS, CBO,
  GAO, CRS reports with report numbers).
- **Academic databases:** search Google Scholar, SSRN (law and policy papers),
  NBER (economics papers), PubMed (health topics) for relevant peer-reviewed
  research. Do not rely solely on news sources.
- **Citations:** include inline in rule-notes prose using short-form citation
  (e.g., "42 U.S.C. sec. 300gg-3 (2010)", "Brown v. Board of Education, 347 U.S.
  483 (1954)", "CBO Report No. 55480 (2023)").
- **Address `<!-- [VERIFY] -->` comments:** any `<!-- [VERIFY] -->` annotation
  in the rule-body is a flag that the underlying claim needs verification.
  Verify the claim before writing rule-notes. If verified, state the source.
  If unverified or false, correct the claim in the rule-stmt you write.
  Remove the `<!-- [VERIFY] -->` comment from the output -- it must not appear
  in the final rule-notes text.

---

## Per-family process

**Preflight check:** Before processing any family, verify that Phase 1 has been
applied to the DB (the `rule_notes` column must exist):

```bash
sqlite3 policy/catalog/policy_catalog_v2.sqlite "PRAGMA table_info(positions);" | grep rule_notes
```

Expected: one line containing `rule_notes`. If no output, stop and notify the
operator that Phase 1 (Task 1.1) has not been run. Do not proceed.

---

For each family, follow these 6 steps in order:

### Step 1: Read and understand the family

Read the family-header text and all cards with `class="rule-body"` in this family.
Understand what each card is trying to accomplish before writing anything.
Identify any `<!-- [VERIFY] -->` annotations that need research.

### Step 2: Convert each card

For each card with `rule-body` in the family:

1. Write `rule-stmt`: a precise, formal policy statement derived from the rule-body
   content. Include specific thresholds, dollar amounts, timeframes, agency names,
   and enforcement mechanisms. Do not be vague where the rule-body was specific.

2. Write `rule-notes`: research-backed rationale. Include:
   - Legal basis (relevant statutes, regulations, case law)
   - Empirical evidence for why this policy is needed (with inline citations)
   - Enforcement mechanisms and implementation notes
   - Adversarial review (all four categories: gap, loophole, unintended
     consequence, abuse path)

3. Replace the existing card HTML in the source file with the canonical format.
   Remove `rule-body` and `rule-citations` elements. Do not change `rule-title`
   or `rule-plain` content unless they contain factual errors.

### Step 3: Update the DB

After converting all cards in the family, update the database in a single
transaction.

**For v2-format IDs** (matching `^[A-Z]{4}-[A-Z]{4}-[0-9]{4}$`): use UPSERT.

```js
const upsert = db.prepare(`
  INSERT INTO positions (id, domain, subdomain, seq, short_title, plain_language, full_statement, rule_notes)
  VALUES (@id, @domain, @subdomain, @seq, @short_title, @plain_language, @full_statement, @rule_notes)
  ON CONFLICT(id) DO UPDATE SET
    full_statement = excluded.full_statement,
    rule_notes     = excluded.rule_notes,
    short_title    = COALESCE(excluded.short_title, short_title),
    plain_language = COALESCE(excluded.plain_language, plain_language),
    updated_at     = datetime('now')
`);

// Parse fields from card ID: 'HLTH-ACCS-0001' -> domain='HLTH', subdomain='ACCS', seq=1
// seq is the integer value of the four-digit suffix (e.g. '0001' -> 1, '0042' -> 42).
// short_title and plain_language come from existing rule-title and rule-plain HTML fields.
```

**For v1-format IDs** (e.g., `HLT-HOSP-001`, `AGR-LBL-001`): the positions table
has a CHECK constraint that rejects non-v2-format IDs. Do NOT attempt to insert
these. Log a warning to stdout and skip the DB update for that card. The HTML
conversion still completes. These IDs need a separate re-ID migration pass.

**Transaction pattern:**

```js
const runFamily = db.transaction((cards) => {
  for (const card of cards) {
    upsert.run(card);
  }
});
try {
  runFamily(familyCards);
} catch (err) {
  console.error('DB transaction failed, rolling back:', err.message);
  throw err; // stop processing this family
}
```

If the transaction fails: stop immediately. Do not write HTML. Surface the error
and do not proceed to the next family.

### Step 4: Write the HTML

After a successful DB transaction, write the modified source file back to disk.
HTML is written AFTER the DB commit.

If file writing fails: log the error. The DB is already correct. Re-running this
process will detect the incomplete state (rule-body still present) and redo the
HTML write without re-running the DB transaction (since the row now exists).

### Step 5: Build and test

```bash
npm run build
npm run test:unit
```

If tests fail: stop immediately. Surface the full test output. Do NOT commit.
Do NOT proceed to the next family. Do NOT attempt to auto-fix.
Leave the DB and HTML changes in place -- they are safe because Phase 4 is
idempotent (cards with rule-stmt are skipped on re-run).

### Step 6: Commit the family

Create a kebab-case slug from the family-header text: lowercase, spaces to hyphens,
`&` becomes `and`, all other punctuation removed.
For example, "Drug Pricing & PBMs" becomes `drug-pricing-and-pbms`.

```bash
git add src/pages/pillars/{{PILLAR_SLUG}}.njk docs/pillars/{{PILLAR_SLUG}}.html \
  policy/catalog/policy_catalog_v2.sqlite
git commit -m "policy({{PILLAR_SLUG}}): complete {{FAMILY_SLUG}} cards

Co-authored-by: Copilot <223556219+Copilot@users.noreply.github.com>"
```

Repeat for every family in the pillar.

---

## After all families are done

Run the full e2e suite:

```bash
npm run test:e2e
```

If e2e fails: surface the failure. Do not proceed. Fix and re-run.

If e2e passes: you are done. Report back with:
- Total cards converted
- Total DB rows upserted
- Any v1-format IDs that were skipped (could not be inserted into DB)
- Any `<!-- [VERIFY] -->` claims that could not be verified (flag for human review)
```

---

### Task 3.2: Phase 4 execution schedule

Run one subagent per pillar in the order below, **waiting for each to complete before starting the next.**

| Order | Pillar slug | Title | Cards |
|---|---|---|---|
| 1 | `equal-justice-and-policing` | Equal Justice and Policing | 101 |
| 2 | `environment-and-agriculture` | Environment and Agriculture | 111 |
| 3 | `consumer-rights` | Consumer Rights | 91 |
| 4 | `antitrust-and-corporate-power` | Antitrust and Corporate Power | 79 |
| 5 | `healthcare` | Healthcare | 79 |
| 6 | `education` | Education | 70 |
| 7 | `labor-and-workers-rights` | Labor and Workers Rights | 61 |
| 8 | `housing` | Housing | 61 |
| 9 | `foreign-policy` | Foreign Policy | 64 |
| 10 | `rights-and-civil-liberties` | Rights and Civil Liberties | 54 |
| 11 | `taxation-and-wealth` | Taxation and Wealth | 55 |
| 12 | `anti-corruption` | Anti-Corruption | 46 |
| 13 | `infrastructure-and-public-goods` | Infrastructure and Public Goods | 41 |
| 14 | `technology-and-ai` | Technology and AI | 40 |
| 15 | `immigration` | Immigration | 39 |
| 16 | `information-and-media` | Information and Media | 35 |
| 17 | `elections-and-representation` | Elections and Representation | 34 |
| 18 | `checks-and-balances` | Checks and Balances | 28 |
| 19 | `administrative-state` | Administrative State | 25 |
| 20 | `science-technology-space` | Science, Technology, and Space | 23 |
| 21 | `gun-policy` | Gun Policy | 17 |
| 22 | `executive-power` | Executive Power | 16 |
| 23 | `legislative-reform` | Legislative Reform | 14 |
| 24 | `courts-and-judicial-system` | Courts and Judicial System | 13 |
| 25 | `term-limits-and-fitness` | Term Limits and Fitness for Office | 4 |

`data-rights-and-privacy`: skip Phase 4 entirely (all 34 cards already complete).

---

## Chunk 4: Phase 4 wrap-up

### Task 4.1: Final e2e after all Phase 4 pillars complete

- [ ] **Step 1: Run the full e2e suite**

```bash
npm run test:e2e
```

Expected: all tests pass.

- [ ] **Step 2: Verify no rule-body elements remain**

```bash
grep -rn "rule-body" src/pages/pillars/
```

Expected: no output (all proposal cards converted).

- [ ] **Step 3: Verify no proposal status classes remain**

```bash
grep -rn "policy-card proposal\|policy-card status-" src/pages/pillars/
```

Expected: no output.

- [ ] **Step 4: Check DB rule_notes coverage**

```bash
sqlite3 policy/catalog/policy_catalog_v2.sqlite \
  "SELECT COUNT(*) as total, COUNT(rule_notes) as with_notes FROM positions;"
```

Record the gap (total minus with_notes). This represents cards in the DB with no
rule_notes -- expected to be low after Phase 4.

- [ ] **Step 5: Log any v1-format IDs that were skipped**

Re-derive the list of v1-format IDs still in the HTML (the canonical recoverable source, independent of whether Phase 4 run logs were captured):

```bash
grep -roh 'id="[A-Z]\{2,3\}-[A-Z]\{3,4\}-[0-9]\{3\}"' src/pages/pillars/
```

Expected: approximately 85 results, all matching the v1 pattern (3-char domain or subdomain, 3-digit seq). Create a GitHub issue tracking the follow-up ID migration pass for these IDs. They need v2 IDs assigned and HTML updated before they can be synced to the DB.

- [ ] **Step 6: Commit the final CSS dead-code cleanup**

After all rule-body elements are removed, these two CSS rules are dead code:

```css
.policy-card.card-clamped-active .rule-body { ... }
.policy-card.expanded .rule-body { ... }
```

First confirm there are no other `rule-body` CSS rules remaining before deleting:

```bash
grep -n "rule-body" docs/assets/css/style.css
```

Expected: exactly the two lines above (card-clamped-active and expanded). If additional `rule-body` rules appear, remove them in the same commit.

Remove them from `docs/assets/css/style.css`, rebuild, and run tests.

```bash
npm run build && npm run test:unit && npm run test:e2e
git add docs/assets/css/style.css
git commit -m "chore(css): remove dead rule-body CSS rules after Phase 4 completion

Co-authored-by: Copilot <223556219+Copilot@users.noreply.github.com>"
```

---

## Known constraints

**v1-format IDs in HTML:** 85 of the 113 proposal card IDs missing from the DB
are v1-format (e.g., `HLT-HOSP-001`). The `positions` table has a CHECK constraint
that rejects non-v2-format IDs. Phase 4 subagents convert these cards' HTML but
cannot sync them to the DB. A dedicated re-ID migration pass is needed post-Phase 4.
The 28 v2-format missing IDs can be upserted normally.

**`full_statement NOT NULL`:** Existing rows have a NOT NULL constraint on
`full_statement`. New UPSERT rows must always populate `full_statement` from the
new rule-stmt content.

**`short_title CHECK(length <= 120)`:** The `short_title` field has a 120-character
limit. Verify rule-title content in HTML does not exceed this before upserting.

**Serial execution:** All Phase 4 subagents must run one at a time. SQLite does not
support concurrent writers.
