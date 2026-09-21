#!/usr/bin/env python3
"""Perform read-only structural, privacy, and document-integrity checks."""

from __future__ import annotations

import argparse
import re
import subprocess
import sys
import zipfile
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

REQUIRED_DIRECTORIES = [
    "thesis/latex/chapters",
    "thesis/latex/appendices",
    "thesis/latex/frontmatter",
    "thesis/latex/bibliography",
    "thesis/latex/figures",
    "thesis/compiled",
    "questionnaire/english",
    "questionnaire/bangla",
    "documentation/codebook",
    "documentation/justification",
    "documentation/interviewer-guide",
    "documentation/methodology",
    "documentation/version-history",
    "analysis/data-preparation",
    "analysis/bayesian",
    "analysis/machine-learning",
    "analysis/explainable-ai",
    "analysis/validation",
    "analysis/reporting",
    "scripts",
    "environment",
    "releases",
    ".github/ISSUE_TEMPLATE",
    ".github/workflows",
]

REQUIRED_REPOSITORY_FILES = [
    "README.md",
    "CHANGELOG.md",
    "CONTRIBUTING.md",
    "CITATION.cff",
    ".gitignore",
    ".gitattributes",
    "LICENSE-NOTICE.md",
    "thesis/README.md",
    "analysis/README.md",
    "scripts/verify_repository.py",
    "scripts/verify_questionnaire.py",
    "scripts/generate_manifest.py",
    "environment/requirements.txt",
    "environment/requirements-dev.txt",
]

EXPECTED_RESEARCH_DOCUMENTS = [
    "thesis/latex/main.tex",
    "thesis/latex/bibliography/references.bib",
    "questionnaire/english/questionnaire-en.docx",
    "questionnaire/english/questionnaire-en.pdf",
    "questionnaire/bangla/questionnaire-bn.docx",
    "questionnaire/bangla/questionnaire-bn.pdf",
    "documentation/codebook/master-codebook.xlsx",
    "documentation/codebook/master-codebook.pdf",
    "documentation/justification/item-justification-en.docx",
    "documentation/justification/item-justification-en.pdf",
]

RESTRICTED_PREFIXES = (
    "data/raw/",
    "data/interim/",
    "data/processed/",
    "private/",
    "confidential/",
)

CREDENTIAL_NAMES = {
    ".env", "credentials.json", "secrets.json", "id_rsa", "id_ed25519"
}

APPENDIX_PATHS = [
    "questionnaire/english/questionnaire-en.pdf",
    "questionnaire/english/questionnaire-en.docx",
    "questionnaire/bangla/questionnaire-bn.pdf",
    "questionnaire/bangla/questionnaire-bn.docx",
    "documentation/codebook/master-codebook.xlsx",
    "documentation/codebook/master-codebook.pdf",
    "documentation/justification/item-justification-en.pdf",
]


def git_tracked_files() -> list[str]:
    result = subprocess.run(
        ["git", "-C", str(ROOT), "ls-files", "-z"],
        check=False,
        capture_output=True,
    )
    if result.returncode != 0:
        return []
    return [item.decode("utf-8") for item in result.stdout.split(b"\0") if item]


