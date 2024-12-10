from file_operations import read_employees, save_employees
from manager import Manager
from worker import Worker

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
