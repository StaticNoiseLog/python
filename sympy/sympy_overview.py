from sympy import *

x, t, z, nu = symbols('x t z nu')

# Make all further examples pretty print with unicode characters.
init_printing(use_unicode=True)

# derivative
print('derivative: ', diff(sin(x)*exp(x), x))

# integral
print('integral: ', integrate(exp(x)*sin(x) + exp(x)*cos(x), x))
print('integral: ', integrate(sin(x**2), (x, -oo, oo)))  # from -inf to +inf

# limes
print('limes: ', limit(sin(x)/x, x, 0))  # x -> 0

# solve equation
print('solve equation: ', solve(x**2 - 2, x))  # solutions: -sqrt(2), +sqrt(2)

# solve differential equation
y = Function('y')
print('solve differential equation: ',
      dsolve(Eq(y(t).diff(t, t) - y(t), exp(t)), y(t)))

# find eigenvalues of a matrix
print('eigenvalues: ', Matrix([[1, 2], [2, 2]]).eigenvals())

# rewrite Bessel function  in terms of spherical Bessel function
print('Rewrite as spherical Bessel function: ', besselj(nu, z).rewrite(jn))

# LATEX
print(latex(Integral(cos(x)**2, (x, 0, pi))))
