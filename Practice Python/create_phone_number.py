"""
Write a function that accepts an array of 10 integers (between 0 and 9),
that returns a string of those numbers in the form of a phone number.
"""


def create_phone_number(integers: list) -> str:
    phone_number = '('
    for number in integers:
        if len(phone_number) == 4:
            phone_number += ') '
        if len(phone_number) == 9:
            phone_number += '-'
        phone_number += str(number)
    return phone_number


def test_if_conversion_to_a_string_works_correct():
    data = [1, 2, 6, 0, 9, 5, 3, 4, 8, 7]

    result = create_phone_number(data)

    assert result == "(126) 095-3487"