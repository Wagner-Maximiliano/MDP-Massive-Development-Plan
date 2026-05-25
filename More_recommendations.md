# More Recommendations

Yes, Max. I found it.

There is no single clean “general management runbook” file yet. The operating system we built is scattered across:

1. Hermes global agent files
2. Tony skills and skill references
3. Game_Automation Kanban governance task/comments
4. Game_Automation project docs
5. Cron watchdog prompt/script
6. Your new MDP project prompt/session notes

That’s actually good news. The material exists. It just needs to be consolidated into the framework/harness you’re building.

The strongest source of truth is this:

```bash
hermes kanban --board game-automation show t_f18836a2
```

Task:

`Project governance: record autonomy rules, decisions, and confidence tracking`

This is the closest thing to the missing runbook. It contains the project-level operating mandate:

- Tony drives the project end to end when safe
- Kanban is the source of truth
- Token usage must stay lean
- Escalate when confidence is low or risk is high
- Alex owns technical architecture/development decisions
- Felipe owns major operational/strategic decisions
- Tom owns finance/cost decisions
- Silva handles low-risk support/inventory work
- Claude Code handles implementation while available
- Confidence scores are recorded in decisions
- Hard gates remain for live-server, destructive git, push/merge, money, reputation, security

Key line from that Kanban task:

> Tony may decide and proceed when confidence is high and risk is low. Escalate to Max for real-world/live-server actions, legal/security/reputation/money risk, destructive changes, or confidence below 90%.

Then later Max lowered the autonomous test threshold:

> Escalation threshold for this test lowered to confidence <70%, plus live-server / destructive / money / reputation / security gates still require explicit Max approval.

So the scoring rule is not in a normal markdown doc. It’s in Kanban governance comments.

## Primary files I found

### 1. Agent hierarchy and lanes

`/home/lobster/.hermes/Agents-Profiles-Details.md`

This defines:

- Tony: primary assistant and orchestrator
- Alex: CTO, architecture, engineering, implementation review
- Tom: CFO, finance/cost/pricing/investment
- Felipe: COO, strategic decision coordinator
- Max: final authority

Most important Felipe rule:

> No major real-world decision should move forward without your evaluation unless Max explicitly overrides it.

### 2. Model and cost routing

`/home/lobster/.hermes/Agent-Model-Routing-Policy.md`

This defines:

- Tony on GPT-5.5 via openai-codex
- OpenRouter only for free models ending in `:free`
- Alex for technical decisions
- Felipe for strategy/operations
- Tom for finance
- high-end models only for hard reasoning, architecture, security, production readiness, major strategic/financial decisions

This belongs in the harness as “Model Routing and Cost Governance.”

### 3. Multi-agent development workflow

`/home/lobster/.hermes/profiles/tony/skills/software-development/subagent-driven-development/SKILL.md`

This is the core execution workflow:

- Fresh subagent per task
- Two-stage review
- Spec compliance first
- Code quality second
- Final integration review
- Don’t skip review loops
- Don’t work directly on main/master
- Don’t claim readiness without verification, rollback, confidence, and review gate
- Report “who did what”

Linked reference files are very important:

`/home/lobster/.hermes/profiles/tony/skills/software-development/subagent-driven-development/references/gates-taxonomy.md`

Defines the reusable gate system:

- Pre-flight gate
- Revision gate
- Escalation gate
- Abort gate

This should absolutely become part of your framework.

`/home/lobster/.hermes/profiles/tony/skills/software-development/subagent-driven-development/references/multi-agent-governance-and-free-routing.md`

This is one of the best general management docs. It defines:

- who did what reporting
- subagent disclosure
- Kanban vs PR split
- branch/PR governance
- 90% escalation rule
- free model routing
- OpenRouter troubleshooting
- stop instead of silently falling back to paid models

Key rule:

> Kanban is the work coordination layer. GitHub PRs are the merge/review layer.

`/home/lobster/.hermes/profiles/tony/skills/software-development/subagent-driven-development/references/context-budget-discipline.md`

This defines token/context discipline:

