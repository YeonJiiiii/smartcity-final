"""Common utilities for static urban analysis preprocessing scripts."""

from __future__ import annotations

import json
import shutil
from pathlib import Path
from typing import Any


def ensure_dir(path: Path) -> Path:
    path.mkdir(parents=True, exist_ok=True)
    return path


def read_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8-sig"))


def write_json(path: Path, payload: Any) -> None:
    ensure_dir(path.parent)
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")


def write_text(path: Path, text: str) -> None:
    ensure_dir(path.parent)
    path.write_text(text, encoding="utf-8")


def mirror_to_public(path: Path, public_root: Path, output_root: Path) -> Path:
    relative = path.relative_to(output_root)
    target = public_root / relative
    ensure_dir(target.parent)
    shutil.copy2(path, target)
    return target


def status_note(message: str) -> dict[str, str]:
    return {"status": "warning", "message": message}
