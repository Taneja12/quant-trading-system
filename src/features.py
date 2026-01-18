import pandas as pd

def add_ema(df, short=5, long=15):
    df[f"ema_{short}"] = df["spot_close"].ewm(span=short).mean()
    df[f"ema_{long}"] = df["spot_close"].ewm(span=long).mean()
    return df

def add_returns(df):
    df["spot_return"] = df["spot_close"].pct_change()
    return df
