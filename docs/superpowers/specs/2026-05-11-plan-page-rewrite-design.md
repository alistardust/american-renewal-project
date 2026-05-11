<!-- /autoplan restore point: /home/alice/.gstack/projects/alistardust-freedom-and-dignity-project/main-autoplan-restore-20260511-092526.md -->
# Design Spec: The Plan Page Rewrite

**Date:** 2026-05-11
**Status:** Approved
**Source:** `src/pages/plan.njk`
**Output:** `docs/plan.html` (generated)

---

## Problem

The current Plan page is negatively framed. It leads with "Why Nothing Else Is Enough" and "Every Platform That's Failed Has the Same Flaw," making the dominant register competitive and diagnostic. It also presents a rigid three-phase roadmap that reads like a strategy deck, not a movement invitation.

The page should do three things: inspire, communicate strategic clarity, and invite participation. It does none of these well in its current form.

---

## Guiding voice

FDR and MLK, in that order. The specific register: invoke the existing American promise, then commit to fulfilling it. Do not lead with diagnosis of others. Do not compare this platform to other movements or platforms. Speak to what is possible and what this project is doing about it. End with an open door.

"Freedom and Dignity" is a placeholder name. Do not write copy that depends on it.

---

## Approved page structure

### 1. Hero

The page title and hero statement replace the current hero. No changes to the structural eyebrow or h1 markup needed -- only the statement.

**Hero statement (approved):**
> The promise of America is not yet kept. This is the plan to keep it.

**`{% set description %}`:** Update to: "The policy platform built in the open, by everyone who has a stake in the outcome."

**`{% block og_description %}`:** Same value: "The policy platform built in the open, by everyone who has a stake in the outcome."

**`{% block twitter_description %}`:** Update to: "The policy platform built in the open, by everyone who has a stake."

---

### 2. Opening section

Replaces "Why Nothing Else Is Enough." No comparison to other platforms. No diagnosis as the headline.

**Section heading:** Remove the "Why Nothing Else Is Enough" eyebrow and "Every Platform That's Failed" h2. Replace with a heading that does not frame the project as a reaction to others. Heading: "The work of keeping a promise."

**Section markup:** `<section class="bg-cream ruled" aria-labelledby="opening-heading">`

**Heading id:** `id="opening-heading"`

**Copy (approved):**

> This country was founded on a set of promises: that every person is born with rights, that government exists to secure those rights, that no one is above the law and no one is beneath its protection.

> Those promises have never been fully kept. That work remains. It belongs to all of us.

No pullquote. The current pullquote doubles down on the negative framing and should be removed.

---

### 3. Built together

Replaces "The Three Phases." The three-phase card layout is removed. This is a continuous prose section, not a card grid.

**Section heading:** "Built together"

**Section markup:** `<section class="bg-dark on-dark ruled" aria-labelledby="built-together-heading">`

**Heading id:** `id="built-together-heading"`

**Copy (approved):**

> This platform is built in the open, because policy that belongs to everyone has to be built by everyone. Anyone can read it, question it, challenge it, improve it. The research is cited so you can check it. The positions are argued so you can disagree with them. Nothing here is handed down from on high.

> Coalition means intellectual participation, not just political support. This platform runs on a rule system (PolicyOS) that governs how policy is written, how evidence is evaluated, how positions are structured and tested. Those rules are designed to make open participation produce quality rather than noise. The review system, in development, is how anyone will be able to formally challenge a position, submit research, or contest a claim, not as commentary, but as structured input that enters the record.

> A coalition too large to be ignored cannot be built from the top. It has to be built from everywhere, by everyone who has a stake in the outcome. That is every one of us.

---

### 4. The demands are the work

This section is new; it does not replace an existing section. It sits between "Built together" and "Work in progress."

**Section markup:** `<section class="bg-cream ruled" aria-labelledby="demands-heading">`

**Heading id:** `id="demands-heading"`

**Section heading:** "The demands are the work"

**Copy (approved):**

> The policy positions on this platform are live and arguable now. Building them and building the coalition around them are the same ongoing work, not sequential phases. Every person who reads a position, challenges it, or helps refine it is part of the coalition taking shape around it.

