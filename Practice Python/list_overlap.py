"""
Take two lists, say for example these two:

  a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
  b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
and write a program that returns a list that contains only the elements that are common between the
lists (without duplicates). Make sure your program works on two lists of different sizes.

Extras:

1. Randomly generate two lists to test this
2. Write this in one line of Python (don’t worry if you can’t figure this out at this point - we’ll get to it soon)
"""
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]


def get_common_elements(dataset_1: list, dataset_2: list) -> list:
    return [data for data in dataset_1 if data in dataset_2]


def test_if_list_have_common_elements():
    list_1 = [23, 567, 45, 90, 12, 123, 34, 235, 1, 2, 9, 13, 120, 131, 1200, 24, 64]
    list_2 = [23, 67, 4531, 909, 12, 123123, 34, 2035, 10, 2, 9]

    assert get_common_elements(list_1, list_2) == [23, 12, 34, 2, 9]


if __name__ == '__main__':
    print(get_common_elements(a, b))