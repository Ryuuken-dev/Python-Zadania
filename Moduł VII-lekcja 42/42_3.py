"""
Zapytaj użytkownika o dowolny tekst, który użytkownik chciałby odwrócić (Wyświetlić od końca do początku).
Jeśli użytkownik poda pusty string, powinien zostać zwrócony wyjątek.
"""


def reverse_string(text: str) -> str:
    new_str = ''
    for i in range(len(text) - 1, -1, -1):
        new_str += text[i]
    return new_str


while True:
    try:
        users_text = input('Podaj tekst, który ma zostać odwrócony lub wpisz "koniec" by zakończyć: ')
        if users_text == 'koniec':
            break
        print(reverse_string(users_text))
        if users_text == "":
            raise Exception('Podano pusty ciąg znaków')
    except Exception as error:
        print(error)
