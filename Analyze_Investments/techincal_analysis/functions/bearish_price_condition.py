
def bearish_price_condition(price, price_before, highest_price_before_30):
    if price > price_before and price > highest_price_before_30:
        return 1
    else:
        return 0
