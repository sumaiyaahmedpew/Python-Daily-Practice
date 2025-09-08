# student Management System

class Student:
    total_students = 0  

    def __init__(self, name, roll, marks):
        self.name = name
        self.roll = roll
        self.marks = marks
        Student.total_students += 1

    def show(self):
        return f"{self.name} ({self.roll}) - Marks: {self.marks}"

    def compare(self, other):
        if self.marks > other.marks:
            return f"{self.name} scored higher than {other.name}"
        elif self.marks < other.marks:
            return f"{other.name} scored higher than {self.name}"
        else:
            return "Both scored the same!"

    @classmethod
    def get_total_students(cls):
        return cls.total_students

    @staticmethod
    def info():
        return "This is a Student Management System"


if __name__ == "__main__":
    s1 = Student("Sumaiya", 101, 95)
    s2 = Student("Tahsin", 102, 90)

    print(s1.show())
    print(s2.show())
    print(s1.compare(s2))

    print("Total Students:", Student.get_total_students())
    print(Student.info())
