from yahoofinancials import YahooFinancials
from pprint import pprint
import logging

# https://en.wikipedia.org/wiki/CAN_SLIM


def test(s, e, symbol):
    results = YahooFinancials(symbol)
    pprint(results.get_historical_price_data(s, e, "monthly"))


# C stands for Current quarterly earnings
# conditions:
# 1). current earnings should be up at least 25% in the most recent financial quarter
# 2). earnings are accelerating in recent quarters
def feature_c(start, end, symbol, growth_rate):
    try:
        up = True
        good_sign_1, good_sign_2, good_sign_3 = (True,) * 3
        yahoo = YahooFinancials(symbol)
        results = yahoo.get_financial_stmts('quarterly', 'income')
        key_data = yahoo.get_key_statistics_data()
        earnings_quarterly_growth = key_data[symbol]['earningsQuarterlyGrowth']
        if earnings_quarterly_growth < growth_rate:
            up = False
        print(symbol, ": ", earnings_quarterly_growth)
        index = 0
        total_revenue = []
        net_income = []
        gross_profit = []
        for r in results['incomeStatementHistoryQuarterly'][symbol]:
            for report in r:
                total_revenue.append(r[report]['totalRevenue'])
                net_income.append(r[report]['netIncome'])
                gross_profit.append(r[report]['grossProfit'])
                if index > 0:
                    if total_revenue[index - 1] < total_revenue[index]:
                        good_sign_1 = False
                    if net_income[index - 1] < net_income[index]:
                        good_sign_2 = False
                    if gross_profit[index - 1] < gross_profit[index]:
                        good_sign_3 = False
                index += 1
        # print(up, good_sign_1, good_sign_2, good_sign_3)
        return up, good_sign_1, good_sign_2, good_sign_3
    except Exception as e:
        logging.exception(e)
        return False, False, False, False


# A stands for Annual earnings growth
# up 25% or more over the last three years. Annual returns on equity should be 17% or more
def feature_a(start, end, symbol):
    try:
        up = True
        good_sign_1, good_sign_2, good_sign_3 = (True,) * 3
        yahoo = YahooFinancials(symbol)
        results = yahoo.get_stock_earnings_data()
        # pprint(results)
        current_earning = 0
        index = 0
        for r in results[symbol]['financialsData']['yearly']:
            if index == 0:
                current_earning = r['earnings']
            else:
                previous_earning = current_earning
                current_earning = r['earnings']
                if current_earning < previous_earning:
                    good_sign_1 = False
                    up = False
                elif current_earning < previous_earning * 1.25:
                    up = False
            index += 1
        index = 0
        for r in results[symbol]['financialsData']['quarterly']:
            if index == 0:
                current_earning = r['earnings']
            else:
                previous_earning = current_earning
                current_earning = r['earnings']
                if current_earning < previous_earning:
                    good_sign_2 = False
            index += 1
        # print(up, good_sign_1, good_sign_2)
        return up, good_sign_1, good_sign_2
    except Exception as e:
        logging.exception(e)
        return False, False, False

