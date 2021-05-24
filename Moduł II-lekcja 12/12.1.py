"""
Przygotuj mały słownik języka angielskiego, pytaj użytkownika co chce zrobić i wyświetlaj mu słowo
przetłumaczone na język polski lub na język angielski.
"""

users_choice = input('Podaj parę językową-Polski>Angielski (P>A), Angielski>Polski (A>P): ').lower()
users_choice = users_choice.replace(' ', '')
words = {
    'chomik': 'hamster',
    'papuga': 'parrot',
    'dzięcioł': 'woodpecker',
    'wieloryb': 'whale',
    'gepard': 'cheetah',

}
users_word = input('Podaj słowo: ').lower()
def check_pol_word():
    for word in words:
        if word == users_word:
            print(f'{word.upper()} po polsku to {words[word].upper()} po angielsku.')
        elif users_word not in words:
            print('Nie mamy takiego słowa w bazie danych!')
            quit()

def check_ang_word():
    for word in words:
        if users_word == words[word]:
            print(f'{words[word].upper()} po angielsku to {word.upper()} po polsku.')
        elif users_word not in words.values():
            print('Nie mamy takiego słowa w bazie danych!')
            quit()

if users_choice == 'p>a':
    check_pol_word()
elif users_choice == 'a>p':
    check_ang_word()

