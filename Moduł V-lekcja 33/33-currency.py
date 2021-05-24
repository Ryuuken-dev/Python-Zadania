from urllib.request import urlopen
from json import loads


with urlopen('http://api.nbp.pl/api/exchangerates/tables/A/') as site:
    data = loads(site.read().decode('utf-8'))
    print(data[0]["rates"])

    users_currency = input('Jaką wartość chcesz wymienić na złotówki? ').upper()
    while ' ' not in users_currency:
        users_currency = input('Podaj wartość rozdzieloną spacją, np. 12 USD ')
    data_table = users_currency.split(' ')
    filter_currency = [value for value in data[0]["rates"] if value["code"] == data_table[1]]
    print(f'Otrzymujesz {round(float(data_table[0]) * filter_currency[0]["mid"], 2)} PLN')