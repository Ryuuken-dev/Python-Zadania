"""
1. Przygotuj grę "Zgadnij liczbę" z interfejsem graficznym:
    a. Program losuje liczbę z zakresu 1-50
    b. Jeśli użytkownik będzie podawał wartości coraz bliższe zgadywanej liczbie program powinien
        wyświetlić "ciepło"
    c. Jeśli użytkownik będzie podawał wartości coraz dalsze zgadywanej liczbie program powinien wyświetlić
        "zimno"
2. Po wpisaniu poprawnej liczby program powinien wyświetlić stosowny komunikat i odpowiedzieć w ilu krokach
    użytkownik zgadł.
"""

from random import choice
import tkinter as tk
from tkinter import messagebox
from math import floor

ai_number = choice(range(1, 51))
step = floor(ai_number / 2)


done = 0


def send_number():

    if users_number.get() == ai_number:
        messagebox.showinfo(title='OK!', message='Zgadłeś!')

    if int(users_number.get()) <= step:
        messagebox.showinfo(title='OK!', message='Zimno')
    elif int(users_number.get()) > step:
        messagebox.showinfo(title='OK!', message='Ciepło')


window = tk.Tk()
window.title('Pystart')
window.geometry('500x500')

label = tk.Label(window, text="Podaj liczbę: ")
label.pack()

users_number = tk.Entry()
users_number.pack()

button = tk.Button(text="OK", command=send_number)
button.pack()
window.mainloop()

send_number()
