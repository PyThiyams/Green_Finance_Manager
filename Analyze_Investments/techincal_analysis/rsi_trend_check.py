

def rsi_trend_check(stock_df):
    last_candle = stock_df.iloc[-1]
    previous_candle = stock_df.iloc[-2]
    candle_before_previous_candle = stock_df.iloc[-3]

    last_candle_rsi = last_candle['rsi']
    previous_candle_rsi = previous_candle['rsi']
    candle_before_previous_candle_rsi = candle_before_previous_candle['rsi']

    if last_candle_rsi > previous_candle_rsi > candle_before_previous_candle_rsi:

        return "rsi_uptrend"

    elif last_candle_rsi < previous_candle_rsi < candle_before_previous_candle_rsi:

        return "rsi_downtrend"

    else:

        return None
