"""
Przygotuj funkcję, której deklaracja będzie wyglądała następująco:

def count_numbers(numbers:list, count_odd:bool = True, count_even:bool = True):

Zadaniem funkcji będzie odpowiedź na pytanie ile jest liczb spełniających podane w argumentach wymagania
w liście przekazanej w pierwszym przedziale.
"""

numbers_list = [2, 6, 8, 10, 25, 33, 21, 29, 30]


def count_numbers(numbers: list, count_odd: bool = True, count_even: bool = True):
    even_list = [number for number in numbers if number % 2 == 0]
    odd_list = [number for number in numbers if number % 2 != 0]
    if count_even and count_odd:
        return len(even_list), len(odd_list)
    elif count_even:
        return len(even_list)
    elif count_odd:
        return len(odd_list)


print(count_numbers(numbers_list, count_odd=True, count_even=False))