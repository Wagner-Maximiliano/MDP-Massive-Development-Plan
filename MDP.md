# MDP Project Pointer

This project follows MDP: Massive Development Plan.

## Project status

- Status: live
- Permission mode: Mode 1, local file edits allowed, no commits or remote actions unless Max explicitly approves.
- GitHub: do not touch unless explicitly approved.
- Human Owner: Max
- PA / Orchestrator: Tony
- COO / Decision Coordinator: Felipe
- CTO / Technical Lead: Alex
- CFO / Finance Lead: Tom
- Operator / Utility Agent: Silva

## Always-read rule

Before working in this project, read this file and load relevant MDP skills.

Start with:

- `mdp-core`

Load task-specific skills when relevant:

- Project intake or setup: `mdp-project-kickoff`
- Decisions, approval, escalation: `mdp-decision-gates`
- Kanban, project health, blockers: `mdp-kanban-health`
- Handovers or context limits: `mdp-handover-restart`
- Testing, verification, rollback: `mdp-verification-rollback`
- Agent roles, ownership, routing: `mdp-agent-routing`
- Model routing, provider cost, token spend: `mdp-model-cost-governance`
- Context pressure, compact prompts, token budget: `mdp-context-budget`
- File creation, edits, no-clobber safety: `mdp-file-safety`
- Scripts, workers, diagnostics, failures: `mdp-error-observability`
- Git, commits, pushes, PRs, deploy permissions: `mdp-repo-permission-modes`

## Safety rules

- Do not create repositories.
- Do not touch GitHub.
- Do not deploy anything.
- Do not run destructive commands.
- Do not silently overwrite existing files. New files must be created with no-clobber behavior.
- Do not hide errors. Add useful diagnostics when tasks, scripts, modules, or automations can fail.
- Keep the project root clean.
- Prefer scripts for repeatable checks.
- Keep Max informed without flooding him.

## Related local context

- `agents.md`: current agent role notes for this project.
- `YourFirstPrompt.md`: original planning prompt for this exercise.
- `docs/decisions.md`: accepted MDP decisions.
