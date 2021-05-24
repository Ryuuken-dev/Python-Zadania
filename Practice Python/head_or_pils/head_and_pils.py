"""
Działanie programu powinno być zbliżone do następującego:

1. Użytkownik wybiera czy obstawia resztę, czy orła (literka r – reszka, literka o – orzeł)
2. Po dokonaniu wybory, Komputer odlicza 3,2,1, a następnie dokonuje 'rzutu', czyli losowego wyboru orzeł / reszka.
3. Komputer wyświetla wynik rzutu.
4. Jeżeli wygrał użytkownik, to dodaje punkt dla użytkownika, jeżeli komputer to dodaje punkt dla komputera.
5. Wyświetla wyniki
6. Wracamy do punktu 1.

Wskazówki:

1. Działanie programu powinno kończyć się po podaniu w punkcie 1, cyfry 0.
2. Wczytanie wyboru użytkownika, może odbyć się przy pomocy funkcji input(), która zwraca podany przez użytkownika ciąg znaków
"""
import time
from random import choice


class Game:
    def __init__(self):
        self.ai_points = 0
        self.player_points = 0
        self.decision = ''

    def set_decision(self, decision):
        self.decision = decision

    def get_result(self):
        for i in range(1, 4):
            print(i)
            time.sleep(1)
        ai_choice = choice(['r', 'o'])
        if self.decision == ai_choice:
            self.player_points += 1
        else:
            self.ai_points += 1


ai_points = 0
player_points = 0
game = Game()
while True:
    users_choice = input('Wybierz:\n-Literka "o": Orzeł\n-Literka "r": Reszka\n-Cyfra 0: Koniec gry\n')
    if users_choice == '0':
        break
    game.set_decision(users_choice)
    game.get_result()
    print(f'Komputer: {game.ai_points}')
    print(f'Gracz: {game.player_points}')


