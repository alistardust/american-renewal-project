# Site Identity Alignment — Design Spec

*Version 2 — 2026-05-01*

---

## Problem Statement

The Freedom & Dignity Project site was built as a policy platform before the project identity was fully defined. The result is a site that reads like a policy library — it shows what the project proposes, but not what the project *is*. The prose, framing, and information architecture were written before `.github/project-identity.md` existed, and they don't reflect the movement voice, the human element, or the theory of participation that now defines the project.

The defining gap: a visitor can read the entire site and still not know where they fit or what they can do. Agency — the "aha moment" that should land in the first 30 seconds — is buried at the end of the journey. There is also a critical missing page: the site shows the destination (what the country should look like) but has no answer to "how do you actually make this happen in the real world?"

---

## North Star

> **"I know exactly where I fit in and what I can do about it."**

This is the feeling a visitor should leave the homepage with. It is the lens through which every design decision is evaluated. Not "did they understand the framework" — "did they find their place?"

---

## What We Are Not Doing

- Rewriting policy content (pillar pages, compare pages — separate effort)
- Changing the visual design system
- Rebuilding the PolicyOS documentation
- Adding new policy positions

---

## Navigation Architecture

### Primary nav — the story arc (5 items)

> **Home | The Problem | The Plan | The Platform | Join the Movement**

The primary nav tells a complete story. A visitor can orient themselves by reading the nav alone.

### Hamburger menu — full site tree (expandable)

Every page on the site, organized hierarchically. Primary nav items at the top level, with sub-pages expanding below. This gives first-time visitors a clean story arc and gives returning supporters a way to jump anywhere without hunting.

```
☰
├── Home
├── The Problem
├── The Plan
├── The Platform
│   ├── Bills of Rights
│   ├── PolicyOS
│   └── Policy Library
│       ├── Accountable Power
│       │   ├── [pillar pages]
│       ├── Clean Democracy
│       ├── Equal Justice
│       ├── Real Freedom
│       └── Freedom to Thrive
├── Join the Movement
├── Roadmap
├── About
└── Compare Platforms
    ├── Republican Party
    └── [other compare pages]
```

---

## Page Inventory

### Pages redesigned or created

| File | Title | Change |
|---|---|---|
| `index.html` | Home | Redesigned — Option C (see below) |
| `problem.html` | The Problem | Renamed from `mission.html`; old file removed |
| `plan.html` | The Plan | **New page** — does not currently exist |
| `platform.html` | The Platform | Expanded — values + rights + PolicyOS + foundations |
| `join.html` | Join the Movement | Renamed from `get-involved.html`; old file removed |

### Pages demoted to hamburger only

| File | Notes |
|---|---|
| `proposals.html` | Becomes "Policy Library" in hamburger tree |
| `roadmap.html` | Secondary nav only |

### Pages folded in or removed

| File | Disposition |
|---|---|
| `rights.html` | Content elevated into `platform.html`; file removed |
| `approach.html` | Content audited; relevant material folded into `platform.html` or `about-us.html`; file removed |
| `constitution.html` | Stale redirect — removed |
| `foundations.html` | Stale redirect — removed |

### Pages audited for voice consistency

All remaining top-level pages — `about-us.html`, `letter-from-the-founder.html`, `roadmap.html`, `about-ai.html` — audited and rewritten as needed against the identity document.

---

## Homepage Redesign — Option C

The homepage restructures around three visitor questions.

### Section 1 — Movement identity and belonging

Lead with hope and belonging. The visitor feels seen and welcomed before they understand what the project is. The emotional line comes first. Movement identity ("right vs. wrong, not left vs. right") is established immediately. Primary CTA leads toward "Join the Movement."

*Section heading: emerges from content, not from this label.*

### Section 2 — Validation

Brief, devastating, validating. Names the reality — things are messed up, the system is broken — without dwelling in it. "You're not wrong. You're not alone." Pivots immediately to hope. Links to The Problem page for visitors who need the full validation before they can trust the project.

*Ratio: brief validation, long hope. Per FDR and MLK — name the reality, spend most time on the vision.*

### Section 3 — Hope and pivot

"It doesn't have to be this way." Brief — the pivot from validation to action. Sets up the champion issues below.

### Section 4 — Champion issues + The Plan tease

3–5 champion issue cards drawn from the Bills of Rights. Each card:
- Names a right every person deserves
- Shows what's blocking it (brief, concrete)
- Links to the relevant pillar page and to The Plan

Followed by a brief tease of The Plan: "Here's how we actually make this happen." Links to `plan.html`.

### Section 5 — Join the Movement

