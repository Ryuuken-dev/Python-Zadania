"""
Your goal in this kata is to implement a difference function, which subtracts one list from another and returns the result.

It should remove all values from list a, which are present in list b keeping their order.
"""


def array_diff(a: list, b: list):
    new_list = []
    for num in a:
        if len(a) == 0 and len(b) != 0:
            return []
        elif len(a) != 0 and len(b) == 0:
            return a
        if num in b:
            continue
        new_list.append(num)
    return new_list


print(array_diff([1, 2], [1]))



