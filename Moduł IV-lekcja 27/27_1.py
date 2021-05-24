"""
Przygotuj dekorator, który zaokrągli zwracaną z funkcji wartość do dwóch miejsc po przecinku.
"""


def rounding_to_two_places(number=0):
    return number


def format_to_two_places(function):
    def wrapper(*args, **kwargs):
        result = function(*args, **kwargs)
        return round(result, 2)
    return wrapper


def test_format_to_two_places():
    @format_to_two_places
    def return_number():
        return 2.34567

    result = return_number()

    assert result == 2.35


if __name__ == '__main__':
    users_number = float(input('Podaj liczbę zmiennoprzecinkową: '))


    @format_to_two_places
    def rounding_to_two_places():
        return users_number

    print(rounding_to_two_places())
