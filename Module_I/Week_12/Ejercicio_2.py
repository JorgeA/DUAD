import math
from abc import ABC, abstractmethod

class Shape(ABC):

    @abstractmethod
    def get_area(self):
        pass
    def get_perimeter(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def get_area(self):
        return math.pi * self.radius ** 2

    def get_perimeter(self):
        return 2 * math.pi * self.radius
    
class Square(Shape):
    def __init__(self, side):
        self.side = side

    def get_area(self):
        return self.side ** 2

    def get_perimeter(self):
        return 4 * self.side
    
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def get_area(self):
        return self.length * self.width

    def get_perimeter(self):
        return 2 * (self.length + self.width)


circle = Circle(5)
print(f"Area del circulo: {circle.get_area()}")
print(f"Perimetro del circulo: {circle.get_perimeter()}")
print()
Square = Square(5)
print(f"Area del cuadrado: {Square.get_area()}")
print(f"Perimetro del cuadrado: {Square.get_perimeter()}")
print()