"""
Na podstawie danych udotępnionych bezpłatnie przez:
https://danepubliczne.imgw.pl/apiinfo
Przygotuj skrypt, który wyświetli informację o temperaturze oraz ciśnieniu
w mieście najbliższym miejscu Twojego zamieszkania.
"""
from urllib.request import urlopen
from json import loads

with urlopen('https://danepubliczne.imgw.pl/api/data/synop') as site:
    weather = loads(site.read().decode('utf-8'))
    users_city = input('W jakim mieście mieszkasz? ')
    city_data = [value for value in weather if value["stacja"] == users_city]
    if len(city_data) == 0:
        print('Nie wiem jaka jest pogoda w tym mieście!')
    else:
        print(f'Miasto: {users_city}\n-Temperatura: {city_data[0]["temperatura"]}\n-Ciśnienie: {city_data[0]["cisnienie"]}')
