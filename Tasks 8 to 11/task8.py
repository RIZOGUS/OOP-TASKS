import csv

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_info(self):
        return f"Name: {self.name}, Age: {self.age}"

class Employee:
    def __init__(self, employee_id, position):
        self.employee_id = employee_id
        self.position = position

    def display_info(self):
        return f"Employee ID {self.employee_id}, Position: {self.position}"

class Staff(Person, Employee):
    def __init__(self, name, age, employee_id, position, department):
        Person.__init__(self, name, age)
        Employee.__init__(self, employee_id, position)
        self.department = department

    def additional_info(self):
        return f"department: {self.department}"

def read_employees(file_name):
    employees = []
    try:
        with open(file_name, mode='r', newline='') as file:
            reader = csv.reader(file)
            for row in reader:
                if row:
                    employees.append(Staff(row[0], row[1], row[2], row[3], row[4]))
    except FileNotFoundError:
        pass
    return employees

def save_employees(file_name, employees):
    with open(file_name, mode='w', newline='') as file:
        writer = csv.writer(file)
        for emp in employees:
            writer.writerow([emp.name, emp.age, emp.employee_id, emp.position, emp.department])

def add_employee(file_name, name, age, employee_id, position, department):
    employees = read_employees(file_name)
    new_employee = Staff(name, age, employee_id, position, department)
    employees.append(new_employee)
    save_employees(file_name, employees)

file_name = 'employees.csv'

add_employee(file_name, 'SAIF', '20', '013', 'Manager', 'SE')
add_employee(file_name, 'ALI', '25', '020', 'Engineer', 'IT')

employees = read_employees(file_name)
for emp in employees:
    print(emp.display_info())
    print(emp.additional_info())
