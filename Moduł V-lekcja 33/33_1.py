"""
Napisz program zarządzający bazą książek w Twojej domowej bibliotece. Program powinien umożliwić
znalezienie i dodanie nowej książki. Przechowuj je w pliku books.json
"""

from json import load, dump


with open('books.json', encoding='utf8') as file:
    books = load(file)

choice = input('Dostępne polecenia: [w]ypisz/[d]odaj').lower()

if choice == 'w':
    print(books["name"])
    for value in books["books"]:
        print(f'-{value["author_name"]} {value["author_surname"]}, {value["title"]}')
elif choice == 'd':
    name = input('Podaj imię autora: ')
    surname = input('Podaj nazwisko autora: ')
    book_title = input('Podaj tytuł książki: ')
    books["books"].append({
        "id": len(books["books"]) + 1,
        "author_name": name,
        "author_surname": surname,
        "title": book_title
    })
    with open('books.json', 'w', encoding="utf8") as in_file:
        dump(books, in_file)






