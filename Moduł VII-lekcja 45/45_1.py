"""
Przygotuj klasę Product, która w inicie pozwoli odebrać cenę i będzie posiadała zadeklarowane metody
calculate_netto i calculate_brutto.

Przygotuj klasę Booking, która w inicie pozwoli odebrać datę początkową i datę końcową oraz metodę liczącą
ilość dni pomiędzy datami get_difference.

Utwórz klasę Reservation, która będzie dziedziczyła po klasie Product oraz Booking, pozwoli na określenie ceny jednego
dnia, wskazanie daty początku i końca, będzie posiadała jedną dodatkową metodę wyliczającą koszt pobytu.
"""
from datetime import datetime


class Product:
    def __init__(self, price: float):
        self.price = price
        self.vat = 0.23

    @property
    def calculate_brutto(self):
        return self.price + self.price * self.vat

    @property
    def calculate_netto(self):
        return self.price

    def change_vat(self, vat: float):
        self.vat = vat

    @property
    def get_vat(self):
        return self.vat


class Booking:
    def __init__(self, begin_date: datetime, end_date: datetime):
        self.end_date = end_date
        self.begin_date = begin_date

    def get_difference(self):
        timedelta = self.end_date - self.begin_date
        return timedelta.days


class Reservation(Product, Booking):
    def __init__(self, price: float, begin_date: datetime, end_date: datetime):
        Product.__init__(self, price)
        Booking.__init__(self, begin_date, end_date)

    @property
    def get_date(self):
        begin = self.begin_date.strftime('%d.%m.%y')
        end = self.end_date.strftime('%d.%m.%y')
        return f'Data przybycia: {begin} *** Zakończenie pobytu: {end}'

    @property
    def total_cost(self):
        return self.get_difference() * self.calculate_brutto


def test_begin_and_end_data_of_reservation():
    price = 123.0
    begin = datetime(2021, 2, 21)
    end = datetime(2021, 2, 24)

    res = Reservation(price, begin, end)

    assert res.get_date == 'Data przybycia: 21.02.21 *** Zakończenie pobytu: 24.02.21'


def test_total_cost_of_residence():
    price = 123.0
    begin = datetime(2021, 2, 21)
    end = datetime(2021, 2, 24)

    res = Reservation(price, begin, end)

    assert res.total_cost == 453.87