> A coalition organized around specific demands is one that every candidate and institution has to answer directly. They either stand for the demands or they do not. There is no room for vague agreement. That is how electoral and legislative pressure flows toward structural reform: by having demands too specific to misrepresent and a coalition too large to ignore.

---

### 5. Work in progress

Replaces "Where We Are Now." Brief. No hardcoded counts. No "We're in Phase 1" framing. The point is that everything is live, open, and evolving by design.

**Section heading:** "A work in progress, by design"

**Section markup:** `<section class="bg-parchment ruled" aria-labelledby="wip-heading">`

**Heading id:** `id="wip-heading"`

**Copy (approved):**

> Everything here is a work in progress, by design. The policy pillars are live, citable, and open to challenge. The research is ongoing. The platform grows as more people engage with it.

> The review system is in development. It is how formal challenge enters the record, and how the platform, over time, is held to its own standards.

(Note: add a link to the review system spec here once it exists.)

**Links to include** -- use an inline `<ul>` with no class (do not use `.arch-intro` or `.arch-item`; those are grid components and will produce broken layout here). Use this markup:

```html
<ul style="list-style:none;padding:0;display:flex;gap:1rem;flex-wrap:wrap;margin-top:1rem">
  <li><a href="get-involved.html">Get involved</a></li>
</ul>
```

Notes:
- `pillars.html` does not exist in `docs/` -- omit this link until a pillar index page exists
- `compare.html` does not exist in `docs/` -- omit this link
- `get-involved.html` exists and should be included

No `data-dynamic` count spans. Dynamic counts are not appropriate here -- the point is that the platform is evolving, not that it has a specific number of items.

---

### 6. CTA

Replaces the current page-nav-cta block.

**CTA copy (approved):**

> The promise of this country is not kept by any one person, or any one party, or any one platform. It is kept by a generation that decides to keep it.

> Come be part of this work.

**Markup pattern** -- replace the current `.page-nav-cta` inner content with:

```html
<p>The promise of this country is not kept by any one person, or any one party, or any one platform. It is kept by a generation that decides to keep it.</p>
<p>Come be part of this work.</p>
<ul style="display:flex;gap:1rem;flex-wrap:wrap;margin-top:1.5rem;list-style:none;padding:0">
  <li><a href="get-involved.html" class="btn-primary">Get Involved</a></li>
  <li><a href="https://github.com/alistardust/freedom-and-dignity-project" class="btn-outline" target="_blank" rel="noopener noreferrer">GitHub</a></li>
</ul>
```

Notes:
- `.btn-primary` exists in `style.css` -- use it
- `.btn-secondary` does not exist in `style.css` -- use `.btn-outline` instead
- `.cta-links` does not exist in `style.css` -- use the inline style on the `<ul>` as shown above
- Do not create new CSS classes

The `.page-nav-cta` wrapper div and `.wrap` inner div are retained unchanged.

---

## What is removed

| Removed element | Reason |
|---|---|
| "Why Nothing Else Is Enough" eyebrow | Sets a negative, competitive frame as the headline |
| "Every Platform That's Failed Has the Same Flaw" h2 | Comparative framing; not how this platform wants to speak |
| Pullquote ("Every platform that's failed...") | Doubles down on the failure framing |
| Three-phase card grid | Reads as a strategy deck, not a movement invitation; doesn't reflect current direction |
| "We're in Phase 1" heading | Phase framing is dropped entirely |
| Hardcoded `data-dynamic="pillar-count"` and `data-dynamic="policy-count"` spans | The WIP section is not the place for counts |

---

## Structural and CSS notes

- The opening section uses `bg-cream ruled` -- keep (specified in section markup above)
- The "Built together" section uses `bg-dark on-dark ruled` -- specified in section markup above
- The "The demands are the work" section uses `bg-cream ruled` -- matches the opening section
- The WIP section uses `bg-parchment ruled` -- keep (specified in section markup above)
- The CTA block uses the `.page-nav-cta` pattern -- keep the structure, replace the copy
- The `.policyos-layers` and `.layer-card` grid markup is removed entirely
- No new CSS classes are required; use existing patterns

---

## Source files

