import csv

with open('ElektrischeEnergieEinfuhrAusfuhr.csv',
          encoding='utf-8', errors='strict',  # insist on correct encoding
          newline=None) as csvfile:
    filereader = csv.reader(csvfile, delimiter=',', quotechar='|')
    data = [line for line in filereader]  # list comprehension forms 2D-list

for row in data:
    print("{0:10} {1:10} {2:10}".format(row[0], row[1], row[2]))
print()

user_input = input("Show data as bar chart? [Y]n: ")
if user_input.lower().startswith('n'):
    raise SystemExit(0)

############################################################################
# optional part: display data as bar chart                                 #
############################################################################

# deferred loading of libraries is non-standard, but saves time if user does
# not need the bar plot
import matplotlib.pyplot as plt
import numpy as np

data_years = [row[0].replace('"', '') for row in data[1:]]
data_ausfuhr = [int(row[1]) for row in data[1:]]
data_einfuhr = [int(row[2]) for row in data[1:]]

bars_count = len(data_ausfuhr)
index = np.arange(bars_count)
bar_width = 0.4

plt.xticks(rotation=90)

plt.bar(index - bar_width/2, data_ausfuhr,
        width=bar_width, color='b', label='Ausfuhr')

plt.bar(index + bar_width/2, data_einfuhr,
        width=bar_width, color='g', label='Einfuhr')

plt.xlabel(data[0][0].replace('"', ''))
plt.ylabel("GWh")

plt.title('Ausfuhr/Einfuhr elektrischer Energie in GWh')
plt.xticks(index, data_years)
plt.legend()

plt.tight_layout()
plt.show()
