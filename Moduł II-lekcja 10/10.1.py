# Z podanej listy liczb policz te, które są podzielne przez 4 i te które są podzielne przez 5
numbers = [2, 9, 15, 12, 20, 55, 34, 40, 32, 28, 64, 13, 17, 18]
countable = []
for number in numbers:
    if number % 4 == 0 and number % 5 == 0:
        countable.append(number)
print(f'Liczba cyfr, które dzielą się przez 4 i 5 wynosi {len(countable)}')