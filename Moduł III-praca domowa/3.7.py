"""
Przygotuj funkcję, która zwróci największy wspólny dzielnik dla dwóch liczb
przekazanych w jej argumentach.
"""


def greatest_common_divisor(num_1: int, num_2: int) -> int:
    bigger = num_1 if num_1 >= num_2 else num_2
    return max([i if num_1 % i == 0 and num_2 % i == 0 else 0 for i in range(1, bigger + 1)])


print(greatest_common_divisor(25, 30))
