"""
Make a two-player Rock-Paper-Scissors game. (Hint: Ask for player plays (using input), compare them,
print out a message of congratulations to the winner, and ask if the players want to start a new game)

Remember the rules:

*Rock beats scissors
*Scissors beats paper
*Paper beats rock
"""
from random import choice


def who_is_the_winner(user: str, si: str) -> str:
    si = si.lower()
    user = user.lower()
    if user == 'paper' and si == 'stone' or user == 'stone' and si == 'scissors' or user == 'scissors' \
        and si == 'paper':
        return 'You won!'
    elif user == 'paper' and si == 'scissors' or user == 'stone' and si == 'paper' or user == 'scissors' \
        and si == 'stone':
        return 'You lose!'
    else:
        return 'Draw!'


def test_if_the_player_wins():
    option_list = ['paper', 'stone', 'scissors']
    assert who_is_the_winner(option_list[0], option_list[1]) == 'You won!'
    assert who_is_the_winner(option_list[1], option_list[2]) == 'You won!'
    assert who_is_the_winner(option_list[2], option_list[0]) == 'You won!'


def test_if_the_computer_wins():
    option_list = ['paper', 'stone', 'scissors']
    assert who_is_the_winner(option_list[0], option_list[2]) == 'You lose!'
    assert who_is_the_winner(option_list[1], option_list[0]) == 'You lose!'
    assert who_is_the_winner(option_list[2], option_list[1]) == 'You lose!'


def test_if_game_end_with_draw():
    option_list = ['paper', 'stone', 'scissors']
    assert who_is_the_winner(option_list[0], option_list[0]) == 'Draw!'
    assert who_is_the_winner(option_list[1], option_list[1]) == 'Draw!'
    assert who_is_the_winner(option_list[2], option_list[2]) == 'Draw!'


def test_if_the_users_choice_is_an_uppercase_but_a_correct_word():
    option_list = ['PaPeR', 'sTONe', 'ScissorS']
    assert who_is_the_winner(option_list[0], option_list[2]) == 'You lose!'
    assert who_is_the_winner(option_list[1], option_list[0]) == 'You lose!'


if __name__ == '__main__':

    continue_or_not = 'y'
    while continue_or_not == 'y':
        player_choice = input('Select paper, scissors or stone: ')
        computer_choice = choice(['paper', 'stone', 'scissors'])

        result = who_is_the_winner(player_choice, computer_choice)

        print(result)
        print(f'Computer choice: {computer_choice}')
        continue_or_not = input('Would you play once more? (Type "Y" or "N": ').lower()
        continue_or_not = continue_or_not
    print('See you later!')