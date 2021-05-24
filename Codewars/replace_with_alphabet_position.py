"""
In this kata you are required to, given a string, replace every letter with its position in the alphabet.

If anything in the text isn't a letter, ignore it and don't return it.

"a" = 1, "b" = 2, etc.
"""


def alphabet_position(text: str, alp) -> str:
    alphabet = {'pl': 'aąbcćdeęfghijklłmnńoópqrsśtuvwxyzźż',
                'eng': 'abcdefghijklmnopqrstuvwxyz'}
    tx_set = [str(alphabet[alp].index(char.lower()) + 1) for char in text if char.lower() in alphabet[alp]]
    return ' '.join(tx_set)


def represent_position(text: str, func):
    if func == "":
        return 'Podany ciąg znaków nie zawiera żadnej litery alfabetu!'
    char_positions = func.split(' ')
    text = text.replace(' ', '')
    visual = [f'Litera {text[i]}: {char_positions[i]} pozycja' for i in range(0, len(char_positions))]
    for item in visual:
        print(item)


def test_if_a_text_is_a_string_and_have_spaces():
    text = "The sunset sets at twelve o' clock."

    result = alphabet_position(text, 'eng')

    assert result == "20 8 5 19 21 14 19 5 20 19 5 20 19 1 20 20 23 5 12 22 5 15 3 12 15 3 11"


def test_if_a_text_is_a_string_and_do_not_have_any_spaces():
    text = "The narwhal bacons at midnight."

    result = alphabet_position(text, 'eng')

    assert result == "20 8 5 14 1 18 23 8 1 12 2 1 3 15 14 19 1 20 13 9 4 14 9 7 8 20"


def test_if_text_is_represented_by_numbers():
    text = ''
    for i in range(10):
        text += str(i)

    result = alphabet_position(text, 'eng')

    assert result == ""


if __name__ == '__main__':
    is_done = False
    while not is_done:
        language = input('Podaj język tekstu (eng, pl itp.) lub wpisz "koniec" by zakończyć:\n')
        word = input('Podaj ciąg znaków lub wpisz "koniec" by zakończyć:\n')
        if language.lower() == 'koniec' or word.lower() == 'koniec':
            is_done = True
            break
        result = alphabet_position(word, language)
        print(represent_position(word, result))
