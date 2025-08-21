# problem_15 Prime Analyzer

from array import array
n = int(input("Enter a number: "))
primes = array('i')  

for num in range(2, n + 1):
    for i in range(2, num):
        if num % i == 0:
            break
    else:   
        primes.append(num)

print("Prime numbers up to", n, ":", primes.tolist())
print("Total primes:", len(primes))

if primes:
    print("Smallest prime:", primes[0])
    print("Largest prime:", primes[-1])

if n in primes:
    print(n, "is prime")
else:
    print(n, "is not prime")
