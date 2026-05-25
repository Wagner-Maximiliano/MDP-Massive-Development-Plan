---
name: mdp-decision-gates
description: Decision confidence, escalation, and blocked-project rules for MDP.
version: 0.1.0
tags: [mdp, decisions, escalation]
---

# MDP Decision Gates

Use for major decisions, blocked projects, or approval questions.

## Confidence rule

- 95 percent or higher: proceed if within permission mode and inform the Human Owner when appropriate.
- Below 95 percent: escalate to the Human Owner with a compact decision brief.
- High-impact, irreversible, legal, financial, reputation, production, or security decisions may still require Human Owner approval above 95 percent.

## COO first rule

The COO / Decision Coordinator is the first approval layer for major operational, strategic, reputation, business, life, or cross-agent decisions.

## Blocked project rule

Before declaring a project stalled, the PA must look for safe parallel work.

If no safe work can continue and confidence is below 95 percent, contact the Human Owner.
