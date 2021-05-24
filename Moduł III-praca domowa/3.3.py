"""
Przygotuj funkcję, która dla dowolnej liczby policzy jej silnię. Skorzystaj z pętli while, np. get_factorial(5)
powinno zwrócić wynik 5 * 4 * 3 * 2 * 1
"""


def get_factorial(number: int):
    count = number
    factorial = number
    while count > 1:
        count -= 1
        factorial *= count
    return factorial


print(get_factorial(7))
