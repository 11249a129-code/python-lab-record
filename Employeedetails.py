class Employee:
    def __init__(self, name, emp_id, department, salary):
        self.name = name
        self.emp_id = emp_id
        self.department = department
        self.salary = salary

    def update_salary(self, department, increment):
        if self.department == department:
            self.salary += increment

    def display(self):
        print(f"Name: {self.name}, ID: {self.emp_id}, Dept: {self.department}, Salary: {self.salary}")

# Creating Employee objects
e1 = Employee("John", 101, "HR", 30000)
e2 = Employee("Sara", 102, "IT", 40000)
e3 = Employee("Mike", 103, "HR", 35000)

employees = [e1, e2, e3]

# Updating salary for HR department
print("\nBefore Salary Update:")
for emp in employees:
    emp.display()

for emp in employees:
    emp.update_salary("HR", 5000)

print("\nAfter Salary Update for HR Department:")
for emp in employees:
    emp.display()