def readable_office_file(path: Path) -> tuple[bool, str]:
    suffix = path.suffix.lower()
    if suffix in {".docx", ".xlsx"}:
        try:
            with zipfile.ZipFile(path) as archive:
                bad = archive.testzip()
                if bad:
                    return False, f"damaged ZIP member: {bad}"
                required = "word/document.xml" if suffix == ".docx" else "xl/workbook.xml"
                if required not in archive.namelist():
                    return False, f"missing {required}"
        except (OSError, zipfile.BadZipFile) as exc:
            return False, str(exc)
    elif suffix == ".pdf":
        try:
            with path.open("rb") as stream:
                if stream.read(5) != b"%PDF-":
                    return False, "missing PDF header"
        except OSError as exc:
            return False, str(exc)
    return True, ""


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--allow-missing-documents",
        action="store_true",
        help="Treat unavailable thesis and instrument sources as warnings during preparation.",
    )
    args = parser.parse_args()
    errors: list[str] = []
    warnings: list[str] = []

    for relative in REQUIRED_DIRECTORIES:
        if not (ROOT / relative).is_dir():
            errors.append(f"Required directory is missing: {relative}")

    for relative in REQUIRED_REPOSITORY_FILES:
        path = ROOT / relative
        if not path.is_file():
            errors.append(f"Required repository file is missing: {relative}")
        elif path.stat().st_size == 0:
            errors.append(f"Required repository file is empty: {relative}")

    for relative in EXPECTED_RESEARCH_DOCUMENTS:
        path = ROOT / relative
        if not path.is_file():
            message = f"Research source is unavailable: {relative}"
            (warnings if args.allow_missing_documents else errors).append(message)
            continue
        if path.stat().st_size == 0:
            errors.append(f"Research source is empty: {relative}")
            continue
        readable, detail = readable_office_file(path)
        if not readable:
            errors.append(f"Research source is unreadable ({detail}): {relative}")

    tex_files = sorted((ROOT / "thesis/latex").rglob("*.tex"))
    if tex_files:
        combined = "\n".join(path.read_text(encoding="utf-8", errors="replace") for path in tex_files)
        for label in ("app:questionnaire", "app:ethics_materials"):
            if f"\\label{{{label}}}" not in combined:
                errors.append(f"LaTeX source does not define required label: {label}")
        for path_text in APPENDIX_PATHS:
            if path_text not in combined:
                warnings.append(f"LaTeX source does not mention expected appendix path: {path_text}")
    else:
        warnings.append("No LaTeX source was available for label, path, citation, or compile checks")

    tracked = git_tracked_files()
    for relative in tracked:
        lowered = relative.lower()
        if lowered.startswith(RESTRICTED_PREFIXES):
            errors.append(f"Tracked file is inside a restricted data directory: {relative}")
        basename = Path(lowered).name
        if basename in CREDENTIAL_NAMES or basename.endswith((".pem", ".p12", ".pfx")):
            errors.append(f"Possible credential file is tracked: {relative}")
        if basename.endswith(".key"):
            errors.append(f"Possible private key is tracked: {relative}")

    for filename, expected in {
        "questionnaire-en.docx": "questionnaire/english/questionnaire-en.docx",
        "questionnaire-en.pdf": "questionnaire/english/questionnaire-en.pdf",
        "questionnaire-bn.docx": "questionnaire/bangla/questionnaire-bn.docx",
        "questionnaire-bn.pdf": "questionnaire/bangla/questionnaire-bn.pdf",
    }.items():
        matches = [path.relative_to(ROOT).as_posix() for path in ROOT.rglob(filename)]
        unexpected = [item for item in matches if item != expected]
        if unexpected:
            errors.append(f"Ambiguous copies of {filename}: {', '.join(sorted(matches))}")

    public_url = re.compile(
        r"https?://github\.com/[^\s)]+/unsafe-overtaking-intercity-bus-drivers-bangladesh",
        re.IGNORECASE,
    )
    for path in ROOT.rglob("*"):
        if not path.is_file() or path.suffix.lower() not in {".md", ".tex", ".txt", ".cff", ".yml", ".yaml"}:
            continue
        text = path.read_text(encoding="utf-8", errors="replace")
        if public_url.search(text):
            warnings.append(
                f"Active GitHub repository URL requires owner and publication verification: {path.relative_to(ROOT)}"
            )

    for message in warnings:
        print(f"WARNING: {message}")
    for message in errors:
        print(f"ERROR: {message}", file=sys.stderr)
    print(f"Repository verification: {len(errors)} error(s), {len(warnings)} warning(s)")
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
