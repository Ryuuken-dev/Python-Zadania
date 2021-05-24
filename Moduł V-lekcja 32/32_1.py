"""
1. Plik csv to plik, w którym kolumny rozdzielone są średnikami. Możesz je odczytać za pomocą funkcji split().
    Z pliku transakcje.txt wybierz tylko te, które mają dodatnią wartość i zapisz je do osobnego pliku o nazwie
    przychody.txt
2. Napisz program, który otworzy plik przychody.txt, odczyta
    wartości zapisane w kolejnych wierszach i wyświetli ich sumę.
"""

summary = 0
with open('przychody.txt', 'r') as income:
    for item in income:
        if item == '\n':
            continue
        item = item.strip('\n')
        summary += int(item)

print(f'Suma przychodów to {summary}')
