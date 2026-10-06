"""Reusable baseline for credit-default classification."""
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, roc_auc_score
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler


def build_logistic_pipeline(numeric_features, categorical_features):
    numeric = Pipeline([("imputer", SimpleImputer(strategy="median")), ("scale", StandardScaler())])
    categorical = Pipeline([("imputer", SimpleImputer(strategy="most_frequent")), ("encode", OneHotEncoder(handle_unknown="ignore"))])
    prep = ColumnTransformer([("num", numeric, numeric_features), ("cat", categorical, categorical_features)])
    return Pipeline([("prep", prep), ("model", LogisticRegression(max_iter=500))])


def evaluate(model, X_test, y_test):
    pred = model.predict(X_test)
    prob = model.predict_proba(X_test)[:, 1]
    print(classification_report(y_test, pred))
    print("ROC-AUC:", roc_auc_score(y_test, prob))
