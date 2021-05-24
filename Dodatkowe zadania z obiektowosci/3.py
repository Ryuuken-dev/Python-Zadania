"""
Przygotuj klasę Odcinek, która w konstruktorze będzie odbierała dwa obiekty klasy Punkt posiadające współrzędne X i Y.
Klasa Odcinek powinna posiadać metodę służącą do obliczania jego długości.
"""
from math import sqrt


class Point:
    def __init__(self, axis_x, axis_y):
        self.axis_x = axis_x
        self.axis_y = axis_y


class Sector:
    def __init__(self, point_1: Point, point_2: Point):
        self.point_1 = point_1
        self.point_2 = point_2

    def sector_length(self):
        return sqrt((self.point_2.axis_x - self.point_1.axis_x) ** 2 + (self.point_2.axis_y - self.point_1.axis_y) ** 2)


def test_sector_length_method():
    point_1 = Point(2, 3)
    point_2 = Point(4, 3)

    sector = Sector(point_1, point_2)

    assert sector.sector_length() == sqrt((4 - 2) ** 2 + (3 - 3) ** 2)
