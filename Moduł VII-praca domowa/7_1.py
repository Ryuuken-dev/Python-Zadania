"""
1. Stwórz klasę BaseEmployee umożliwiającą przechowywanie imienia, nazwiska oraz
daty zatrudnienia. Jeśli użytkownik poda datę późniejszą niż data dzisiejsza lub wskazującą
na czas pracy dłuższy niż 50 lat to wyrzuć wyjątek InvalidDateOfEmployment. Dodaj metody
specjalne umożliwiające sortowanie względem długości zatrudnienia.

2. Utwórz w klasie BaseEmployee metodę employment_time, która będzie posiadała dekorator
property. Metoda ta powinna każdorazowo zwracać informację, ile dni pracuje dany
pracownik (od początku).

3. Utwórz klasę Employee, która będzie dziedziczyła po klasie BaseEmployee, klasa ta
powinna posiadać stawkę godzinową, wymiar etatu (np. pełen etat to 160 godzin), oraz
wartość premii pracownika. Przygotuj metodę wyliczającą wartość jego wynagrodzenia.

4. W klasie Employee utwórz metody klasowe create_fulltime oraz create_part_time
tworzące odpowiednio pracownika pełnoetatowego oraz pracownika, który pracuje na pół
etatu.
"""
from datetime import datetime
from math import floor


class InvalidDateOfEmployment(Exception):
    pass


class BaseEmployee:
    def __init__(self, name: str, surname: str, date_of_employment: datetime):
        try:
            self.date_of_employment = date_of_employment
            self.surname = surname
            self.name = name
            if date_of_employment > datetime.today() or self.work_time > 50:
                raise InvalidDateOfEmployment()

        except InvalidDateOfEmployment:
            print('Niewłaściwa data zatrudnienia!')

    @property
    def work_time(self):
        diff = datetime.today() - self.date_of_employment
        return floor(diff.days / 365)

    @property
    def employment_time(self):
        diff = datetime.today() - self.date_of_employment
        return diff.days


class Employee(BaseEmployee):
    def __init__(self, name, surname, date_of_employment, hourly_rate: float, response: str, bonus: float):
        super().__init__(name, surname, date_of_employment)
        self.bonus = bonus
        self.response = response
        self.hourly_rate = hourly_rate

    @property
    def __get_response(self):
        dataset = {'full-time': 160,
                   '1/2': 80,
                   '3/4': 120}
        return dataset[self.response]

    def get_salary(self, worker: BaseEmployee):
        added_bonus = self.hourly_rate * self.bonus
        return f'{worker.name} zarobił {self.__get_response * self.hourly_rate + added_bonus}'

    @classmethod
    def create_full_time_worker(cls, name: str, surname: str, date: datetime, hourly: float, full: str, bonus: float):
        worker = cls(name, surname, date, hourly, full, bonus)
        return worker

    @classmethod
    def create_part_time_worker(cls, name: str, surname: str, date: datetime, hourly: float, full: str, bonus: float):
        worker = cls(name, surname, date, hourly, full, bonus)
        return worker





