"""
Zapytaj użytkownika o wartość najmniejszą i największą. Napisz program, który wypisze wszystkie liczby
pierwsze z tego przedziału.
"""
min_value = int(input('Podaj najmniejszą wartość: '))
max_value = int(input('Podaj największą wartość: '))
for i in range(min_value, max_value + 1):
    print(i)