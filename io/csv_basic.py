import matplotlib.pyplot as plt
import csv

x = []
y = []

with open('io/csv_data.csv', 'r') as csvfile:
    plots = csv.reader(csvfile, delimiter=',')
    for row in plots:
        x.append(int(row[0]))
        y.append(int(row[1]))

plt.plot(x, y, label='loaded from file')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Loading CSV Data')

plt.legend()
plt.show()
