def fib(n):
    """Naive implementation for Fibonacci sequence
    The number of recursive calls is counted with the global variable total_calls.
    """
    global total_calls
    total_calls += 1
    if n == 0 or n == 1:
        return n
    return fib(n - 1) + fib(n - 2)


max_fibonacci = int(input("Fibonacci numbers for range 0 to "))

for n in range(0, max_fibonacci + 1):
    total_calls = 0
    fib_n = fib(n)
    print("n: {0:3}    fib(n): {1:3}    total_calls: {2:4}".format(
        n, fib_n, total_calls))
