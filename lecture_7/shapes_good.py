import math

class Rectangle:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def get_area(self):
        return self.a * self.b


class Square:
    def __init__(self, a):
        self.a = a

    def get_area(self):
        return self.a ** 2

class Circle:
    def __init__(self, r):
        self.r = r

    def get_area(self):
        return self.r ** 2 * 3.14

class Triangle:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def get_area(self):
        p = self.a + self.b + self.c
        return math.sqrt(p * (p - self.a) * (p - self.b) * (p - self.c))


shapes = [Rectangle(4, 5), Square(4), Circle(4), Triangle(3, 4 ,5)]

# GOOD CODE with Polymorphism
for shape in shapes:
    print(shape.get_area())




