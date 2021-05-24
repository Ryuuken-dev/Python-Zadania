import sqlite3

with sqlite3.connect('library.db') as connection:
    cursor = connection.cursor()
    cursor.execute('''CREATE TABLE books(
    book_id INTEGER PRIMARY KEY AUTOINCREMENT,
    title VARCHAR(100) UNIQUE NOT NULL,
    author VARCHAR(100),
    pages_number VARCHAR(4),
    isbn_number VARCHAR(17),
    print VARCHAR(30),
    release_date VARCHAR(4)
    )''')
    connection.commit()
