"""
Przygotuj metody specjalne umożliwiające dodawanie obiektów do siebie, odejmowanie oraz
porównywanie ich ze sobą.
"""


class LengthUnit:
    def __init__(self, value: int):
        self.value = value

    def to_centimeter(self):
        return self.value / 10

    def to_meter(self):
        return self.value / 10 / 100

    def __add__(self, other):
        return self.value + other.value

    def __sub__(self, other):
        return self.value - other.value

    def __eq__(self, other):
        return self.value == other.value


def test_if_objects_sum_value_is_correct():
    value_1 = 70
    value_2 = 30

    obj_1 = LengthUnit(value_1)
    obj_2 = LengthUnit(value_2)

    assert obj_1 + obj_2 == 100


def test_if_objects_subtraction_value_is_correct():
    value_1 = 70
    value_2 = 30

    obj_1 = LengthUnit(value_1)
    obj_2 = LengthUnit(value_2)

    assert obj_1 - obj_2 == 40


def test_if_objects_comparison_value_is_correct():
    value_1 = 70
    value_2 = 30

    obj_1 = LengthUnit(value_1)
    obj_2 = LengthUnit(value_2)
    com = obj_1 == obj_2

    assert com == False


if __name__ == '__main__':

    unit_1 = LengthUnit(10)
    unit_2 = LengthUnit(100)
    print(unit_1 + unit_2)
    print(unit_1 - unit_2)
    print(unit_1 == unit_2)