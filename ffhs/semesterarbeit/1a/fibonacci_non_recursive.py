"""Uses the fact that we only need the two preceding numbers, no need to cache the entire sequence.
See https://avikdas.com/2019/04/15/a-graphical-introduction-to-dynamic-programming.html 
"""


def fib(n):
    a = 1  # f(i - 2)
    b = 1  # f(i - 1)
    for i in range(2, n + 1):  # end of range is exclusive
        # the old "a" is no longer accessible after this
        print(a)
        a, b = b, a + b
    return b


max_fibonacci = int(input("Fibonacci numbers for range 0 to "))

print(fib(max_fibonacci))
