"""
Przygotuj program, który odbierze od użytkownika dowolny string, a następnie zwróci słownik
zawierający informację ile razy wystąpiło każde słowo, np. "raz raz dwa trzy" powinno zwrócić
słownik {"raz": 2, "dwa": 1, "trzy": 1}
"""
users_text = input('Podaj dowolny tekst: ')
lower_text = users_text.lower()
lower_text = lower_text.split(" ")
data = {}
for text in lower_text:
    count = lower_text.count(text)
    data[text] = count
print(data)

