"""
Przygotuj funkcję, która zliczy ilość znaków w tekście zawierających się wewnątrz nawiasów okrągłych.
Nawiasy mogą występować w tekście wielokrotnie, nigdy nie będą się w sobie zawierać.
"""


def char_counter(word: str, start='', end=''):
    brackets = ['(', '<', '{', '[', ')', '>', '}', ']']
    word_list = word.split(' ')
    count = ''
    if start in brackets:
        word_list.insert(0, start)
    if end in brackets:
        word_list.append(end)
    for word in word_list:
        if word[0] == '(' and word[-1] == ')':
            count += str(len(word) - 2)
        else:
            return 0
    return count


print(char_counter('Ala ma kota'))
