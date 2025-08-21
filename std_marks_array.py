# problem_16 Students Marks with Array
30
from array import array

n = int(input("Enter number of students: "))

if n == 0:
    pass  
else:
    marks = array('i', [])
    for i in range(n):
        m = int(input(f"Enter marks of student {i+1}: "))
        marks.append(m)

    print("\nMarks List:", marks.tolist())
    avg = sum(marks) / len(marks)
    print("Average marks:", avg)
    print("Highest marks:", max(marks))
    print("Lowest marks:", min(marks))

    for m in marks:
        if m < 40:
            print("One or more students failed. Stopping check...")
            break
