# problem_14 Pattern Printing Dashboard

while True:
    print("\n--- Pattern Printing Dashboard ---")
    print("1. Right-angle triangle")
    print("2. Pyramid")
    print("3. Diamond")
    print("0. Exit")

    choice = int(input("Enter choice: "))

    if choice == 0:
        print("Exiting...")
        break

    n = int(input("Enter number of rows: "))

    if choice == 1:
        for i in range(1, n + 1):
            print("*" * i)

    elif choice == 2:
        for i in range(1, n + 1):
            print(" " * (n - i) + "*" * (2 * i - 1))

    elif choice == 3:
        # Top half
        for i in range(1, n + 1):
            print(" " * (n - i) + "*" * (2 * i - 1))
        # Bottom half
        for i in range(n - 1, 0, -1):
            print(" " * (n - i) + "*" * (2 * i - 1))

    else:
        print("Invalid choice, try again...")
        continue
