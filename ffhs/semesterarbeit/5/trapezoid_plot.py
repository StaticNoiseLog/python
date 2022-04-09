import numpy as np
import matplotlib.pyplot as plt



def f(x): return 1/(1+x**2)

a = 0
b = 5
N = 10
n = 10  # Use n*N+1 points to plot the function smoothly

x = np.linspace(a, b, N+1)
y = f(x)

X = np.linspace(a, b, n*N+1)
Y = f(X)

plt.plot(X, Y)

for i in range(N):
    xs = [x[i], x[i], x[i+1], x[i+1]]
    ys = [0, f(x[i]), f(x[i+1]), 0]
    plt.fill(xs, ys, 'b', edgecolor='b', alpha=0.2)

plt.title('Trapezoid Rule, N = {}'.format(N))
plt.show()

