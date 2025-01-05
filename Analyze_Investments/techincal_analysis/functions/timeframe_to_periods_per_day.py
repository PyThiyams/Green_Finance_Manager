
def timeframe_to_periods_per_day(timeframe, trading_hours_per_day=6.5):
    # Debug statement to trace the input value
    # Extract the unit and value from the timeframe
    if timeframe[-2:] == 'MO':
        unit = 'MO'
        value = int(timeframe[:-2])  # The preceding characters represent the value
    else:
        unit = timeframe[-1]  # The last character represents the unit (D, H, M, W)
        value = int(timeframe[:-1])  # The preceding characters represent the value

    if unit == 'D':
        # Daily data
        return 1
    elif unit == 'H':
        # Hourly data, calculate periods based on trading hours
        return trading_hours_per_day // value
    elif unit == 'M':
        # Minute data, calculate periods based on minutes in trading hours
        minutes_per_day = trading_hours_per_day * 60
        return minutes_per_day // value
    elif unit == 'W':
        # Weekly data, assume 5 trading days per week
        return 5 // value
    elif unit == 'MO':
        # Monthly data, assume about 21 trading days per month
        return 21 // value
    else:
        raise ValueError("Unsupported timeframe format. Use 'D' for days, 'H' for hours, 'M' for minutes, "
                         "'W' for weeks, or 'MO' for month.")
