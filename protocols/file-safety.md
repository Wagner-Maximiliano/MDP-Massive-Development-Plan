# File Safety Protocol

MDP-managed work must be no-clobber by default.

## Core rule

Do not create or write a file in a way that can silently overwrite existing content.

Before creating a file, the agent or script must check whether the target path already exists. If it exists, the operation must fail or escalate unless the task explicitly authorizes overwrite.

## Safe creation patterns

Use one of these patterns:

- Python: `Path(path).open('x')` or `open(path, 'x')` for exclusive creation.
- Shell: `set -o noclobber` and `>` redirection, or test first with `[ ! -e "$path" ]`.
- Agent tools: search/read the target path first, then use patch for targeted edits or ask/escalate if overwrite is not explicitly allowed.

## Overwrite rule

Overwriting is allowed only when all are true:

1. The existing file was inspected or its purpose is known.
2. The overwrite was explicitly requested or approved.
3. The agent states what will be replaced.
4. A backup, diff, or rollback path exists when the file matters.

## Case-insensitive filesystem warning

On Windows-mounted paths, names like `AGENTS.md` and `agents.md` can refer to the same file. Agents must treat path comparisons as case-insensitive when working under `/mnt/c`, `/mnt/d`, or other Windows mounts.

## Preferred edit behavior

- Use targeted patches for existing files.
- Use exclusive create for new files.
- Never use blind full-file writes on existing project files unless overwrite is part of the explicit task.
