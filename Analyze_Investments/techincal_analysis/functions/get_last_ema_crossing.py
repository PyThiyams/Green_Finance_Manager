

def get_last_ema_crossing(recent_crossings):

    for index, crossing in reversed(recent_crossings):
        if crossing == 1:
            return "ema_crossing_above", index
        elif crossing == -1:
            return "ema_crossing_below", index

    return None, None
