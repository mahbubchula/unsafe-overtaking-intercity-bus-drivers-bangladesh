#!/usr/bin/env python3
"""Generate a checksum manifest without reading file contents into output."""

from __future__ import annotations

import argparse
import csv
import hashlib
import subprocess
from datetime import datetime, timezone
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
EXCLUDED_PARTS = {".git", "__pycache__", ".pytest_cache", ".venv"}
RESTRICTED_PREFIXES = (
    "data/raw/",
    "data/interim/",
    "data/processed/",
    "private/",
    "confidential/",
)


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def tracked_paths() -> set[str]:
    result = subprocess.run(
        ["git", "-C", str(ROOT), "ls-files", "-z"],
        check=False,
        capture_output=True,
    )
    if result.returncode != 0:
        return set()
    return {item.decode("utf-8") for item in result.stdout.split(b"\0") if item}


def iter_files(output: Path):
    for path in sorted(ROOT.rglob("*")):
        if not path.is_file() or any(part in EXCLUDED_PARTS for part in path.parts):
            continue
        if path.resolve() == output.resolve():
            continue
        relative = path.relative_to(ROOT).as_posix()
        if relative.startswith(RESTRICTED_PREFIXES):
            continue
        yield path, relative


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--output",
        type=Path,
        default=ROOT / "documentation/version-history/repository-manifest.csv",
        help="Manifest destination; relative paths are resolved from the repository root.",
    )
    args = parser.parse_args()
    output = args.output if args.output.is_absolute() else ROOT / args.output
    output.parent.mkdir(parents=True, exist_ok=True)
    tracked = tracked_paths()

    with output.open("w", encoding="utf-8", newline="") as stream:
        writer = csv.DictWriter(
            stream,
            fieldnames=["path", "bytes", "sha256", "modified_utc", "git_tracked"],
            lineterminator="\n",
        )
        writer.writeheader()
        for path, relative in iter_files(output):
            stat = path.stat()
            writer.writerow(
                {
                    "path": relative,
                    "bytes": stat.st_size,
                    "sha256": sha256(path),
                    "modified_utc": datetime.fromtimestamp(
                        stat.st_mtime, tz=timezone.utc
                    ).isoformat(),
                    "git_tracked": "yes" if relative in tracked else "no",
                }
            )

    print(f"Wrote manifest: {output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
