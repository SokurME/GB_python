"""
Найти максимальный элемент среди минимальных элементов столбцов матрицы.
"""

import random

SIZE = 5
MIN_ITEM = 0
MAX_ITEM = 20
array = [[random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE + 1)] for _ in range(SIZE)]
for i in array:
    for j in i:
        print(f'{j:4d}  ', end=' ')
    print()

# находим min в первом столбце
max_of_min = array[0][0]
for j in range(len(array[0])):
    if array[0][j] < max_of_min:
        max_of_min = array[0][j]

# находим остальные min и среди них max
for j in range(len(array[0])):
    spam_min = array[0][j]
    for i in range(1, len(array)):
        if array[i][j] < spam_min:
            spam_min = array[i][j]
    if spam_min > max_of_min:
        max_of_min = spam_min
print("Максимальный элемент среди минимальных элементов столбцов матрицы: ", max_of_min)
