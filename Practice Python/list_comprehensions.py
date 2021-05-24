"""
Let’s say I give you a list saved in a variable: a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100].
Write one line of Python that takes this list a and makes a new list that has only the even elements of this list in it.
"""
numbers = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]


def get_even_numbers_list(num: list) -> list:
    return [number for number in num if number % 2 == 0]


def test_if_numbers_in_list_are_even():
    values = [1, 3, 67, 456, 23, 12, 10, 24, 11, 100, 68, 111, 123]

    assert get_even_numbers_list(values) == [456, 12, 10, 24, 100, 68]


if __name__ == '__main__':
    print(get_even_numbers_list(numbers))
