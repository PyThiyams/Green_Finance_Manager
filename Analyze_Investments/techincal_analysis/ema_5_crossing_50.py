import pandas as pd
import numpy as np
from functions.timeframe_to_periods_per_day import timeframe_to_periods_per_day
from functions.get_last_ema_crossing import get_last_ema_crossing


def calculate_ema_5_and_ema_50(stock_df, timeframe):

    periods_per_day = timeframe_to_periods_per_day(timeframe)

    signal_df = pd.DataFrame()

    signal_df['datetime'] = stock_df['datetime']
    signal_df['Signal'] = 0.0
    signal_df['Signal'] = np.where(stock_df['ema_5'] > stock_df['ema_50'], 1.0, 0.0)
    signal_df['Position'] = signal_df['Signal'].diff()

    return signal_df, periods_per_day


def check_ema_5_crossing_50(current_date, stock_df, timeframe, days):
    signal_df, periods_per_day = calculate_ema_5_and_ema_50(stock_df, timeframe)
    x = int(periods_per_day * days)

    signal_df_filtered = signal_df[(signal_df['datetime'] > current_date)]

    recent_crossings = signal_df_filtered['Position'].iloc[-x:]
    recent_crossings_list = []

    for index, value in recent_crossings.items():
        recent_crossings_list.append((index, value))

    last_crossing_result, last_crossing_index = get_last_ema_crossing(recent_crossings_list)

    if last_crossing_result == "ema_crossing_above" and (len(signal_df_filtered) - last_crossing_index) <= 5:
        return "ema_crossing_above_50", last_crossing_index
    elif last_crossing_result == "ema_crossing_below" and (len(signal_df_filtered) - last_crossing_index) <= 5:
        return "ema_crossing_below_50", last_crossing_index
    else:
        return None, None
