"""
Przygotuj program, który wartości zapisane w systemie dwójkowym będzie zamieniał na wartości
dziesiętne i odwrotnie
"""
users_answer = int(input('Wybierz rodzaj konwersji: \n'
                     'System dwójkowy na system dziesiętny (1) \n'
                     'System dziesiętny na system dwójkowy (2) \n'))

counter = 0
result = 0
int_result = ''
if users_answer == 1:
    bin_number = input('Podaj liczbę w systemie dwójkowym: ')
    bin_number2 = list(bin_number)
    counter = len(bin_number2) - 1
    for number in bin_number2:
        result += int(number) * 2 ** counter
        counter -= 1
    print(f'Liczba {bin_number} w systemie dziesiętnym to {result}')
elif users_answer == 2:
    int_number = int(input("Podaj liczbę w systemie dziesiętnym: "))
    to_divide = int_number
    divide_results = ()
    while to_divide >= 1:
        divide = to_divide // 2
        divide_results += tuple(str(to_divide % 2))
        to_divide = divide
    divide_results = tuple(reversed(divide_results))
    final_result = ''
    for result in divide_results:
        final_result += result
    print(f'Liczba {int_number} to {final_result} w systemie dwójkowym')


