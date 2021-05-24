# Napisz program generujący bardzo "silne" hasła. Zamień każdą literę "a" na @ oraz każdą literę s na $
users_password = input('Podaj hasło: ')
users_password = users_password.replace('a', '@')
users_password = users_password.replace('s', '$')
print(users_password)
# Metoda replace zamienia każdy znak w podanym tekście

