import math

class Shape:
    def init(self):
        pass

class TwoDimensionalShape(Shape):
    def area(self):
        pass

class ThreeDimensionalShape(Shape):
    def volume(self):
        pass

class Square(TwoDimensionalShape):
    def __init__(self, side_length):
        self.side_length = side_length

    def area(self):
        return self.side_length ** 2

class Triangle(TwoDimensionalShape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height

class Cube(ThreeDimensionalShape):
    def __init__(self, side_length):
        self.side_length = side_length

    def volume(self):
        return self.side_length ** 3

class Cone(ThreeDimensionalShape):
    def __init__(self, radius, height):
        self.radius = radius
        self.height = height

    def volume(self):
        return (1/3) * math.pi * self.radius ** 2 * self.height

# Example usage:
square = Square(4)
triangle = Triangle(3, 6)
cube = Cube(5)
cone = Cone(3, 8)

print(f"Square Area: {square.area()}")
print(f"Triangle Area: {triangle.area()}")
print(f"Cube Volume: {cube.volume()}")
print(f"Cone Volume: {cone.volume()}")
