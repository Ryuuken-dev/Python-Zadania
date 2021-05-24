# Przygotuj funkcję, która zwróci True albo False, w zależności od tego czy liczba ta jest pierwsza.
from math import floor
users_number = int(input('Podaj liczbę: '))


def is_prime(number):
    number_list = [0 if number % i == 0 else 1 for i in range(2, floor(number ** (1/2) + 1))]
    if 1 in number_list:
        return True
    else:
        return False


print('')
print(is_prime(users_number))

# Python będzie czekał aż wykona się pętla i dopiero po tym przejdzie do kolejnych instrukcji programu