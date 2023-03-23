def make_negative(number):
    return number if number <= 0 else 0 - number


print(make_negative(23))
print(make_negative(-1))
print(make_negative(0))
print(make_negative(-34))