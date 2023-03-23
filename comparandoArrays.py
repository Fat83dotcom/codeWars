import numpy as np

a: list = []
b: list = []


def comp(array1, array2):
    print(array1)
    print(array2)
    if array1 is not None and array2 is not None:
        array1.sort()
        array2.sort()
        bN = np.array(array2)
        c = [x*x for x in array1]
        c.sort()
        cN = np.array(c)
        return np.array_equal(bN, cN)
    return False


print(comp(a, b))

print(b is not None)
