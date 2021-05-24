"""
Przygotuj funkcję, która będzie odbierała argumenty w postaci:
group_them(wall="red", tomato="red", light="yellow", lemon="yellow", grass="green")
W odpowiedzi funkcja powinna wyświetlić (w osobnych wierszach)
Wall is red \n Tomato is red \n Light is yellow itd.
"""


def group_them(**kwargs):
    values = kwargs
    words = ''
    for val in values:
        words += val.capitalize() + ' is ' + values[val] + '\n'
    return words


print(group_them(wall='red', tomato='red', light='yellow', lemon='yellow', grass='green'))
