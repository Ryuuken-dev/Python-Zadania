"""
Przygotuj program, który będzie przechowywał listę zakupów. Każdy wpis jest osobnym
obiektem klasy ListItem. Jeśli dany produkt znajduje się już na liście nie powinien
być dodany drugi raz, zamiast tego powinna być zwiększana jego ilość. Produkty do
zakupienia przechowuj w zmiennej prywatnej.
"""


class Product:
    def __init__(self, name: str, price: float):
        self._price = price
        self._name = name

    def get_price(self):
        return self._price


class ListItem:
    def __init__(self, product: Product, quantity: float):
        self._quantity = quantity
        self._product = product

    def get_product_cost(self):
        return self._quantity * self._product.get_price()

    def get_product(self):
        return self._product

    def increase_quantity(self, quantity):
        self._quantity += quantity

    def decrease_quantity(self, quantity):
        self._quantity -= quantity


class List:
    def __init__(self):
        self._items = []

    def add_item(self, product: Product, quantity: float):
        for item in self._items:
            if item.get_product() == product:
                item.increase_quantity(quantity)
                return
        self._items.append(ListItem(product, quantity))

    def remove_item(self, product: Product, quantity: float):
        for item in self._items:
            if item.get_product() == product:
                item.decrease_quantity(quantity)
                return

    def list_items(self):
        return self._items

    def calculate_total_cost(self) -> float:
        pass







