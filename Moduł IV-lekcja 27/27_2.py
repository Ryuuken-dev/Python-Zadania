"""
Przygotuj dekorator, który zwróci informację ile sekund wykonywała się dana funkcja,
z jakimi została uruchomiona argumentami.
"""
from time import time, sleep
from math import pi
number = pi


def get_function_working_time(function):
    def wrapper(*args, **kwargs):
        print(*args)
        print(**kwargs)
        start = time()
        result = function(*args, **kwargs)
        end = time()
        print(f'Czas działania funkcji: {end - start}')

        return result
    return wrapper


def test_time_of_the_function_work():
    num_1 = 10
    num_2 = 20

    @get_function_working_time
    def numbers_plus(a, b):
        list_1 = []
        list_2 = []
        max_num = 0
        min_num = 0
        if a - b <= 0:
            max_num = b
            min_num = a
        else:
            max_num = a
            min_num = b
        for i in range(1, max_num + 1):
            if i <= min_num:
                list_1.append(i)
            else:
                list_2.append(i)
        return list_1, list_2

    result = numbers_plus(num_1, num_2)

    assert result > 0


if __name__ == '__main__':
    @get_function_working_time
    def generate_numbers_list(lowest: int, biggest: int, delay: int) -> list:
        sleep(delay)
        numbers_list = []
        for i in range(lowest, biggest + 1):
            numbers_list.append(i)
        return numbers_list

    fun = generate_numbers_list(3, 6, 3)
