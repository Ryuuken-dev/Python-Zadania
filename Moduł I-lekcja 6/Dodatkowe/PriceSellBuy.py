user_answer = input('Chcesz kupić czy sprzedać? (K/S): ')
if user_answer == 'K':
    money_value = float(input('Ilość posiadanej gotówki [zł]: '))
    print(f'Otrzymujesz {money_value / 3.8507:.2f} USD')
elif user_answer == 'S':
    money_value = float(input('Ilość posiadanej gotówki [zł]: '))
    print(f'Otrzymujesz {money_value * 3.8507:.2f} PLN')