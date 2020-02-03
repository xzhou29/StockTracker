import pandas as pd
from pprint import pprint


def get_stock_list_symbol(file_name):
    results = []
    dfs = pd.read_excel(file_name, sheet_name=None)
    list_symbol = dfs['Sheet1']['Symbol']
    for symbol in list_symbol:
        rest = symbol.split('^', 1)[0]
        rest = rest.split('/', 1)[0]
        results.append(symbol)
    return results


def get_stock_symbol_sp_500(file_name):
    results = []
    dfs = pd.read_excel(file_name, sheet_name=None)
    list_symbol = dfs['Characteristics']['Ticker']
    for symbol in list_symbol:
        results.append(symbol)
    return results[:-2]


