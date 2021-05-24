# Napisz program, który odwróci wyrazy w zdaniu


def reverse_letters(word: str) -> str:
    words_list = word.split(' ')
    digits = ''
    single_word = ''
    for item in words_list:
        for letter in item[::-1]:
            if not letter.isalpha():
                digits += letter
                continue
            single_word += letter
        if len(digits):
            single_word += digits
            digits = digits.strip(digits[0])
        single_word += ' '
    return single_word


if __name__ == '__main__':
    test_word = 'ilśeJ ycsyzsw ąlśym kat ,omas ot śotk ein ilśym elacw'
    res = reverse_letters(test_word)
    print(res)