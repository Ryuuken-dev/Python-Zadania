"""
Przygotuj klasę Car, która powinna przechowywać nazwę samochodu oraz jego cenę
i maksymalną prędkość. Zapytaj użytkownika o 5 samochodów, a następnie wypisz je na ekranie w
kolejności od najdroższego do najtańszego oraz poniżej od najwolniejszej do najszybszej
prędkości.
"""


class Car:
    def __init__(self, car_name: str, car_price: int, max_speed: int):
        self.car_name = car_name
        self.car_price = car_price
        self.max_speed = max_speed
        self.data = [self.car_name, self.car_price, self.max_speed]

    def add_data(self):
        return self.data


cars = []
for num in range(1, 6):
    users_car_name = input('Podaj markę samochodu: ')
    users_car_price = int(input('Podaj cenę samochodu: '))
    users_car_speed = int(input('Podaj prędkość maksymalną samochodu: '))
    users_car = Car(users_car_name, users_car_price, users_car_speed)
    cars.append(users_car.add_data())

from_dearest = list(reversed(sorted(cars, key=lambda car: car[1])))
from_slower = sorted(cars, key=lambda car: car[2])
print(from_dearest)
print(from_slower)

