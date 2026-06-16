## Summary

Add a `CONTRIBUTING.md` guide at the repository root to give new and returning contributors a clear, single source of guidance on how to set up the project, make changes, and submit them. The issue is open-ended on scope, so this plan proposes a sensible, conventional structure covering setup, workflow, standards, and submission—while keeping the document concise and maintainable.

## Scope

In scope:
- A single `CONTRIBUTING.md` at the repo root covering the standard contributor lifecycle.
- A short pointer to it from `README.md` (if one exists).

Out of scope:
- Code of Conduct, issue/PR templates, and CI configuration (these can be follow-ups; mention them as links/placeholders only).
- Changing any existing build, lint, or test tooling.
- Governance, release process, or licensing changes.

## Files to change

- `CONTRIBUTING.md` (new) — the contributor guide.
- `README.md` (edit, if present) — add a one-line link to `CONTRIBUTING.md`.

## Steps

1. Inspect the repo to ground the guide in reality: detect language/build tooling, existing scripts (test/lint/format), branch naming, and any existing docs so instructions are accurate rather than generic.
2. Draft `CONTRIBUTING.md` with these sections:
   - **Introduction** — who the guide is for and how to ask questions.
   - **Getting started / local setup** — prerequisites, clone, install, build, run.
   - **Development workflow** — branching model, making changes, running the app locally.
   - **Coding standards** — formatting/linting commands, naming conventions, commit message style.
   - **Testing** — how to run tests and expectations for new tests.
   - **Submitting changes** — fork/branch, PR process, review expectations, what makes a PR mergeable.
   - **Reporting issues** — how to file bugs/feature requests.
   - **Where to get help** — discussion/contact channels.
3. Use real, copy-pasteable commands derived from step 1; mark any unknowns as `TODO` rather than inventing details.
4. Add a brief "Contributing" link in `README.md` if one exists.
5. Self-review for accuracy, broken links, and tone; verify all referenced commands and paths exist.

## Acceptance criteria

- `CONTRIBUTING.md` exists at the repo root and renders correctly as GitHub markdown.
- It covers setup, workflow, coding standards, testing, and the PR/submission process.
- All commands and file paths referenced actually exist in the repo (no placeholders left except clearly labeled `TODO`s).
- All internal/external links resolve.
- If a `README.md` exists, it links to `CONTRIBUTING.md`.

## Risks

- **Repo specifics unknown at planning time** — actual tooling/commands must be confirmed during implementation; generic instructions risk being wrong. Mitigate via step 1 inspection.
- **Drift** — the guide can fall out of date as tooling changes; keep it concise and link to canonical sources rather than duplicating them.
- **Scope creep** — open-ended ask may invite adding CoC, templates, and CI; keep those out of this change and list as follow-ups.
