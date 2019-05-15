""" Find a polynom that goes through given points.
For n+1 points you can always find exactly one polynom of degree n that
goes through all points.
"""
from sympy import *

x = symbols("x")
polynom = interpolate([(-1, 10), (2, 1), (3, 6)], x)
print(polynom)
