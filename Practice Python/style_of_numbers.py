"""
Napisz funkcję moda(), która jako parametr przyjmuje listę liczb całkowitych.
Funkcja zwraca tę liczbę, która pojawia się w tej liście najczęściej. Jeśli mamy remis, zwróć którąkolwiek z tych liczb.
"""
from random import choice


def most_common_number(nums: list) -> int:
    nums_list = [

    ]
    for number in nums:
        nums_list.append([number, nums.count(number)])
    rev = list(sorted(nums_list, key=lambda num: num[1], reverse=True))
    return rev[0][0]



def test_if_the_number_from_the_list_is_most_common():
    # given
    numbers = [4, 6, 10, 4, 3, 4, 11, 56, 34, 9]

    # when
    result = most_common_number(numbers)

    # then
    assert result == 4


def test_if_there_are_two_most_common_numbers():
    # given
    numbers = [4, 6, 10, 3, 3, 4, 11, 56, 34, 9]

    # when
    result = most_common_number(numbers)

    # then
    assert result == 3 or 4


if __name__ == '__main__':
    numbers = [4, 8, 10, 4, 3, 4, 11, 56, 34, 9]
    print(most_common_number(numbers))