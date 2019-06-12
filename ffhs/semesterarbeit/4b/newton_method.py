from sympy import *

x = symbols('x')

function_input_incomplete = True
while function_input_incomplete:
    try:
        print("Use SymPy syntax: x-1, x*2, sqrt(x), exp(x), x**2, etc.")
        function_string = input(
            "Enter a function of x [3*x**3 - 4]: ").strip()
        if not function_string:
            function_string = '3*x**3 - 4'
        function_sympy = sympify(function_string)
        function_input_incomplete = False
    except (AttributeError, SympifyError) as bad_input_error:
        print(bad_input_error)
        pass

function_sympy_first_derivative = diff(function_sympy, x)

epsilon_input_incomplete = True
while epsilon_input_incomplete:
    epsilon_string = input(
        'Epsilon criterion for ending iteration [0.00001]: ').strip()
    if not epsilon_string:
        epsilon_string = '0.00001'
    try:
        epsilon = float(epsilon_string)
        epsilon_input_incomplete = False
    except (ValueError) as bad_epsilon_string:
        print(bad_epsilon_string)
        continue

approximate_value_input_incomplete = True
while approximate_value_input_incomplete:
    approximate_value_string = input(
        'Starting approximate value [1.0]: ').strip()
    if not approximate_value_string:
        approximate_value_string = '1.0'
    try:
        approximate_value = float(approximate_value_string)
        validation = function_sympy_first_derivative.subs(x, approximate_value)
        if approximate_value == 0:
            print(approximate_value,
                  ' cannot be used as a starting value (causes divison by 0), choose something else')
        else:
            approximate_value_input_incomplete = False
    except (ValueError) as bad_approximate_value_string:
        print(bad_approximate_value_string)
        continue

approximate_value_prev = approximate_value - epsilon - 1
iterations_allowed = 100
while abs(approximate_value - approximate_value_prev) > epsilon:
    iterations_allowed -= 1
    if iterations_allowed < 0:
        break
    print(approximate_value)
    # Newton method
    approximate_value_prev = approximate_value
    approximate_value = approximate_value_prev - function_sympy.subs(
        x, approximate_value)/function_sympy_first_derivative.subs(x, approximate_value)

print('')
if iterations_allowed >= 0:
    print('Zero found at approximately: ', approximate_value)
else:
    print('Aborted, exceeded maximum number of iterations.')
