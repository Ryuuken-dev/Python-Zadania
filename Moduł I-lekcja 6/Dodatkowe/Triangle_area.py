length_of_a_side = int(input('Podaj długość boku trójkąta równobocznego: '))
height_of_a_triangle = (length_of_a_side ** (1/3)) / 2
area_of_a_triangle = ((length_of_a_side ** 2) ** (1/3)) / 4
side_area_of_a_cone = 3.14 * (length_of_a_side / 2) ** 2
cone_capacity = (1/3) * side_area_of_a_cone * height_of_a_triangle
print(f'Pole trójkąta równobocznego wynosi {area_of_a_triangle:.1f}, a objętość stożka to {cone_capacity:.1f}')
