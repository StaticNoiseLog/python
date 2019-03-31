import matplotlib.pyplot as plt
import numpy as npy

random_numbers = npy.random.randn(10000) # NumPy array with random numbers
plt.hist(random_numbers, bins=20, color="yellow", linewidth=2)
plt.title('Histogram of normally distributed random numbers')
plt.show()
