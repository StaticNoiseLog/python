# %%

import matplotlib.pyplot as plt


def f(n):
    return 2 * n ** 2 + 7 * n + 7


def g(n):
    return 6 * n + 4

X = range(1, 10)
plt.scatter(X, [f(n) for n in X], label='f(n)')
plt.scatter(X, [g(n) for n in X], label='g(n)')

plt.legend()
plt.show()
