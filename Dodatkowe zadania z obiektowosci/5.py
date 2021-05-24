"""
Utwórz klasę Schedule. Klasa ta powinna posiadać metodę
log_time(employee:Worker, minutes:int), której zadaniem będzie zbieranie informacji o
czasie pracy poszczególnych pracowników. Klasa ta powinna posiadać także metody umożliwiające zwrócenie informacji o tym
ile czasu pracowali poszczególni pracownicy oraz ile im się należy za tę pracę pieniędzy.
"""


class Worker:
    def __init__(self, name: str, surname: str, hourly_rate: float):
        self._hourly_rate = hourly_rate
        self.surname = surname
        self.name = name
        self.time_spent = 0

    def get_hourly_rate(self):
        return self._hourly_rate


class Schedule:
    def __init__(self):
        self.data = []
        self.selected_time = []
        self.selected_paid = []

    def log_time(self, employee: Worker, minutes):
        for worker in self.data:
            if worker == employee:
                worker.time_spent += minutes
                return

        employee.time_spent = minutes
        self.data.append(employee)

    def get_time(self, name='', surname=''):
        for obj in self.data:
            if name == obj.name or surname == obj.surname:
                return f'Imię: {obj.name}\nNazwisko: {obj.surname}\nCzas pracy: {obj.time_spent}\n'

    def get_paid(self, name='', surname=''):
        for obj in self.data:
            if name == obj.name or surname == obj.surname:
                return f'Imię: {obj.name}\nNazwisko: {obj.surname}\nWynagrodzenie: {obj.time_spent * obj.get_hourly_rate()}\n'


adam = Worker('Adam', 'Kowalski', 19.50)
piotr = Worker('Piotr', 'Wawrzynosek', 20.50)
roman = Worker('Roman', 'Wrzaskiewicz', 18.30)

summary = Schedule()
summary.log_time(adam, 160)
summary.log_time(piotr, 120)
summary.log_time(roman, 120)
print(summary.get_paid(surname='Kowalski'))


