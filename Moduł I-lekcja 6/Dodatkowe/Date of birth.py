actual_year = 2021
user_year = int(input('Podaj swój rok urodzenia: '))
user_age = actual_year - user_year
if user_year % 4 == 0 and user_year % 100 != 0 and user_year % 400 == 0:
    print(f'{user_year} był rokiem przestępnym.')
elif user_age >= 18:
    print('Jesteś pełnoletni.')
elif user_year >= actual_year:
    print('Nie mamy jeszcze takiego roku lub podałeś obecny rok! Nie mogę ustalić Twojego wieku.')
elif user_year < actual_year:
    print(f'Masz {user_age} lat.')