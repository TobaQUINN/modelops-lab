import os
import pandas as pd
from sklearn.model_selection import train_test_split


def preprocess_data(input_path: str, output_dir: str, test_size: float = 0.2, random_state: int = 42):
    # Load raw data
    df = pd.read_csv(input_path)
    print(f"Loaded raw data from {input_path}, shape: {df.shape}")

    # Drop ID column if present
    if "Id" in df.columns:
        df = df.drop(columns=["Id"])
        print("Dropped Id column to prevent leakage.")

    # Clean column names
    df.columns = [col.strip() for col in df.columns]

    # Split features and target
    X = df.drop(columns=["quality"])
    y = df["quality"]

    # Train/test split
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=test_size, random_state=random_state, stratify=y
    )
    print("Performed train/test split.")

    # Save processed data
    os.makedirs(output_dir, exist_ok=True)
    pd.concat([X_train, y_train], axis=1).to_csv(
        os.path.join(output_dir, "train.csv"), index=False)
    pd.concat([X_test, y_test], axis=1).to_csv(
        os.path.join(output_dir, "test.csv"), index=False)
    print(f"Processed data saved to {output_dir}")


if __name__ == "__main__":
    preprocess_data("data/raw/WineQT.csv", "data/processed")
