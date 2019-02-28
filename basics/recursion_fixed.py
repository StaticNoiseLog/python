def fac(n):
    if n == 1:
        return 1
    return n * fac(n - 1)


print("Factorial of 5: ", fac(5))
