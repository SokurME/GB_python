"""
Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
заданный случайными числами на промежутке [0; 50). Выведите на экран исходный и отсортированный массивы.
"""

# import timeit
from random import random


def merge_sort(a, start, end):
    if end - start > 1:
        mid = (start + end) // 2
        merge_sort(a, start, mid)
        merge_sort(a, mid, end)
        merge_list(a, start, mid, end)


def merge_list(a, start, mid, end):
    left = a[start:mid]
    right = a[mid:end]
    k = start
    i = 0
    j = 0
    while start + i < mid and mid + j < end:
        if left[i] <= right[j]:
            a[k] = left[i]
            i = i + 1
        else:
            a[k] = right[j]
            j = j + 1
        k = k + 1
    if start + i < mid:
        while k < end:
            a[k] = left[i]
            i = i + 1
            k = k + 1
    else:
        while k < end:
            a[k] = right[j]
            j = j + 1
            k = k + 1


MIN_VALUE = 0
MAX_VALUE = 50
array = [random() * MAX_VALUE + MIN_VALUE for _ in range(10)]
print(f'Исходный массив: {array}')
merge_sort(array, 0, len(array))
print(f'Отсортированный массив: {array}')

# size = 1
# while size != 1000:
#     size *= 10
#     array = [random() * MAX_VALUE + MIN_VALUE for _ in range(size)]
#     print(timeit.timeit('merge_sort(array,0, len(array))', number=1000, globals=globals()))

"""
0.0289441
0.43687269999999995
6.5181178
"""
