import os
import pandas as pd


def load_data(file_path: str) -> pd.DataFrame:
    """Load dataset from a CSV file."""
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Data file not found at {file_path}")

    try:
        df = pd.read_csv(file_path)
        print(f"Data successfully loaded from {file_path}")
        return df
    except Exception as e:
        raise RuntimeError(f"Error loading data: {e}")


def validate_data(df: pd.DataFrame, expected_columns: list) -> None:
    """Validate that dataframe has expected columns and no empty dataset."""
    if df.empty:
        raise ValueError("Loaded dataframe is empty.")

    missing_cols = [col for col in expected_columns if col not in df.columns]
    if missing_cols:
        raise ValueError(f"Missing expected columns: {missing_cols}")

    print("Data validation passed.")


def save_raw_data(df: pd.DataFrame, output_path: str) -> None:
    """Save dataframe to raw data folder."""
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    df.to_csv(output_path, index=False)
    print(f"Raw data saved to {output_path}")


if __name__ == "__main__":
    input_file = "WineQT.csv"
    output_file = "data/raw/WineQT.csv"
    expected_cols = ['fixed acidity', 'volatile acidity', 'citric acid', 'residual sugar',
                     'chlorides', 'free sulfur dioxide', 'total sulfur dioxide', 'density', 'pH',
                     'sulphates', 'alcohol', 'quality', 'Id']

    df = load_data(input_file)
    validate_data(df, expected_cols)
    save_raw_data(df, output_file)

# Did not run this script because i already had the dataset in the repository. Just did this to practice ingestation
# and hopefully soon will write for ingestation from other sources to practice my python skills
