# Unsafe Overtaking among Professional Intercity Bus Drivers in Bangladesh

Repository for the Master of Engineering thesis **Understanding and Predicting Unsafe Overtaking among Professional Intercity Bus Drivers in Bangladesh: An Integrated Bayesian and Explainable Machine Learning Framework**.

> **Document status:** Repository preparation stage. Proposal-defense / expert-and-cognitive-review copies of the English and Bangla questionnaires, the editable master codebook, and the English item-justification document were incorporated on 21 September 2026. They are review materials, not ethics-authorized or administered instruments. The thesis source remains unavailable. Ethics approval, recruitment, data collection, analysis completion, and publication are not claimed.

## Research information

| Item | Details |
| --- | --- |
| Student researcher | Mahbub Hassan |
| Degree | Master of Engineering (M.Eng.) |
| Field | Civil Engineering (Transportation Engineering) |
| Division | Transportation Engineering Division |
| Department | Department of Civil Engineering |
| Faculty | Faculty of Engineering |
| University | Chulalongkorn University, Bangkok, Thailand |
| Thesis advisor | Prof. Kasem Choocharukul |

## Research overview

This quantitative, cross-sectional study concerns professional intercity passenger-bus drivers in Bangladesh. The survey is designed for interviewer administration. The planned analytical sample is 450–550 drivers, with approximately 500 analyzable drivers as the working target. Recruitment locations are Dhaka, Rajshahi, Khulna, Chattogram, and Rangpur.

The questionnaire design comprises exactly 45 coded questions plus a separate informed-consent script. Eligibility is established from A1–A6 and D1, with D1 asked immediately after A6. The primary binary outcome is derived from UO1–UO5.

## Research objectives

1. Examine selected adjusted associations with self-reported unsafe-overtaking occurrence using Bayesian regression, with crash and near-crash history examined separately.
2. Develop, compare, and internally validate supervised machine-learning models for unsafe-overtaking occurrence.
3. Interpret the fitted predictive models using SHAP, accumulated local effects, selected interactions, and explanation-stability analyses.

## Analytical framework

The prespecified primary analytical core comprises C2, D2, D3, E4, and F1. These five source questions provide six slope parameters in the restricted Bayesian model. F1 distinguishes delayed-trip exposure from recovery pressure conditional on experiencing a delayed trip.

S1 measures collision involvement during the preceding 12 months. S2 measures overtaking-related near-crash involvement during the preceding three months. S1 and S2 are exploratory safety-history measures and are not primary machine-learning predictors. D1 is an eligibility variable and is not treated as a predictive variable within the screened analytical sample.

Planned methods include Bayesian logistic regression, regularized logistic regression, Random Forest, XGBoost, CatBoost, nested internal cross-validation, discrimination, calibration, prediction error, SHAP, accumulated local effects, prespecified interaction interpretation, and explanation-stability analysis. These methods are planned; this repository does not claim completed analyses or results.

## Repository structure

| Path | Purpose |
| --- | --- |
| `thesis/` | LaTeX thesis source, bibliography, figures, appendices, and compiled outputs |
| `questionnaire/` | Verified English and Bangla blank survey instruments |
| `documentation/codebook/` | Editable master codebook and review PDF |
| `documentation/justification/` | Item-level methodological justification |
| `documentation/interviewer-guide/` | Interviewer procedures and supporting material |
| `documentation/methodology/` | Method and reproducibility notes that do not replace Chapter 3 |
| `documentation/version-history/` | Instrument relationships, status records, and manifests |
| `analysis/` | Planned data preparation, modeling, validation, explanation, and reporting workflows |
| `scripts/` | Read-only repository and questionnaire validation utilities |
| `environment/` | Python dependency specifications |
| `releases/` | Release documentation; no release artifacts are currently claimed |

## Research documents and questionnaire versions

The following standardized paths identify the document package. Available source files are marked below:

- `questionnaire/english/questionnaire-en.docx` — available, review copy
- `questionnaire/english/questionnaire-en.pdf` — not supplied
- `questionnaire/bangla/questionnaire-bn.docx` — available, review copy
- `questionnaire/bangla/questionnaire-bn.pdf` — not supplied
- `documentation/codebook/master-codebook.xlsx` — available, editable source
- `documentation/codebook/master-codebook.pdf` — not supplied
- `documentation/justification/item-justification-en.docx` — available, review copy
- `documentation/justification/item-justification-en.pdf` — not supplied
- `documentation/justification/item-justification-bn.pdf`, only if a real translation exists

The available English and Bangla DOCX files and the codebook share the same 45-item code inventory. This structural agreement does not establish semantic translation equivalence or approval. No questionnaire version is designated final, approved, ethics-authorized, or administered. The relationship among the questionnaires, codebook, and justification document is tracked in `documentation/version-history/`.

## Data availability and privacy

This repository is intended for blank instruments, thesis source, nonconfidential documentation, and reusable analysis code. It must not contain raw or derived participant-level data, completed questionnaires, signed consent forms, direct identifiers, employer-identifying information, confidential ethics correspondence, credentials, or private research records. Restricted paths are excluded by `.gitignore`.

No participant data are currently included. Any future data-sharing decision must follow the applicable consent, ethics, institutional, legal, and data-governance requirements. De-identification alone does not establish that data may be made public.

## Ethics and document status

No ethics approval or authorization is claimed in this repository. The thesis must preserve the appendix labels `app:questionnaire` and `app:ethics_materials`. Repository links in the questionnaire appendix should remain inactive or explicitly pending until the repository owner, visibility, and archived instrument version are confirmed. The administered instrument should ultimately be cited using an immutable release tag or commit SHA.

## Reproducibility

The `analysis/` directory records the planned workflow without fabricating data, executable results, or performance estimates. Development dependencies are listed in `environment/requirements-dev.txt`. Run the local checks from the repository root:

```bash
python scripts/verify_repository.py
python scripts/verify_questionnaire.py
python scripts/generate_manifest.py --output documentation/version-history/repository-manifest.csv
```

The checks report missing or inconsistent materials and do not modify scientific content.

## Citation

Citation metadata are provided in `CITATION.cff`. Update the repository version and add an immutable repository URL only after the corresponding Git state and remote have been confirmed. Do not add a DOI or publication date unless one exists.

## Licensing

Copyright and reuse permissions may differ for thesis text, questionnaires, documentation, figures, and code. See `LICENSE-NOTICE.md`. No blanket open-source or open-content license is granted at this stage.

## Contributions and contact

See `CONTRIBUTING.md` before proposing a change. Scientific-content changes require documented review and must not alter the established research design silently. Project correspondence should use an institutionally appropriate channel supplied by the researcher; no private contact information is published here.
