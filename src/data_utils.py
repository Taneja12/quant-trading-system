import pandas as pd

def load_csv(path):
    """Load CSV with datetime parsing"""
    df = pd.read_csv(path)
    if "datetime" in df.columns:
        df["datetime"] = pd.to_datetime(df["datetime"])
    return df
