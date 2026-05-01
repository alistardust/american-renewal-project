# Contributing to the Freedom & Dignity Project

Welcome. Thank you for being here.

Before you contribute, please read **[`.github/project-identity.md`](.github/project-identity.md)** — it describes what this project is, who it speaks to, and how it speaks. Everything we build together flows from that document.

---

## What kind of contributions are welcome?

This project needs people with many different skills. You do not need to be a developer to contribute.

- **Research** — investigate issues, source claims, verify citations
- **Writing** — draft or refine policy positions, plain-language summaries, or site content
- **Review** — critique language, evidence, framing, and tradeoffs on existing content
- **Structure and systems** — help organize PolicyOS, schema, and system logic
- **Development** — HTML, CSS, JavaScript, Python scripting, database work
- **Accessibility** — review and improve how the site works for people with disabilities
- **Community** — help expand the conversation on social media, in your community, or anywhere else

---

## Where to start

<!-- TODO: Fill this in once contribution pathways are designed (see ROADMAP.md Phase 4) -->

For now, the best place to start is:
- Browse [open issues](../../issues) to see what needs attention
- Read [`ROADMAP.md`](ROADMAP.md) to understand what phase we're in and what's coming
- Join the community discussion (Discord link coming)

---

## How to submit code or content changes

<!-- TODO: Expand with PR workflow, branch naming, commit conventions, and review expectations -->

This project follows **Conventional Commits** for all commit messages:

```
<type>[scope]: <description>
```

Types: `feat`, `fix`, `docs`, `refactor`, `test`, `chore`, `perf`, `ci`, `revert`

Before submitting a pull request:

1. Run `npm run test:unit` — all tests must pass
2. Run `npm run test:e2e` after any HTML/CSS/JS changes
3. Make sure your changes are consistent with `.github/project-identity.md` in voice and values
4. Keep PRs focused — one logical change per PR, ideally under 400 lines

---

## Policy content contributions

If you are contributing to policy content (pillar cards, policy positions, plain-language summaries):

- All policy positions need a v2 structured ID (`XXXX-XXXX-0000` format)
- Every factual claim must be cited — see `.github/ai-repo-context.md` for citation standards
- New policy must be consistent with PolicyOS (`policy/policyos/`)
- New positions must be backfilled into the DB in the same commit

---

## Code of conduct

This project is for everyone. We expect contributors to:

- Be welcoming and respectful to others — especially people new to the work
- Disagree constructively — critique ideas, not people
- Not engage in harassment, exclusion, contempt, or bad faith

This is not a partisan space. People with different backgrounds, political histories, and starting points are welcome here.

---

## Questions?

<!-- TODO: Add specific contact info, Discord link, or GitHub Discussions link -->

Open an issue and ask. We're glad you're here.
