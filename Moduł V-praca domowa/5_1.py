"""
Przygotuj grę "Wisielec" z interfejsem graficznym. Gra powinna losować jedno z haseł zapisywanych w kodzie.
Jeśli użytkownik trafi literę znajdującą się w haśle, litera ta powinna być odkrywana. W przeciwnym
wypadku zdobywa kolejną z liter W-I-S-I-E-L-E-C. Gra kończy się gdy użytkownik odgadnie hasło, nim skompletuje
całego "WISIELCA".
"""
from random import choice
import tkinter as tk
from tkinter import messagebox


def password():
    pass


random_values = []
with open('wisielec/passwords.txt', encoding='utf8') as file:
    for item in file:
        random_values.append(item)
option = choice(random_values)


def random_slogan(random):
    hidden_word = ''
    for _ in range(1, len(random)):
        hidden_word += '_  '
    word_area.configure(text=f'{hidden_word}')
    return hidden_word


def guess_word(data, rand):
    data_list = [val for val in data if val.isalpha()]
    hidden = [char for char in rand if '_' in char]
    result = ''
    count = 0
    loss = 'Wisielec'
    loss_word = ''
    print(data_list)
    print(hidden)
    player = users_number.get()
    if users_number.get() == data:
        word_area.configure(text=f'{data}')
    for value in range(0, len(player)):
        for i in range(0, len(data_list)):
            if i < len(player):
                if player[value] == data_list[i]:
                    hidden[i] = player[value]
    result += '  '.join(hidden)
    word_area.configure(text=result)
    if not result.isalpha():
        loss_word += loss[count]
        lose_area.configure(text=f'{loss_word}')
        count += 1


window = tk.Tk()
window.title('Gra "Wisielec"')
window.geometry('600x600')

label = tk.Label(window, text="Wpisz słowo: ")
label.pack()

users_number = tk.Entry()
users_number.pack(pady='10px')

generate_button = tk.Button(text="Losuj słowo do odgadnięcia", command=lambda: random_slogan(option))
generate_button.pack(pady='20px')
accept_button = tk.Button(text="Potwierdź", command=lambda: guess_word(option, random_slogan(option)))
accept_button.pack(pady='10px')
word_area = tk.Label(window, text='', pady='30px', font='28px')
word_area.pack()
lose_area = tk.Label(window, text='', pady='30px', font='28px')
lose_area.pack()

window.mainloop()
