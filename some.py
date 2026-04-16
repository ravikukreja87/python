import math
from turtle import circle

class Circle:
    def __init__(self, radius):
        "Constructor to initialize the radius."
        self.radius = radius

    def area(self):
        "Calculates and returns the area: π * r^2"
        return math.pi * (self.radius ** 2)

    def perimeter(self):
        "Calculates and returns the perimeter (circumference): 2 * π * r"
        return 2 * math.pi * self.radius



    # Taking input from the user
    user_radius = float(input("Enter the radius of the circle: "))

    # Creating an instance of the Circle class
    my_circle = circle(user_radius)

    # Displaying the results
    print(f"\nResults for a circle with radius {user_radius}:")
    print(f"Area: {my_circle.area():.2f}")
    print(f"Perimeter: {my_circle.perimeter():.2f}")

