"""
Policz pierwiastek kwadratowy każdego elementu listy, a następnie przefiltruj tylko te elementy których
pierwiastek jest liczbą parzystą, np. [16, 36, 25, 49]
"""
from math import sqrt
from math import floor
numbers = [16, 36, 25, 49, 64, 81, 3]
square_root = list(map(lambda num: floor(sqrt(num)), numbers))
filtered = filter(lambda num: num % 2 == 0, square_root)


def test_if_numbers_have_squares():
    assert len(square_root) == len(numbers)


def test_if_numbers_are_even():
    for number in filtered:
        assert number % 2 == 0
