"""
Poszukaj innych funkcji niż upper i lower i spróbuj ze zdania:
"12 kilogramów jabłek, 10 kilogramów gruszek, 20 kilogramów śliwek"
policzyć ile łącznie razem ważą zakupione produkty (spacje przed kilogramami muszą być)
"""
sentence = '12 kilogramów jabłek, 10 kilogramów gruszek, 20 kilogramów śliwek'
words = sentence.split(' ')
total = 0
for word in words:
    if word.isnumeric():
        total += int(word)
print(f'Lączna waga towarów to {total}')
# words_list = words.split(' ')
# words_list.sort()
# words_list = words_list[0:3]
# value_1, value_2, value_3 = words_list
# sum_value = int(value_1 + value_2 + value_3)
# print(f'Produkty ważą {sum_value}')