| File | Action |
|---|---|
| `src/pages/plan.njk` | Rewrite content per this spec |
| `docs/plan.html` | Regenerated output -- do not edit directly |
| `tests/e2e/site.spec.js` | Update plan.html describe block (see below) |
| `policy/briefing-pack.md` | Update if page framing changes are relevant |

### Required test updates

Before running `npm run test:e2e`, update `tests/e2e/site.spec.js`:

1. **`hero statement contains expected copy`** -- change the assertion:
   ```js
   // was: .toContainText('Voting matters')
   await expect(page.locator('.hero-statement')).toContainText('The promise of America is not yet kept');
   ```

2. **`all three phase names are present`** -- remove this test entirely; `.policyos-layers` is being deleted. Replace with:
   ```js
   test('three-phase card grid is removed', async ({ page }) => {
     await expect(page.locator('.policyos-layers')).toHaveCount(0);
   });
   ```

3. **Add new assertion for section headings:**
   ```js
   test('section headings match spec', async ({ page }) => {
     const headings = page.locator('h2');
     await expect(headings.filter({ hasText: 'The work of keeping a promise' })).toHaveCount(1);
     await expect(headings.filter({ hasText: 'Built together' })).toHaveCount(1);
     await expect(headings.filter({ hasText: 'The demands are the work' })).toHaveCount(1);
     await expect(headings.filter({ hasText: 'A work in progress, by design' })).toHaveCount(1);
   });
   ```

Run after editing:
```bash
node scripts/build-site.js
npm run test:unit
npm run test:e2e
```

---

## Out of scope

- Navigation changes
- Footer changes
- New CSS components
- Policy content on this page (the Plan page does not contain policy positions)
- Changes to any other page

---

## Success criteria

1. No comparison language referencing other platforms, parties, or movements
2. No negative framing as the headline or section heading
3. Hero statement, opening, "Built together," WIP, and CTA copy all match approved text in this spec
4. Three-phase card grid is fully removed
5. No hardcoded counts or `data-dynamic` count spans in the WIP section
6. Page builds cleanly, all tests pass
7. No em-dashes in body copy. Note: the page `<title>` tag uses a real em-dash character (`—` U+2014) and is explicitly permitted as an exception; this applies to the title block only.

---

<!-- AUTONOMOUS DECISION LOG -->
## GSTACK REVIEW REPORT

**Reviewed by:** /autoplan (CEO + Design + Eng phases)
**Date:** 2026-05-11
**Voices:** Claude subagent + Codex (all three phases)

---

### Phase 1: CEO Review

#### What already exists
- `src/pages/plan.njk` — current source with three-phase mechanism: platform → electoral pressure → constitutional reform
- office-hours design doc (2026-05-10) identifying three user friction points: "don't know what this is," "don't know how to contribute," "overwhelmed by scope"
- `/approach.html` — philosophy; `/problem.html` — diagnosis; `/get-involved.html` — participation

#### Premises challenged
1. **"Reads like a strategy deck, not a movement invitation"** — The three-phase framing can be rewritten in movement register without being removed. The premise that mechanism and inspiration are mutually exclusive is assumed, not proven.
2. **"FDR/MLK register is the right voice"** — Both models accept this as a sound voice choice. The register shift is valid; what's lost is not the register but the strategic content.
3. **"The page should inspire, communicate strategic clarity, and invite participation"** — Stated in the Problem section. The approved copy achieves #1 and #3; it does not achieve #2 by either model's assessment.

#### CEO Dual Voices

**CLAUDE SUBAGENT (CEO — strategic independence):**
1. CRITICAL: Spec removes the platform's only mechanism explanation. The old page, for all its problems, told people: platform → electoral pressure → constitutional reform. New page has none. "Inspired and specific are not mutually exclusive."
2. HIGH: The office-hours design doc's core resolution (constitutional reform is the endgame; three-phase arc explains the mechanism; page must serve the exhausted organizer) is abandoned without documentation.
3. HIGH: 6-month regret — "another beautiful empty vision statement." The political landscape already has FDR/MLK register in abundance. What was distinctive was the named mechanism that exists nowhere else on the left.
4. MEDIUM: Article V context (right is at ~19-20 states, no serious countermovement) disappears entirely. This was the most urgency-generating fact in the project.
5. MEDIUM: "Come be part of this work" is not a call to action. The narrowest wedge (share the plan for creators with audiences) is unaddressed.

