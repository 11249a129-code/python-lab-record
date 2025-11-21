import math

class Shape:
    def area(self):
        pass

class Triangle(Shape):
    def area(self, base, height):
        return 0.5 * base * height

class Circle(Shape):
    def area(self, radius):
        return math.pi * radius * radius

class Rectangle(Shape):
    def area(self, length, width):
        return length * width

# Create objects
t = Triangle()
c = Circle()
r = Rectangle()

print("Area of Triangle:", t.area(10, 5))
print("Area of Circle:", c.area(7))
print("Area of Rectangle:", r.area(8, 4))
