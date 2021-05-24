"""
Przygotuj funkcję, która odbierze argument, który określa ile kolejnych wyrazów ciągu Fibonacciego
ta funkcja zwróci. Ciąg Fibonacciego to taki ciąg, gdzie każdy kolejny wyraz jest sumą
dwóch poprzednich.
"""


def fibonacci_sequence(items: int) -> list:
    result = []
    if items <= 0:
        return 0
    for i in range(0, items):
        if i == 0 or i == 1:
            result.append(i)
            continue
        result.append(result[-2] + result[-1])
    return result


print(fibonacci_sequence(1))
