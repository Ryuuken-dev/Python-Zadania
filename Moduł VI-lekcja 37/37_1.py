class Authors:
    def __init__(self):
        self.authors = []

    def add_items(self, name: str, surname: str, date_of_birth: str):
        self.authors.append([name, surname, date_of_birth])

    def get_elements(self):
        res = ''
        for i in range(0, len(self.authors)):
            for x in range(0, len(self.authors[i])):
                res += self.authors[i][x] + ', '
        return res


class Book:
    def __init__(self, title: str, grade: str, des: str, sm: str, rate: float, author='Authors'):
        self.title = title
        self.grade = grade
        self.author = author
        self.des = des
        self.sm = sm
        self.rate = rate

    def get_elements(self):
        return f'Tytuł: {self.title}\nGatunek: {self.grade}\nAutor: {self.author}\nOpis: {self.des}\nInfo: {self.sm}\nOcena: {self.rate}'


auth = Authors()
for _ in range(2):
    auth.add_items('Adam', 'Mickiewicz', '12-04-2021')

book = Book('300', 'Kryminał', 'Krwawy', 'Akcja', 8.5, auth.get_elements())
print(book.get_elements())

