# Przygotuj program, który będzie sprawdzał czy dwa podane słowa są wzajemnymi palindromami lub anagramami
word_1 = 'Ala'
word_2 = 'Kęs'
m_word = ''
for i in range(len(word_1) - 1, -1, -1):
    m_word += word_1[i]
print(m_word)


