"""
Przygotuj program, który będzie szyfrował i odszyfrowywał wyrażenia korzystając z szyfru Cezara. Mogą Ci się przydać
funkcje ord() oraz chr()
"""
word = 'glmny'.lower()
word_crypted = str()
step = 2
# print(ord(word))
# print(chr(79))
for char in word:

    if ord(char) < 97 - step or ord(char) > 122 + step:
        continue
    char_num = chr(ord(char) + 3)
    word_crypted += str(char_num)
    if ord(char) > 122 - step:

        word_crypted += str(crypt)
print(word_crypted)
