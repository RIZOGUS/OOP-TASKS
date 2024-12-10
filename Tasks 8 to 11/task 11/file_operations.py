import csv
from manager import Manager
from worker import Worker

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
