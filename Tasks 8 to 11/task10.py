import csv

class Employee:
    def __init__(self, name, age, salary):
        self.__name = name
        self.__age = age
        self.__salary = salary

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_age(self):
        return self.__age

    def set_age(self, age):
        self.__age = age

    def get_salary(self):
        return self.__salary

    def set_salary(self, salary):
        self.__salary = salary

class Manager(Employee):
    def __init__(self, name, age, salary, department):
        super().__init__(name, age, salary)
        self.__department = department

    def get_department(self):
        return self.__department

    def set_department(self, department):
        self.__department = department

class Worker(Employee):
    def __init__(self, name, age, salary, hours_worked):
        super().__init__(name, age, salary)
        self.__hours_worked = hours_worked

    def get_hours_worked(self):
        return self.__hours_worked

    def set_hours_worked(self, hours_worked):
        self.__hours_worked = hours_worked

def save_employees(file_name, employees):
    with open(file_name, mode='w', newline='') as file:
        writer = csv.writer(file)
        for emp in employees:
            if isinstance(emp, Manager):
                writer.writerow([emp.get_name(), emp.get_age(), emp.get_salary(), emp.get_department(), ""])
            elif isinstance(emp, Worker):
                writer.writerow([emp.get_name(), emp.get_age(), emp.get_salary(), "", emp.get_hours_worked()])

def read_employees(file_name):
    employees = []
    try:
        with open(file_name, mode='r', newline='') as file:
            reader = csv.reader(file)
            for row in reader:
                if row[3]:
                    employees.append(Manager(row[0], row[1], row[2], row[3]))
                elif row[4]:
                    employees.append(Worker(row[0], row[1], row[2], row[4]))
    except FileNotFoundError:
        pass
    return employees

def add_employee(file_name, employee):
    employees = read_employees(file_name)
    employees.append(employee)
    save_employees(file_name, employees)

def display_employees(file_name):
    employees = read_employees(file_name)
    for emp in employees:
        if isinstance(emp, Manager):
            print(f"name {emp.get_name()} age {emp.get_age()} salary {emp.get_salary()} department {emp.get_department()}")
        elif isinstance(emp, Worker):
            print(f"name {emp.get_name()} age {emp.get_age()} salary {emp.get_salary()} hours worked {emp.get_hours_worked()}")

def update_employee(file_name, name, attribute, value):
    employees = read_employees(file_name)
    for emp in employees:
        if emp.get_name() == name:
            if attribute == "name":
                emp.set_name(value)
            elif attribute == "age":
                emp.set_age(value)
            elif attribute == "salary":
                emp.set_salary(value)
            elif attribute == "department" and isinstance(emp, Manager):
                emp.set_department(value)
            elif attribute == "hours worked" and isinstance(emp, Worker):
                emp.set_hours_worked(value)
    save_employees(file_name, employees)

def delete_employee(file_name, name):
    employees = read_employees(file_name)
    employees = [emp for emp in employees if emp.get_name() != name]
    save_employees(file_name, employees)

file_name = 'employees.csv'

while True:
    print("1 add employee")
    print("2 display employees")
    print("3 update employee")
    print("4 delete employee")
    print("5 exit")
    choice = input("enter choice ")
    if choice == "1":
        emp_type = input("Enter type (Manager/Worker) ")
        name = input("Enter name: ")
        age = input("Enter age: ")
        salary = input("Enter salary: ")
        if emp_type == "manager":
            department = input("Enter department  ")
            add_employee(file_name, Manager(name, age, salary, department))
        elif emp_type == "worker":
            hours_worked = input("enter hours worked ")
            add_employee(file_name, Worker(name, age, salary, hours_worked))
    elif choice == "2":
        display_employees(file_name)
    elif choice == "3":
        name = input("enter name of the employee to update ")
        attribute = input("Enter attribute to update (name/age/salary/department/hours worked): ")
        value = input("enter new value: ")
        update_employee(file_name, name, attribute, value)
    elif choice == "4":
        name = input("enter name of the employee to delete ")
        delete_employee(file_name, name)
    elif choice == "5":
        break
