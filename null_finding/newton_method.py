from sympy import *
x = symbols('x')

f = 3*x**3 - 4
ff = diff(f, x)

val_prev = 0
val = 1.5

while abs(val - val_prev) > 0.00001:
    print(val)
    val_prev = val
    val = val_prev - f.subs(x, val)/ff.subs(x, val)

print(val)