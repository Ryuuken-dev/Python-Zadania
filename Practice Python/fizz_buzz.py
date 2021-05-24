"""
Wypisz liczby od 1 do 100, przy czym liczby podzielne przez 3 zastąp słowem ‘Fizz’, liczby podzielne przez 5
zastąp słowem ‘Buzz’, natomiast liczby podzielne i przez 3 i przez 5 zastąp słowem ‘FizzBuzz’.

A w rezultacie, powinniśmy otrzymać – 1, 2, Fizz, 4, Buzz, 6, 7, 8, Fizz, Buzz, 11, Fizz, 13, 14, FizzBuzz, 16 itd
"""


class Numbers:
    def __init__(self, min_number: int, max_number: int):
        self.min_number = min_number
        self.max_number = max_number

    def fizz_buzz(self):
        final = []
        for number in range(self.min_number, self.max_number + 1):
            if number % 3 == 0 and number % 5 == 0:
                final.append('FizzBuzz')
            elif number % 3 == 0:
                final.append('Fizz')
            elif number % 5 == 0:
                final.append('Buzz')
            else:
                final.append(number)
        return final


numbers = Numbers(1, 100)
print(numbers.fizz_buzz())


