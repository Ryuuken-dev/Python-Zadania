"""
Generate a random number between 1 and 9 (including 1 and 9).
Ask the user to guess the number, then tell them whether they guessed too low, too high, or exactly right.

Extras:

1. Keep the game going until the user types “exit”
2. Keep track of how many guesses the user has taken, and when the game ends, print this out.
"""
from random import choice


def generate_numbers_list(lowest: int, biggest: int) -> list:
    numbers_list = []
    for i in range(lowest, biggest + 1):
        numbers_list.append(i)
    return numbers_list


def randomize_number(values) -> int:
    ai_choice = values
    return choice(ai_choice)


def start_game(player_choice: int, correct_value) -> str:
    if player_choice < correct_value:
        return 'Podałeś za małą liczbę!'
    elif player_choice > correct_value:
        return 'Podałeś za dużą liczbę!'
    return 'Trafiłeś idealnie!'


def test_if_the_generated_values_are_correct():
    min_num = 1
    max_num = 10
    result = generate_numbers_list(min_num, max_num)
    assert result == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def test_if_the_game_prints_a_proper_value():
    values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    assert start_game(values[0], values[5]) == 'Podałeś za małą liczbę!'
    assert start_game(values[5], values[3]) == 'Podałeś za dużą liczbę!'
    assert start_game(values[9], values[9]) == 'Trafiłeś idealnie!'


if __name__ == '__main__':
    is_done = True
    guesses_counter = 0
    numbers_collection = []
    change_interval = 't'
    while is_done:
        if len(numbers_collection) != 0:
            change_interval = input('Czy chcesz zmienić przedział liczbowy? (T/N): ').lower()
        if len(numbers_collection) == 0 or change_interval == 't':
            min_value = int(input(f'Podaj najmniejszą liczbę z przedziału do odgadnięcia: '))
            max_value = int(input(f'Podaj największą liczbę z przedziału do odgadnięcia: '))
            numbers_collection.clear()
            numbers_collection.append(min_value)
            numbers_collection.append(max_value)
        generate_result = generate_numbers_list(numbers_collection[0], numbers_collection[1])
        print(f'Przedział: {generate_result}')
        users_option = int(input('Jak myślisz, która to liczba?: '))
        randomize_result = randomize_number(generate_result)
        print(start_game(users_option, randomize_result))
        to_continue = input('Wpisz "Dalej" by zagrać jeszcze raz lub "Koniec" by zakończyć: ').lower()
        guesses_counter += 1
        if to_continue == 'koniec':
            is_done = False
            print(f'Zgadywałeś {guesses_counter} razy')

