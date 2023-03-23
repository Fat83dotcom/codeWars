def xO(s: str):
    x = s.lower().count('x')
    o = s.lower().count('o')

    if x == 0 and o == 0 or (x != 0 and o != 0) and (x == o):
        return True
    else:
        return False


print(xO('dfdfsdf'))
