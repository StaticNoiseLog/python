import matplotlib.pyplot as plt

x = [1, 2, 3]
y = [5, 7, 4]

x2 = [1, 2, 3]
y2 = [10, 14, 12]

plt.plot(x, y, label='Plot 1')
plt.plot(x2, y2, label='Plot 2')

plt.xlabel('Plot Number')
plt.ylabel('Important Variable')
plt.title('Interesting Graph\n(Hackish Subtitle)')
plt.legend()

plt.show()
