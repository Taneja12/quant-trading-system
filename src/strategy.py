import numpy as np

def ema_strategy(df):
    df["ema_signal"] = np.where(
        df["ema_5"] > df["ema_15"], 1, -1
    )
    df["trade_signal"] = df["ema_signal"] * df["regime_trade_allowed"]
    return df
