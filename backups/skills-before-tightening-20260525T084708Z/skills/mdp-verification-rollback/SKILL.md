---
name: mdp-verification-rollback
description: Verification, warnings, and rollback protocol for MDP implementation tasks.
version: 0.1.0
tags: [mdp, verification, rollback, safety]
---

# MDP Verification and Rollback

Use for meaningful implementation work.

## Verification record

Record:

- command
- result
- warnings
- known non-blocking issues
- remaining risk

## Rollback record

Before execution, identify:

- what will change
- how to undo it
- files, configs, or data affected
- whether rollback is automatic, manual, or impossible
- verification command after rollback
- who approves rollback if things go wrong

If rollback is impossible or risky, raise decision risk and consider Human Owner approval.
