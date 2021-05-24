# Odbierz od użytkownika 10 adresów e-mail i wyświetl je poniżej bez duplikatów.
emails = set()
for i in range(1, 11):
    users_email = input(f'Podaj {i} adres e-mail: ')
    emails.add(users_email)
print(f'Twoje adresy email: {emails}')
