
def directional_indicator_check(stock_df, index):

    minus_di = stock_df.iloc[index]['mdi']

    plus_di = stock_df.iloc[index]['pdi']

    if minus_di < plus_di:

        return "plus_di_above_minus_di"

    elif minus_di > plus_di:

        return "minus_di_above_plus_di"

    else:

        return None
