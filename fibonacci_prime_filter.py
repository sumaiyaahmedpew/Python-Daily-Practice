# problem_19 Fibonacci Prime Filter

from array import array

n = int(input("Enter how many Fibonacci numbers: "))
fib = [0, 1]
for i in range(2, n):
    fib.append(fib[-1] + fib[-2])

primes = array('i')

for num in fib:
    if num < 2:
        continue
    for i in range(2, num):
        if num % i == 0:
            break
    else: 
        primes.append(num)

print("Fibonacci numbers:", fib[:n])
print("Prime Fibonacci numbers:", primes.tolist())
