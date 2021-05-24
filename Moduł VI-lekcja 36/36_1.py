"""
Zaimplementuj klasę Circle, która w metodzie __init__ powinna odebrać promień koła.
Klasa ta powinna posiadać dwie metody liczące pole, a także obwód koła. Pamiętaj o testach.
Zapytaj użytkownika o promień koła i wyświetl jego pole i obwód.
"""
from math import pi
pi_data = pi


class Circle:
    def __init__(self, circle_radius, pi_val: float):
        self.circle_radius = circle_radius
        self.pi_val = pi_val

    def circle_area(self):
        return round(self.pi_val * self.circle_radius ** 2, 1)

    def circumference(self):
        return round(2 * self.pi_val * self.circle_radius, 1)


def test_if_circle_area_is_correct():
    radius = 10
    pi_value = 3.14
    circ = Circle(radius, pi_value)
    assert circ.circle_area() == 314


def test_if_circumference_is_correct():
    radius = 10
    pi_value = 3.14
    circ = Circle(radius, pi_value)
    assert circ.circumference() == 62.8


if __name__ == '__main__':
    users_radius = float(input('Podaj promień koła: '))
    circum = Circle(users_radius, pi_data)
    print(f'Pole koła: {circum.circle_area()}, Obwód koła: {circum.circumference()}')