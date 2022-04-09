import sympy as sym
import numpy as np


def calc(f, n):
    ll = sym.lambdify(x, f, "numpy")
    da_range = np.arange(0, 1, (1-0)/n)[1:]
    results = list(map(ll, da_range))
    # print(results)
    return sum(results) / n


x = sym.symbols('x')

print("wuff ", np.arange(1, 4))

f = -x**2 + 1

calc(f, 2)
print(calc(f, 1))
print(calc(f, 2))
print(calc(f, 3))
print(calc(f, 4))
print(calc(f, 5))
print(calc(f, 6))
print(calc(f, 12))
print(calc(f, 24))
print(calc(f, 48))
print(calc(f, 96))
