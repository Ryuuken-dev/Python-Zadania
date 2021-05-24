"""
Przygotuj mini program do zarządzania Twoimi oszczędnościami. Starasz się wpłacać pieniądze
z różnych źródeł, chcesz na bieżąco wiedzieć, ile udało Ci się już zaoszczędzić.
"""
from datetime import datetime


class Saving:
    def __init__(self, date: datetime, saving_value: float):
        self._saving_value = saving_value
        self._date = date

    @property
    def saving(self):
        return self._saving_value

    @saving.setter
    def saving(self, value):
        if value > 0:
            self._saving_value += value

    @property
    def get_date(self):
        return self._date

    @get_date.setter
    def get_date(self, date):
        self._date = date


class Savings:
    def __init__(self):
        self.savings = []

    def add_saving(self, saving: Saving):
        self.savings.append(saving)

    @property
    def collection(self):
        total = ''
        for item in self.savings:
            total += f'Oszczędności: {item.saving}\tData: {item.get_date}\n'
        return total

    @property
    def total(self):
        summary = 0
        for item in self.savings:
            summary += item.saving
        return f'Razem: {summary}'


saving = Saving(datetime(2021, 4, 12), 120.64)
saving_2 = Saving(datetime(2021, 5, 12), 1200.64)
saving.saving = 1200
saving.get_date = datetime(2021, 5, 13)
savings = Savings()
savings.add_saving(saving)
savings.add_saving(saving_2)
print(savings.collection)
print(savings.total)