#!/usr/bin/env python3
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REQUIRED = [
    'README.md',
    'MDP.md',
    'agents.md',
    'docs/decisions.md',
    'docs/role-model.md',
    'protocols/repo-permission-modes.md',
    'protocols/project-health-monitoring.md',
    'protocols/file-safety.md',
    'protocols/error-handling-observability.md',
    'templates/project-pointer-AGENTS.md',
    'templates/decision-brief.md',
    'templates/human-handover.md',
    'templates/technical-handover.md',
    'templates/restart-prompt.md',
    'skills/mdp-core/SKILL.md',
    'skills/mdp-project-kickoff/SKILL.md',
    'skills/mdp-decision-gates/SKILL.md',
    'skills/mdp-kanban-health/SKILL.md',
    'skills/mdp-handover-restart/SKILL.md',
    'skills/mdp-verification-rollback/SKILL.md',
    'skills/mdp-agent-routing/SKILL.md',
    'skills/mdp-model-cost-governance/SKILL.md',
    'skills/mdp-context-budget/SKILL.md',
    'skills/mdp-file-safety/SKILL.md',
    'skills/mdp-error-observability/SKILL.md',
    'skills/mdp-repo-permission-modes/SKILL.md',
]


def find_missing(required: list[str], root: Path) -> list[str]:
    """Return the subset of *required* paths that do not exist under *root*."""
    return [p for p in required if not (root / p).exists()]


missing = find_missing(REQUIRED, ROOT)
if missing:
    print('Missing required MDP files:')
    for p in missing:
        print(f'- {p}')
    raise SystemExit(1)
print(f'MDP structure OK. Checked {len(REQUIRED)} files.')
