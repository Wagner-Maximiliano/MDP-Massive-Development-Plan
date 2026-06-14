# MDP - Massive Development Plan

MDP is a reusable operating layer for AI-assisted project delivery.

It does not replace Hermes. It defines how to use Hermes profiles, skills, Kanban, cron, delegation, memory, and GitHub safety in a clean repeatable way.

## Current mode

This repository is in early v1 implementation.

## Notes

The `backups/skills-before-tightening-20260525T084708Z/` directory is a snapshot of `skills/` taken before the 2026-05-25 tightening pass, kept for reference.

## Core principles

1. Small always-read core, on-demand skills for detail.
2. Planning depth scales with risk, complexity, uncertainty, and impact.
3. Use scripts for repeatable logic. Use LLMs for ambiguity, synthesis, judgment, and decisions.
4. Use role-based lanes: Human Owner, PA/Orchestrator, COO, CTO, CFO, Operator, Specialist Workers.
5. Major decisions go through the relevant lead role. The COO is the default first approval layer for strategic and operational decisions.
6. Confidence below 95 percent escalates to the Human Owner.
7. Meaningful implementation tasks need verification and rollback notes.
8. File creation and writing must be no-clobber by default. Never silently overwrite existing files.
9. Tasks, scripts, modules, and automations need appropriate error handling and useful diagnostics.
10. Project health must be monitored proactively. The Human Owner is not the monitoring system.

## Repository layout

- `MDP.md`: local project pointer and always-read project context.
- `docs/`: explanations and design notes.
- `skills/`: installable or skill-ready Hermes skills.
- `templates/`: copy-paste artifacts.
- `protocols/`: operating rules and source notes that may also be represented as skills.
- `scripts/`: lightweight automation and validation.
- `tests/`: validation checks for the MDP repository.

## v1 skills

- `mdp-core`
- `mdp-project-kickoff`
- `mdp-decision-gates`
- `mdp-kanban-health`
- `mdp-handover-restart`
- `mdp-verification-rollback`
- `mdp-agent-routing`
- `mdp-model-cost-governance`
- `mdp-context-budget`
- `mdp-file-safety`
- `mdp-error-observability`
- `mdp-repo-permission-modes`

## File safety

New files must be created with no-overwrite behavior. Existing files should be changed with targeted patches unless an overwrite is explicitly approved.

See `protocols/file-safety.md`.

## Error handling

Failures should leave enough evidence to understand what failed, where it failed, why it likely failed, and what should happen next.

See `protocols/error-handling-observability.md`.
