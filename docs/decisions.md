# MDP Decisions Log

This file records accepted planning decisions for the v1 MDP harness.

## Accepted decisions

1. MDP uses a small always-read core plus on-demand skills and templates.
2. MDP is generalized by roles, not hardcoded agent names.
3. Current mapping: Max is Human Owner, Tony is PA, Felipe is COO, Alex is CTO, Tom is CFO, Silva is Operator.
4. Planning depth scales with risk, complexity, uncertainty, and impact.
5. MDP is script-first for repeatable logic and LLM-first for judgment.
6. Major operational or strategic decisions go through the COO first.
7. If confidence is 95 percent or higher, proceed and inform the Human Owner when appropriate.
8. If confidence is below 95 percent, contact the Human Owner with a compact decision brief.
9. Blocked projects should keep safe parallel work moving when possible.
10. Full project stall only happens when no safe useful work can continue.
11. Meaningful implementation tasks require rollback notes.
12. Project health needs proactive monitoring.
13. MDP should reuse Hermes primitives first and only add new content where there is a gap.
14. The first pilot creates six core operational skills.
15. File creation and writing must be no-clobber by default. Agents must not silently overwrite existing files.
16. Tasks, scripts, modules, and automations must include appropriate error handling and diagnostics so failures can be identified quickly.
