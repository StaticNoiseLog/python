from math import pi
import sympy as sym
import numpy as np


def integrate_trapezoid_method(f, a, b, n):
    '''
    Numerical integration of definite integral from a to b of function f.
    Uses trapezoid rule (große Trapezregel), dividing the range [a, b]
    into n equal intervals.
    '''
    x_sigma_sum = np.arange(a, b, (b-a)/n)[1:]
    sigma_sum = sum(list(map(f, x_sigma_sum)))
    return ((f(a) + f(b))/2 + sigma_sum) * (b - a) / n


def integrate_simpson_method(f, a, b, n):
    '''
    Numerical integration of definite integral from a to b of function f.
    Uses Simpson formula (große Simpsonformel), dividing the range [a, b]
    into n*2 equal intervals.
    '''
    x_odd_indexes = np.arange(a, b, (b-a)/(2*n))[1::2]
    # print('x_odd_indexes', x_odd_indexes)
    sum_x_odd_indexes = sum(list(map(f, x_odd_indexes)))
    # print('sum_x_odd_indexes', sum_x_odd_indexes/(n-2))

    x_even_indexes = np.arange(a, b, (b-a)/(2*n))[0::2][1:]
    # print('x_even_indexes', x_even_indexes)
    sum_x_even_indexes = sum(list(map(f, x_even_indexes)))
    # print('sum_x_even_indexes', sum_x_even_indexes/(n-2))

    return (f(a) + f(b) + 2*sum_x_even_indexes + 4*sum_x_odd_indexes) * (b - a) / (6*n)


'''
Zwei Halbkreise integrieren als Rotationskoerper, dann Summe der beiden = Torus
r = Radius des kleinen Kreises des Toruskoerpers
R = Radius des Torus selbst (bis Mitte der Wurst)
sqrt(r**2 - x**2) + R

'''

x = sym.symbols('x')

f_sympy = -x**2 + 1
f = sym.lambdify(x, f_sympy, "numpy")


print('Trapezoid   4 intervals: ', integrate_trapezoid_method(f, 0, 1, 4))
print('Trapezoid  10 intervals: ', integrate_trapezoid_method(f, 0, 1, 10))
print('Trapezoid  80 intervals: ', integrate_trapezoid_method(f, 0, 1, 80))
print('Trapezoid 400 intervals: ', integrate_trapezoid_method(f, 0, 1, 400))

print('Simpson   4 intervals: ', integrate_simpson_method(f, 0, 1, 2))
print('Simpson  10 intervals: ', integrate_simpson_method(f, 0, 1, 5))
print('Simpson  80 intervals: ', integrate_simpson_method(f, 0, 1, 40))
print('Simpson 400 intervals: ', integrate_simpson_method(f, 0, 1, 200))

r = 0.5
R = 4
f_sympy = (sym.sqrt(r**2 - x**2) + R)**2  # halbkreis nach oben
f = sym.lambdify(x, f_sympy, "numpy")

halbkreis_oben = pi * integrate_simpson_method(f, -r, r, 100)

f_sympy=(-sym.sqrt(r**2 - x**2) + R)**2  # halbkreis nach oben
f=sym.lambdify(x, f_sympy, "numpy")

halbkreis_unten = pi * integrate_simpson_method(f, -r, r, 100)

torus = halbkreis_oben - halbkreis_unten
print('torus simpson', torus)



f_sympy = (sym.sqrt(r**2 - x**2) + R)**2  # halbkreis nach oben
f = sym.lambdify(x, f_sympy, "numpy")

halbkreis_oben = pi * integrate_trapezoid_method(f, -r, r, 100)

f_sympy=(-sym.sqrt(r**2 - x**2) + R)**2  # halbkreis nach oben
f=sym.lambdify(x, f_sympy, "numpy")

halbkreis_unten = pi * integrate_trapezoid_method(f, -r, r, 100)

torus = halbkreis_oben - halbkreis_unten
print('torus trapezoid', torus)
