# problem_29_Prime & Fibonacci Analyzer with Lambda + FMR

from functools import reduce

def fibonacci_series(n):
    series = []
    a, b = 0, 1
    for _ in range(n):
        series.append(a)
        a, b = b, a + b
    return series

def is_prime(x):
    if x < 2:
        return False
    for i in range(2, int(x**0.5) + 1):
        if x % i == 0:
            return False
    return True

fib = fibonacci_series(10)
print("Fibonacci:", fib)

primes = list(filter(lambda x: is_prime(x), fib))
print("Prime Fibonacci:", primes)

squares = list(map(lambda x: x**2, fib))
print("Squares:", squares)

total = reduce(lambda a, b: a + b, fib)
print("Sum of Fibonacci:", total)
