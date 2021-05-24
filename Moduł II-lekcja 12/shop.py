products = {
    'Zestaw dwóch maczet': 80,
    'Japońska katana': 2000,
    'Nóż motylkowy': 50,
    'Pałka teleskopowa': 70,
    'Paralizator': 200,
    'Wiatrówka "Winchester"': 300,
    'Rewolwer "Magnum"': 250
}
merchant_money = 3000
buyer_money = 1500
users_answer = input('Witaj w moim sklepie! Chciałbyś kupić czy sprzedać? (K/S): ').lower()
if users_answer == 'k':
    print(f'Twoje złoto: {buyer_money} \n')
    for product in products:
        print(f'Nazwa: {product} *** Cena: {products[product]}')
    print('')
    product_to_buy = input('Co podać? ')
    if product_to_buy not in products:
        print('Nie mamy tej rzeczy, wróć później!')
        quit()
    how_many = int(input('Podaj ilość: '))
    money_out = products[product_to_buy] * how_many
    print(f'Do zapłaty: {money_out} PLN')
    if buyer_money < money_out:
        print('Nie stać Cię na ten przedmiot!')
    else:
        buyer_money -= money_out
        print(f'Pozostało Ci {buyer_money} PLN w portfelu')
elif users_answer == 's':
    print(f'Złoto sklepikarza: {merchant_money} \n')
    sell_thing = input('Co chciałbyś sprzedać? ')
    thing_cost = int(input('Podaj cenę: '))
    thing_value = int(input('Podaj ilość: '))
    total_cost = thing_cost * thing_value
    if total_cost > merchant_money:
        print('Nie stać mnie na ten przedmiot.')
    else:
        print(f'Dobijmy targu. Oto Twoje złoto: {total_cost} PLN')
        merchant_money -= thing_cost
        print(f'Złoto sklepikarza: {merchant_money} \n')