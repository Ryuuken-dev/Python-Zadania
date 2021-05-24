"""
Na podstawie API przygotuj aplikację, która zapyta użytkownika o nazwę Państwa, a następnie wyświetli jego stolicę.
"""
from urllib.error import HTTPError, URLError
from urllib.request import urlopen
from json import loads

country_data = {}
while True:
    country = input('Podaj nazwę państwa lub wpisz "koniec" by zakończyć: ')
    if country in country_data.keys():
        print(f'Kraj: {country} *** Stolica kraju: {country_data[country]}')
        continue
    if country == 'koniec':
        break
    try:
        with urlopen(f'htps://restcountries.eu/rest/v2/name/{country}') as site:
            data = loads(site.read().decode('utf-8'))
            country_data[country] = data[0]["capital"]
            print(f'Kraj: {data[0]["name"]} *** Stolica kraju: {data[0]["capital"]}')

        # for item in data:
        #     if country not in item['name']:
        #         raise HTTPError(f'{country} nie znajduje się na liście!')
    except HTTPError:
        print(f'{country} nie znajduje się na liście!')

    except URLError:
        print('You do not have an internet connection!')

# with urlopen('https://restcountries.eu/rest/v2/all') as site:
#     data = loads(site.read().decode('utf-8'))
#     # print(f'Kraj: {data[0]["name"]}***Stolica: {data[0]["capital"]}')
#     for value in data:
#         print(value)


# data = [{"name": 'Adam', "age": 16}, {"name": 'Wojtek', "age": 24}]
# answer = input('Imię: ')
# values = []
# for item in data:
#     if answer == item["name"]:
#         values.append(item)
# print(f'{answer} ma {values[0]["age"]} lat.')
