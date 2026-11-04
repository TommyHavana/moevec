"""Stage text exports before replacing existing files, preserving them on ENOSPC."""
import os
import tempfile
from pathlib import Path


def atomic_export(exports):
    staged = []
    try:
        for destination, text in exports:
            destination = Path(destination)
            descriptor, temporary = tempfile.mkstemp(prefix='.' + destination.name + '.', suffix='.tmp', dir=destination.parent)
            temporary = Path(temporary)
            staged.append((temporary, destination))
            with os.fdopen(descriptor, 'w', encoding='utf-8', newline='') as stream:
                stream.write(text)
                stream.flush()
                os.fsync(stream.fileno())
            os.chmod(temporary, destination.stat().st_mode & 0o777 if destination.exists() else 0o644)
        # Every complete export exists before the first previous version is replaced.
        for temporary, destination in staged:
            os.replace(temporary, destination)
    finally:
        for temporary, _ in staged:
            if temporary.exists():
                temporary.unlink()
