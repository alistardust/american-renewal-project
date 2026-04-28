# PolicyOS Governance v1

## Purpose

This document defines the operating process for proposing, reviewing,
adopting, and amending PolicyOS rules and the pillars that must comply with
them.

PolicyOS is a rule system. Rule systems need governance — someone has to be
able to reject non-compliant proposals, and there must be a defined path from
proposal to adoption. This document provides that path at the scale the
platform currently operates.

This is intentionally lightweight. It is designed for a small, trust-based
team. It will need to grow as the platform grows.

---

## The principle

The process for proposing, reviewing, adopting, and amending PolicyOS rules
must itself comply with the anti-capture, transparency, and independence
requirements of the system. This governance document is the mechanism for that
self-compliance.

---

## Roles

**Platform maintainer** — The project originator. Currently the primary
responsible actor for all PolicyOS governance decisions. Can propose, review,
accept, or reject rules. All decisions are traceable and documented.

**Contributing reviewer** — Any person contributing to the platform who
participates in a rule review. Contributing reviewers may raise objections,
propose alternatives, and request revision. They do not have unilateral
acceptance/rejection authority at this stage.

**Adversarial reviewer** — Any person or process (including AI-assisted
review) that conducts a formal adversarial review per PAOS-TEST-0004 through
0007. Adversarial review findings must be documented and addressed before
adoption; they may not be silently dismissed.

---

## Proposal process

A new PolicyOS rule or amendment to an existing rule follows this path:

1. **Draft** — A proposed rule is written with: the rule ID, rule text, which
   values it advances or protects (per PAOS-NORM-0001), the responsible actor,
   trigger condition, intended outcome, and enforcement path (per
   PAOS-AUTH-0001, 0002).

2. **Self-review** — The proposer reviews the draft against the full NORM,
   AUTH, and TEST family checklists and documents the review.

3. **Adversarial review** — For rules that materially expand or restrict policy
   scope, or that affect KERN or overlay structure, an adversarial review per
   PAOS-TEST-0004 through 0007 is required. The review must be documented.
   Review findings must be addressed (with documented rationale) before the rule
   proceeds.

4. **Platform maintainer review** — The platform maintainer reviews the draft,
   the self-review, and any adversarial review findings. The maintainer may
   accept, request revision, or reject.

   Acceptance requires: the rule complies with NORM, AUTH, and TEST families;
   adversarial review findings have been addressed; and the rule does not
   conflict with any existing layer without an explicit cross-layer resolution
   per the conflict-resolution clause in `policyos_1_0_rules_proposal.md`.

5. **Adoption** — The accepted rule is added to the appropriate layer document
   with the adoption date noted. If the rule supersedes an existing rule, the
   superseded rule is marked deprecated with a reference to the new rule
   (per PAOS-MAINT-0003).

---

## Pillar compliance review

When a pillar is proposed or substantially revised:

1. **KERN compliance** — The pillar is reviewed against all mandatory KERN
   rules (PLOS-KERN-0001 through 0027). A pillar may not be published if it
   fails a KERN rule without an explicit, documented, reviewable justification
   that passes PAOS-NORM-0002 scrutiny.

2. **Overlay identification** — The pillar identifies which overlays apply to
   its design area and documents its inheritance.

3. **NORM review** — The pillar is reviewed against the full NORM family
   checklist. Value tensions must be surfaced and resolved per PAOS-NORM-0008.

4. **Adversarial review** — High-stakes pillars (those governing healthcare,
   criminal justice, immigration, voting, housing, or essential public goods)
   require adversarial review before publication.

5. **Acceptance gate** — The platform maintainer must sign off on KERN
   compliance and NORM review before a pillar is published to the site.

**Consequence of non-compliance:** A pillar that fails the acceptance gate is
flagged in the public-facing index as under review and may not be cited as
canonical policy until it passes. It is not deleted — the draft is visible
with its review status clearly disclosed.

---

## Amendment process

PolicyOS rules may be amended following the same process as new rules. See
also the amendment protocol in `policyos_platform_values_v1.md` for Layer 1
amendments.

Amendments must be versioned. Commit messages follow Conventional Commits
format. The amendment record in the document must show what changed and why.
Prior text is retained in git history; it need not be duplicated in the
document itself.

---

## Transparency requirements

All governance decisions — acceptances, rejections, revision requests — must
be documented in commit messages or review notes accessible in the repository.
The governance process is not conducted in private. Decisions are not made
anonymously. The reasoning for every acceptance or rejection is visible.

---

## Limitations and evolution

This governance model is intentionally limited to what is achievable at the
current platform scale. Known limitations:

- The platform maintainer is not independent of the platform. This creates a
  potential conflict of interest that is partially mitigated by transparency
  and documented reasoning, but not eliminated.
- There is no external review body, no civil society oversight, and no formal
  appeal path beyond the maintainer.
- Contributing reviewers have advisory standing, not decision-making authority.

These are not hidden. They are acknowledged and will need to be addressed as
the platform grows and as a more formal governance structure becomes possible.
The goal is the structure described in this document, not the current minimum.
