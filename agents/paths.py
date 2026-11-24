"""Locate project and user storage under .agent."""

from pathlib import Path


_AGENT_DIR = ".agent"


def project_agent_path(project: Path, name: str) -> Path:
    return project / _AGENT_DIR / name


def user_agent_path(name: str, *parts: str) -> Path:
    return Path.home().joinpath(_AGENT_DIR, name, *parts)
