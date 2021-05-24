# Napisz program zliczający ilość wystąpień każdego znaku w zadanym napisie
users_word = input('Podaj zdanie: ')
how_many_chars = {}
for word in users_word:
    if word not in how_many_chars:
        how_many_chars[word] = users_word.count(word)
        print(f'Znak: {word} Ilość: {how_many_chars[word]}')
