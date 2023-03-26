def last_digit(n1, n2):
    return (n1 ** (n2 % 4 + 4)) % 10
    # return pow(n1, n2, 10)


print(last_digit(2, 321656516546546549849516165198))
