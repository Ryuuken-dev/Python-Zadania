"""
Przygotuj funkcję, która odbierze dwie listy, wynikiem powinna być nowa lista, której
elementami będą sumy.
"""
a = [2, 6, 8, 10, 12]
b = [4, 12, 16, 20, 24]


def sum_lists(list_1: list, list_2: list):
    new_list = []
    for number_1, number_2 in zip(list_1, list_2):
        new_list.append(number_1 + number_2)
    return new_list


print(sum_lists(a, b))
