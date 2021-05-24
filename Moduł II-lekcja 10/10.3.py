# Zapytaj użytkownika o liczbę, w wyniku wyświetl informację czy jest ona liczbą pierwszą
user_number = float(input('Podaj liczbę: '))
if user_number % user_number == 0 and user_number % 1 == 0:
    print(f'Liczba {user_number} jest liczbą pierwszą')
else:
    print(f'Liczba {user_number} nie jest liczbą pierwszą')