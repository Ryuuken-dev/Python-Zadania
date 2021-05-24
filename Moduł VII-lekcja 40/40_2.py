"""
Przygotuj klasę Emloyee, która w inice będzie odbierała imię, nazwisko oraz stawkę godzinową.
Przygotuj klasę Manager, która będzie dziedziczyła po klasie Employee, którego każda godzina
pracy będzie liczona podwójnie, a dodatkowo będzie możliwość określenia premii managera.
"""


class Employee:
    def __init__(self, name, surname, hour_rate: float):
        self.hour_rate = hour_rate
        self.surname = surname
        self.name = name


class Manager:
    def __init__(self, hour_rate: float):
        super().__init__()
        self.total_price = hour_rate * 2 * 160

    def add_bonus(self, amount: int):
        total = self.total_price * amount / 100
        return self.total_price + total

    def get_basic_salary(self):
        return self.total_price


zenek = Employee('Zenon', 'Kraal', 13)

ben = Manager(23)
bonus = 5
print(f'Podstawowe wynagrodzenie: {ben.get_basic_salary()}')
print(f'Wynagrodzenie wraz z premią: {ben.add_bonus(bonus)}')