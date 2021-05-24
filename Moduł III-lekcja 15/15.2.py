"""
Poproś użytkkownika o podawanie liczb, gdzie każda kolejna będzie większa od poprzedniej. Jeśli ten warunek nie nastąpi,
program powinien się zakończyć. Wyświetl średnią z tych liczb.
"""
numbers = []

print('Podawaj liczby, każda kolejna liczba powinna być większa od pozostałej')
while True:
    users_number = int(input('Podaj liczbę: '))
    if len(numbers):
        if users_number < numbers[-1]:
            break
    numbers.append(users_number)
print(f'Srednia z podanych liczb: {numbers} wynosi {sum(numbers) / len(numbers)}')