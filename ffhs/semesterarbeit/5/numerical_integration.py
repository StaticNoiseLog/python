'''
Demonstrates two numerical integration methods (trapezoid and Simpson) and compares
them to values calculated with SymPy.
'''
from math import pi
import sympy as sym
import numpy as np
import matplotlib.pyplot as plt


def integrate_trapezoid(f, a, b, n):
    '''
    Numerical integration of definite integral from a to b of function f.
    Uses trapezoid rule (große Trapezregel), dividing the range [a, b]
    into n equal intervals.

    Parameters
    ----------
    f : function
        The function to be integrated.
    a : number
        Lower bound of integral.
    b : number
        Upper bound of integral.
    n : number
        Count of intervals into which [a, b] is divided for approximation.

    Returns
    -------
    number
        Integral as approximated value.
    '''
    x_sigma_sum = np.arange(a, b, (b-a)/n)[1:]
    sigma_sum = sum(list(map(f, x_sigma_sum)))
    return ((f(a) + f(b))/2 + sigma_sum) * (b - a) / n


def integrate_simpson(f, a, b, n):
    '''
    Numerical integration of definite integral from a to b of function f.
    Uses Simpson formula (große Simpsonformel), dividing the range [a, b]
    into n*2 equal intervals.

    Parameters
    ----------
    f : function
        The function to be integrated.
    a : number
        Lower bound of integral.
    b : number
        Upper bound of integral.
    n : number
        Controls precision of approximation. The range [a, b] is divided into 2*n intervals.

    Returns
    -------
    number
        Integral as approximated value.
    '''
    x_odd_indexes = np.arange(a, b, (b-a)/(2*n))[1::2]
    sum_x_odd_indexes = sum(list(map(f, x_odd_indexes)))

    x_even_indexes = np.arange(a, b, (b-a)/(2*n))[0::2][1:]
    sum_x_even_indexes = sum(list(map(f, x_even_indexes)))

    return (f(a) + f(b) + 2*sum_x_even_indexes + 4*sum_x_odd_indexes) * (b - a) / (6*n)


def plot_f(title, f_sympy, f, lower_bound, upper_bound, margin=0):
    '''
    Helper function for plotting.
    '''
    x_axis = np.linspace(lower_bound - margin,
                         upper_bound + margin, int(margin * 100))
    plt.title(title)
    plt.plot(x_axis, f(x_axis), color='blue', linewidth=2, label=str(f_sympy))
    plt.grid(True)
    section = np.linspace(lower_bound, upper_bound, 100)
    plt.fill_between(section, f(section), color='red', alpha=0.2)
    plt.legend()
    return plt


def input_number(prompt, default=1, minimum=0, maximum=1000):
    '''
    Helper function for reading a number from standard input.
    '''
    number_incomplete = True
    while number_incomplete:
        number_string = input(prompt + ' [' + str(default) + ']: ').strip()
        if not number_string:
            number_string = str(default)
        try:
            number_value = float(number_string)
            if number_value < minimum:
                print(number_value, 'is below minimum', minimum)
            elif number_value > maximum:
                print(number_value, 'is above maximum', maximum)
            else:
                number_incomplete = False
        except (ValueError) as bad_number_string:
            print(bad_number_string)
            continue
    return number_value


def parabola(comment, f_integrate, n, f_parabola):
    '''
    Helper function for calculating and printing the definite integral of a parabola.
    '''
    print('{0} {1}: '.format(comment, n),
          f_integrate(f_parabola, -1, 1, n))


def torus(comment, f_integrate, n, f_concave, f_convex):
    '''
    Helper function for calculating and printing the volume of a torus.
    '''
    print('{0} {1}: '.format(comment, n),
          pi * f_integrate(f_concave, -r, r, n)
          - pi * f_integrate(f_convex, -r, r, n))


x = sym.symbols('x')

