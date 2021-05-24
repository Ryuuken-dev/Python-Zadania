user_number = int(input('Podaj liczbę: '))
if user_number % 5 == 0 and user_number % 11 == 0:
    print('Liczba jest podzielna przez 5 i 11')
elif user_number % 5 == 0:
    print('Liczba jest podzielna przez 5')
elif user_number % 11 == 0:
    print('Liczba jest podzielna przez 11')
else:
    print('Liczba nie dzieli się przez 11 i 5')