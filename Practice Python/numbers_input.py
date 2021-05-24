"""
Napisz program wprowadzający trzy liczby z klawiatury a następnie wyświetlający na ekranie:
- Największą z tych liczb
- Medianę (środkową liczbę)
- Sekwencję tych trzech liczb uporządkowaną rosnąco lub malejąco
- Informację czy przynajmniej dwie z tych liczb mają identyczną wartość.
Uwzględnia przypadki gdy wszystkie liczby są różne oraz że mogą wystąpić powtórzenia
"""
from math import floor


def greatest_number(outer_values: list) -> int:
    greatest = 0
    for number in outer_values:
        if greatest == 0 or greatest < number:
            greatest = number
    return greatest


def get_sequence(random_list: list, seq='upper') -> list:
    median_list = random_list
    for number in median_list:
        for i in range(0, len(median_list) - 1):

            if median_list[i] > median_list[i + 1]:
                bigger = median_list[i]
                median_list[i] = median_list[i + 1]
                median_list[i + 1] = bigger
    if seq == 'lower':
        return list(reversed(median_list))

    return median_list


def get_median(num_list: list) -> int:
    sorted_nums = get_sequence(num_list)
    return sorted_nums[floor(len(num_list) / 2)]


def numbers_comparison(nums: list) -> str:
    if nums[0] == nums[1] and nums[0] == nums[2]:
        return 'Wszystkie liczby mają identyczną wartość!'
    elif nums[0] == nums[1]:
        return 'Dwie liczby mają identyczną wartość!'
    return 'Wszystkie liczby są różne!'


def get_final_result(values: list) -> dict:
    numbers = {
        'Największa liczba': greatest_number(values),
        'Mediana': get_median(values),
        'Malejąco': get_sequence(values, 'lower'),
        'Rosnąco': get_sequence(values),
        'Liczby': numbers_comparison(values)
    }
    return numbers


data_values = []

for i in range(1, 4):
    choice = int(input('Podaj liczbę: '))
    data_values.append(choice)
data_set = get_final_result(data_values)
for data in data_set:
    print(f'{data}: {data_set[data]}')

