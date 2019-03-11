import math

epsilon = 0.0000001

upperLimit = int(input("from 1 to: "))

for x in range(0, upperLimit):
    print(x, ": ", math.sin(x))
#    print(x, ": ", (-1)**x*2**x)
