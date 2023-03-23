def narcisist(value):
    sumList = [pow(int(number), len(str(value))) for number in str(value)]
    return True if sum(sumList) == value else False


print(narcisist(7))
