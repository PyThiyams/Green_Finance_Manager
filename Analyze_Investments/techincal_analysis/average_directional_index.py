def check_adx_greater_than_14(stock_df, index):
    last_adx_result = stock_df.iloc[index]['adx']
    if last_adx_result > 14:
        return "adx_greater_than_14"
    else:
        return None