**CODEX (CEO — strategy challenge):**
1. Swaps strategic theory of change for civic liturgy. Not falsifiable. Interchangeable with a dozen progressive platforms that died because they were inspiring but non-specific.
2. "Built by everyone" is a dangerous premise if governance is not visible. No decision rights, moderation standards, legitimacy rules, or conflict resolution specified.
3. Removing comparisons may overcorrect. A movement invitation still needs contrast — not dunking on others, but explaining why another policy platform is necessary.
4. CTA operationally weak. "Come be part of this work" doesn't tell a serious person what costly action is needed this week.
5. FDR/MLK register may be rhetorically overbuilt relative to institutional maturity. If the product is still pre-reconciliation and procedurally incomplete, grand national-promise language risks looking overbuilt.

**CEO CONSENSUS TABLE:**
```
CEO DUAL VOICES — CONSENSUS TABLE:
═══════════════════════════════════════════════════════════════
  Dimension                             Claude   Codex   Consensus
  ──────────────────────────────────── ──────── ──────── ─────────
  1. Premises valid?                    NO       NO       CONFIRMED
  2. Right problem to solve?            NO       PARTIAL  DISAGREE
  3. Scope calibration correct?         NO       NO       CONFIRMED: overcorrection
  4. Alternatives explored?             NO       NO       CONFIRMED
  5. Competitive/market risks covered?  NO       NO       CONFIRMED: differentiator lost
  6. 6-month trajectory sound?          NO       NO       CONFIRMED: risk of homogenization
═══════════════════════════════════════════════════════════════
```

#### NOT in scope (deferred)
- Rewriting the page content (that's the implementation task)
- Human Review System UI (future feature)
- Article V framing (content decision for Alice)

#### Dream state delta
CURRENT: Negative, diagnostic, strategy-deck register. Technically complete but tonally wrong.
THIS PLAN: Inspirational register, collaborative framing, open invitation. Mechanism removed.
12-MONTH IDEAL: Inspirational register + compressed mechanism + concrete first action for specific personas (creators, organizers, uninitiated visitors).

#### Error & Rescue Registry
| Risk | Trigger | Recovery |
|------|---------|----------|
| Page doesn't answer "what is the plan?" | Visitor with no prior context reads the new page | Add compressed mechanism sentence to "Built together" or WIP section |
| "Built by everyone" looks naive | Critic asks "who decides?" | Add link to governance/contribution path, or soften the claim |
| CTA doesn't convert | Analytics show low get-involved click rate | A/B test with more specific persona-directed CTAs |

---

### Phase 2: Design Review

#### Design Dual Voices

**CLAUDE SUBAGENT (Design — independent review):**
1. CRITICAL: `.btn-secondary` does not exist in `style.css`. Only `.btn-primary`, `.btn-outline`, `.btn-pin` exist. GitHub button will be completely unstyled. Spec's fallback clause covers `.cta-links` only. Fix: specify `.btn-outline` or provide inline style fallback for this button.
2. CRITICAL: `pillars.html` does not exist in `docs/`. Will 404 silently. Likely target: the individual pillar pages or a non-existent aggregate index.
3. HIGH: Information hierarchy — opening section is 300 words of philosophical prose before any action affordance. The question "what can I do right now?" isn't answered until the very bottom.
4. HIGH: "Built by everyone" governance unspecified. Copy says "anyone can challenge it, improve it" with no UI path to do so. Human Review System link is removed from WIP section.
5. MEDIUM: `cta-links` undefined, `compare.html` doesn't exist (spec's conditional omission is correct; confirm omit).

**CODEX (Design — UX challenge):**
1. `pillars.html` and `compare.html` both missing. Actual structure is `docs/pillars/*.html` (individual pages) with no aggregate index.
2. `.btn-secondary` and `.cta-links` don't exist. Inline debt baked into a central page.
3. Info hierarchy removes strategic mechanism — "The Plan" no longer answers "what is the plan?"
4. WIP section arch-intro class conflicts with existing CSS grid pattern.
5. CTA weak: GitHub as secondary CTA sends nontechnical visitors to a contributor-hostile surface.

