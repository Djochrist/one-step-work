#!/usr/bin/env python3
"""Validate the One Step Work skill's required files and core sections."""
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parent.parent
SKILL = ROOT / "SKILL.md"
REQUIRED_SECTIONS = (
    "## Purpose",
    "## Core rule",
    "## Workflow",
    "## Interaction guidelines",
    "## Respect user direction",
    "## Boundaries and safety",
    "## Quality checklist",
)
REQUIRED_FILES = (
    ROOT / "README.md",
    ROOT / "LICENSE",
    ROOT / "references" / "examples.md",
)


def validate() -> list[str]:
    problems: list[str] = []
    for path in (SKILL, *REQUIRED_FILES):
        if not path.is_file():
            problems.append(f"Missing required file: {path.relative_to(ROOT)}")

    if not SKILL.is_file():
        return problems

    text = SKILL.read_text(encoding="utf-8-sig")
    match = re.match(r"\A---\s*\n(.*?)\n---\s*(?:\n|$)", text, re.DOTALL)
    if not match:
        problems.append("SKILL.md must start with a YAML frontmatter block")
        return problems

    frontmatter = match.group(1)
    for key in ("name", "description", "license", "compatibility", "metadata"):
        if not re.search(rf"(?m)^{re.escape(key)}\s*:", frontmatter):
            problems.append(f"SKILL.md frontmatter is missing '{key}'")

    for section in REQUIRED_SECTIONS:
        if section not in text:
            problems.append(f"SKILL.md is missing section: {section}")

    if "references/examples.md" not in text:
        problems.append("SKILL.md should point agents to references/examples.md")
    elif not (ROOT / "references" / "examples.md").is_file():
        problems.append("SKILL.md references a missing references/examples.md")

    return problems


def main() -> int:
    problems = validate()
    if problems:
        print("Skill validation failed:")
        for problem in problems:
            print(f"- {problem}")
        return 1
    print("Skill validation passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