Multiple pathways, multiple roles, no credentials required. Organizer, donor, writer, developer, volunteer. Replaces "Get Involved" — same content, stronger framing. CTAs: sign up, find your role, share.

---

## The Plan Page (`plan.html`) — New

The critical missing piece. The site currently shows the destination (what the country should look like) but has no answer to "how do you actually make this happen?" This page is primarily a call to action, not an explanation. It does not re-litigate the problem.

*Voice note: short, forward-looking, action-oriented. Assumes the visitor is already convinced and ready to act.*

### Sections

1. **The strategy** — organize, build coalitions too large to ignore, elect officials who support these positions, apply sustained pressure that never stops, comprehensive communications and outreach
2. **Where we are now** — honest about current state; links to Roadmap for specifics
3. **Your part** — multiple roles, multiple entry points, no credentials required
4. **CTAs** — sign up, find your role, share

---

## The Platform Page (`platform.html`) — Expanded

The Platform is a *vision and principles* page, not a policy library. Visitors who want depth can reach the full policy library from here via the hamburger or an explicit CTA. The Platform's job is to establish what we believe and how we work.

*Logical flow: why we believe → what every person deserves → how we build it → what we're building.*

### Sections

1. **Statement of values** — the foundation everything flows from; what we believe at the core
2. **Bills of Rights** — what flows from those values; what every person deserves; rights language stated directly (currently in `rights.html`, elevated here)
3. **PolicyOS** — how we turn rights into policy that actually works; the core values built into the system; 2–3 example rules shown in action (demonstrates rigor and differentiation — this isn't a wish list)
4. **Foundations overview** — the five structural areas we cover; each foundation with its "What It Demands / What It Rejects" framing; links to the full pillar pages for depth
5. **CTA** → "Explore the full policy library" — links to `proposals.html`

---

## About Page (`about-us.html`) — Rewritten

Movement-first. Who we are as a project, what we're building, how to contribute. The founder's presence is included for transparency and relatability — not as the focus. Brief, human, honest: "I'm a person who got fed up and decided to do something about it. You can too." `approach.html` content is audited and any relevant material is folded here.

---

## Voice and Prose Alignment

Every top-level page is audited and rewritten as needed against `.github/project-identity.md`.

### Audit framework (per page)

Each page is evaluated against five questions:

1. **Voice** — Does it sound like the movement? Or like a policy briefing?
2. **Welcome** — Does it feel open to anyone, or does it assume the visitor already agrees?
3. **Agency** — Does the visitor learn their role? Is there something they can do?
4. **Human element** — Are there people in it, or just mechanisms and frameworks?
5. **Connection** — Does it connect to the rest of the site's story?

Rating: ✅ solid · ⚠️ needs work · ❌ missing entirely

### Rewrite priorities

1. `index.html` — front door
2. `plan.html` — new, must be written from scratch
3. `platform.html` — now a major nav page
4. `problem.html` — second page most visitors see
5. `join.html` — the conversion page
6. `about-us.html` — movement-first rewrite
7. `roadmap.html`, `letter-from-the-founder.html`, `about-ai.html` — lower priority

### Per-page rewrite brief

Each rewrite must:

1. Open with human stakes before architectural explanation
2. Use the movement voice from the identity document
3. Give the visitor at least one clear signal of where they fit
4. Connect forward to the next step in their journey
5. Remove jargon that gates access

---

## Identity Document Reference

Every decision in this spec flows from `.github/project-identity.md`. Key constraints:

- **What we are:** Reform movement. Not a think tank, not a policy library.
- **Who we speak to:** Everyone — especially the next person who might walk in.
- **How we speak:** Direct, not preachy. Welcoming, not exclusive. Hopeful, not naive. Human first. Right vs. wrong, not left vs. right.
- **What we won't be:** A lecture. A fear machine. A partisan scoreboard.
- **Writing intent:** Visitors feel welcomed, seen, inspired, hopeful, cared for, belonging. Never overwhelmed, afraid, attacked, or like this isn't for them.

---

## Success Criteria

A visitor arriving with no prior knowledge of the project should, after the homepage:

1. Understand this is a reform movement, not a policy library
2. Feel this is for them — not just for policy wonks or insiders
3. See a clear path to participation
4. Want to keep reading

A visitor who reads through the top-level pages should leave with:

1. A clear answer to "what is this project and why does it exist"
2. A clear answer to "what can I do"
3. The sense that things can actually be fixed — and that this project has a concrete plan for how

---

## Out of Scope (Future Work)

- Real human stories (requires real people who consent)
- Champion issue dedicated pages (future phase — homepage cards first)
- Full pillar page rewrites
- Compare page updates
- CONTRIBUTING.md expansion
