# problem_30_Student Grade System with Decorators

def logger(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print(f"[LOG] Called {func.__name__} with {args}, Result = {result}")
        return result
    return wrapper

@logger
def calculate_grade(marks):
    if marks >= 90:
        return "A+"
    elif marks >= 80:
        return "A"
    elif marks >= 70:
        return "B"
    elif marks >= 60:
        return "C"
    elif marks >= 50:
        return "D"
    else:
        return "Fail"

students = {"pew": 95, "tahsin": 72, "sumaiya": 40}

for name, mark in students.items():
    grade = calculate_grade(mark)
    print(f"{name}: {grade}")
