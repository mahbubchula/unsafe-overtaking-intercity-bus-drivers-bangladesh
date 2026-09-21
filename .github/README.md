<div align="center">

![Unsafe overtaking research banner](../assets/thesis-banner.svg)

# Unsafe Overtaking among Professional Intercity Bus Drivers in Bangladesh

[![Research status](https://img.shields.io/badge/status-questionnaire%20review-7C3AED?style=for-the-badge&labelColor=312E81)](#-research-status)
[![Questionnaire](https://img.shields.io/badge/questionnaire-45%20coded%20items-059669?style=for-the-badge&labelColor=064E3B)](#-research-at-a-glance)
[![Languages](https://img.shields.io/badge/languages-English%20%7C%20Bangla-DC2626?style=for-the-badge&labelColor=7F1D1D)](#-research-documents)
[![Framework](https://img.shields.io/badge/framework-Bayesian%20%2B%20ML%20%2B%20XAI-0284C7?style=for-the-badge&labelColor=0C4A6E)](#-analytical-framework)
[![Data privacy](https://img.shields.io/badge/participant%20data-none-F59E0B?style=for-the-badge&labelColor=78350F)](#-privacy-first)

**A bilingual, privacy-conscious research repository for safer intercity transport.**

[Full project documentation](../README.md) • [Questionnaires](../questionnaire/) • [Codebook](../documentation/codebook/) • [Planned analysis](../analysis/) • [Reproducibility tools](../scripts/)

</div>

> [!IMPORTANT]
> **Repository preparation stage.** The available questionnaires and supporting documents are proposal-defense / expert-and-cognitive-review materials. They are not described as ethics-authorized, administered, or final instruments.

## 🌈 Research at a glance

| 🚌 Study | 🗺️ Coverage | 🧾 Instrument | 🧠 Planned analysis |
| --- | --- | --- | --- |
| Professional intercity bus drivers | Dhaka, Rajshahi, Khulna, Chattogram & Rangpur | 45 coded questions | Bayesian regression, ML validation & XAI |
| Cross-sectional survey | Bangladesh | English and Bangla, interviewer administered | SHAP, ALE & stability analysis |

## 🎯 Research objectives

1. Examine selected adjusted associations with self-reported unsafe-overtaking occurrence using Bayesian regression.
2. Develop, compare, and internally validate supervised machine-learning models.
3. Interpret fitted predictive models using SHAP, accumulated local effects, selected interactions, and explanation-stability analyses.

## 🧠 Analytical framework

The planned framework combines Bayesian logistic regression with regularized logistic regression, Random Forest, XGBoost, CatBoost, nested internal cross-validation, calibration analysis, SHAP, accumulated local effects, and explanation-stability assessment.

These methods are planned. This repository does not claim completed analyses, model performance, or study results.

## 🌐 Research documents

| Document | Format | Status |
| --- | --- | --- |
| English questionnaire | DOCX | 🟢 Review copy available |
| Bangla questionnaire | DOCX | 🟢 Review copy available |
| Master codebook | XLSX | 🟢 Editable source available |
| English item justification | DOCX | 🟢 Review copy available |
| Thesis source | LaTeX | 🟡 Awaiting source |

## 🛡️ Privacy first

No participant-level data are included. The repository excludes completed questionnaires, identifiers, employer-identifying information, confidential ethics correspondence, credentials, private research records, and restricted administrative documents.

## 🔎 Explore the repository

| Area | What you will find |
| --- | --- |
| [`questionnaire/`](../questionnaire/) | English and Bangla blank survey instruments |
| [`documentation/`](../documentation/) | Codebook, methodological justification, and version records |
| [`analysis/`](../analysis/) | Planned Bayesian, machine-learning, validation, and XAI workflows |
| [`scripts/`](../scripts/) | Validation and controlled synchronization utilities |
| [`thesis/`](../thesis/) | Structured location for future LaTeX thesis sources |
| [`README.md`](../README.md) | Full research, ethics, methods, and reproducibility documentation |

---

<sub>This `.github/README.md` is the visual landing page selected by GitHub. The root README contains the complete project documentation. GitHub workflows and issue templates in this folder must remain free of participant data and confidential credentials.</sub>
