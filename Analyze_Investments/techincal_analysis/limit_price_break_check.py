

def check_limit_price_break(crossing_index, stock_df):
    crossing_candle = stock_df.loc[crossing_index]
    crossing_high = crossing_candle["high"]
    crossing_low = crossing_candle["low"]

    last_candle = stock_df.iloc[-1]
    last_close = last_candle['close']

    if last_close > crossing_high:

        return "price_above_limit_high"

    elif last_close < crossing_low:

        return "price_below_limit_low"

    else:

        return None
