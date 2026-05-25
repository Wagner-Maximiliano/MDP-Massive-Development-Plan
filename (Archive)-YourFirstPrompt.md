MDP - Massive Development Plan

Tony helped me draft this based on lessons from a recent multi-agent software project.

Important: this is a planning and learning session only.

Do not create a repository.
Do not touch GitHub.
Do not write files unless I explicitly ask.
Do not deploy anything.
Do not assume the structure is final.

I already have a GitHub repository for this project, but I do not want you to touch it yet unless I explicitly say so.

## Mission

# What this project is looking to tackle

Hw to build a great project plan that can be used from beguinning to end
- Clear instructions
- Interviewing
- Covering all bases
- Making less assumptions and get more information from the user
- Follow project creation template
- High level tasks (GUI, Backend, Database, Website, iOS application, UI/UX, Script)
Who the agents are and what they do.
What is the basic structure that all projects need to follow.
What is the expected results expected from each agent (What good looks like)
How agents and specially the personal assistant manages long coversarions and contexts.
How are projects run
- How to keep it clean
- How to keep it secure and not break it
How to work with multiple models from multiple vendors
How to assign tasks
How to make sure tasks run in parallel without breaking the flow or cause unexpected conflicts
How to handle frozen/stuck sessions
How to handle agents errors from multiple different vendors
How to manage santize and keep tokens usage low
How to best use free models
How to leverage logic scripts to automate, monitor, report, log, etc. In order to reduce the need for model reasoning where logi automation can perform a reliable job, thus reducing the need for wasting tokens, and creating structured solid solutions that don't deviate.
- There are a number of different processes that can be automated with scripting instead of triggering LLM models, wherever possible we should leverage this. Therefore this should be part of our MAP.
How to delegate tasks and make sure they are carried out as expected.
How to self improve
How to auto improve the MAP (Massive Action Plan)
- Confidence scoring
- Feedback loop
- Improving on-demand
Hwo to keep the Human informed without overloading them with information
How to better manage memory
How to have better interaction and collaboration between agents.
How to identify when tokens are low or have run out.

I want to create a reusable software/application development harness for future projects.

This harness should eventually become a top-layer operating system for how I build software with AI agents. It should capture processes, protocols, templates, skills, checklists, decision gates, folder standards, Kanban workflows, multi-agent coordination rules, handover standards, and verification practices.

But right now, we are just planing it, not building.

Right now, your job is to learn the lessons from a recent project, help me organize them, combine them with my own ideas, and brainstorm a strong plan before we implement anything.

It should not be big as this is a context that will constantly have to be read and followed for every prompt, so we need to harness what is really important without overloading the sessions' context.

We might want to break this up into a series of skills so that only the relevant information for the task at hand is extracted from this, but we need to make sure that anhthing that is done that needs to have information from MDP, that it can find it and won't skip it.

## Working Mode

This session should be collaborative and hands-on.

I want to be deeply involved.

Your job is to:
1. Absorb the lessons below.
2. Ask clarifying questions where needed.
3. Help me organize the ideas into categories.
4. Help me identify gaps, conflicts, and priorities.
5. Help me combine these lessons with my own improvement list.
6. Help me design the future harness before we create files.
7. Keep the process practical and grounded.

Do not rush into implementation.

## Project Concept

The project is a reusable development harness for AI-assisted software delivery.

Project Name: MDP - Massive Development Plan

The harness should eventually help future agents and projects follow consistent processes for:

- Project kickoff
- Folder structure
- Documentation hygiene
- Kanban execution
- Multi-agent coordination
- Subagent delegation
- Model routing and token discipline
- Planning before implementation
- Testing and verification
- Handover writing
- Cleanup and refactoring
- Stale task recovery
- Decision gates
- Human approval gates
- Git and GitHub discipline
- Safe use of automation
- Avoiding project root chaos
- Avoiding agents stepping on each other
- Keeping Max involved where needed

## Lessons Learned From Recent Project

These are the lessons we want to capture and potentially turn into protocols, skills, templates, or checklists.

### 1. Do not let agents dump files into the project root, 

We learned that agents tend to create too many files directly in the repository root.

This quickly becomes messy and cause issues over time.

Root should be reserved for true project entry files only, such as:

