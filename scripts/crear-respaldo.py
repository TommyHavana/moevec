#!/usr/bin/env python3
"""Crea una copia local portable del proyecto, sin dependencias ni secretos."""

from datetime import datetime
from pathlib import Path
from zipfile import ZipFile, ZIP_DEFLATED


ROOT = Path(__file__).resolve().parents[1]
BACKUPS = ROOT.parent / "mee-backups"
EXCLUDED_DIRS = {"node_modules", ".next", "out", ".git", "__pycache__", "data"}
EXCLUDED_FILES = {".DS_Store"}


def include(path: Path) -> bool:
    parts = path.relative_to(ROOT).parts
    if any(part in EXCLUDED_DIRS for part in parts[:-1]):
        return False
    name = parts[-1]
    return name not in EXCLUDED_FILES and (not name.startswith(".env") or name.endswith(".example"))


def main() -> None:
    BACKUPS.mkdir(exist_ok=True)
    timestamp = datetime.now().strftime("%Y-%m-%d_%H%M%S")
    target = BACKUPS / f"MEE_Codex_{timestamp}.zip"
    with ZipFile(target, "w", ZIP_DEFLATED, compresslevel=8) as archive:
        for path in sorted(ROOT.rglob("*")):
            if path.is_file() and not path.is_symlink() and include(path):
                archive.write(path, Path(ROOT.name) / path.relative_to(ROOT))
    with ZipFile(target) as archive:
        bad_file = archive.testzip()
        if bad_file:
            raise RuntimeError(f"El respaldo contiene un archivo dañado: {bad_file}")
        print(f"Respaldo creado: {target} ({len(archive.namelist())} archivos)")


if __name__ == "__main__":
    main()
