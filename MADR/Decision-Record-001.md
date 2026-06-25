# Decision Record 001: Project Structure and EDA Approach

-Status: Accepted
-Date: 2026-06-24

## Context and Problem Statement
I need a clear and maintainable project structure, and how to properly handle Exploratory Data Analysis without including it with the producution code

## Decision Drivers
- Maintainability, Reproducibility, and Clarity
- Seperation of concerns (exploration vs. production)
- Professional porfolio standards :)
- Replication (That's why I named it modelops-lab instead of wine-quality-ml)

## Considered Options
1. Flat structure with all scripts and notebooks in one folder
2. Structured hierarchy with dedicated folders for data(raw and preprocessed), source code, models for saved pkl models, and app for the streamlit app with EDA a jupyter notebook

## Decision Outcome
Chosen option: **Structured hierarchy with EDA in Jupyter notebooks, production code in Python scripts**

## Pros and Cons of Options
- **Flat structure and EDA in scripts**
✅ Simple to set up
❌ May be confusing for larger projects, and less neat.


**Structured hierarchy**
✅ Clear separation of responsibilities
✅ Easier collaboration and scaling
❌ Slightly more setup effort.(Though did most of it in the terminal)


## Links and References
nil