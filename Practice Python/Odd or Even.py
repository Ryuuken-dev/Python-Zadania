"""
Ask the user for a number.
Depending on whether the number is even or odd, print out an appropriate message to the user.
Extras:

1. If the number is a multiple of 4, print out a different message.
2. Ask the user for two numbers: one number to check (call it num) and one number to divide by (check).
If check divides evenly into num, tell that to the user. If not, print a different appropriate message.
"""

users_number = int(input('Podaj liczbę: '))
multiple_num = 4

if users_number % multiple_num == 0:
    print(f'Liczba {users_number} jest wielokrotnością liczby {multiple_num}')
if users_number % 2 == 0:
    print(f'Liczba {users_number} jest parzysta!')
else:
    print(f'Liczba {users_number} jest nieparzysta!')


num = int(input('Podaj pierwszą liczbę: '))
check = int(input('Podaj drugą liczbę: '))

if num % check == 0:
    print(f'Liczba {num} dzieli się przez {check}')
else:
    print(f'Liczba {num} nie dzieli się przez {check}')