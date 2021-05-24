"""
Create a program that asks the user to enter their name and their age.
Print out a message addressed to them that tells them the year that they will turn 100 years old.
"""
users_name = input('Podaj swoje imię: ')
users_age = int(input('Podaj swój wiek: '))


def year_of_age_100_count(age, actual_year=2021):
    return actual_year + (100 - age)


if users_age == 100:
    print('Jesteś już stulatkiem!')
while users_age <= 0:
    users_age = int(input('Podaj swój wiek: '))
print(f'{users_name}, 100 lat osiągniesz w {year_of_age_100_count(users_age)} roku')
