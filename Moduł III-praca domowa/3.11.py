"""
Przygotuj funkcję, która odbierze dwa punkty w postaci tupli (x, y). Wynikiem powinna być długość odcinka
utworzonego w wyniku połączenia tych dwóch punktów.
"""
from typing import Tuple
from math import sqrt


def get_episode_length(point_1: Tuple[int, int], point_2: Tuple[int, int]) -> int:
    return int(sqrt((point_2[0] - point_1[0]) ** 2 + (point_2[1] - point_1[1]) ** 2))


print(get_episode_length((1, 1), (1, 1)))