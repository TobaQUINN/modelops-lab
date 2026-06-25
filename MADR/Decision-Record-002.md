# Decision Record: Training Multiple Supervised Models

- Status: Accepted
- Date: 2026-06-24

## Context and Problem Statement
I want to build an end-to-end ML system using the Wine Quality dataset. The goal for me is to learn supervised learning algorithms through implementation, while applying basic MLOps practices (DVC, MLflow, Git).

## Decision Drivers
- Breadth of learning across common supervised models
- Demonstrating basic MLOps practices in a portfolio project
- Clear documentation of my thought process
- Deployability in an interactive web app

## Considered Options
1. Train only one model (I initially wanted to use this avenue to learn Random Forest properly using logistic regression as the baseline model)
2. Train a small subset of models (e.g., Logistic Regression + XGBoost)
3. Train all common supervised models (Logistic Regression, Decision Tree, Random Forest, XGBoost, SVM, KNN)[I also recognize that it would take time to go with this approach, so patience it is!]

## Decision Outcome
Chosen option: **Train all common supervised models**

## Pros and Cons of Options
- I think this would be helpful for me, because i am leveraging the time it would take to initialize another project to learn another supervised learning algorithm.

## Deployment Consideration
I will deploy all models in a Streamlit app:
- Input interface: user provides wine features and selects model
- Output: prediction from chosen model
- Comparison interface: metrics and SHAP explanations across models
- Optional: Claude API integration for natural language explanations

## Links / References
- [MLflow Documentation](https://mlflow.org/docs/latest/index.html)

