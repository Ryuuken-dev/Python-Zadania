# Na podstawie dwóch słów przygotuj zbiór znaków, które nie są dla nich wspólne.
name_1 = 'Bartek'
name_2 = 'Kacper'

print(set(name_1.lower()) ^ set(name_2.lower()))



