"""
Odbierz od użytkownika słowa rozdzielone przecinkami, a następnie wyświetl te słowa wiersz pod wierszem, ale
każde tylko jeden raz.
"""
users_words = input('Podaj słowa rozdzielone przecinkami: ')
words_list = users_words.split(' ')
words_box = set()
for word in words_list:
    words_box.add(word)
for word in words_box:
    print(word)



