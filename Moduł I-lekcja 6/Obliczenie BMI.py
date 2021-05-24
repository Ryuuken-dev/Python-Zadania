# Obliczenie BMI
weight = int(input('Masa ciała[kg]: '))
height = int(input('Wzrost[cm]: ')) / 100
bmi = round(weight / (height ** 2), 2)

if bmi < 16:
    print(f'Wskaźnik BMI wynosi {bmi} i oznacza wygłodzenie. Życie takiej osoby jest zagrożone!')
elif 16 <= bmi < 16.99:
    print(f'Wskaźnik BMI wynosi {bmi} i oznacza wychudzenie (spowodowane zwykle przez ciężką chorobę lub anoreksję).')
elif 17 <= bmi < 18.49:
    print(f'Wskaźnik BMI wynosi {bmi} i oznacza niedowagę.')
elif 18.5 <= bmi < 24.99:
    print(f'Wskaźnik BMI wynosi {bmi} i oznacza wartość prawidłową.')
elif 25 <= bmi < 29.99:
    print(f'Wskaźnik BMI wynosi {bmi} i oznacza nadwagę.')
elif 30 <= bmi < 34.99:
    print(f'Wskaźnik BMI wynosi {bmi} i oznacza I stopień otyłości.')
elif 35 <= bmi < 39.99:
    print(f'Wskaźnik BMI wynosi {bmi} i oznacza II stopień otyłości.')
else:
    print(f'Wskaźnik BMI wynosi {bmi} i oznacza otyłość skrajną.')

#1.5 do 2.5

