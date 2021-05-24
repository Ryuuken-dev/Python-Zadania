"""
Przygotuj listę, która zawiera 10 elementów. Zapytaj użytkownika o to, która z wartości powinna zostać zwrócona.
Jeśli użytkownik odwoła się do wartości, która nie istnieje (indexError), to wyświetl komunikat, że takiej wartości
nie ma.
"""

items_list = [12, 45, 78, 14, 90, 100, 24, 55, 4, 3]

print('Dostępne wartości:')
for id, value in enumerate(items_list):
    print(f'{id}. {value}')
try:
    users_choice = int(input('Co wybierasz? '))
    print(items_list[users_choice])
except IndexError:
    print('Wartość o podanej pozycji nie istnieje!')
