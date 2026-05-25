# Repository Permission Modes

Every MDP-managed project declares a permission mode at kickoff.

## Modes

- Mode 0: read-only inspection.
- Mode 1: local file edits allowed, no commits.
- Mode 2: local commits allowed, no push.
- Mode 3: remote actions allowed, such as push or PR within approved limits.
- Mode 4: privileged actions, such as merge, force-push, branch deletion, repo settings, repo creation, or deploy.

## Role guidance

- Operator: usually max Mode 2.
- CTO: usually max Mode 3.
- COO: approval authority, usually max Mode 3 if acting directly.
- PA: can orchestrate Mode 4 only when the Human Owner or approval chain explicitly allows it.
- Human Owner: final override.

## Enforcement

MDP defines policy. Hermes profiles, toolsets, approval prompts, wrapper scripts, and GitHub branch protection enforce what they can.
