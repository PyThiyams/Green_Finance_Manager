
def price_50ema(stock_df, ltp, index):
    ema_value = stock_df.iloc[index]['ema_50']
    print("ema value:", ema_value)
    if ltp > ema_value:
        print("pass")
        return "price_above_50ema"

    elif ltp < ema_value:
        print("fail")
        return "price_below_50ema"

    else:

        return None
