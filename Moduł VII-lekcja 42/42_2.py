"""
Przygotuj słownik zawierający 3 wartości. Sprawdź co się stanie, jeśli spróbujesz odwołać się do klucza, który
nie istnieje w tym słowniku. Spróbuj obsłużyć taką sytuację łapiąc taki wyjątek.
"""

person = {
    "Imię": 'John',
    "Nazwisko": 'Wick',
    "Zawód": 'Szpieg'
}
try:
    print(person["Profesja"])
except KeyError:
    print('Niewłaściwa wartość')