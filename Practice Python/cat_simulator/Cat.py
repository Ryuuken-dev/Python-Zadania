from Box import Box
from random import choice


class Cat:
    def __init__(self):
        self.results = []

    def verify(self, box: Box):
        cat_reaction = choice([1, 2, 3])
        self.box = box
        if cat_reaction == 1 or cat_reaction == 3:
            self.box.toy["Odrzucenia"] += 1
        elif cat_reaction == 2:
            self.box.toy["Polubienia"] += 1
        self.results.append(self.box.toy)

    def get_results(self):
        for value in self.results:
            print(f'-- Zabawka: {value["Zabawka"]} Polubienia: {value["Polubienia"]} Odrzucenia: {value["Odrzucenia"]}')
    