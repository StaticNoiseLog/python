""" Stock Market Price Change Analysis
Reads a CSV file downloaded from Yahoo finance, e.g. https://finance.yahoo.com/quote/^GDAXI/history/.
Subsequent adjusted closing prices (the sixth field - position 5 - in the CSV file) are compared
and a value calculated that represents the increase or decrease of the market price in relation to
the previous closing day.
A histogram is displayed that shows the distribution of these changes: Big or small price jumps
from one day to the next.
"""
import numpy as np
import matplotlib.pyplot as plt
import csv
from tkinter import filedialog
from tkinter import Tk
import platform
from matplotlib.ticker import FormatStrFormatter

# navigate to CSV file with dialog unless it is Mac OS
if platform.system() != 'Darwin':
    root = Tk()
    root.filename = filedialog.askopenfilename(
        initialdir="", title="Select file", filetypes=(("CSV files", "*.csv"), ("all files", "*.*")))
    filename = root.filename
    root.destroy()
else:
    filename = 'DAX_DAILY_1996_2018.csv'  # workaround for Mac OS

# read CSV file with historic price data (Yahoo Finance format)
with open(filename,  # try with resources (file object closed automatically)
          encoding='utf-8', errors='strict',
          newline=None) as csvfile:
    filereader = csv.reader(csvfile, delimiter=',', quotechar='|')
    close_history_list = [float(line[5]) for line in filereader
                          if line[5].replace('.', '', 1).isdigit()]

close_history = np.array(close_history_list)

daily_price_changes = np.log(close_history[1:]/close_history[:-1])

bins = [-0.08, -0.07, -0.06, -0.05, -0.04, -0.03, -0.02, -0.01,
        0, 0.01, 0.02, 0.03, 0.04, 0.05, 0.06, 0.07, 0.08]

plt.rcParams["figure.figsize"] = (10, 4)  # display 10 inches wide, 4 high

plt.title('Histogram of daily price changes')
plt.hist(daily_price_changes,
         bins=bins,
         rwidth=0.8,
         color="blue")

plt.xticks(bins)

plt.tight_layout(rect=[0, 0.03, 1, 0.95])
plt.show()
