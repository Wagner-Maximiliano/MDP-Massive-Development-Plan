# Automated Intake Checklist

Use this checklist when Tony is asked to place a live project under MDP.

The point is simple: inspect first, ask later.

## Human gives

- project path
- goal
- permission mode
- optional hard constraints

## Tony auto-collects

Check these in order.

### 1. Project pointer

- [ ] check for `MDP.md`
- [ ] read it first if present
- [ ] capture current permission mode and constraints

### 2. Repo shape

- [ ] inspect root folders and key files
- [ ] identify likely source, docs, scripts, config, and test paths
- [ ] detect whether the project is tiny, small, medium, or large

### 3. Git state

- [ ] detect whether `.git` exists
- [ ] capture current branch if available
- [ ] note whether remotes exist
- [ ] note whether the working tree is clean or dirty

### 4. Tech stack

- [ ] infer primary languages
- [ ] identify likely runtime or framework
- [ ] identify likely entrypoints
- [ ] identify package manager or environment files

### 5. Verification paths

- [ ] locate tests if they exist
- [ ] locate scripts that look like checks or validators
- [ ] note whether verification is strong, weak, or missing

### 6. Current operating state

- [ ] find existing docs that explain status or decisions
- [ ] find current handovers if they exist
- [ ] infer likely project state: live, waiting, paused, or unclear
- [ ] identify the first obvious blockers or risks

### 7. Minimum artifact check

Ensure these exist or are queued for creation:

- [ ] `MDP.md`
- [ ] `docs/decisions.md`
- [ ] `docs/handover-human-summary.md`
- [ ] `docs/handover-technical-agent.md`
- [ ] `docs/handover-restart-prompt.md`

### 8. First task list

- [ ] draft 3 to 5 human-readable tasks
- [ ] keep the first list small and safe
- [ ] include verification or safety work if missing

### 9. Human decision filter

Only ask the human when one of these is true:

- [ ] permission needs to increase
- [ ] a risky action is proposed
- [ ] a strategic tradeoff needs Felipe
- [ ] a technical direction fork needs Alex
- [ ] a financial tradeoff needs Tom
- [ ] confidence is below the threshold

## Output format

After intake, Tony should return:

1. what was found
2. what artifacts exist or are missing
3. first 3 to 5 tasks
4. only the decisions needed from the human

## Anti-pattern

Do not ask the human for facts the repo can reveal by inspection.