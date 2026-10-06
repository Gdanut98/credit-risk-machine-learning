# Model Evaluation

For credit default, evaluation should emphasize the minority/default class rather than aggregate accuracy alone.

- **Recall:** proportion of actual defaulters correctly identified. Low recall means risky accounts are missed.
- **Precision:** proportion of predicted defaulters that actually default.
- **F1:** balances precision and recall.
- **ROC-AUC:** measures ranking/discrimination across classification thresholds.
- **Confusion matrix:** makes the business consequences of false positives and false negatives explicit.

The course work demonstrated why a majority-class prediction pattern can appear superficially acceptable while providing poor default detection. Random Forest was considered valuable because nonlinear repayment interactions may improve discrimination relative to a linear baseline.
