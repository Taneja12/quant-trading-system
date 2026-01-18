def compute_returns(df):
    df["strategy_return"] = df["trade_signal"].shift(1) * df["spot_return"]
    df["cum_strategy_return"] = (1 + df["strategy_return"]).cumprod()
    return df
