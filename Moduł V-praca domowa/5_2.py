"""
Pytaj użytkownika o nazwy produktów tak długo, aż nie napisze słowa "koniec".
Zapisz wówczas do pliku o nazwie według wzoru ddmmrrrr.txt tylko unikatowe nazwy
wprowadzonych przez niego produktów.
"""

products = set()
is_done = False
while not is_done:
    answer = input('Podaj nazwę produktu lub wpisz "koniec" by zakończyć: ').lower()
    if answer != 'koniec':
        products.add(answer)
    else:
        is_done = True
with open('24042021.txt', 'a') as file:
    for product in products:
        file.write(product + '\n')


