"""
Przygotuj funkcję, która będzie szukała wspólnych dzielników dla dwóch liczb.
Funkcja posiada trzeci argument domyślny określający wartość początkową, gdzie
największy wspólny dzielnik musi być zawsze większy niż ta wartość.
"""


def common_divisors(num_1, num_2, div=2):
    smaller = num_1 if num_1 <= num_2 else num_2
    divisors = set()
    for i in range(2, smaller + 1):
        if num_1 % i == 0 and num_2 % i == 0 and i > div:
            divisors.add(i)
    if len(divisors) == 0:
        return 0
    return divisors


print(common_divisors(3, 6))


