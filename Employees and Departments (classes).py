class Department:
    count = 0
    def __init__(self, name):
        self.name = name
        self.count = 0
        self.employees = []

        Department.count += 1

    def add_employee(self, employee):
        self.employees.append(employee)
        self.count += 1

    def remove_employee(self, employee):
        self.employees.remove(employee)
        self.count -= 1

class Employee:
    count = 0
    def __init__(self, name, age, email):
        self.id = Employee.count
        self.name = name
        self.age = age
        self.email = email
        self.department = None

        Employee.count += 1

    def unassign(self):
        if self.department:
            self.department.remove_employee(self)
            self.department = None

    def assign_to(self, department):
        self.unassign()
        self.department = department
        self.department.add_employee(self)