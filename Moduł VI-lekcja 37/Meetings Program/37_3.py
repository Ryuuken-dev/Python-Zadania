"""
Przygotuj program, który będzie przechowywał wszystkie Twoje spotkania.
Informacje o spotkaniach przechowuj w pliku meetings. json.

Wymagania:
Każde ze spotkań trwa zawsze godzinę
Spotkania mogą mieć różne tytuły
Na dany dzień, na daną godzinę może być zapisane tylko jedno spotkanie
Kalendarz posiada metody umożliwiające:
    1. Wyświetlanie wszystkich spotkań (posortowanych po dacie)
    2. Sprawdzenie czy dany termin (data i godzina) jest wolny
    3. Znalezienie następnej wolnej godziny w określonej dacie
"""
from json import dump
from datetime import date


class Meetings:
    def __init__(self):
        self.meet_data = []

    def add_meet(self, title: str, date, hour):
        with open('meetings.json', 'a') as self.meet_data:
            dump({"Tytuł": title, "Data": date, "Godzina": hour}, self.meet_data)


class Calendar:
    def __init__(self, meetings=Meetings):
        self.meetings = meetings


meet = Meetings()
meet.add_meet("Raporty", str(date(2020, 4, 12)), 14)
meet.add_meet("Deadline", str(date(2020, 4, 14)), 12)
print(meet.meet_data)
