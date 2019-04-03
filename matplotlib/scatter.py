import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5, 6, 7, 8]
y = [5, 2, 4, 2, 1, 4, 5, 2]

# s is size of marker
plt.scatter(x, y, label='skitscat', color='g', marker='o', s=100)

plt.xlabel('x')
plt.ylabel('y')
plt.title('Scatter Plot')
plt.legend()

plt.show()
