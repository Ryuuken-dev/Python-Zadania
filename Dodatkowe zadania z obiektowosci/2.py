"""
Przygotuj klasę Student, która przyjmie rok urodzenia oraz imię.
Klasa ta powinna posiadać metody umożliwiające odpowiedź na pytanie ile student ma lat. Skorzystaj z:

from datetime import datetime
today = datetime.today()
today.year
"""
from datetime import datetime


class Student:
    def __init__(self, name, year):
        self.name = name
        self.year = year
        self.today = datetime.today().year

    def get_years(self):
        return self.today - self.year


def test_actual_student_age():
    name = 'Bartek'
    year = 1993

    student = Student(name, year)

    assert student.get_years() == 28
