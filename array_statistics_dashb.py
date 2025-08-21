# problem_22 Array Statistics Dashboard

from array import array

n = int(input("Enter number of elements: "))
arr = array('i', [])

for i in range(n):
    val = int(input(f"Enter element {i+1}: "))
    arr.append(val)

while True:
    print("\n--- Array Dashboard ---")
    print("1. Show all elements")
    print("2. Separate Odd and Even")
    print("3. Find Prime Numbers")
    print("4. Reverse Array")
    print("5. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        print("Array elements:", arr.tolist())

    elif choice == 2:
        odd = [x for x in arr if x % 2 != 0]
        even = [x for x in arr if x % 2 == 0]
        print("Odd:", odd)
        print("Even:", even)

    elif choice == 3:
        primes = []
        for num in arr:
            if num < 2:
                continue
            for i in range(2, num):
                if num % i == 0:
                    break
            else:
                primes.append(num)
        print("Prime numbers:", primes)

    elif choice == 4:
        arr.reverse()
        print("Reversed Array:", arr.tolist())

    elif choice == 5:
        print("Exiting Dashboard...")
        break

    else:
        print("Invalid choice! Try again...")
