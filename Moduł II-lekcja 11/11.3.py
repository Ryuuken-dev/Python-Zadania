# Policz ile razy w zdaniu "Pies to najlepszy przyjaciel człowieka, lecz nie każdy pies o tym wie" wystąpiło słowo "pies"
words = 'Pies to najlepszy przyjaciel człowieka, lecz nie każdy pies o tym wie'.lower()
counter = []
list_words = words.split(' ')
for word in list_words:
    if word == 'pies':
        counter.append(1)
print(f'W tekście "Pies to najlepszy przyjaciel człowieka, lecz nie każdy pies o tym wie" słowo "pies" występuje {len(counter)} razy')

