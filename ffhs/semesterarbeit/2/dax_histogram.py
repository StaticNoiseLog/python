""" Stock Market Rates Analysis
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

root = Tk()
root.filename = filedialog.askopenfilename(
    initialdir="", title="Select file", filetypes=(("CSV files", "*.csv"), ("all files", "*.*")))

with open(root.filename,  # try with resources (file object closed automatically)
          encoding='utf-8', errors='strict',
          newline=None) as csvfile:
    filereader = csv.reader(csvfile, delimiter=',', quotechar='|')
    adjusted_close_historic = [float(line[5]) for line in filereader
                               if line[5].replace('.', '', 1).isdigit()
                               ]

print(adjusted_close_historic)

closes = np.array(adjusted_close_historic)

the_differences = np.log(closes[1:]/closes[:-1])

print(the_differences)

fig, ax = plt.subplots()
counts, bins, patches = plt.hist(
    the_differences, bins=20, color="orange", linewidth=2)
ax.set_xticks(bins)

plt.title('Histogram of daily DAX price changes')
plt.show()
