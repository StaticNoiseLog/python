from numpy import r_
import matplotlib.pyplot as plt
from sympy import *

"""
Taylor polynomial of variable degree.
"""
x = symbols('x')
x_axis = r_[0:20:2000j]

original_function = log(x + 1) * sin(x)  # change function here
print('Taylor polynomial for: ', original_function)
original_function_lambda = lambdify(x, original_function, "numpy")
y_values_original_function = original_function_lambda(x_axis)
original_function_lambda = lambdify(x, original_function, "numpy")

while True:
    print('')

    degree_string = input(
        'Desired degree for Taylor polynomial (at least 2, <CR> to end): ').strip()
    if not degree_string:
        break
    try:
        degree = int(degree_string)
    except (ValueError) as bad_degree_string:
        print(bad_degree_string)
        continue
    if degree < 2:
        print('Degree must be 2 or higher...')
        continue

    plt.title("Taylor Polynomial of " + str(original_function))
    plt.plot(x_axis, y_values_original_function, label=original_function)

    taylor_series = original_function.series(x, 10, degree).removeO()
    print('Taylor polynomial (without Big-O): ', taylor_series)
    taylor_series_lambda = lambdify(x, taylor_series, "numpy")
    y_values_taylor_series = taylor_series_lambda(x_axis)
    plt.plot(x_axis, y_values_taylor_series,
             label="Taylor polynomial, degree " + str(degree))

    plt.legend()
    plt.show()

print('Program ending...')
