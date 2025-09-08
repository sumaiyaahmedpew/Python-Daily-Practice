#36-EMployee Management
class Employee:
    company = "TechCorp"

    def __init__(self, name, emp_id, salary):
        self.name = name
        self.emp_id = emp_id
        self.salary = salary

    def show(self):
        return f"{self.name} (ID: {self.emp_id}), Salary: {self.salary}, Company: {Employee.company}"

    def compare(self, other):
        if self.salary > other.salary:
            return f"{self.name} earns more than {other.name}"
        elif self.salary < other.salary:
            return f"{other.name} earns more than {self.name}"
        else:
            return "Both earn the same"

    @classmethod
    def change_company(cls, new_name):
        cls.company = new_name

    @staticmethod
    def info():
        return "Employees are the backbone of the company"


if __name__ == "__main__":
    e1 = Employee("Sumaiya", 1, 50000)
    e2 = Employee("Tahsin", 2, 60000)

    print(e1.show())
    print(e2.show())
    print(e1.compare(e2))

    Employee.change_company("NextGenTech")
    print(e1.show())

    print(Employee.info())
