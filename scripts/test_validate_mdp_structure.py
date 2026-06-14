"""Tests for scripts/validate_mdp_structure.py — specifically the find_missing() helper."""
from pathlib import Path

from scripts.validate_mdp_structure import find_missing


def test_find_missing_returns_only_absent_paths(tmp_path: Path) -> None:
    """find_missing should return exactly the paths that do not exist under *root*."""
    # Create some required paths, leave others absent.
    (tmp_path / "README.md").write_text("# ok")
    (tmp_path / "docs").mkdir()
    (tmp_path / "docs" / "decisions.md").write_text("# ok")

    required = [
        "README.md",          # exists
        "MDP.md",             # missing
        "docs/decisions.md",  # exists
        "docs/role-model.md", # missing
    ]

    result = find_missing(required, tmp_path)

    assert sorted(result) == sorted(["MDP.md", "docs/role-model.md"])


def test_find_missing_empty_when_all_present(tmp_path: Path) -> None:
    """No missing paths should yield an empty list."""
    (tmp_path / "a.txt").write_text("a")
    (tmp_path / "b.txt").write_text("b")

    result = find_missing(["a.txt", "b.txt"], tmp_path)

    assert result == []


def test_find_missing_all_missing(tmp_path: Path) -> None:
    """When nothing exists, every required path is returned."""
    required = ["x.md", "y.md", "z.md"]

    result = find_missing(required, tmp_path)

    assert sorted(result) == sorted(required)
