"""
Jeśli tupla ma parzystą ilość elementów to zsumuj wszystkie elementy, a jeśli ilość jest nieparzysta to
policz ich średnią. Wyklucz wszystkie tuple zawierające mniej niż 2 lub więcej niż 6 elementów.
"""
weapons = [
    (1, ),
    (2, 3),
    (4, 5, 6, 7, 8, 9, 10),
    (11, ),
    (12, 13, 14),
    (15, 16, 17)
]
new_list = [weapon for weapon in weapons if 2 <= len(weapon) <= 6]
final_list = [sum(new) if len(new) % 2 == 0 else sum(new) / len(new) for new in new_list]
print(final_list)