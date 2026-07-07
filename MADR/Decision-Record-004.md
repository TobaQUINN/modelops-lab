# Decision Record 004: Logistic Regression Model

- Status: Accepted
- Date: 07-07-2026

## Context and Problem Statement
The wine quality dataset has 6 quality classes (3-8) with significant 
class imbalance — classes 5 and 6 dominate with 483 and 462 samples 
respectively, while classes 3, 4, and 8 have only 6, 33, and 16 samples. 
A baseline supervised classification model is needed to predict wine 
quality from 11 physicochemical features.

## Decision Drivers
- Need a simple, interpretable baseline model before complex models
- Class imbalance must be observed in baseline before applying fixes
- Logistic regression coefficients provide insight into feature importance
- Linear model sensitivity to multicollinearity must be observed

## Considered Options
- Logistic Regression (selected)
- Decision Tree (deferred to next model)
- Random Forest (deferred)
- XGBoost (deferred)

## Decision Outcome
Logistic regression was selected as the first model because it is the 
simplest interpretable baseline. Key implementation decisions:

- StandardScaler applied — fit on training data only, transform on both train and test to prevent data leakage
- max_iter set to 1000 to ensure convergence on multiclass problem
- random_state=42 for reproducibility
- One vs Rest (OvR) strategy used — sklearn trains one binary classifier per class and selects the most confident prediction
- Outliers retained intentionally to observe their effect on model performance at baseline
- Id column dropped — meaningless row identifier with risk of spurious correlations and data leakage

## Insights
- Overall accuracy: 62% — misleading due to class imbalance
- Model completely failed on classes 3, 4, and 8 (F1 = 0.00) because it never predicted them — insufficient training samples
- Classes 5 and 6 performed reasonably (F1 = 0.74 and 0.61) because they had enough samples to learn from
- Accuracy alone is not a reliable metric for imbalanced multiclass problems — F1 score per class is more honest
- Multicollinearity effect on coefficients to be investigated after all baseline models are trained
- Addressed class imbalance using class_weight = 'balanced'