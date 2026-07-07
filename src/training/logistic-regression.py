# Training the Logistic Regression Model

# Data Loading
import pandas as pd

# Modeling, Metrics, Preprocessing
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, accuracy_score
from sklearn.preprocessing import StandardScaler

# Experiment tracking
import mlflow

# Saving Model
import joblib

from pathlib import Path


# Loading the data
BASE_DIR = Path(__file__).resolve().parent.parent.parent
DATA_DIR = BASE_DIR / "data" / "processed"

train = pd.read_csv(DATA_DIR / "train.csv")
test = pd.read_csv(DATA_DIR / "test.csv")

# Splitting features and target for train and test data
X_train = train.drop(columns=["quality"])
y_train = train["quality"]

X_test = test.drop(columns=["quality"])
y_test = test["quality"]

# Feature scaling using StandardScaler (Logistic Regression is sensitive to feature scale)
scaler = StandardScaler()

X_train_scaled = scaler.fit_transform(X_train)  # fit tranform on train data
X_test_scaled = scaler.transform(X_test)  # transform on test data

# Model Training
# Experiment tracking with MLflow
mlflow.set_experiment("Wine Quality Logistic Regression")

with mlflow.start_run():
    mlflow.log_param("random_state", 42)
    mlflow.log_param("max_iter", 1000)
    mlflow.log_param("class_weight", "balanced")
    mlflow.log_param("scaler", "StandardScaler")

    # Fit the model
    model = LogisticRegression(
        max_iter=1000, random_state=42, class_weight='balanced')
    model.fit(X_train_scaled, y_train)

    y_pred = model.predict(X_test_scaled)
    y_pred_proba = model.predict_proba(X_test_scaled)

    # Model evaluation and Log metrics
    accuracy = accuracy_score(y_test, y_pred)

    report = classification_report(
        y_test, y_pred,
        output_dict=True,
        zero_division=0
    )
    mlflow.log_metric("accuracy", accuracy)
    mlflow.log_metric("precision", report["weighted avg"]["precision"])
    mlflow.log_metric("recall", report["weighted avg"]["recall"])
    mlflow.log_metric("f1", report["weighted avg"]["f1-score"])

    # Log artifact
    mlflow.sklearn.log_model(model, name="logistic_regression_model")

MODEL_DIR = BASE_DIR / "models"
joblib.dump(model, MODEL_DIR / "logistic_regression.pkl")
