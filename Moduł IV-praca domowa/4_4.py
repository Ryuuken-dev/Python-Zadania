"""
Przygotuj dekorator, który będzie wycinał listę według podanych przez użytkownika argumentów
@cut(1, 10) -> powinien wyciąć [1:10] z podanej listy
"""


def cut(begin: int, to: int):
    def wrapper(func):
        result = func()
        return result[begin:to]
    return wrapper


def test_if_cutting_works_correct():
    items = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

    @cut(1, 10)
    def random_list(nums: list):
        return nums
    result = random_list(items)

    assert result == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]