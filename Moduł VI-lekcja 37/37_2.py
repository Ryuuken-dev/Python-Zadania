class Basket:
    def __init__(self):
        self.fruits = []

    def add_fruit(self, color, taste, sort):
        self.fruits.append([color, taste, sort])

    def get_result(self):
        return self.fruits


class Report:
    def __init__(self, fruits_list):
        self.fruits_list = fruits_list

    def filter_fruits(self, find):
        number = 0
        for fruit in self.fruits_list:
            if find in fruit:
                number += 1
        return f'Liczba owoców: {number}'


basket = Basket()
basket.add_fruit('czerwony', 'słodki', 'dojrzały')
basket.add_fruit('czerwony', 'słodki', 'dojrzały')
basket.add_fruit('zielony', 'kwaśny', 'niedojrzały')
basket.add_fruit('żółty', 'słodki', 'niedojrzały')
report = Report(basket.get_result())
print(report.filter_fruits('czerwony'))

