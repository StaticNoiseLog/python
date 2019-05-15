import sympy as sp
x = sp.Symbol('x')
y = sp.Symbol('y')  # lowercase works
# x, y = symbols('x y') # shortcut

x**2

sp.init_printing()  # generate solution in LaTex

x**2

(x**5).diff()
(x**5).diff(x)  # explicit

(x**3 * y**4).diff(y)

(x**3 + y**4).diff(x)

#f = 1./3.*x**3+4*x**2+5
f = (x**2+1)**1000
e = sp.diff(f, x)
print(f)
print(e)
