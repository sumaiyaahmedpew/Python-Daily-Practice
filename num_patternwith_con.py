# problem_17 Number Pattern with Condition

N = int(input("Enter a number: "))

for i in range(1, N + 1):
    if i % 2 == 0:  
        continue
    if i % 13 == 0:  
        print("Stopping at", i, "since divisible by 13")
        break
    print("*" * i)
