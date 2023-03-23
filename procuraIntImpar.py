numbers = [2, 2, 3, 3, 3, 4, 4, 6, 6]


def impar(lista):
    conjunto = set(lista)

    for number in conjunto:
        count = 0
        for n in lista:
            if number == n:
                count += 1
        if count % 2 != 0:
            return number


print(impar(numbers))
