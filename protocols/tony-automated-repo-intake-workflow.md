# Tony Automated Repo Intake Workflow

This spec defines how Tony should inspect a repo and generate the minimum MDP artifacts automatically.

## Goal

Given only:

- project path
- goal
- permission mode
- optional hard constraints

Tony should gather the rest by inspection and return only the decisions the human must make.

## Inputs

Required:

- project path
- goal

Default if not specified:

- permission mode: Mode 1

Optional:

- hard constraints
- special approval boundaries

## Output contract

Tony must return:

1. a short status summary
2. what was discovered
3. what artifacts were created or updated
4. the first 3 to 5 tasks
5. only the decisions that require human input

## Minimum artifacts

Tony should ensure these exist:

- `MDP.md`
- `docs/decisions.md`
- `docs/handover-human-summary.md`
- `docs/handover-technical-agent.md`
- `docs/handover-restart-prompt.md`

## Workflow

### Phase 1: Safety and scope

1. confirm the project path exists
2. confirm the permission mode, defaulting to Mode 1
3. assume no commit, no merge, and no GitHub action unless explicitly allowed
4. inspect before writing anything

### Phase 2: Read the smallest useful context

1. read `MDP.md` first if present
2. read the smallest relevant docs such as `README.md`, status docs, or decisions docs
3. avoid loading large or irrelevant files unless needed

### Phase 3: Inspect the repository

Tony should inspect and infer:

- root structure
- likely source folders
- docs, scripts, tests, configs, and environment files
- current git state if available
- likely language and runtime stack
- likely entrypoints
- missing basics such as tests, handovers, or validation paths

### Phase 4: Infer current project state

Tony should label the project as one of:

- live
- waiting
- paused
- unclear

Tony should also note:

- current risks
- obvious blockers
- likely next safe action

### Phase 5: Ensure minimum artifacts

If an artifact is missing, Tony should create it conservatively.

If an artifact exists, Tony should update it carefully instead of replacing it blindly.

### Phase 6: Draft the first task list

Tony should generate 3 to 5 small, human-readable tasks.

The first list should usually cover:

- current state capture
- permission and safety confirmation
- verification baseline
- handover continuity
- first safe execution task

### Phase 7: Route decisions internally

Tony should route work by role without making the human choose lanes.

- Felipe for strategic or operational tradeoffs
- Alex for technical architecture or implementation strategy
- Tom for financial or cost tradeoffs
- utility workers for bounded scans or formatting

### Phase 8: Ask only for decisions

Tony should ask the human only when:

- permission needs to increase
- a risky action is proposed
- the best path is unclear
- there is a meaningful strategic tradeoff
- there is a technical fork that needs Alex
- there is a financial tradeoff that needs Tom
- confidence is below the threshold

## Artifact content expectations

### `MDP.md`

Should contain at minimum:

- project status
- permission mode
- role map
- required skills
- local paths
- do-not-do rules

### `docs/decisions.md`

Should capture accepted project decisions, not raw notes.

### Handovers

The handover set should make restart easy for both humans and agents.

- human summary for the owner
- technical handover for the next agent
- restart prompt for the next session

## Anti-rules

Tony should not:

- ask the human for facts the repo can reveal
- create large ceremony for a tiny project
- silently overwrite existing files
- touch GitHub without approval
- claim readiness without verification evidence
- flood the human with internal process detail

## Verification

Before reporting completion, Tony should verify:

- the inspected project path was correct
- the artifact set exists or missing items are explicitly reported
- the first task list is small and actionable
- the output contains decisions only where needed
- warnings and limits are stated honestly

## Rollback

If the intake writes incorrect artifacts, rollback is simple:

- revert the new artifact files on the working branch
- or close the PR and delete the branch if the work has not been merged

## Recommended operating rule

If Tony can inspect it safely, Tony should inspect it.
If the human is being used as a data-entry layer, the workflow is failing.