import utils
from datetime import datetime
from tkinter import *
import features

START_DATE = '2005-01-01'
END_DATE = str(datetime.now().strftime('%Y-%m-%d'))
SAMPLE_STOCK = 'TM'
USA_STOCK_SYMBOL_LIST = utils.get_stock_symbol_USA_stock('resources/US-Stock-Symbols.xlsx')
USA_STOCK_SYMBOL_SP500 = utils.get_stock_symbol_sp_500('resources/SP_500.xlsx')
SAMPLE_LIST = utils.get_stock_symbol_sp_500('resources/sample.xlsx')


class Control(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent, v=None, raw_input=None)
        self.parent = parent
        self.parent.geometry("640x640+0+0")
        self.parent.title("Stock Screener")
        self.parent.resizable(False, False)
        self.inp = None
        self.v = StringVar()
        self.raw_input = None
        self.initUI()

    def analyze_stock_single(self):
        # Get entry1 value, store it as an attribute and print to console
        self.raw_input = symbol = self.v.get().upper()
        a, b1, b2, b3 = features.current_earning_growth_grater_than_15_percent(START_DATE, END_DATE, symbol)
        print(a, b1, b2, b3)
        if a:
            print(" ***　Current earning growth rate is greater than 15%!")
        if b1:
            print(" ******　Green sign #1: earnings are accelerating in recent quarters!")
        if b2:
            print(" ******　Green sign #1: net income are accelerating in recent quarters!")
        if b3:
            print(" ******　Green sign #1: gross profit are accelerating in recent quarters!")

    def initUI(self):
        self.frame = Frame(self, relief=RAISED, borderwidth=0)
        Label(self.frame, text="Analyze a stock symbol", font=("arial", 20, "bold")).pack()
        self.frame.pack(fill=BOTH, expand=True)
        self.entry1 = Entry(self.frame, textvariable=self.v)
        self.entry1.pack(side=TOP, fill=X, expand=False, padx=2, pady=2)
        self.entry1.focus_set()
        self.rename_button = Button(self.frame, text="Start", command=self.analyze_stock_single)
        self.rename_button.pack(side=TOP, expand=False, padx=2, pady=2)

        # root.title("Stock Screener")
        # root.geometry("640x640+0+0")
        # heading = Label(root, text="Welcome", font=("arial", 40, "bold"), fg="steelblue").pack()
        # label = Label(root, text="Enter a stock symbol: ", font=("arial", 16, "bold"), fg="black").place(x=10, y=200)
        # entry_box = Entry(root, textvariable=stock_symbol, width=25, bg="lightgreen").place(x=240, y=206)
        #
        # work = Button(root, text="Start", width=30, height=5, bg="blue", command=do_it()).place(x=250,y=300)
        # print(str(stock_symbol.get()))
        # root.mainloop()
        # print("START")
        # You can remove the triple quotes to display these widgets

        """
        self.entry2 = Entry(self.frame)
        self.entry2.pack(side=TOP, fill=X, expand=False, padx=2, pady=2)


        self.quit_button = Button(self.frame, text="Quit", command=self.quit)
        self.quit_button.pack(side=RIGHT, padx=5, pady=5)

        self.ok_button = Button(self.frame, text="OK")
        self.ok_button.pack(side=RIGHT, padx=5, pady=5)

        """
        self.pack(fill=BOTH, expand=True)


def main():
    root = Tk()
    app = Control(root)
    root.mainloop()


if __name__ == "__main__":
    main()


# def find_ca_symbols(list_symbol):
#     results = []
#     for symbol in list_symbol:
#         a1, s1, s2, s3 = CANSLIM.feature_c(START_DATE, END_DATE, symbol)
#         a2, s4, s5 = CANSLIM.feature_a(START_DATE, END_DATE, symbol)
#         if a1 is True and a2 is True:
#             results.append(symbol)
#             print(symbol, a1, s1, s2, s3, a2, s4, s5 )
#     return results
#
#
# def write_into_results(symbol_list):
#     workbook = xlsxwriter.Workbook('results/results.xlsx')
#     worksheet = workbook.add_worksheet()
#     # Add a bold format to use to highlight cells.
#     bold = workbook.add_format({'bold': 1})
#     # Adjust the column width.
#     worksheet.set_column(1, 1, 15)
#     # Write some data headers.
#     worksheet.write('A1', 'Symbol', bold)
#     worksheet.write('B1', 'Sample_1', bold)
#     worksheet.write('C1', 'Sample_2', bold)
#     # Start from the first cell below the headers.
#     row = 1
#     col = 0
#     for item in symbol_list:
#         worksheet.write_string(row, col, item)
#         row += 1
#     workbook.close()