- don’t read agent definition files unnecessarily
- don’t inline large files into subagent prompts
- delegate heavy work
- watch context pressure
- checkpoint/abort when context gets poor
- verify subagent claims structurally and semantically

### 4. Repository hygiene / cleanup process

`/home/lobster/.hermes/profiles/tony/skills/software-development/repository-organization/SKILL.md`

This contains the general cleanup runbook:

- clean project root
- docs under `docs/`
- handovers under `docs/handovers/`
- tests under `tests/`
- scripts under `tools/verification/`
- inspect before moving
- search references before moving
- preserve compatibility forwarders
- verify after moving

Linked project example:

`/home/lobster/.hermes/profiles/tony/skills/software-development/repository-organization/references/game-automation-cleanup-2026-05-24.md`

This is the reusable cleanup pattern extracted from Game_Automation.

### 5. Game_Automation project governance docs

These are project-specific, but they contain reusable management patterns.

`/mnt/c/Users/lobster/Github_Projects/Game_Automation/docs/reviews/GATE_REVIEW_TIER2.md`

This defines autonomy boundaries:

Tony can autonomously do:

- local/offline development
- unit tests
- mock/local loopback integration tests
- docs/prep
- controlled lab testing

Requires Max approval:

- live server interaction
- live feature testing
- live security testing
- data collection involving live systems

It also defines explicit approval checklist and confidence score.

`/mnt/c/Users/lobster/Github_Projects/Game_Automation/docs/live-validation/LIVE_VALIDATION_OPERATING_RECORD.md`

This is the live-validation operating boundary:

- current approval scope
- hard gates
- missing details required from Max
- proposed allowed actions
- disallowed actions
- stop conditions
- evidence rules
- confidence score
- Go/No-Go state

Very reusable for “risky/live system work.”

`/mnt/c/Users/lobster/Github_Projects/Game_Automation/docs/live-validation/COO_GO_NOGO_BRIEF.md`

This is a Felipe-style decision brief:

- current readiness
- remaining risks
- approval checklist
- confidence score
- recommendation

`/mnt/c/Users/lobster/Github_Projects/Game_Automation/docs/live-validation/PRE_LIVE_RUNBOOK.md`

This is more project-specific, but has useful structure:

- scope
- prerequisites
- validation steps
- evidence to collect
- rollback/restore
- risks
- confidence
- what must go to Felipe/Max

### 6. Game_Automation active watchdog automation

Cron job config:

`/home/lobster/.hermes/profiles/tony/cron/jobs.json`

Job:

`3396392ada21`
`Game Automation Tony auto-advance watchdog`

Prompt contains the live autonomy rule:

- use script output as compact context
- keep project moving without user check-ins
- inspect board if unfinished cards exist
- dispatch ready work
- recover crashed tasks if confidence >= 70%
- complete cards only with evidence
- create next card only when implied by completed parent cards
- respect hard gates
- record confidence scores in Kanban comments
- deliver locally unless Max must approve something or confidence is below 70%

Script:

`/home/lobster/.hermes/profiles/tony/scripts/game_auto_kanban_watch.py`

This is useful as a mechanical watchdog pattern:

- dispatch board
- parse task statuses
- detect no running/ready/scheduled work
- escalate to Tony when unfinished cards exist
- surface blockers
- keep output compact

### 7. Your MDP framework seed

`/mnt/c/Users/lobster/Github_Projects/MDP-Massive-Development-Plan/YourFirstPrompt.md`

Also found:

`/mnt/c/Users/lobster/Github_Projects/MDP-Massive-Development-Plan/agents.md`

`/mnt/c/Users/lobster/Github_Projects/MDP-Massive-Development-Plan/Goals.md`

The active MDP session already captured a good categorized map:

- project kickoff and planning
- folder hygiene
- cleanup safety
- Kanban discipline
- agent roles
- subagent delegation
- model/token discipline
- handovers
- verification and quality
- harness artifact types

## My recommendation for the framework/harness structure

Core always-read file:

`MDP_CORE.md`

Keep this tiny. It should include only:

