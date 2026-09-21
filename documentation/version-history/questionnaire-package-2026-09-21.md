# Questionnaire Package Record 2026 09 21

## Status

The supplied documents identify themselves as proposal-defense / expert-and-cognitive-review materials. This record does not designate them as final, validated, ethics-authorized, piloted, or administered.

## Source mapping

| Supplied source | Repository path | SHA-256 |
| --- | --- | --- |
| `Questionnaire_EN (1).docx` | `questionnaire/english/questionnaire-en.docx` | `941a8697dfa9fae21f5976b6e057940dbded736c867c43139ed0117b897fd56a` |
| `Questionnaire_BN.docx` | `questionnaire/bangla/questionnaire-bn.docx` | `2677b544f2fb84fb4106b4431eafd10c23c30c18ae830d14a267d6eda9a2ad1d` |
| `Question_Justification.docx` | `documentation/justification/item-justification-en.docx` | `ccec8ea4496c10389bedff17fd47b378b9590ec18afa09de0358f8eccee6415a` |
| `Codebook.xlsx` | `documentation/codebook/master-codebook.xlsx` | `a5846963a9a56c212a6f4e53e90b21b066adf23b5c32f5527933b8a7ccb5ba95` |

Each repository copy matched its supplied source checksum after copying. The original files remain in the supplied Desktop folder.

## Structural verification

- The codebook Variable register contains exactly 45 item codes.
- Both questionnaire DOCX files contain all 45 codebook item codes.
- The administered-question sequence in both questionnaires begins A1–A6 followed immediately by D1.
- UO1–UO5, C2, D2, D3, E4, F1, S1, and S2 are present in both questionnaires and the codebook.
- The English questionnaire uses the term “overtaking-related near-crash” and does not use “near-collision” as the research-variable name.
- The codebook contains seven worksheets and remained editable; no worksheets, definitions, formatting, or formulas were replaced.

These checks establish code-level structural agreement. They do not establish complete English–Bangla semantic equivalence, content validity, ethics approval, or readiness for administration.

## Visual verification

The English questionnaire rendered as 21 pages and the item-justification document rendered as 18 pages without observed clipping, overlap, broken tables, or missing English glyphs.

The Bangla questionnaire contains 17,106 Bengali Unicode characters and specifies `Noto Serif Bengali`. That font was unavailable to the bundled headless renderer, causing Bengali glyphs to disappear from the QA preview. The original DOCX was preserved unchanged. Visual verification should be repeated in Microsoft Word or another environment with the specified font installed before review or field use.

## Missing companion files

No source PDFs were supplied for the English questionnaire, Bangla questionnaire, codebook, or item justification. No Bangla item-justification document was supplied. No PDF was generated automatically, because doing so in the current renderer would not provide a trustworthy Bangla output.

## Privacy and file-integrity checks

The four files contained no detected email addresses, telephone-number-like values, external relationships, or embedded macros. Their package metadata identified generic generation tools (`python-docx` or `openpyxl`) rather than a personal author. All seven codebook worksheets are visible. These automated checks reduce accidental-disclosure risk but do not replace human review before any publication.
