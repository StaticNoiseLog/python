from sympy import *
x = symbols('x')
#f = 1./3.*x**3+4*x**2+5
#f = (x**2+1)**1000
#f = 1/sin(x)
f = 10 * (4**x)
e = diff(f, x)
print(f)
print()
print(e)
