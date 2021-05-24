"""
Dana jest klasa Item, która posiada dekorator @dataclass i pozwala na tworzenie obiektów z właściwościami takimi jak:
name(str), price(float), discount(float) oraz klasa Collection, która pozwala na dodawanie do niej obiektów:
collection = Collection()
collection.items.append(item)

Przygotuj metodę klasową, która umożliwi stworzenie kolekcji wraz z elementami w taki sposób:
Collection.create_with_items(item1, item2, item3)
"""
from dataclasses import dataclass


@dataclass
class Item:
    name: str
    price: float
    discount: float = 0.0


class Collection:
    def __init__(self):
        self.items = []

    @classmethod
    def create_with_items(cls, *args: Item):
        collection = cls()                  # Przypisujemy aktualną klasę (Collection) do collection
        collection.items.extend(args)       # Wskazujemy items w klasie Collection i dodajemy wszystkie args do tablicy
        return collection


a1 = Item("Book", 50.0)
a2 = Item("Notebook", 10.0, 0.2)
a3 = Item("Pencil", 100.0)
c = Collection.create_with_items(a1, a2, a3)
print(c.items)
