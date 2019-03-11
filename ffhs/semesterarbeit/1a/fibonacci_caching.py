from fibonacci_module import fib_caching
from time import time

max_fibonacci = int(input("Fibonacci numbers for range 0 to "))

for n in range(0, max_fibonacci + 1):
    start_time = time()
    fib_n = fib_caching(n)
    elapsed_seconds = time() - start_time
    print("n: {0:3}    fib(n): {1:21}    elapsed seconds: {2}".format(
        n, fib_n, elapsed_seconds))
