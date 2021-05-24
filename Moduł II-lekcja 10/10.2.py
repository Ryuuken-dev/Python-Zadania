# Z podanej listy imion o różnej długości znajdź to, które jest najkrótsze i to, które jest najdłuższe
names = ['Ralph', 'Victoria', 'Lily', 'James', 'Andrew', 'Aurelia', 'Amelia', 'Jack']
name_data = []
for name in names:
    name_data.append(len(name))
name_max = max(name_data)
name_min = min(name_data)
for name in names:
    if len(name) == name_max:
        print(f'Imię {name} jest najdłuższe')
    elif len(name) == name_min:
        print(f'Imię {name} jest najkrótsze')

