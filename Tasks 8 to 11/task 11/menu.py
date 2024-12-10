from manager import Manager
from worker import Worker
from employee_operations import add_employee, display_employees, update_employee, delete_employee

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
        if emp_type.lower() == "manager":
            department = input("Enter department ")
            add_employee(file_name, Manager(name, age, salary, department))
        elif emp_type.lower() == "worker":
            hours_worked = input("Enter hours worked ")
            add_employee(file_name, Worker(name, age, salary, hours_worked))
    elif choice == "2":
        display_employees(file_name)
    elif choice == "3":
        name = input("Enter name of the employee to update ")
        attribute = input("Enter attribute to update (name/age/salary/department/hours worked): ")
        value = input("Enter new value: ")
        update_employee(file_name, name, attribute, value)
    elif choice == "4":
        name = input("Enter name of the employee to delete ")
        delete_employee(file_name, name)
    elif choice == "5":
        break
