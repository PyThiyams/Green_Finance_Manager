import pandas as pd


def get_bullish_prices_and_rsi_from_df(df, current_date):

    current_date = pd.to_datetime(current_date)

    matching_row = df[df['datetime'] == current_date]

    current_index = matching_row.index[0]

    current_price = df.at[current_index, 'low']

    current_rsi = df.at[current_index, 'rsi']

    if current_index > 0:
        price_before = df.at[current_index - 6, 'low']
        rsi_before = df.at[current_index - 6, 'rsi']
        before_date = df.at[current_index - 6, 'datetime']
    else:
        price_before = current_price
        rsi_before = current_rsi
        before_date = current_date

    if current_index > 1:

        min_rsi_index = df['rsi'].iloc[max(0, current_index - 31):current_index - 6].idxmin()

        lowest_price_before_previous = df.at[min_rsi_index, 'low']

        lowest_before_previous_date = df.at[min_rsi_index, 'datetime']

        lowest_rsi_before_previous = df.at[min_rsi_index, 'rsi']

    else:

        lowest_price_before_previous = current_price

        lowest_before_previous_date = current_date

        lowest_rsi_before_previous = current_rsi

    return current_index, current_price, price_before, lowest_price_before_previous, current_rsi, rsi_before, \
        lowest_rsi_before_previous, current_date, before_date, lowest_before_previous_date
