# Przygotuj zbiór liczb podzielnych przez 3 oraz zbiór liczb podzielnych przez 5, znajdź część wspólną obu zbiorów.
numbers_divide_by_3 = set([])
numbers_divide_by_5 = set([])
for i in range(1, 1001):
    if i % 3 == 0:
        numbers_divide_by_3.add(i)
    if i % 5 == 0:
        numbers_divide_by_5.add(i)
print(f'Część wspólna dla zbiorów to {numbers_divide_by_3 & numbers_divide_by_5}')

