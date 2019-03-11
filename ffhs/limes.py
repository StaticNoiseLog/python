import math

epsilon = 0.0000000001

previous = -1
current = 0
n = 1
#while current - previous > epsilon:
while n < 1009:
    previous = current
    current = 1/n**3 + math.log10(n)/3628800
    #  current = math.sqrt(9 + (-1**n/n))
    print("n: ", n, "   -   ", current)
    n += 1