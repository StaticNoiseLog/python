import numpy as np
import matplotlib.pyplot as plt
from scipy import interpolate
import sympy as sym

x = sym.symbols('x')

print("Use SymPy syntax: x-1, x*2, sqrt(x), exp(x), x**2, etc.")
function_string = input("Function of x [x**3 - 3*x**2]: ").strip()
if not function_string:
    function_string = 'x**3 - 3*x**2'

function_sympy = sym.sympify(function_string)
function_lambda = sym.lambdify(x, function_sympy, "numpy")

support_points_x = np.r_[-5:5:10j]
support_points_y = function_lambda(support_points_x)

# plot support points
plt.scatter(support_points_x, support_points_y, c="k")

x_axis = np.r_[-5:5:200j]

# plot original function
y_values = function_lambda(x_axis)
plt.plot(x_axis, y_values, label=function_string + " [original]")

# plot interpolated graphs
for kind in ['nearest', 'zero', 'slinear', 'linear', 'quadratic', 'cubic']:
    function_interpolated = interpolate.interp1d(
        support_points_x, support_points_y, kind=kind)
    y_values_interpolated = function_interpolated(x_axis)
    plt.plot(x_axis, y_values_interpolated, label=kind)

plt.legend()
plt.show()
