"""
Napisz funkcję, która sprawdzi czy elementy krotki pierwszej
znajdują się w krotce drugiej.
"""


def data_check(dataset_1: tuple, dataset_2: tuple) -> bool:
    for item in dataset_1:
        if item not in dataset_2:
            return False
    return True


def test_if_elements_in_first_dataset_are_in_second_dataset():
    data_1 = (1, 5, 23)
    data_2 = (1, 5, 23, 89, 12, 34, 8)

    result = data_check(data_1, data_2)

    assert result == True


def test_if_elements_in_first_dataset_are_not_in_second_dataset():
    data_1 = (11, 5, 23)
    data_2 = (1, 5, 23, 89, 12, 34, 8)

    result = data_check(data_1, data_2)

    assert result == False


if __name__ == '__main__':
    data_1 = (11, 5, 23)
    data_2 = (1, 5, 23, 89, 12, 34, 8)
    res = data_check(data_1, data_2)
    print(res)
