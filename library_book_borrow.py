# problem_20 Library Book Borrow System

from array import array

books = []
n = int(input("How many books to add initially? "))
for i in range(n):
    name = input(f"Enter book {i+1} name: ")
    books.append(name)

while True:
    print("\n--- Library Menu ---")
    print("1. Show all books")
    print("2. Search book")
    print("3. Borrow book")
    print("4. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        print("Books:", books)

    elif choice == 2:
        title = input("Enter book to search: ")
        for b in books:
            if b.lower() == title.lower():
                print("Book found!")
                break
        else:
            print("Book not found.")

    elif choice == 3:
        title = input("Enter book to borrow: ")
        for b in books:
            if b.lower() == title.lower():
                books.remove(b)
                print("You borrowed:", b)
                break
        else:
            print("Book not available.")

    elif choice == 4:
        print("Exiting Library...")
        break

    else:
        print("Invalid choice, try again...")
        continue
