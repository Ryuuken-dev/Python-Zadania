from math import sqrt
x_a = int(input('Podaj współrzędną X wierzchołka A: '))
y_a = int(input('Podaj współrzędną Y wierzchołka A: '))
x_b = int(input('Podaj współrzędną X wierzchołka B: '))
y_b = int(input('Podaj współrzędną Y wierzchołka B: '))
x_c = int(input('Podaj współrzędną X wierzchołka C: '))
y_c = int(input('Podaj współrzędną Y wierzchołka C: '))
triangle_area = ((x_b - x_a) * (y_c - y_a) - (y_b - y_a) * (x_c - x_a)) / 2
ab_value = sqrt((x_b - x_a) ** 2 + (y_b - y_a) ** 2)
bc_value = sqrt((x_c - x_b) ** 2 + (y_c - y_b) ** 2)
ac_value = sqrt((x_c - x_a) ** 2 + (y_c - y_a) ** 2)
triangle_circuit = ab_value + bc_value + ac_value
print(f'Pole trójkąta o wierzchołkach ABC wynosi {triangle_area:.1f}, a jego obwód to {triangle_circuit:.1f}')
