value1 = float(input('Podaj pierwszą wartość liczbową: '))
value2 = float(input('Podaj drugą wartość liczbową: '))

if value1 > value2:
    print(f'Liczba {value1} jest większa')
elif value1 < value2:
    print(f'Liczba {value2} jest większa')
else:
    print('Obie liczby są równe')
