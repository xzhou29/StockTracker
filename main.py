import CANSLIM
import utils
from datetime import datetime
import xlsxwriter
import xlrd

START_DATE = '2005-01-01'
END_DATE = str(datetime.now().strftime('%Y-%m-%d'))
SAMPLE_STOCK = 'TM'
USA_STOCK_SYMBOL_LIST = utils.get_stock_symbol_USA_stock('resources/US-Stock-Symbols.xlsx')
USA_STOCK_SYMBOL_SP500 = utils.get_stock_symbol_sp_500('resources/SP_500.xlsx')
SAMPLE_LIST = utils.get_stock_symbol_sp_500('resources/sample.xlsx')


def find_ca_symbols(list_symbol):
    results = []
    for symbol in list_symbol:
        a1, s1, s2, s3 = CANSLIM.feature_c(START_DATE, END_DATE, symbol)
        a2, s4, s5 = CANSLIM.feature_a(START_DATE, END_DATE, symbol)
        if a1 is True and a2 is True:
            results.append(symbol)
            print(symbol, a1, s1, s2, s3, a2, s4, s5 )
    return results


def write_into_results(symbol_list):
    workbook = xlsxwriter.Workbook('results/results.xlsx')
    worksheet = workbook.add_worksheet()
    # Add a bold format to use to highlight cells.
    bold = workbook.add_format({'bold': 1})
    # Adjust the column width.
    worksheet.set_column(1, 1, 15)
    # Write some data headers.
    worksheet.write('A1', 'Symbol', bold)
    worksheet.write('B1', 'Sample_1', bold)
    worksheet.write('C1', 'Sample_2', bold)
    # Start from the first cell below the headers.
    row = 1
    col = 0
    for item in symbol_list:
        worksheet.write_string(row, col, item)
        row += 1
    workbook.close()


write_into_results(find_ca_symbols(USA_STOCK_SYMBOL_LIST))
