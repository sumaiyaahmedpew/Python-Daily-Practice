# problem_28 Recursive Math Utility

def factorial(n):
    if n < 0:
        return "Error: Negative number!"
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

def fibonacci(n):
    if n < 0:
        return "Error: Negative number!"
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

def sum_of_digits(n):
    if n < 0:
        return "Error: Negative number!"
    if n == 0:
        return 0
    return n % 10 + sum_of_digits(n // 10)

print("Factorial(5):", factorial(5))
print("Fibonacci(7):", fibonacci(7))
print("Sum of digits(1234):", sum_of_digits(1234))
