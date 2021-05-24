"""
Pytaj użytkownika o liczbę tak długo jak długo nie napisze "koniec". Wyświetl iloczyn wszystkich
liczb parzystych podanych przez użytkownika.
"""


def numbers_collector():
    numbers = []
    is_done = False
    while not is_done:
        users_choice = input('Podaj liczbę albo wpisz "koniec" by zakończyć: ').lower()
        if users_choice == 'koniec':
            is_done = True
        else:
            numbers.append(int(users_choice))
    return numbers


numbers_base = numbers_collector()


def even_numbers_ratio(numbers):
    even_numbers = [number for number in numbers if number % 2 == 0]
    final_ratio = even_numbers[0]
    for i in range(1, len(even_numbers)):
        final_ratio *= even_numbers[i]
    return final_ratio


print(even_numbers_ratio(numbers_base))
