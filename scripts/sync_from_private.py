#!/usr/bin/env python3
"""Copy explicitly allowlisted files from the private thesis workspace."""

from __future__ import annotations

import argparse
import hashlib
import json
import shutil
import sys
from datetime import datetime
from pathlib import Path


DEFAULT_SOURCE = Path.home() / "Desktop/MS-Thesis"
DEFAULT_DESTINATION = Path.home() / "Desktop/MS-Thesis-GitHub"
BLOCKED_PARTS = {
    "01-administrative", "04-literature-review", "05-dataset",
    "correspondence", "confidential", "ethics", "interim", "pdfs",
    "private", "processed", "raw", "submissions",
}


def digest(path: Path) -> str:
    result = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            result.update(chunk)
    return result.hexdigest()


def inside(path: Path, root: Path) -> bool:
    try:
        path.resolve().relative_to(root.resolve())
        return True
    except ValueError:
        return False


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source-root", type=Path, default=DEFAULT_SOURCE)
    parser.add_argument("--destination-root", type=Path, default=DEFAULT_DESTINATION)
    parser.add_argument(
        "--allowlist",
        type=Path,
        default=Path(__file__).with_name("github-allowlist.json"),
    )
    parser.add_argument("--apply", action="store_true", help="Perform approved copies")
    parser.add_argument(
        "--replace",
        action="store_true",
        help="Replace differing destination files after preserving backups",
    )
    args = parser.parse_args()
    source_root = args.source_root.expanduser().resolve()
    destination_root = args.destination_root.expanduser().resolve()
    config = json.loads(args.allowlist.expanduser().read_text(encoding="utf-8"))
    mappings = config.get("mappings", [])
    if not mappings:
        raise SystemExit("Allowlist contains no mappings")

    errors: list[str] = []
    actions: list[tuple[Path, Path, str]] = []
    for entry in mappings:
        source_rel = Path(entry["source"])
        destination_rel = Path(entry["destination"])
        lowered_parts = {part.lower() for part in source_rel.parts}
        if source_rel.is_absolute() or destination_rel.is_absolute():
            errors.append(f"Absolute path rejected: {source_rel} -> {destination_rel}")
            continue
        if lowered_parts & BLOCKED_PARTS:
            errors.append(f"Restricted source path rejected: {source_rel}")
            continue
        source = source_root / source_rel
        destination = destination_root / destination_rel
        if not inside(source, source_root) or not inside(destination, destination_root):
            errors.append(f"Path traversal rejected: {source_rel} -> {destination_rel}")
            continue
        if source.is_symlink() or not source.is_file():
            errors.append(f"Allowlisted source is missing, not a file, or a symlink: {source_rel}")
            continue
        if destination.exists() and digest(source) == digest(destination):
            state = "unchanged"
        elif destination.exists():
            state = "replace-required"
        else:
            state = "copy"
        actions.append((source, destination, state))

    print("Selected GitHub files:")
    for source, destination, state in actions:
        print(
            f"- {source.relative_to(source_root)} -> "
            f"{destination.relative_to(destination_root)} [{state}]"
        )
    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1
    if not args.apply:
        print("Dry run only. No files were copied.")
        return 0

    backup_root = source_root / "Workspace-Tools/sync-backups"
    copied = 0
    for source, destination, state in actions:
        if state == "unchanged":
            continue
        if state == "replace-required" and not args.replace:
            print(f"ERROR: replacement requires --replace: {destination}", file=sys.stderr)
            return 1
        destination.parent.mkdir(parents=True, exist_ok=True)
        if destination.exists():
            flattened = "__".join(destination.relative_to(destination_root).parts)
            backup = backup_root / (
                datetime.now().strftime("%Y%m%d-%H%M%S--") + flattened
            )
            shutil.copy2(destination, backup)
        shutil.copy2(source, destination)
        if digest(source) != digest(destination):
            raise RuntimeError(f"Checksum verification failed: {destination}")
        copied += 1
    print(f"Copied {copied} file(s). No files were deleted, committed, or pushed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
