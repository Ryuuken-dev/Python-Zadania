"""
Zadanie jest następujące. Przy użyciu języka Python, należy znaleźć najmniejszą oraz największa liczbę na liście.
"""


class Collection:
    def __init__(self):
        self.numbers = []
        self.all = []

    def format(self, data: str):
        data_list = data.split(',')
        for word in data_list:
            self.numbers.append(int(word))

    def generate(self):
        for i in range(self.numbers[0], self.numbers[1] + 1):
            self.all.append(i)
        if self.numbers[1] < 0:
            for i in range(self.numbers[0], self.numbers[1] - 1, -1):
                self.all.append(i)


class Numbers:
    def __init__(self, collection: Collection):
        self.the_biggest = 0
        self.the_smallest = 0
        self.collection = collection

    def smallest_filter(self):

        self.the_smallest = self.collection.all[0]
        for number in self.collection.all:
            if number < self.the_smallest:
                self.the_smallest = number
        return self.the_smallest

    def biggest_filter(self):
        self.the_biggest = self.collection.all[0]
        for number in self.collection.all:
            if number > self.the_biggest:
                self.the_biggest = number
        return self.the_biggest


def test_if_numbers_filter_works_correctly_for_the_min_value():
    numbers_list = [2, 10, -2, 9, 67]

    result = Numbers()

    assert result.smallest_filter(numbers_list) == -2


def test_if_numbers_filter_works_correctly_for_the_max_value():
    numbers_list = [2, 10, -2, 9, 67]

    result = Numbers()

    assert result.biggest_filter(numbers_list) == 67


if __name__ == '__main__':

    while True:
        users_numbers = input('Podaj przedział liczbowy(od 0 do 100: 0, 100): ')
        if users_numbers == 'koniec':
            break
        numbers_collection = Collection()

        numbers_collection.format(users_numbers)
        numbers_collection.generate()

        values = Numbers(numbers_collection)
        print(f'Najmniejsza liczba: {values.smallest_filter()}')
        print(f'Największa liczba: {values.biggest_filter()}')
