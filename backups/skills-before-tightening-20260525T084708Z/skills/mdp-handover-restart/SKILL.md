---
name: mdp-handover-restart
description: Handover, context limit, and restart prompt protocol for MDP projects.
version: 0.1.0
tags: [mdp, handover, context]
---

# MDP Handover and Restart

Use when context is high, work is pausing, ownership changes, or a project needs a restart package.

## Trigger

Near 160k tokens or before context quality collapses, create a handover package.

## Required outputs

1. Human summary handover.
2. Technical agent handover.
3. Copy-paste restart prompt for the Human Owner.

## Review

A cheaper operator model may draft the handovers. The PA reviews and accepts only when confidence is 95 percent or higher.