- README.md
- pyproject.toml or package.json
- requirements.txt or lockfile
- .gitignore
- maybe CLAUDE.md or AGENTS.md if needed
- critical compatibility forwarders only when justified

Everything else should go into structured folders.

Potential standard:

text
docs/
tests/
tools/
config/
src/ or app/
examples/
scripts/ (1/5)


Docs should go under `docs/`.

Tests should go under `tests/`.

Verification scripts should go under `tools/verification/`.

Temporary notes, handovers, plans, and generated reports should not pile up in the root, and they should be removed or archived Once there is no need for them anymore.

### 2. Folder cleanup needs a safety protocol

Cleaning a project can break things if done recklessly.

Before moving files:
- List current root files.
- Classify each file.
- Decide what must stay in root.
- Decide what can move safely.
- Decide what needs a compatibility forwarder.
- Search for references before moving.
- Move low-risk files first.
- Update docs and commands.
- Run tests after moving.
- Report before/after root file counts.

File classification should include:
- Must stay in root
- Safe to move
- Move with compatibility forwarder
- Move only after config/import update
- Do not move yet

When moving tests:
- Update imports.
- Update pytest config if needed.
- Run the moved tests.
- Watch for headless GUI blockers.
- Update docs with new commands.

Example command after moving GUI smoke tests:

bash
QT_QPA_PLATFORM=offscreen python -m pytest -q tests/gui_smoke

### 5. Verification scripts should be separated from tests

Manual or CI-style verification scripts should go under:

text
tools/verification/

Example:

text
tools/verification/verify_offline_packet_inspector.py

Docs should show the canonical command.

Example:

bash
QT_QPA_PLATFORM=offscreen timeout 30 python tools/verification/verify_offline_packet_inspector.py

### 6. KANBAN DESCRIPTIONS SHOULD ALSO BE HUMAN READABLE

Use paragraphs, lists, separation and title so that a Human can quickly glance over it and find the sections they are interested in.

### 7. Human-readable Kanban task titles matter

Task titles must be understandable in list view.

Bad examples:
- `M10-N`
- `t_309162e0`
- `Phase 3 thing`
- `Fix stuff`

Good format:

text
<Phase/Area>: <action/outcome> - <artifact/scope> (2/5)

Examples:
- `GUI/UX tooling: integrate offline modules - main app shell`
- `Live validation: record server details and approval boundaries`
- `Documentation cleanup: organize handovers - docs/handovers`
- `Testing: relocate GUI smoke tests - tests/gui_smoke`

IDs can remain internal, but visible task titles should explain the work.

### 8. Kanban tasks need clear ownership and recovery rules

Stuck or stale workers must not be ignored.

Stuck worker protocol:
1. Inspect task state.
2. Inspect run logs.
3. Inspect heartbeats.
4. Check process state.
5. Reclaim only when safe.
6. Block with a clear reason.
7. Include recovery path.
8. Avoid leaving silent stale work as “running”.

Blocked task reasons should explain:
- What is blocked
- Why it is blocked
- Who can unblock it
- What exact information or action is needed
- What should not happen until unblocked

### 9. Kanban comments should be useful operational records

When adding comments to tasks, include:
- What changed
- Files created or moved
- Verification results
- Remaining blockers
- Next action
- Safety notes

Avoid vague comments like:
- “Done”
- “Fixed”
- “Updated stuff”

When completing a task the following information must be added as a comment:
- Summary of the work done
- Agents involved in the task
- Number of tokens used
- Improvements suggestions if any
- Next step for this specific task if applicable.

### 10. Multi-agent work needs explicit lanes

Agent roles should be clear.

Max:
- Final decision-maker.
- Can override all agents.
- Should be involved in important or experimental projects.

Tony:
- Primary assistant and orchestrator.
- Keeps momentum.
- Routes work.
- Synthesizes.
- Should not overbuild or flood context.
- Any work in which Tony is not an expertise he delegates, Tony makes decisions, doesn't do the leg work. 

Felipe:
- COO and strategic decision coordinator.
- Reviews operational, strategic, reputational, business, and cross-agent decisions.
- Has oversight of all projects and the Agency's Goals and ambitions
- Knows the risks
- Demands structured development, security standards and best practices

