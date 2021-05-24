"""
Program pozwala na dodawanie książek do bazy danych SQLite z poziomu konsoli Pythona.
Można w ten sposób stworzyć swoją własną "domową bibliotekę"
"""


import sqlite3

is_done = False
while not is_done:
    action = input('Co chcesz zrobić? [d]odaj / [w]yświetl / [k]oniec').lower()

    if action == 'w':
        with sqlite3.connect('library.db') as connection:
            cursor = connection.cursor()
            for book in cursor.execute(
                    'SELECT book_id, title, author, pages_number, isbn_number, print, release_date FROM books'):
                book_id, title, author, pages_number, isbn_number, pr, release_date = book
                print(f'Id: {book_id}, Tytuł: {title}, Autor: {author}, Strony: {pages_number}, ISBN: {isbn_number}, Wydawnictwo: {pr}, Data wydania: {release_date}')

    elif action == 'd':
        with sqlite3.connect('library.db') as connection:
            cursor = connection.cursor()
            title = input('Tytuł: ')
            author = input('Autor: ')
            pages = input('Liczba stron: ')
            isbn = input('Numer ISBN: ')
            publish = input('Wydawnictwo: ')
            r_date = input('Data wydania: ')
            cursor.execute('INSERT INTO books(title, author, pages_number, isbn_number, print, release_date) VALUES(?, ?, ?, ?, ?, ?)',
                       (title, author, pages, isbn, publish, r_date))
            connection.commit()

    elif action == 'k':
        is_done = True

