# Decision Record 003: Approach to Preprocessing  III

-Status: Accepted
-Date: 2026-06-28

## Context and Problem Statement
After an extensive Exploratory Data Analysis, since the goal of this project was for me to understand the supervised learning algortihms, how to train them, understand what could go wrong and how to fix it, I would not be learning much if I decide to use a very clean data to train the models.

## Decision Drivers
- To understand how Machine Learning algorithms operate under the hoods
- To see how different supervised learning algorithms behave with datasets having outliers and correlated features
- Structured and intentional approach to preprocessing

## Considered Options
- Will not deal with outliers and correlated features in preprocessing, so that I can see how they affect different models in production

## Decision Outcome
incoming

## Insights
✅ Id dropped
✅ Train/test split done correctly with stratification (to prevent the silent danger of class imabalance)
✅ Class distribution checked and understood
✅ Outliers retained intentionally (baseline approach)
✅ Multicollinearity noted, deferred post-baseline
✅ Decisions documented in MADR