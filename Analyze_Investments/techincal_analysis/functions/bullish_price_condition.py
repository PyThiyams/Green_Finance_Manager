
def bullish_price_condition(price, price_before, lowest_price_before_30):
    if price < price_before and price < lowest_price_before_30:
        return 1
    else:
        return 0
