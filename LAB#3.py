class Rectangle:
    def __init__(Saif, Width: float, Height: float):
        Saif.Width = Width
        Saif.Height = Height

    def __str__(Saif):
        return f"Rectangle: {Saif.Width} x {Saif.Height}"

    def Area(Saif):
        return Saif.Width * Saif.Height

    def Perimeter(Saif):
        return 2 * (Saif.Width + Saif.Height)

Width = float(input("Enter the width of the rectangle: "))
Height = float(input("Enter the height of the rectangle: "))

RectangleInstance = Rectangle(Width, Height)

print(RectangleInstance)
print("Area of the rectangle:", RectangleInstance.Area())
print("Perimeter of the rectangle:", RectangleInstance.Perimeter())