Alex:
- CTO and technical systems lead.
- Handles architecture, coding, infrastructure, deployment, automation, and technical decisions.
- Makes all technical decisions but delegates most of the tasks to the developers

Tom:
- CFO and wealth strategist.
- Handles budgets, pricing, subscriptions, costs, and financial tradeoffs.

Silva and helper agents:
- Use for bounded reading, summarization, sanity checks, and low-risk drafting.
- Give narrow tasks.
- Avoid dumping huge context.
- Use free models where possible.

### 11. Subagents should get narrow, bounded tasks

Bad subagent prompt:
text
Look around the repo and tell me what you think.

Better:
text
Inspect root-level Python tests only. Do not modify files. Return:
1. list of files
2. import/path risks
3. safest target folder
4. verification command
Keep output under 300 words. (3/5)


Rules:
- Give exact repo path.
- Give exact task.
- Give exact output format.
- Say whether they may modify files.
- Prefer read-only for scans.
- Verify their claims yourself.
- If they time out, report it honestly.

### 12. Use free/cheap helper models carefully

Free helper agents can time out or stall.

Protocol:
- Use them for bounded tasks only.
- Pre-collect compact facts before delegating.
- Avoid raw dumps.
- Ask for short outputs.
- Use them for reading and summarization, not critical final decisions.
- If they fail, fall back to local inspection with the next available cheapest model
- Report timeouts so that they are not left stuck with no intervention.

### 13. Tony should not pretend subagents succeeded

If subagents fail, time out, or return incomplete work, the orchestrator should say that clearly.

If agents/subagents fail, Tony should deleget the the next cheapest model and not do the work himself unless strictly required

Report:
- Which subagents were attempted.
- What they were asked to do.
- Whether they succeeded.
- Whether their outputs were verified.
- Whether Tony had to take over.

### 14. Planning should come before implementation


Before creating files:
- Clarify goal.
- Clarify scope.
- Clarify repository name and location.
- Clarify what should be automated versus hands-on.
- Clarify whether GitHub can be touched.
- Clarify what “done” means.
- Clarify which parts are reusable skills versus protocols versus templates.

For this harness project, planning comes first.

### 15. Do not touch GitHub without approval

GitHub safety:
- No push without approval.
- No merge without approval.
- No destructive git commands unless explicitly confirmed by Human - provide human necessary information for an informed decision without overwhelm.
- Always check git status before changes.
- Report branch and dirty state.

### 16. Handover discipline is critical

Handovers should be standard and complete.

A good handover includes:
- Instructions of where the find the MAP plan
- Project name
- Agents that worked on it with the Models each agent used
- Date
- Branch
- Git status
- Completed work
- Active work
- Blocked work
- Key decisions
- Important files
- Verification commands and results
- Known risks
- Next steps for Max
- Next steps for Tony
- Next steps for technical agents
- What not to do
- What part of the MDP had to be overulled - What parts of the standard was deviated and why.
- Open questions

Handovers should live in:

text
docs/handovers/

### 17. Docs need canonical paths

After moving files:
- Update docs to point to canonical paths.
- Search for stale references.
- Avoid duplicated path mistakes.
- Keep docs aligned with actual commands.

Example issue that can happen:
text
tools/verification/tools/verification/script.py

So cleanup must include reference verification.

### 18. A docs index helps agents navigate

Every docs folder should have a README when useful.

Example:

text
docs/README.md
docs/handovers/README.md
docs/testing/README.md
docs/live-validation/README.md
docs/architecture/README.md
docs/reviews/README.md
docs/offline/README.md (4/5)


These should explain what belongs in each folder.

### 19. Major decisions need gates

Use decision gates to prevent uncontrolled work.

Possible gate types:
- Pre-flight gate
- Revision gate
- Escalation gate
- Abort gate
- Human approval gate
- Technical review gate
- Safety review gate
- Go/No-Go gate

The harness should define these simply.

### 20. Safety constraints should be explicit

For projects involving live systems, servers, users, money, data, security, or production:
- Define what is allowed.
- Define what is forbidden.
- Define stop conditions.
- Define who approves escalation.
- Define notification rules.
- Define rollback or recovery steps.

