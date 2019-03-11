import math

part_sum_size = int(input("length of partial sum: "))

sum = 0

k = 2
while k <= part_sum_size:
    #    summand = 0.5**k
    #sum += 5*(-11/12)**(k-1)
    sum += 9**(1/k) - 9**(1/(k+1))
    #   print("summand: ", summand)
    #sum += 1/(k*(k+1))
    k += 1

print(k, "-te Partialsumme: ", sum)
#print(k, "-te Partialsumme VARIANTE B: ", (1/k - (1/(k+1))))
