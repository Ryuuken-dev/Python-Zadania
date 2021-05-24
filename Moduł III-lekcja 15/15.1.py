"""
Zapytaj użytkownika o 10 liczb dodatnich. Jeśli użytkownik poda liczbę ujemną to nie powinna być ona zliczana.
Wyświetl największą i najmniejszą liczbę.
"""
numbers = []
done = False
while not done:
    users_number = int(input('Podaj liczbę: '))
    if len(numbers) == 9:
        done = True
    if users_number < 0:
        continue
    numbers.append(users_number)
print(f'Liczby: {numbers}')
print(f'Największa liczba: {max(numbers)}')
print(f'Najmniejsza liczba: {min(numbers)}')
