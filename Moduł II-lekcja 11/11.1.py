# Poproś użytkownika o podanie imienia. W zależności od jego ostatniej litery wyświetl "Witam Panią" lub "Witam Pana".
user_name = input('Podaj imię: ').lower()
if (user_name[len(user_name) - 1]) == 'a':
    print('Witam Panią')
else:
    print('Witam Pana')