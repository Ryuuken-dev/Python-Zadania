"""
Zdefiniuj listę skreslone i wpisz do niej sześć losowych liczb z zakresu od 1 do 19 np.
[10, 15, 2, 13, 4, 9]. Następnie wykorzystując funkcję random.randint wylosuj
kolejne sześć liczb i zapisz je do nowej listy wylosowane. Wylosowane liczby nie mogą się
powtarzać. Porównaj otrzymane liczby ze skreślonymi i zapisz ile z nich się powtarza w obu
listach.

W zależności od otrzymanego wyniku wydrukuj jeden z poniższych komunikatów:
● 6 - Główna nagroda
● 3-5 - Nagroda pieniężna za trafienie X liczb
● <3 - Spróbuj ponownie
"""
from random import randint


def win_numbers():
    numbers = []
    while len(numbers) < 6:
        random = randint(1, 19)
        if random in numbers:
            continue
        numbers.append(random)
    return numbers


def lotto(f, nums_list: list):
    game_result = 0
    for num in nums_list:
        if num in f:
            game_result += 1
    if game_result == 6:
        return 'Główna wygrana!'
    elif 3 <= game_result <= 5:
        return f'Nagroda pieniężna za trafienie {game_result} liczb'
    elif game_result < 3:
        return 'Spróbuj ponownie'


users_numbers = [10, 15, 2, 13, 4, 9]

print(lotto(win_numbers(), users_numbers))