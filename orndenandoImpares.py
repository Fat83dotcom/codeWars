a = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
b = [3, 5, 2, 8, 1, 4]
c = [2, 4, 66, 24, 44, 6, 7, 99, 3, 1, 5, 999, 33, 11]


def sort_array(array):
    firstOdd = int()
    flag = True
    for index in range(len(array)):
        if array[index] % 2 != 0:
            if flag:
                firstOdd = index
                flag = False
            key = array[index]
            count = index - 1
            while count >= firstOdd:
                if array[count] % 2 != 0 and array[count] > key:
                    keyAux = key
                    array[index] = array[count]
                    index = count
                    key = array[count] = keyAux
                count -= 1
    return array
                



    


sort_array(a)
sort_array(b)
sort_array(c)

print(a)
print(b)
print(c)


# void insertionSort(int *vetor, int tamanhoVetor){
#     int i, j, chave;
#     for ( j = 1; j < tamanhoVetor; j++){
#         chave = vetor[j];
#         i = j - 1;
#         while (i >= 0 && vetor[i] > chave){
#             vetor[i + 1] = vetor[i];
#             i--;
#         }
#         vetor[i + 1] = chave;
#     }
# }