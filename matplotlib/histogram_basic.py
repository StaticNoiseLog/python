import matplotlib.pyplot as plt

population_ages = [22, 55, 62, 45, 21, 22, 34, 42, 42,
                   4, 99, 102, 11, 55, 30, 66, 72, 12, 22, 41, 58, 81]

bins = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110]
plt.hist(population_ages, bins, histtype='bar', rwidth=0.8)

plt.xlabel('x')
plt.ylabel('y')
plt.title('Histogram')

plt.show()
