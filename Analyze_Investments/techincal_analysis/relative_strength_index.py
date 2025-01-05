
def check_rsi(stock_df, index):

    rsi_value = stock_df.iloc[index]['rsi']
    rsi_value = int(rsi_value)

    if rsi_value > 60:

        return "rsi_above_60"

    elif rsi_value < 40:

        return "rsi_below_40"

    else:

        return None
