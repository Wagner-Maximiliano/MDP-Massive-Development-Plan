---
name: mdp-kanban-health
description: Kanban execution, task hygiene, and proactive project health monitoring.
version: 0.1.0
tags: [mdp, kanban, health, monitoring]
---

# MDP Kanban and Health

Use for Kanban tasks, blocked work, stale workers, and project health checks.

## Kanban standards

Task titles should be human-readable:

`<Area>: <action/outcome> - <artifact/scope>`

Task comments should record:

- what changed
- files touched
- verification result
- blockers
- next action
- safety notes

## Health rule

Detect hiccups proactively. Do not wait for the Human Owner.

Watch for:

- new blocked tasks
- stale workers
- silent agents
- no ready tasks while project is live
- repeated failures
- provider/API errors
- token exhaustion
- auth expiry
- stale claims

Use scripts and structured status before model reasoning where possible.
