def count_vowels(text):
    return sum([1 if char in 'aeyioąęuó' else 0 for char in text])


print(count_vowels('programowanie'))
