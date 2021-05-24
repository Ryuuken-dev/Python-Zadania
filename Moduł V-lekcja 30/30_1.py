"""
Przygotuj program, który wyświetli datę Twoich następnych urodzin oraz odpowie na pytanie
ile musisz czekać na nie dni. Jeśli dzień Twoich urodzin w danym roku już minął powinna
pokazać się data w roku następnym.
"""
from datetime import date

is_done = True
while is_done:
    birth_mon = int(input('Podaj miesiąc urodzin (1-12): '))
    birth_day = int(input('Podaj dzień urodzin (1-31): '))
    if 1 <= birth_mon <= 12 and 1 <= birth_day <= 31:
        is_done = False
    else:
        continue
    today = date.today()
    birthday = date(today.year, birth_mon, birth_day)

    if birthday > today:
        diff = today - birthday
        print(f'Do dnia Twoich następnych urodzin pozostało {diff.days} dni')
        print(f'Będzie to dzień: {birthday.strftime("%A")}')

    else:
        next_date = date(today.year + 1, birth_mon, birth_day)
        print(f'Następna data Twoich urodzin to {next_date}')
