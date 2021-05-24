# Przygotuj funkcję, która usunie wszystkie samogłoski z przekazanego do funkcji napisu


def delete_vowels(word: str) -> str:
    vowels_list = ['a', 'e', 'y', 'i', 'o', 'ą', 'ę', 'u', 'ó', 'A', 'E', 'Y', 'I', 'O', 'Ą', 'Ę', 'U', 'Ó']
    new_word = word
    for vowel in vowels_list:
        if vowel in word:
            new_word = new_word.replace(vowel, "")
    return new_word


def test_word_with_vowels():
    assert delete_vowels('Hello World') == 'Hll Wrld'


def test_word_without_vowels():
    assert delete_vowels('Zs') == 'Zs'


def test_when_a_word_had_large_vowels():
    assert delete_vowels('Once Upon A Time I was in Yorkshire') == 'nc pn  Tm  ws n rkshr'





