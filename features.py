import CANSLIM


def current_earning_growth_grater_than_15_percent(start, end, symbol):
    return CANSLIM.feature_c(start, end, symbol, 0.15)


