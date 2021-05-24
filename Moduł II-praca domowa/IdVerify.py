# Przygotuj program weryfikujący czy numer PESEL jest prawidłowy
users_pesel = tuple(input('Podaj numer PESEL: '))
char_count = 0
if len(users_pesel) < 11:
    print('Zbyt krótki PESEL!')
    quit()

for i in range(0, 11):
    if i == 0 or i == 4 or i == 8 or i == 10:
        char_count += int(users_pesel[i]) * 1
    elif i == 1 or i == 5 or i == 9:
        char_count += int(users_pesel[i]) * 3
    elif i == 2 or i == 6:
        char_count += int(users_pesel[i]) * 7
    else:
        char_count += int(users_pesel[i]) * 9

if char_count % 10 == 0:
    print('Numer PESEL jest prawidłowy!')
else:
    print('Nieprawidłowy numer PESEL!')




# mnożenie przez 1: 1, 5, 9 i 11 cyfra
# mnożenie przez 3: 2, 6, 10
# mnożenie przez 7: 3, 7
# mnożenie przez 9: 4, 8
# jeśli ostatnia cyfra sumy iloczynów wynosi zero to pesel jest poprawny
# 12345678909