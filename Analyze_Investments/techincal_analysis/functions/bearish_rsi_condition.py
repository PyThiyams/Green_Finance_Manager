
def bearish_rsi_condition(current_rsi, rsi_before, highest_rsi_before_previous):

    try:
        if rsi_before < current_rsi < highest_rsi_before_previous:
            return 1
        else:
            return 0
    except Exception as e:
        f"{e}"
        return 0
