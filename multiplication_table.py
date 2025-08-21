# problem_21 Multiplication Table Manager

while True:
    n = int(input("\nEnter a number for multiplication table (negative to exit, 0 to skip): "))

    if n < 0:
        print("Exiting program...")
        break

    elif n == 0:
        print("Skipping... (pass used)")
        pass  
        continue

    else:
        print(f"\nMultiplication Table of {n}")
        for i in range(1, 11):
            print(f"{n} x {i} = {n * i}")