### 21. Root-cause debugging beats random fixes

When something is stuck:
- Understand before fixing.
- Reproduce if possible.
- Inspect logs.
- Identify root cause.
- Patch the cause, not the symptom.
- Add a regression test or verification check.
- Document the lesson.

Example lesson:
- Headless PyQt tests hung because message boxes were not mocked.

### 22. Verification should be targeted and recorded

Every change should have a verification command.

Examples:
bash
python -m pytest -q tests/gui_smoke
QT_QPA_PLATFORM=offscreen timeout 30 python tools/verification/verify_offline_packet_inspector.py
git status --short

Record:
- Command
- Result
- Warnings
- Known non-blocking issues
- Remaining risk

### 23. Warnings should be reported honestly

Example:
- Tests passed but had `PytestReturnNotNoneWarning`.
- That should be reported as non-blocking but worth cleaning later.

Do not hide warnings.

### 24. Separate skills, protocols, templates, and checklists

The future harness may contain different artifact types:

Skills:
- Procedural memory for agents.
- Trigger conditions and exact steps.
- Example: safe cleanup refactor skill.

Protocols:
- Operating rules.
- Example: Kanban execution protocol.

Templates:
- Copy-paste starting documents.
- Example: handover template.

Checklists:
- Short human/agent validation lists.
- Example: pre-flight checklist.

Docs:
- Explanation and design rationale.
- Example: agent operating model.

We need to decide the exact boundaries before creating the repository content.

### 25. Keep the harness practical, not theoretical

Avoid:
- Corporate fluff
- Overly abstract process design
- Huge documents nobody reads
- Repeating the same rule everywhere
- Making the system so heavy that agents avoid it

Prefer:
- Short rules
- Clear examples
- Copy-paste prompts
- Decision trees
- Exact commands
- Practical checklists
- Minimal but strong structure

### For this harness project

This is important.

For this project:
- Do not run ahead.
- Do not create files unless asked.
- Brainstorm first.
- Combine Tony’s lessons with Max’s own improvement list.
- Help me shape the system.
- Ask good questions.
- Suggest options.
- Let me make the key decisions.

## What I Want From You Now

Please do not implement anything yet.

First, respond with:

1. Your understanding of the project in 5 bullets.
2. A categorized map of the lessons above.
3. The main design tensions or tradeoffs you see.
4. A proposed brainstorming agenda.
5. Questions for me before we design the harness.
6. A suggested way to merge my additional improvement list into this.

Remember:
- No repo creation.
- No GitHub action.
- No file writes.
- This is planning only.

Here are my unorganized thoughts on this:



## The Structure of a project:

Max tells Tony his goal and what he wants to achieve.

Max inteprets whethere this is new or something they have been working on before.

If it is new, Tony asks Max if he wants to start a new Repository for this.
If an existing project, then Tony asks Felipe and Alex to assist with Max's request.


All projects should follow best Practices [Look up what best practices for development is and define it]
As well as best practices, we have our own best practices document that should be followed to better manage a project between multiple agents, models and 1 human in the specific structure that Max and Tony have designed. We call our own best practices a MAP (Massive Action Plan) for this we have a dedicated Repository in Github containing a small set of files that contains rules, processes, etc.

# Things to create a process for


When an agent session reaches 160k tokens, build a handover document and compact it
There should be a handover diretory, that will contain all handover files. These handovers must be worked in the folowing way
 - There will be a template handover in the folder that must be used for every handover session
 - Because the will be a template, the handover document can be created by an Free or low cost model. Tony should assess only the handover and use Silva to fetch the information and return the responses. In other words, Tony has overview of the project to know when things don't seem right. so Tony assesses the handover from Silva and if he's at least 95% confident, then Tony confirms that the Handover is complete otherwise Tony improves the prompt to Silva or send a follow up prompt to address what ever is necessary to improve confidence.

 Once the handover is complete, a message must be sent Max, letting him know the 


There should always be 2 handover files and this handover file should contain:
versioned secrtions - So that every time a new handover is done, the last one is checked 


- Agents should have their own memories as well as a shared set of memories. but just like in the way humans have memories, so should the agents. There are scertain rules that they all follow, but memories that are specific to their own roles should be contained within their own Agent's memory file(s)


