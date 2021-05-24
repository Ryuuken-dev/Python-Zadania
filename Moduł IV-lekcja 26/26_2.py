"""
Sformatuj listę osób tak, aby imiona i nazwiska były zapisane z wielkiej litery:
people = ['zofia nowak', 'kryStyna kowalska', 'michał lewandowski']
A następnie posortuj te osoby według pierwszej litery nazwiska.
"""
people = ['zofia nowak', 'kryStyna kowalska', 'michał lewandowski']


def capitalize(word) -> list:
    return word[0].upper() + word[1:].lower()


def add_big_letters(persons: list) -> list:
    persons = map(lambda person: person.lower(), persons)
    persons = map(lambda person: person.split(' '), persons)
    persons = map(lambda person: capitalize(person[0]) + ' ' + capitalize(person[1]), persons)
    persons = sorted(persons, key=lambda person: person.split(' ')[1])
    return list(persons)


def test_if_words_are_sorted():
    persons = ['Mark Twain', 'Jack Sparrow', 'Mark Zuckerberg']
    assert add_big_letters(persons) == ['Jack Sparrow', 'Mark Twain', 'Mark Zuckerberg']


def test_if_letters_of_name_and_surname_are_big():
    persons = ['adam mickiewicz', 'henryk sienkiewicz', 'licia troisi']
    assert add_big_letters(persons) == ['Adam Mickiewicz', 'Henryk Sienkiewicz', 'Licia Troisi']


if __name__ == '__main__':
    print(f'Przed posortowaniem: {people}')
    print(f'Posortowana lista: {add_big_letters(people)}')
