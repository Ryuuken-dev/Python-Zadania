"""
Welcome. In this kata, you are asked to square every digit of a number and concatenate them.
For example, if we run 9119 through the function, 811181 will come out, because 92 is 81 and 12 is 1.
"""


def square_digits(num: int) -> int:
    nums = str(num)
    new_num = ''
    for num in nums:
        value = int(num) ** 2
        new_num += str(value)
    return int(new_num)


def test_square_digits():
    number = 9119

    result = square_digits(number)

    assert result == 811181


if __name__ == '__main__':
    users_number = int(input('Podaj liczbę: '))
    print(f'Twoja nowa liczba to: {square_digits(users_number)}')
