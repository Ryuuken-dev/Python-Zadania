"""
Korzystając z rekurencji wyświetl sumę wyrazów ciągu Fibonacciego
fibonacci_sum(10) powinno zwrócić:
1 + 1 + 2 + 3 + 5 + 8 + 13 + 21 + 34 + 55
"""


# def fibonacci_sum(num: int):
#     if num <= 0:
#         return None
#     result = []
#     counter = 0
#     if len(result) == 0 or len(result) == 1:
#         result.append(counter)
#     elif len(result) > 1:
#         result.append(result[len(result) - 2] + result[len(result) - 1])
#     counter += 1
#     if counter > num:
#         return sum(result)
#
#     fibonacci_sum(num)


def fibonacci_sum(num):
    if num == 0:
        return 0
    return num + fibonacci_sum(num - 1)


def test_if_the_summary_of_fibonacci_sequence_is_correct():
    numbers_of_words = 10
    result = fibonacci_sum(numbers_of_words)
    assert result == 143


if __name__ == '__main__':
    number = 5
    print(fibonacci_sum(number))
