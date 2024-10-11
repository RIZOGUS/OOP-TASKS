class Vehicle:
    def __init__(Saif, Make, Model):
        Saif.Make = Make
        Saif.Model = Model

    def DisplayInfo(Saif):
        print(f"Make: {Saif.Make}, Model: {Saif.Model}")


class Car(Vehicle):
    def __init__(Saif, Make, Model, NumDoors):
        super().__init__(Make, Model)
        Saif.NumDoors = NumDoors

    def AdditionalInfo(Saif):
        print(f"Number of Doors: {Saif.NumDoors}")


class LuxuryCar(Car):
    def __init__(Saif, Make, Model, NumDoors, Features):
        super().__init__(Make, Model, NumDoors)
        Saif.Features = Features

    def AdditionalInfo(Saif):
        print(f"Luxury Features: {', '.join(Saif.Features)}")


def RegisterVehicles():
    Car1 = Car("Honda", "Yaris", 4)
    Car1.DisplayInfo()
    Car1.AdditionalInfo()

    LuxuryCar1 = LuxuryCar("Dodge", "Challenger Hellcat", 2, ["Supercharged V8 engine", "Sport suspension", "Leather upholstery"])
    LuxuryCar1.DisplayInfo()
    LuxuryCar1.AdditionalInfo()

RegisterVehicles()
