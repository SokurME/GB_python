"""
В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
Сами минимальный и максимальный элементы в сумму не включать.
"""

import random

SIZE = 20
MIN_ITEM = 0
MAX_ITEM = 20
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)

ind_max = 0
ind_min = 0
for i in range(1, len(array)):
    if array[i] > array[ind_max]:
        ind_max = i
    elif array[i] < array[ind_min]:
        ind_min = i
if ind_max < ind_min:
    t = ind_max  # или ind_min, ind_max = ind_max, ind_min
    ind_max = ind_min
    ind_min = t
summa = 0
for i in range(ind_min + 1, ind_max):
    summa += array[i]
print(f'Сумма элементов, находящихся между {ind_min + 1}-ым (max) и {ind_max - 1}-ым (min) равна {summa}')
