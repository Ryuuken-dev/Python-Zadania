"""
Policz wynagrodzenie zatrudnionego sprzedawcy, który zarabia 2000zł za pomocą skróconej wersji ifa.
Zapytaj go o staż pracy, ilość przepracowanych godzin i ilość sprzedanych towarów.
"""
basic_salary = 2000
internship = int(input('Podaj swój staż pracy: '))
numbers_of_hours = int(input('Podaj ilość przepracowanych godzin w tygodniu: '))
goods = int(input('Podaj ilość sprzedanych towarów: '))

internship_addition = 0.10 if internship > 2 else 0.02 * internship
sale_bonus = 0.25 if goods > 30 else 0
active_bonus = 0.08 if numbers_of_hours > 160 and internship > 1 else 0.02

final_salary = basic_salary + (basic_salary * internship_addition + basic_salary * sale_bonus + basic_salary * active_bonus)
print(f'Finalnie zarabiasz {final_salary} PLN')
