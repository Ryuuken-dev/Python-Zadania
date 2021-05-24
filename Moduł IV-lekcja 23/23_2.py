"""
Przygotuj funkcję, którą nazwij play_game. Jej argumenty to player_choice i computer_choice.
Do wyboru "papier", "kamień", "nożyce". Jeśli wygra gracz funkcja powinna zwrócić 1, jeśli
komputer funkcja zwraca 2, jeśli remis 0.
"""
from random import choice


def play_game(player_choice: str, computer_choice: str) -> int:
    if player_choice == 'papier' and computer_choice == 'kamień' or player_choice == 'kamień' \
    and computer_choice == 'nożyce' or player_choice == 'nożyce' and computer_choice == 'papier':
        return 1
    if player_choice == 'papier' and computer_choice == 'nożyce' or player_choice == 'kamień' \
    and computer_choice == 'papier' or player_choice == 'nożyce' and computer_choice == 'kamień':
        return 2
    if player_choice == 'papier' and computer_choice == 'papier' or player_choice == 'kamień' \
    and computer_choice == 'kamień' or player_choice == 'nożyce' and computer_choice == 'nożyce':
        return 0


def test_player_won():
    assert play_game('papier', 'kamień') == 1
    assert play_game('kamień', 'nożyce') == 1
    assert play_game('nożyce', 'papier') == 1


def test_computer_won():
    assert play_game('papier', 'nożyce') == 2
    assert play_game('kamień', 'papier') == 2
    assert play_game('nożyce', 'kamień') == 2


def test_when_draw():
    assert play_game('papier', 'papier') == 0
    assert play_game('kamień', 'kamień') == 0
    assert play_game('nożyce', 'nożyce') == 0


# def test_when_user_puts_an_number_in_the_function_or_an_incorrect_value():
#     assert play_game(123, 'papier') == -1
#     assert play_game('papier', 123) == -1
#     assert play_game(123, 1234) == -1
#     assert play_game('paper', 'kamień') == -1
#     assert play_game('nożyce', 'kmień') == -1
#     assert play_game('paier', 'nżyce') == -1


if __name__ == '__main__':
    player = input('Wpisz papier, kamień lub nożyce: ')
    computer = choice(['papier', 'kamień', 'nożyce'])
    print(f'Wybór komputera: {computer}')

    result = play_game(player, computer)

    while player not in ['papier', 'kamień', 'nożyce']:
        player = input('Wpisz papier, kamień lub nożyce: ')
    if result == 1:
        print('Wygrałeś!')
    elif result == 2:
        print('Przegrałeś!')
    else:
        print('REMIS!')