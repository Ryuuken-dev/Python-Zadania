"""
Przygotuj funkcję, która będzie odbierała od użytkownika słowo, a następnie zwróci zbiór samogłosek znajdujących
się w tym słowie.
"""
user_word = input('Podaj słowo: ')


def get_vowel(word):
    speech = word.lower()
    vowel_list = ['a', 'ą', 'e', 'ę', 'i', 'o', 'u', 'y']
    vowels = set(char for char in speech if char in vowel_list)
    return vowels


print(f'Samogłoski słowa {user_word} to: {get_vowel(user_word)}')
