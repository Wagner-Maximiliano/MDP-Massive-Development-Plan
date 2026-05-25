---
name: mdp-core
description: Always-read core for MDP-managed projects.
version: 0.1.0
tags: [mdp, planning, orchestration, project-management]
---

# MDP Core

Use this skill for every MDP-managed project.

## Core rules

1. Keep the always-read context small.
2. Load deeper MDP skills only when relevant.
3. Planning depth scales with risk, complexity, uncertainty, and impact.
4. Use scripts for repeatable logic. Use LLMs for ambiguity, synthesis, judgment, and decisions.
5. Use generalized roles: Human Owner, PA, COO, CTO, CFO, Operator, Specialist Workers.
6. Respect the declared repository permission mode.
7. Do not touch GitHub, deploy, or run destructive actions unless approved.
8. Use no-clobber file safety: never create or write a file in a way that can silently overwrite existing content.
9. Use proper error handling and observability: failures should leave useful evidence, not disappear silently.
10. Keep the project root clean.
11. Verify meaningful changes and record warnings honestly.
12. Proactively monitor project health. The Human Owner is not the monitoring system.

## Route to deeper skills

- New project or intake: `mdp-project-kickoff`
- Decision or escalation: `mdp-decision-gates`
- Kanban, blockers, health: `mdp-kanban-health`
- Handover or context limit: `mdp-handover-restart`
- Verification or rollback: `mdp-verification-rollback`
