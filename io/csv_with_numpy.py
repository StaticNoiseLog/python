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
