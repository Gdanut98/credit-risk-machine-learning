# Credit Risk Machine Learning

A graduate machine-learning portfolio project focused on credit-card default classification, preprocessing, model evaluation, and the practical consequences of class imbalance.

## Portfolio story
**Raw credit data → data-quality review → missing-value handling → preprocessing → train/test split → Logistic Regression → Random Forest comparison → confusion-matrix and ROC-AUC interpretation → deployment recommendation**

## Core analytical lessons
- Classification accuracy alone is insufficient when the default class is the business risk of interest.
- Missing and nonnumeric repayment-status values must be handled before scaling/modeling.
- Logistic Regression provides an interpretable baseline.
- Random Forest can capture nonlinear relationships and interactions that a linear log-odds model may miss.
- Recall for actual defaulters is a critical operational metric because false negatives represent missed risky accounts.

## Source-derived evidence
The original course notebook used an 80/20 train/test workflow. During model development, `PAY_1` required data-quality handling because it contained nonnumeric “Not available” values. A corrected confusion-matrix interpretation identified **4,716 true negatives and 1,284 false negatives** in one baseline result, illustrating a model that largely predicted the majority non-default class and missed actual defaults.

## Skills demonstrated
Python • Pandas • scikit-learn • Data Cleaning • Missing-Value Handling • Standardization • Logistic Regression • Random Forest • Confusion Matrix • Recall • F1 • ROC-AUC • Model Selection

## Repository structure
- `notebooks/original_coursework/` — executed graduate course evidence
- `src/` — reusable baseline modeling pipeline
- `docs/` — provenance, executable evidence, and evaluation guidance
- `portfolio/` — interview-ready project summary

## Evidence boundary
This repository packages graduate coursework for portfolio review. The original notebook is retained as course evidence; reusable code and documentation are portfolio extensions. Results should not be presented as a production credit-underwriting system.

## Portfolio navigation
- [George Danut — Analytics & BI Portfolio](https://gdanut98.github.io/GeorgeDanut.github.io/)
- [GitHub profile](https://github.com/Gdanut98)
