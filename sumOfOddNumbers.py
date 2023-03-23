def row_sum_odd_numbers(n):
    qtdSumNumbers = sum([i + 1 for i in range(n)])
    setOddNumbers = [number for number in range(qtdSumNumbers * 2) if number % 2 != 0]
    sumNlastNumbers = sum([number for number in setOddNumbers[qtdSumNumbers - n : qtdSumNumbers]])
    return sumNlastNumbers


row_sum_odd_numbers(3)