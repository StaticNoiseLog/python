import math

epsilon = 0.00001

previous = -1
current = 0
n = 1
while current - previous > epsilon:
    previous = current
    current = math.sqrt(9 + (-1**n/n))
    print(current)
    n += 1