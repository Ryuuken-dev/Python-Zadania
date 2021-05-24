"""
Given two integers a and b, which can be positive or negative, find the sum of all the integers
between and including them and return it. If the two numbers are equal return a or b.
"""


def get_sum(a: int, b: int):
    if a == b:
        return a
    try:
        step = -1 if a > b else 1
        numbers = [number for number in range(a, b + step, step)]
        return sum(numbers)
    except TypeError:
        return 'Podano niewłaściwy argument funkcji, podaj liczbę całkowitą'


def test_if_user_try_to_sum_two_equal_numbers():
    a = 2
    b = 2

    result = get_sum(a, b)

    assert result == 2


def test_try_to_sum_two_different_numbers():
    a = 2
    b = 3

    result = get_sum(a, b)

    assert result == 5
    assert get_sum(-1, 5) == 14
    assert get_sum(-1, 0) == -1
    assert get_sum(5, -1) == 14
    assert get_sum(0, -1) == -1


def test_try_to_sum_a_range_of_numbers():
    a = 2
    b = 10

    result = get_sum(a, b)

    assert result == 54


def test_try_to_give_an_unexpected_arguments_to_the_function():
    a = 'Przemek'
    b = 10

    result = get_sum(a, b)

    assert result == 'Podano niewłaściwy argument funkcji, podaj liczbę całkowitą'


if __name__ == '__main__':
    try:
        num_1 = int(input('Podaj pierwszą liczbę: '))
        num_2 = int(input('Podaj drugą liczbę: '))
        print(f'Suma cyfr z przedziału {num_1}, {num_2} wynosi {get_sum(num_1, num_2)}')
    except ValueError:
        print('Podano niewłaściwą wartość, podaj liczbę całkowitą.')


