"""
In order to load data with Numpy, you can use the functions
numpy.genfromtxt or numpy.loadtxt, where the difference is that
\np.genfromtxt can read CSV files with missing data and gives
you options like the parameters missing_values and filling_values
that help with missing values in the CSV.
"""
import matplotlib.pyplot as plt
import numpy as np

# unpack True makes the function return two unpacked values x and y
x, y = np.loadtxt('io/csv_data.csv', delimiter=',', unpack=True)

plt.plot(x, y, label='loaded from file')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Loading CSV Data')

plt.legend()
plt.show()
