delta = 5
start = 1
n = 20

sum = 1
for x in range(start, n):
    next = 1 + x*delta
    print("next: ", next)
    sum += next

print("SUM == ", sum)