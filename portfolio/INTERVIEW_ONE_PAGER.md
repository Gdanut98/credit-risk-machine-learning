# Interview One-Pager — Credit Risk Machine Learning

**Problem:** Identify customers at risk of default while avoiding misleading conclusions from an imbalanced target.

**Approach:** Clean repayment-status data, handle missing/non-numeric values, split train/test data, build an interpretable Logistic Regression baseline, compare a nonlinear Random Forest, and evaluate with confusion-matrix and ROC-AUC metrics.

**Key lesson:** Accuracy is not the decision metric when the costly class is rare. Default recall and the false-negative rate materially change the business interpretation.

**Technical evidence:** Python, pandas, scikit-learn, preprocessing, classification, model evaluation.

**Portfolio extension:** Repository structure and reusable baseline code were added after the original graduate analysis.