- mission
- lifecycle
- agent hierarchy
- decision gates
- confidence thresholds
- approval rules
- Kanban as work coordination layer
- PR as merge/review layer
- verification required
- handover required before context collapse
- where deeper protocols live

Protocols folder:

`protocols/agent-routing.md`
Based on:
- `Agents-Profiles-Details.md`
- `Agent-Model-Routing-Policy.md`
- `multi-agent-governance-and-free-routing.md`

`protocols/confidence-and-escalation.md`
Based on:
- Kanban task `t_f18836a2`
- `GATE_REVIEW_TIER2.md`
- `COO_GO_NOGO_BRIEF.md`

`protocols/kanban.md`
Based on:
- Game_Automation board practice
- human-readable title memory
- watchdog script
- multi-agent governance reference

`protocols/gates.md`
Based on:
- `gates-taxonomy.md`

`protocols/context-budget.md`
Based on:
- `context-budget-discipline.md`

`protocols/live-risk.md`
Based on:
- `LIVE_VALIDATION_OPERATING_RECORD.md`
- `GATE_REVIEW_TIER2.md`
- `COO_GO_NOGO_BRIEF.md`

`protocols/repository-hygiene.md`
Based on:
- `repository-organization/SKILL.md`
- `game-automation-cleanup-2026-05-24.md`

Templates folder:

`templates/project-intake.md`
`templates/kanban-task.md`
`templates/blocked-task-comment.md`
`templates/handover.md`
`templates/go-no-go-brief.md`
`templates/live-validation-operating-record.md`
`templates/pre-live-runbook.md`
`templates/subagent-task-prompt.md`
`templates/verification-report.md`

Checklists folder:

`checklists/max-approval.md`
`checklists/live-system-safety.md`
`checklists/offline-readiness.md`
`checklists/merge-readiness.md`
`checklists/context-handover.md`
`checklists/root-cleanup.md`

## Key rules to extract into the harness

- Max is final authority.
- Tony orchestrates, routes, synthesizes, and keeps momentum.
- Alex owns technical architecture/development decisions.
- Felipe owns major operational/strategic gates.
- Tom owns finance/cost decisions.
- Silva/helpers do bounded, low-risk scans/summaries.
- Claude/coding agents implement, but don’t merge.
- Kanban is the work coordination layer.
- PRs are the review/merge layer.
- Confidence must be stated for important decisions.
- Below 90% confidence, escalate by default.
- For the Game_Automation autonomy experiment, below 70% escalates.
- Real-world, live-system, money, reputation, destructive, security, or user-impacting actions require approval regardless of confidence.
- Complete cards only with evidence.
- Create next cards only when clearly implied.
- Don’t let an idle board stall. Watchdog should inspect and advance safely.
- Don’t read or dump huge context unless needed.
- Use cheap/free agents for bounded support.
- Never silently route to paid OpenRouter.
- Handover before context collapse.
- Root folder stays clean.

## Bottom line

The “runbook” exists, but it’s currently distributed. The best consolidation seed is:

1. Kanban governance task:
   `t_f18836a2`

2. Hermes hierarchy:
   `/home/lobster/.hermes/Agents-Profiles-Details.md`

3. Model routing:
   `/home/lobster/.hermes/Agent-Model-Routing-Policy.md`

4. Multi-agent skill:
   `/home/lobster/.hermes/profiles/tony/skills/software-development/subagent-driven-development/`

5. Game_Automation gate docs:
   `/mnt/c/Users/lobster/Github_Projects/Game_Automation/docs/reviews/GATE_REVIEW_TIER2.md`
   `/mnt/c/Users/lobster/Github_Projects/Game_Automation/docs/live-validation/LIVE_VALIDATION_OPERATING_RECORD.md`
   `/mnt/c/Users/lobster/Github_Projects/Game_Automation/docs/live-validation/COO_GO_NOGO_BRIEF.md`

6. Watchdog automation:
   `/home/lobster/.hermes/profiles/tony/cron/jobs.json`
   `/home/lobster/.hermes/profiles/tony/scripts/game_auto_kanban_watch.py`

That’s the spine of the framework.
