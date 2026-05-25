# MDP Live Project Quickstart

This is the simplified version.

The human should provide only:

- the project path
- the goal
- the decision boundaries

The framework should collect the rest.

## The operating model

Human responsibilities:

1. Choose the project
2. State the goal
3. Approve the permission mode
4. Make important decisions when escalated

Framework responsibilities:

1. Inspect the repo
2. Discover structure, docs, and current status
3. Infer stack, major modules, and likely risks
4. Create or update the MDP project pointer
5. Create kickoff and handover artifacts
6. Build the first task list
7. Route decisions to the correct role
8. Keep continuity through handovers and restart prompts

## Default rule

If the framework can discover it safely, the human should not have to type it.

Start conservative. Default to Mode 1 unless the human explicitly grants more.

---

## What the human gives

Use this minimal input:

```text
Project path: <PROJECT_PATH>
Goal: <ONE OR TWO SENTENCE GOAL>
Permission mode: Mode 1
Optional decisions or constraints: <ANY HARD BOUNDARIES>
```

That is enough to start.

## What the framework should auto-collect

After receiving the minimal input, the framework should gather:

- repo root files
- existing docs
- current git state if available
- languages and main tech stack
- likely entrypoints
- tests and verification scripts
- current handover files if they exist
- blockers or missing basics
- recommended first tasks

The framework should do this by inspection, not by asking the human to repeat obvious facts.

---

## Step 1: Put MDP in the live project

In the target project, place one file in the root:

- `MDP.md`

This is the project pointer.

If it does not exist, the framework should create it.
If it exists, the framework should update it carefully.

### Minimum content of `MDP.md`

- project status
- permission mode
- Human Owner
- PA / Orchestrator
- COO
- CTO
- CFO
- Operator
- what to read first
- what not to do
- where handovers live

## Step 2: Create the minimum MDP artifact set

The framework should ensure these files exist:

```text
MDP.md
docs/decisions.md
docs/handover-human-summary.md
docs/handover-technical-agent.md
docs/handover-restart-prompt.md
```

Optional files can come later. These five are enough to start.

## Step 3: Run automated project intake

Once the project path and goal are given, the framework should run an intake pass automatically.

The intake pass should:

1. Read `MDP.md` if present
2. Read the smallest relevant repo docs
3. Inspect folder structure
4. Check for git
5. Check for tests, scripts, and verification paths
6. Identify the likely current project state
7. Draft the kickoff summary
8. Draft the first task list
9. Surface only the decisions the human must make

The human should receive a summary, not a long questionnaire.

## Step 4: Ask only for decisions, not raw facts

After intake, the framework should come back with:

- what it found
- what it recommends
- what decision is needed next

### Good framework question

```text
I inspected the project. It appears to be a Python automation repo with partial tests and no current handover package. I recommend staying in Mode 1 and starting with kickoff, verification baseline, and a safe first task list. Decision needed: do you want this project treated as Small or Medium scope for tracking?
```

### Bad framework question

```text
What language is the project?
What files exist?
Do you have tests?
What is the current structure?
```

If the framework can inspect it, it should inspect it.

## Step 5: Route the work automatically

Once intake is done, the framework should route work by role:

- Tony: intake, synthesis, continuity, next actions
- Felipe: operational and strategic decisions
- Alex: technical direction, architecture, implementation strategy
- Tom: cost, pricing, budget, financial tradeoffs
- Silva or cheap utility workers: scans, summaries, inventories, formatting

The human should not have to manually choose the internal lane for normal work.

## Step 6: Start with a tiny first board

The framework should create the first task list automatically.

Use 3 to 5 tasks only.

Good first tasks:

- Kickoff: capture current project state - live repo intake
- Safety: declare permission mode and forbidden actions - project pointer
- Verification: locate current checks and test paths - repo baseline
- Handover: create continuity package - docs
- Planning: identify first safe execution task - next step

Keep the first board small and obvious.

## Step 7: Keep the human in the decision loop only

The framework should interrupt the human only when one of these is true:

- permission needs to increase
- the best path is unclear
- there is a strategic tradeoff
- there is a technical architecture fork
- there is a financial tradeoff
- a risky or irreversible action is proposed
- confidence is below the decision threshold

Everything else should keep moving automatically.

## Step 8: Maintain continuity automatically

At the end of meaningful work, the framework should update:

- `docs/handover-human-summary.md`
- `docs/handover-technical-agent.md`
- `docs/handover-restart-prompt.md`

The human should not need to ask for handovers every time.

## Step 9: Re-enter with one prompt

When returning later, the human should only need something like this:

```text
Resume this MDP project.
Project path: <PROJECT_PATH>
Goal: <CURRENT GOAL>
Keep permission mode at Mode 1 unless you need approval.
```

The framework should read the restart prompt and continue.

---

## The one-message bootstrap prompt

Use this to put a live project under MDP with minimal human effort:

```text
Put this live project under MDP.
Project path: <PROJECT_PATH>
Goal: <GOAL>
Permission mode: Mode 1.
Collect the rest by inspection.
Create or update the minimum MDP artifacts.
Give me a short summary, the first task list, and only the decisions you need from me.
Do not commit, do not touch GitHub, and do not silently overwrite files.
```

## Expected framework behavior after that prompt

The framework should:

1. inspect the project
2. create or update `MDP.md`
3. create the minimum docs if missing
4. summarize current state
5. build the first small task list
6. route important decisions to the correct lead
7. ask the human only for decisions

## Human success condition

This is working when the human mostly does this:

- gives the goal
- approves boundaries
- answers decision prompts

And the framework mostly does this:

- gathers context
- organizes the work
- maintains continuity
- keeps the agents in the right lanes

## Design rule for future MDP improvements

When improving MDP, prefer this order:

1. automate collection
2. reduce human typing
3. reduce repeated context gathering
4. escalate only real decisions
5. keep artifacts small and useful

If a step can be automated safely, automate it.
If a question can be answered by inspection, do not ask the human.
If the human is being used as a data-entry layer, the framework is failing.
