"""
Pytaj użytkownika o nazwy 10 owoców, jeżeli dany owoc znajduje się już na liście to powinien zostać wyrzucony
wyjątek i program powinien przestać pytać.
"""
fruits = []

try:
    for _ in range(1, 11):
        fruit = input('Podaj nazwę owocu: ')
        if fruit in fruits:
            raise Exception(f'{fruit} znajduje się już na liście!')
        fruits.append(fruit)

except Exception as error:
    print(error)

print('Posiadane owoce:')
for id, fruit in enumerate(fruits, start=1):
    print(f'{id}. {fruit}')
