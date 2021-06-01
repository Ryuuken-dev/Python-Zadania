"""
Write a function that takes in a string of one or more words, and returns the same string, but with all five or more
letter words reversed (like the name of this kata).

Strings passed in will consist of only letters and spaces.
Spaces will be included only when more than one word is present.

Examples:

spinWords("Hey fellow warriors") => "Hey wollef sroirraw"
spinWords("This is a test") => "This is a test"
spinWords("This is another test") => "This is rehtona test"
"""


def word_reverse(word: str) -> str:
    elements = word.split(' ')
    result = [element if len(element) < 5 else element[::-1] for element in elements]
    return ' '.join(result)


def test_if_letter_have_less_than_five_chars():
    word = 'This is an test'

    result = word_reverse(word)

    assert result == 'This is an test'


def test_if_letter_have_five_or_more_chars():
    word = 'Hey fellow warriors'

    result = word_reverse(word)

    assert result == "Hey wollef sroirraw"


if __name__ == '__main__':
    print(word_reverse("Welcome"))


