class Employee:
    def __init__(Saif, Name, Position):
        Saif.Name = Name
        Saif.Position = Position

    def DisplayInfo(Saif):
        print(f"Name: {Saif.Name}, Position: {Saif.Position}")


class Manager(Employee):
    def __init__(Saif, Name, Position, Department):
        super().__init__(Name, Position)
        Saif.Department = Department

    def AdditionalInfo(Saif):
        print(f"Department: {Saif.Department}")


class Worker(Employee):
    def __init__(Saif, Name, Position, HoursWorked):
        super().__init__(Name, Position)
        Saif.HoursWorked = HoursWorked

    def AdditionalInfo(Saif):
        print(f"Hours Worked: {Saif.HoursWorked}")


def RegisterEmployees():
    Manager1 = Manager("Rasikh Ali", "Project Manager", "SE")
    Manager1.DisplayInfo()
    Manager1.AdditionalInfo()

    Worker1 = Worker("Saifullah", "AI Scientist", 1000)
    Worker1.DisplayInfo()
    Worker1.AdditionalInfo()

RegisterEmployees()
