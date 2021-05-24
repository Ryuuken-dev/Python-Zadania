"""
Przygotuj funkcje, która za pomocą wyrażenia list comprehension będzie potrafiła przefiltrować
liczby parzyste z listy przekazanej w argumencie.
"""


def even_filter(numbers: list):
    return [number for number in numbers if number % 2 == 0]


print(even_filter([1, 2, 3, 4, 6]))