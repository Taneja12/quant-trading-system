def iv_proxy(df):
    """Simple IV proxy"""
    df["iv_proxy"] = df["avg_iv"]
    return df
