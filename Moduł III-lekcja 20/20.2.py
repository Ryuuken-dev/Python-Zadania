"""
Przygotuj funkcję, która na podstawie czasu pracy, ilości zużywanych kilowatogodzin odpowie ile zapłacę za prąd, który
zużywa urządzenie. Domyślny koszt 1kwh to 0.617.
"""
working_time = int(input('Czas pracy urządzenia [min]: '))
how_much_energy = int(input('Ilość zużywanych kWh: '))
energy_cost = 0.617


def energy_bill(time, energy, cost):
    time = round(time / 60, 1)
    return (energy * time) * cost


print(f'Rachunek za prąd wynosi {energy_bill(working_time, how_much_energy, energy_cost):.2f} ')
