how_many_liquid = int(input('Ilość cieczy [ml]: '))
number_of_bottles = how_many_liquid / 330
remained_liquid = (330 * 0.12) * number_of_bottles

if number_of_bottles < 1:
    print('Za mało cieczy by napełnić przynajmniej jedną butelkę!')
else:
    print(f'Ilość cieczy, która pozostała to {remained_liquid}')