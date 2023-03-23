s = None
d = ''
f = '<<^^~>>///'
h = 'a'
o = 'sTreSS'


def first_non_repeating_letter(string: str):    
    stringLow = string.lower()
    for i, letter in enumerate(stringLow):
        if stringLow.count(letter) == 1:
            return string[i]
    return ''

# print(first_non_repeating_letter(s))
# print(first_non_repeating_letter(d))
# print(first_non_repeating_letter(f))
# print(first_non_repeating_letter(h))
print(first_non_repeating_letter(o))