**Design Litmus Scorecard:**
```
Design Litmus — CONSENSUS TABLE:
═══════════════════════════════════════════════════════════════
  Dimension                             Claude   Codex   Consensus
  ──────────────────────────────────── ──────── ──────── ─────────
  1. CSS classes exist?                 FAIL     FAIL     CONFIRMED FAIL
  2. Link targets valid?                FAIL     FAIL     CONFIRMED FAIL
  3. Information hierarchy sound?       MEDIUM   MEDIUM   CONFIRMED concern
  4. Governance/participation path?     FAIL     FAIL     CONFIRMED: missing
  5. WIP link markup pattern clear?     FAIL     FAIL     CONFIRMED: ambiguous
  6. External link security?            MEDIUM   —        flagged
═══════════════════════════════════════════════════════════════
```

---

### Phase 3: Eng Review

#### Architecture ASCII diagram
```
src/pages/plan.njk  (edit target)
      │
      ▼ (node scripts/build-site.js)
docs/plan.html  (generated output)
      │
      ├── docs/assets/css/style.css  (read-only, existing classes only)
      │     ├── .btn-primary  ✓ exists
      │     ├── .btn-secondary  ✗ MISSING — spec error
      │     ├── .cta-links  ✗ MISSING — spec provides fallback
      │     ├── .arch-intro  ✓ exists (grid component, WRONG for link list)
      │     └── .page-nav-cta  ✓ exists
      │
      ├── docs/pillars.html  ✗ MISSING — broken link in spec
      ├── docs/compare.html  ✗ MISSING — spec says omit if not present ✓
      └── docs/get-involved.html  ✓ exists
```

#### Eng Dual Voices

**CLAUDE SUBAGENT (Eng — independent review):**
1. CRITICAL: `hero statement contains expected copy` test (line 961) asserts `.hero-statement` contains "Voting matters". New hero copy won't match. Test will fail.
2. CRITICAL: `all three phase names are present` test (lines 964-968) asserts `.policyos-layers` content. Grid is removed. Test will throw locator-not-found. Test must be removed/replaced.
3. HIGH: `.arch-intro` is a CSS grid component (`background: var(--parchment)`, `border-bottom`, grid children). Using it for a `<ul>` of links will produce broken layout. Spec should specify inline styles for the WIP links.
4. HIGH: `aria-labelledby` attribute on `<section>` elements not made explicit. Spec specifies heading IDs but never shows the full `<section aria-labelledby="...">` attribute.
5. HIGH: `pillars.html` doesn't exist. `compare.html` doesn't exist (conditional omission correct).
6. HIGH: `btn-secondary` not in stylesheet. No fallback instruction for this class (unlike `cta-links`).
7. MEDIUM: `rel="noopener"` should be `rel="noopener noreferrer"` on external link.

**CODEX (Eng — architecture challenge):**
1. Tests will fail on implementation: hero copy assertion and policyos-layers assertion.
2. `pillars.html` and `compare.html` both missing from `docs/`.
3. `btn-secondary` and `cta-links` not in stylesheet; only `cta-links` has a fallback.
4. Em-dash success criterion scope unclear — "title block only" is ambiguous if other metadata or base template contains them.
5. AGENTS.md commit checklist requires documentation updates for public page framing changes. Spec doesn't mention this.

**ENG CONSENSUS TABLE:**
```
ENG DUAL VOICES — CONSENSUS TABLE:
═══════════════════════════════════════════════════════════════
  Dimension                             Claude   Codex   Consensus
  ──────────────────────────────────── ──────── ──────── ─────────
  1. Test suite stays green?            FAIL     FAIL     CONFIRMED FAIL
  2. All link targets valid?            FAIL     FAIL     CONFIRMED FAIL
  3. All CSS classes exist?             FAIL     FAIL     CONFIRMED FAIL
  4. WIP link markup correct?           FAIL     FAIL     CONFIRMED: ambiguous
  5. Security (rel attr)?               MEDIUM   —        flagged
  6. Repo doc update required?          —        YES      flagged
═══════════════════════════════════════════════════════════════
```

#### Test diagram — codepaths to coverage

