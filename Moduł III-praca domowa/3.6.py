"""
Przygotuj funkcję, która za pomocą list comprehension przefiltruje tylko słowa, których długość
jest większa od 4 i mniejsza od 8.
"""


def words_len(word: str):
    words_list = word.split(' ')
    return [word for word in words_list if 4 < len(word) < 8]


print(words_len('ada basia tomasz'))
