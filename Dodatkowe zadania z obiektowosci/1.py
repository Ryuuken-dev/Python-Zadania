"""
Przygotuj klasy prostokąt, koło i trójkąt, posiadające właściwości konieczne do obliczenia pola tych figur.
"""
from math import pi
pi = pi


class Rectangle:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def get_area(self):
        return self.a * self.b


class Circle:
    def __init__(self, radius, pi):
        self.radius = radius
        self.pi = pi

    def get_area(self):
        return self.pi * self.radius ** 2


class Square:
    def __init__(self, flank):
        self.flank = flank

    def get_area(self):
        return self.flank ** 2


def test_rectangle_get_area():
    a = 10
    b = 20

    rect = Rectangle(a, b)

    assert rect.get_area() == 200


def test_circle_get_area():
    radius = 10

    circle = Circle(radius, pi)

    assert circle.get_area() == pi * radius ** 2


def test_square_get_area():
    side = 10

    square = Square(side)

    assert square.get_area() == 100