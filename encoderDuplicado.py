def duplicate_encode(word: str):
    newWord = ''
    for letter in word:
        if word.count(letter.lower()) == 1:
            newWord += '('
        else:
            newWord += ')'
    return newWord


print(duplicate_encode('Success'))

# def duplicate_encode(word):
#     return "".join(
#       ["(" if word.lower().count(c) == 1 else ")" for c in word.lower()]
#       )
