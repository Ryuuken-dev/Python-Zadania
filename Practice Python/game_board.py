"""
Time for some fake graphics! Let’s say we want to draw game boards that look like this:

 --- --- ---
|   |   |   |
 --- --- ---
|   |   |   |
 --- --- ---
|   |   |   |
 --- --- ---
This one is 3x3 (like in tic tac toe).
Obviously, they come in many other sizes (8x8 for chess, 19x19 for Go, and many more).

Ask the user what size game board they want to draw, and draw it for them to the screen using Python’s print statement.
"""


# Funkcja generująca planszę do gry
def generate_board(size: int, cor='0'):
    coor_list = cor.replace(' ', '').split(',')
    field = str()
    line = False
    count = 1
    for i in range(1, size + 2):
        for x in range(1, size + 1):
            if line:
                field += '\n'
                line = False
                count += 1

            field += ' ---'
            if i < size + 1:
                if x % size == 0:
                    field += '\n'
                    line = True
                    for z in range(1, size + 2):
                        if len(coor_list) > 1 and count == int(coor_list[0]) and z == int(coor_list[1]):
                            field += '| X '
                        else:
                            field += '|\t'

    return field


def board_with_options(board: str, coor: str):
    game_field = board
    coor_list = coor.split()


game_data = [

]
val = []
print('Tic Tac Toe Game')
# game_mode = input('Wybierz tryb:\n1. Gracz vs. Komputer\n2. Gracz vs. Gracz\n')
board_size = int(input('Podaj rozmiar (liczbę pól) planszy do gry: '))
for i in range(1, board_size + 1):
    if len(val) == board_size:
        val.clear()
    for x in range(1, board_size + 1):
        val.append(0)
    game_data.append(val)
print(generate_board(board_size))

co_ordinates_player_1 = input('Podaj współrzędne dla Twojego znacznika gracza (X): ')
co_ordinates_player_2 = input('Podaj współrzędne dla Twojego znacznika gracza (O): ')
print(generate_board(board_size, cor=co_ordinates_player_1))


# def who_is_the_winner(game_data: list) -> str:
#     winner = ''
#     results = [
#         [],
#         [],
#         [],
#         []
#     ]
#
#     for i in range(0, len(game_data)):
#         for x in range(0, len(game_data)):
#             if x < len(game_data) - 1:
#                 if game_data[i][0] == game_data[i][x + 1]:          # x-axis check
#                     results[0].append(game_data[i][0])
#
#                 if game_data[0][i] == game_data[x + 1][i]:          # y-axis check
#                     results[1].append(game_data[0][i])
#
#                 if i == 0:                                          # z-axis check
#                     if game_data[0][0] == game_data[x + 1][x + 1]:
#                         results[2].append(game_data[0][0])
#                 if i == 1:
#                     if game_data[0][len(game_data) - 1] == game_data[x + 1][len(game_data) - 1 - (x + 1)]:
#                         results[3].append(game_data[0][len(game_data) - 1])
#
#         for result in results:
#             if len(result) == len(game_data) - 1:
#                 if 1 in result:
#                     winner += 'Wygrałeś!'
#                 if 2 in result:
#                     winner += 'Przegrałeś!'
#             result.clear()
#     return winner
#
#
# def test_if_the_computer_wins():
#     results = [
#         [2, 2, 0],
#         [2, 1, 0],
#         [2, 1, 1]
#     ]
#
#     winner = who_is_the_winner(results)
#
#     assert winner == 'Przegrałeś!'
#
#
# def test_if_the_player_wins():
#     results = [
#         [1, 1, 0, 2, 2],
#         [2, 1, 0, 2, 0],
#         [2, 1, 1, 0, 1],
#         [2, 2, 1, 1, 1],
#         [2, 1, 0, 2, 1]
#     ]
#
#     winner = who_is_the_winner(results)
#
#     assert winner == 'Wygrałeś!'
#
#
# choices = [[2, 1, 0, 2], [2, 1, 0, 0], [2, 1, 1, 0], [2, 1, 0, 0]]

# if __name__ == '__main__':
#     res = who_is_the_winner(choices)
#     print(res)
