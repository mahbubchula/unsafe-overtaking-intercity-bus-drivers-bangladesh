# Planned Analysis Workflow

This directory prepares the repository for future implementation of the approved methodology. It contains no respondent-level data, fitted models, performance estimates, figures, or completed research results.

## Workflow

1. **Data preparation** verifies import schemas, eligibility from A1–A6 and D1, missing-value codes, structural skips, and the UO1–UO5 outcome derivation.
2. **Bayesian analysis** will implement the approved Bayesian logistic-regression specification. The restricted primary model uses C2, D2, D3, E4, and F1, yielding six slope parameters because F1 separates delayed-trip exposure from conditional recovery pressure.
3. **Machine learning** will compare regularized logistic regression, Random Forest, XGBoost, and CatBoost for unsafe-overtaking occurrence.
4. **Validation** will use nested internal cross-validation and assess discrimination, calibration, and prediction error.
5. **Explainable AI** will use SHAP, accumulated local effects, selected interactions, and explanation-stability analyses.
6. **Reporting** will create traceable tables, manuscript figures, and reproducibility records after analyses are implemented and verified.

## Analytical boundaries

- S1 is collision involvement during the preceding 12 months.
- S2 is overtaking-related near-crash involvement during the preceding three months.
- S1 and S2 are exploratory safety-history measures, not primary machine-learning predictors.
- D1 establishes eligibility and is not a predictor within the screened analytical sample.
- Codes 95–99 are categorical missingness or inapplicability codes and must never be treated as numeric measurements.

Each subdirectory contains a scope note. Future executable code must follow the actual Chapter 3 methodology rather than treating this outline as a replacement for it.
