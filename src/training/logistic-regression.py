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

df = pd.read_csv("data/processed/train.csv")
