# MDP Bootstrap Prompt

Use this prompt to put a live project under MDP with minimal human input.

## Human input only

Fill in:

- project path
- goal
- permission mode
- optional hard constraints

## Copy-paste prompt

```text
Put this project under MDP.

Project path: <PROJECT_PATH>
Goal: <ONE OR TWO SENTENCE GOAL>
Permission mode: <MODE 1 BY DEFAULT>
Optional constraints: <ONLY IF NEEDED>

Do the rest by inspection.

Your job:
1. Read any existing `MDP.md` first.
2. Inspect the repo structure and smallest relevant docs.
3. Infer the stack, likely entrypoints, tests, scripts, and current state.
4. Create or update the minimum MDP artifacts if missing.
5. Draft the first small task list.
6. Ask me only for decisions, approvals, or unclear tradeoffs.

Minimum artifacts to ensure:
- `MDP.md`
- `docs/decisions.md`
- `docs/handover-human-summary.md`
- `docs/handover-technical-agent.md`
- `docs/handover-restart-prompt.md`

Rules:
- Do not commit
- Do not merge
- Do not touch GitHub unless explicitly allowed
- Do not silently overwrite files
- Default to conservative actions when unsure

Output format:
- What you found
- What you created or updated
- First 3 to 5 tasks
- Decisions needed from me
```

## Expected behavior

A good MDP bootstrap run should:

- avoid a long questionnaire
- inspect before asking
- keep the first plan small
- escalate only real decisions
- leave a clean restart path for the next session

## Notes

- Default to Mode 1 when the human does not explicitly allow more.
- If the repo already has MDP artifacts, update them carefully instead of rebuilding everything.
- If the project is tiny, keep the task list and artifacts lean.