import math

upperlimit = int(input("Upper limit of sum: "))

n = 1
pi_approx = 0
while n < upperlimit:
    pi_approx += 4/((-1)**(n+1) * (2*n - 1))
    n += 1

print("pi_approx: ", pi_approx)
print("pi_actual: ", math.pi)
