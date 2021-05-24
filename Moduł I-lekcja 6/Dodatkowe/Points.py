from math import sqrt
point_a_x = int(input('Podaj współrzędną X punktu A: '))
point_a_y = int(input('Podaj współrzędną Y punktu A: '))
point_b_x = int(input('Podaj współrzędną X punktu B: '))
point_b_y = int(input('Podaj współrzędną Y punktu B: '))
ab_distance = sqrt((point_b_x - point_a_x) ** 2 + (point_b_y - point_a_y) ** 2)
area_of_a_circle = 3.14 * (ab_distance / 2) ** 2
print(f'Pole okręgu opisanego na odcinku AB jest równe {area_of_a_circle}, a jego promień to {ab_distance / 2}')