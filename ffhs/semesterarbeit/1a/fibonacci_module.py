"""Module with Fibonacci functions
"""


def fib(n):
    """Naive implementation for Fibonacci sequence
    """
    if n == 0 or n == 1:
        return n
    return fib(n - 1) + fib(n - 2)


def fib_caching(n, cache={}):
    """This implementation for calculating a Fibonacci number
    caches the already calculated numbers.
    """
    cached_fibonacci_number = cache.get(n, None)
    if cached_fibonacci_number is not None:
        return cached_fibonacci_number
    if n == 0 or n == 1:
        cache[n] = n
        return n
    fibonacci_number = fib_caching(n - 1, cache) + fib_caching(n - 2, cache)
    cache[n] = fibonacci_number
    return fibonacci_number
