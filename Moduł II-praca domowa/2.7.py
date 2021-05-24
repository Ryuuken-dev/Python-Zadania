"""
Zapytaj użytkownika o dwa wyrażenia, a następnie wyświetl wszystkie znaki wspólne dla obu tych wyrażeń.
Np. sala i balkon powinno wyświetlić "a" oraz "l"
"""
word_1 = input('Podaj pierwsze wyrażenie: ')
word_2 = input('Podaj drugie wyrażenie: ')
print(f'Wspólne znaki dla wartości {word_1} i {word_2} to {set(word_1) & set(word_2)}')
