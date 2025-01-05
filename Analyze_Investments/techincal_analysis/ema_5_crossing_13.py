import pandas as pd
import numpy as np
from Analyze_Investments.techincal_analysis.functions.timeframe_to_periods_per_day import timeframe_to_periods_per_day
from Analyze_Investments.techincal_analysis.functions.get_last_ema_crossing import get_last_ema_crossing


def calculate_ema_5_and_ema_13(stock_df, timeframe):
    periods_per_day = timeframe_to_periods_per_day(timeframe)
    signal_df = pd.DataFrame()

    signal_df['datetime'] = stock_df['datetime']

    signal_df['Signal'] = 0.0

    signal_df['Signal'] = np.where(stock_df['ema_5'] > stock_df['ema_13'], 1.0, 0.0)

    signal_df['Position'] = signal_df['Signal'].diff()

    return signal_df, periods_per_day


def check_ema_5_crossing_13(current_date, stock_df, timeframe, days):

    if isinstance(current_date, str):
        current_date = pd.to_datetime(current_date)

    if 'datetime' not in stock_df.columns:
        print(f"Missing datetime column. DataFrame columns: {stock_df.columns}")
        return None, None

    signal_df, periods_per_day = calculate_ema_5_and_ema_13(stock_df, timeframe)
    x = int(periods_per_day * days)

    signal_df_filtered = signal_df[(signal_df['datetime'] > current_date)]

    if signal_df_filtered.empty:
        print(f"No data found after {current_date}")
        return None, None

    recent_crossings = signal_df_filtered['Position'].iloc[-x:]
    recent_crossings_list = [(index, value) for index, value in recent_crossings.items()]

    last_crossing_result, last_crossing_index = get_last_ema_crossing(recent_crossings_list)

    if last_crossing_result == "ema_crossing_above":
        return "ema_crossing_above_13", last_crossing_index
    elif last_crossing_result == "ema_crossing_below":
        return "ema_crossing_below_13", last_crossing_index
    else:
        return None, None