| Codepath | Test type | Current test | Post-rewrite status |
|---|---|---|---|
| Hero statement copy | e2e assertion | `hero statement contains expected copy` (line 961) | WILL FAIL — asserts "Voting matters" |
| Phase grid present | e2e assertion | `all three phase names are present` (lines 964-968) | WILL FAIL — `.policyos-layers` removed |
| CTA btn-primary link | e2e assertion | `Get Involved CTA links correctly` (line 970) | WILL PASS — locator still resolves |
| Page title | e2e assertion | `has correct title` | WILL PASS — title unchanged |
| H1 content | e2e assertion | `renders h1` | WILL PASS — h1 unchanged |
| Nav aria-current | e2e assertion | `nav shows aria-current` | WILL PASS |
| New hero copy | e2e assertion | MISSING | Must add: assert "The promise of America" |
| Phase grid absent | e2e assertion | MISSING | Must add: assert `.policyos-layers` absent |
| New section headings | e2e assertion | MISSING | Must add: assert "The work of keeping a promise" |
| WIP links present | e2e assertion | MISSING | Must add: assert links to get-involved.html |
| Two CTA buttons | e2e assertion | MISSING | Must add: assert `.page-nav-cta` has 2 buttons |

---

### Cross-Phase Themes

**Theme: Strategic mechanism loss** — flagged in Phase 1 (CEO) by both voices, flagged in Phase 2 (Design) by Codex. High-confidence signal across 3 independent voice assessments. The page's name is "The Plan" but the approved content no longer contains what a plan is.

**Theme: Missing CSS classes / broken links** — flagged in Phase 2 (Design) and Phase 3 (Eng) by all 4 voices. `btn-secondary`, `pillars.html` are confirmed absent. High-confidence signal.

**Theme: Test suite breakage** — flagged in Phase 3 (Eng) by both voices. 2 tests will fail on implementation. Success criterion #6 ("all tests pass") is impossible to meet without test updates, which the spec doesn't mention.

---

## Decision Audit Trail

| # | Phase | Decision | Classification | Principle | Rationale | Rejected |
|---|-------|----------|----------------|-----------|-----------|---------|
| 1 | CEO | Strategic mechanism loss — flag as USER CHALLENGE | User Challenge | P6 | Both models agree the user's stated direction loses the differentiating mechanism; user must decide | Auto-deciding |
| 2 | CEO/Eng | `btn-secondary` class missing — flag as spec error | Mechanical | P1, P5 | Class confirmed absent; spec assumes it exists; implementer will ship unstyled button | Ignore |
| 3 | CEO/Eng | `pillars.html` missing — flag as broken link | Mechanical | P1 | File confirmed absent in docs/; link will 404 on production site | Ignore |
| 4 | Design | `compare.html` conditional omission — spec is correct | Mechanical | P5 | Spec already handles this: "if a compare index page exists; otherwise omit" | Flag as broken |
| 5 | Eng | Test updates required — flag as missing spec section | Mechanical | P1 | 2 e2e tests will fail; success criterion #6 cannot be met without them; add to spec | Defer |
| 6 | Eng | `arch-intro` guidance ambiguous — flag for clarification | Mechanical | P5 | Existing class is a grid component; wrong semantic for link list; inline style fallback needed | Keep ambiguous |
| 7 | Eng | `rel="noopener noreferrer"` — flag as spec error | Mechanical | P1 | External link should have both tokens; `noreferrer` prevents Referer header leak | Leave as-is |
| 8 | Eng | `aria-labelledby` must be explicit — flag for clarification | Mechanical | P5 | Section-to-heading wiring implied but not shown; implementer may miss it | Leave implicit |
| 9 | Eng | Repo doc update required (AGENTS.md commit checklist) | Mechanical | P5 | Page framing changes are a public-state change; commit checklist applies | Ignore |
| 10 | Design | Background color for "Built together" (dark vs parchment) | Taste | P3 | Spec says "implementer's call, but dark is preferred" — auto-decide: use dark | Parchment |
| 11 | Design | Hero eyebrow "The Path Forward" retained while path removed | Taste | P5 | Explicit instruction: "No changes to structural eyebrow" — follow spec | Change eyebrow |
