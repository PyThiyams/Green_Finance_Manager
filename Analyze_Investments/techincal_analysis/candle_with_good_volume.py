
def candle_with_good_volume(crossing_index, stock_df):

    total_data_points = 20

    last_candle = stock_df.loc[crossing_index]
    previous_volumes = stock_df['volume'].iloc[crossing_index-total_data_points:crossing_index]
    average_volume = sum(previous_volumes) / len(previous_volumes)

    if last_candle['volume'] > average_volume and last_candle['close'] > last_candle['open']:
        return "bullish_candle_with_good_volume", last_candle['volume']
    elif last_candle['volume'] > average_volume and last_candle['close'] < last_candle['open']:
        return "bearish_candle_with_good_volume", last_candle["volume"]
    else:
        return None, last_candle['volume']
