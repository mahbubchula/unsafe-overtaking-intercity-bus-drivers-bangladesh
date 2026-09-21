# Contributing

This repository supports an academic thesis and associated human-participant research documentation. Contributions must preserve the approved research design and the provenance of every research instrument.

## Before contributing

- Do not add participant-level data, completed questionnaires, consent records, identifiers, confidential correspondence, credentials, or private research records.
- Do not change questionnaire content, response categories, recall periods, screening rules, eligibility requirements, analytical roles, or thesis claims without documented authorization from the researcher and, where applicable, the advisor or ethics process.
- Preserve original source files. Add a reviewed copy under the standardized path only after establishing which version is current.
- Do not describe a document as final, approved, ethics-authorized, administered, or translated unless supporting records establish that status.
- Keep the terms “overtaking-related near-crash,” “collision involvement,” and the specified recall periods unchanged.

## Proposed workflow

1. Create a focused branch.
2. Record the source document, its prior status, and the reason for change.
3. Make the smallest necessary change.
4. Run the repository and questionnaire validation scripts.
5. Review the Git diff for scientific-content changes, identifiers, credentials, and unintended binary replacements.
6. Obtain the required academic or administrative review before merging status-sensitive changes.

## Document provenance

For questionnaire, codebook, justification, and thesis updates, add an entry under `documentation/version-history/` that records:

- source filename and checksum;
- language;
- document status;
- relationship to the companion files;
- reviewer or authorizing record, when applicable;
- immutable commit SHA or release tag, when assigned.

Do not use Git history as the sole record of ethics authorization or instrument administration.

## Code contributions

Analysis code should be deterministic where practical, document its inputs and outputs, and avoid reading from restricted directories in automated workflows. Tests must use schema-only fixtures or explicitly synthetic technical fixtures that cannot be mistaken for study data. Do not generate illustrative respondent-level records or simulated research results in this repository.
