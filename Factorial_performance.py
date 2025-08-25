# problem_31_Factorial Performance Comparison
import time
from functools import reduce

def fact_recursive(n):
    if n == 0 or n == 1:
        return 1
    return n * fact_recursive(n - 1)

def fact_reduce(n):
    return reduce(lambda a, b: a * b, range(1, n + 1), 1)

def compare(n):
    start = time.time()
    fact_recursive(n)
    end = time.time()
    print(f"Recursive factorial({n}) time: {end - start:.6f}s")

    start = time.time()
    fact_reduce(n)
    end = time.time()
    print(f"Reduce factorial({n}) time: {end - start:.6f}s")

compare(10)
compare(50)
compare(100)
