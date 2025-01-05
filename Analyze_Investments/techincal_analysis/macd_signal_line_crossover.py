

def find_most_recent_crossing(stock_df):
    for i in range(len(stock_df) - 1, 0, -1):
        crossing_date = stock_df.iloc[i]['datetime']
        if (crossing_date is not None and stock_df.iloc[i]['macd'] is not None and stock_df.iloc[i]['macd_signal'] is
                not
                None and
                stock_df.iloc[i - 1]['macd'] is not None and stock_df.iloc[i - 1]['macd_signal'] is not None):

            if (stock_df.iloc[i]['macd'] > stock_df.iloc[i]['macd_signal'] and stock_df.iloc[i - 1]['macd'] <=
                    stock_df.iloc[i - 1]['macd_signal']):
                return "macd_over_signal"
            elif (stock_df.iloc[i]['macd'] < stock_df.iloc[i]['macd_signal'] and stock_df.iloc[i - 1]['macd'] >=
                  stock_df.iloc[i - 1]['macd_signal']):
                return "signal_over_macd"
            else:
                continue

    return None


def check_most_recent_macd_crossing(stock_df):
    most_recent_crossing = find_most_recent_crossing(stock_df)

    if most_recent_crossing:
        return most_recent_crossing
    else:
        return None
