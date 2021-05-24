"""
Zbadaj czy na liście licz A, znajdują się dwie liczby – a i b, których suma wynosi liczbę L.

Czyli przykładowo, mamy podaną listę A = [1,3,5,2,11,7] .
Należy sprawdzić czy suma, którychkolwiek liczb na liście wynosi 9.
W tym prostym przykładnie już ‘na oko’ widzimy że będą to liczby 2 oraz 7.
"""


def numbers_summary(nums_list: list, sumn=9):
    for value in nums_list:
        for num in nums_list:
            if num == value:
                continue
            if num + value == sumn:
                return value, num
    return 0


def test_if_two_numbers_in_list_get_a_summary():
    list_a = [1, 3, 5, 2, 11, 7]

    result = numbers_summary(list_a)

    assert result == (2, 7)


def test_if_two_numbers_in_list_do_not_get_a_summary():
    list_a = [1, 3, 5, 2, 11, 7]

    result = numbers_summary(list_a, 99)

    assert result == 0


if __name__ == '__main__':
    print()
