"""
* Poproś użytkownika o datę rozpoczęcia, datę zakończenia, a także o jego dniówkę. W odpowiedzi powinna
wyświetlić się informacja ile użytkownik zarobi.
* Spróbuj wyświetlić za pomocą pętli wszystkie dni pomiędzy datami.
* Policz podwójnie wynagrodzenie pracownika za pracę w soboty i niedziele.
"""
from datetime import datetime, timedelta


start_date = input('Podaj datę rozpoczęcia pracy w formacie dd.mm.rrrr: ')
end_date = input('Podaj datę zakończenia pracy w formacie dd.mm.rrrr: ')
rate = float(input('Podaj stawkę za jeden dzień pracy: '))


first_day = datetime.strptime(start_date, '%d.%m.%Y')
final_day = datetime.strptime(end_date, '%d.%m.%Y')

diff = final_day - first_day

working_days = diff.days
project_day = first_day
for i in range(0, working_days + 1):
    if project_day.strftime('%a') in ['Sat', 'Sun']:
        working_days += 1
    print(f'Pracowałem: {project_day.strftime("%a, %d.%m.%Y")}')
    project_day += timedelta(days=1)

print(f'Zarobiłeś {working_days * rate}')










