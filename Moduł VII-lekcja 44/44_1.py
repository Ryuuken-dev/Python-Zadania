"""
Dana jest klasa Person, która w konstruktorze odbiera imię i nazwisko. Bardzo często jednak
obiekty tej klasy tworzone są także z pliku CSV, którego wiersze wyglądają tak:
Jan;Kowalski
Zofia;Nowak
Krystyna;Krychowiak

Przygotuj metodę klasową o nazwie from_row, która będzie tworzyła nam obiekty klasy
Person wygodniej.
"""


class Person:
    def __init__(self, name: str, surname: str):
        self.surname = surname
        self.name = name

    @staticmethod
    def from_file(file: str):
        with open(file, 'r', encoding='utf-8') as file:
            lines = [line.strip('\n').replace(';', ' ').split(' ') for line in file]
            return lines

    @classmethod
    def from_row(cls, file: str, line: int):
        data = cls.from_file(file)
        try:
            if line <= 0 or line > len(data):
                raise IndexError('Podano niewłaściwy numer wiersza pliku!')
            human = cls(data[line - 1][0], data[line - 1][1])
            return f'{human.name} {human.surname}'
        except IndexError as error:
            print(error)


print(Person.from_row('names.csv', 4))



# {% if lista_filmow %}
#     <ul>
#     {% for film in lista_filmow %}
#         <li><b1>{{ film.tytul }}</b1></li>
#         <ul>
#             <li><b2>Opis: </b2>{{ film.opis }}</li>
#             <li><b2>Rok: </b2>{{ film.rok }}</li>
#             <li><b2>Premiera: </b2>{{ film.premiera }}</li>
#             <li><b2>imdb_rating: </b2>{{ film.imdb_rating }}</li>
#         </ul>
#     {% endfor %}
#     </ul>
# {% else %}
#     <p>Nie ma dostepnych filmow.</p>
# {% endif %}



# Moja templatka:
# {% load static %}
# <!DOCTYPE html>
# <html lang="pl">
# <head>
#     <meta charset="UTF-8">
#     <meta http-equiv="X-UA-Compatible" content="IE=edge">
#     <meta name="viewport" content="width=device-width, initial-scale=1.0">
#     <title>Document</title>
# </head>
# <body>
# <div class="wrapper">
#     {% if not lista_filmow|length %}
#     <h2 class="error">Brak filmów do wyświetlenia!</h2>
#     {% else %}
#     <nav class="navigationBar">
#         <h1>Filmy</h1>
#     </nav>
#
#     <main class="generalContent">
#         <table class="mainContent">
#             <thead class="mainContent__headerSection">
#             <tr class="mainContent__headings">
#                 <th class="mainContent__titleHeader">Tytuł</th>
#                 <th class="mainContent__ratingHeader">Ocena</th>
#                 <th class="mainContent__yearHeader">Rok produkcji</th>
#             </tr>
#             </thead>
#             <tbody>
#             {% for film in lista_filmow %}
#             <tr class="mainContent__film">
#                 <td class="mainContent__filmTitle">{{ film.tytul }}</td>
#                 {% if film.ocena == None %}
#                 <td class="mainContent__filmRating">-</td>
#                 {% else %}
#                 <td class="mainContent__filmRating">{{ film.ocena }}</td>
#                 {% endif %}
#                 <td class="mainContent__filmYear">{{ film.rok }}</td>
#             </tr>
#             {% endfor %}
#             </tbody>
#             <tfoot class="mainContent__footer">
#             <tr class="mainContent__quantityArea">
#                 <td class="mainContent__filmsQuantity">Ilość filmów: {{ lista_filmow|length }}</td>
#             </tr>
#             </tfoot>
#         </table>
#         {% endif %}
#     </main>
# </div>
# </body>
# </html>