########################################################################
# A parabola as a simple case for testing.
########################################################################
f_parabola_sympy = -x**2 + 1
f_parabola = sym.lambdify(x, f_parabola_sympy, "numpy")

parabola_integral_sympy = sym.integrate(f_parabola_sympy, (x, -1, 1))

title = 'Area under curve {0} from -1 to 1'.format(f_parabola_sympy)
print(' ')
print(title)
print('-'*len(title))

print('SymPy: ', parabola_integral_sympy)

n_values_trapezoid = [4, 10, 80, 400]
list(map(lambda x: parabola('Parabola Trapezoid', integrate_trapezoid, x, f_parabola),
         n_values_trapezoid))

n_values_simpson = [2, 5, 40, 200]
list(map(lambda x: parabola('Parabola Simpson', integrate_simpson, x, f_parabola),
         n_values_simpson))

plot_f('Area under curve with SymPy: ' +
       str(parabola_integral_sympy), f_parabola_sympy, f_parabola, -1, 1, 0.5)
plt.show()


########################################################################
# Torus volume (solid of revolution)
########################################################################
print(' ')
r = input_number('Enter Torus Minor Radius r', 0.5, 0.1, 10)
R = input_number('Enter Torus Major Radius R', 4, 1, 20)

plt.figure('Two Solids of Revolution for Calculating a Torus Volume')

# First solid of revolution is defined by a concave semicircle.
f_semicircle_concave_sympy = sym.sqrt(r**2 - x**2) + R
f_semicircle_concave = sym.lambdify(x, f_semicircle_concave_sympy, "numpy")

volume_semicircle_concave_sympy = pi * \
    sym.integrate(f_semicircle_concave_sympy**2, (x, -r, r))

plt.subplot(1, 2, 1, title='Semicircle Concave')
plt.axis('equal')
plt.ylim(-0.5, R*1.3)
plot_f('Volume: ' + str(volume_semicircle_concave_sympy),
       f_semicircle_concave_sympy, f_semicircle_concave, -r, r)

# Second solid of revolution is defined by a convex semicircle.
f_semicircle_convex_sympy = -sym.sqrt(r**2 - x**2) + R
f_semicircle_convex = sym.lambdify(x, f_semicircle_convex_sympy, "numpy")

volume_semicircle_convex_sympy = pi * \
    sym.integrate(f_semicircle_convex_sympy**2, (x, -r, r))

plt.subplot(1, 2, 2, title='Semicircle Convex')
plt.axis('equal')
plt.ylim(-0.5, R*1.3)
plot_f('Volume: ' + str(volume_semicircle_convex_sympy),
       f_semicircle_convex_sympy, f_semicircle_convex, -r, r)

title = 'Volume of Torus with r={0} R={1}'.format(r, R)
print(' ')
print(title)
print('-'*len(title))

f_semicircle_concave_squared = sym.lambdify(
    x, f_semicircle_concave_sympy**2, "numpy")
f_semicircle_convex_squared = sym.lambdify(
    x, f_semicircle_convex_sympy**2, "numpy")

print('SymPy: ', volume_semicircle_concave_sympy - volume_semicircle_convex_sympy)

# Calculate and print torus volume with trapezoid method for n from 2^2 to 2^15.
n_values_trapezoid = list(map(lambda x: 2**x, np.arange(2, 16)))  # 2^2 to 2^15
list(map(lambda x: torus('Trapezoid', integrate_trapezoid, x,
                         f_semicircle_concave_squared, f_semicircle_convex_squared),
         n_values_trapezoid))

# Calculate and print torus volume with Simpson method for n from 2^1 to 2^14.
n_values_simpson = list(map(lambda x: 2**x, np.arange(1, 15)))  # 2^1 to 2^14
list(map(lambda x: torus('Simpson', integrate_simpson, x,
                         f_semicircle_concave_squared, f_semicircle_convex_squared),
         n_values_simpson))

plt.show()
