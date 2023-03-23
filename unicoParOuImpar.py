lista = [2, 4, 0, 100, 4, 11, 2602, 36]


def parOuImpar(seq):
    odd: list = [0, 0]
    even: list = [0, 0]
    for n in seq:
        if n % 2 == 0:
            even[0] += 1
            even[1] = n
        else:
            odd[0] += 1
            odd[1] = n
    if even[0] == 1:
        return even[1]
    else:
        return odd[1]


print(parOuImpar(lista))
