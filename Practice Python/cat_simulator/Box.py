from random import choice


class Box:
    def __init__(self):
        self.toy = {}
        self.toy_list = []

    def unpack(self):
        with open('toys.txt', encoding='utf8') as file:
            for toy in file:
                toy.strip('\n')
                self.toy_list.append({"Zabawka": toy,
                                      "Polubienia": 0,
                                      "Odrzucenia": 0})

    def add_toy(self):
        self.toy = (choice(self.toy_list))