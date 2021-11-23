"""
Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив,
заданный случайными числами на промежутке [-100; 100).
Выведите на экран исходный и отсортированный массивы. Сортировка должна быть реализована в виде функции.
По возможности доработайте алгоритм (сделайте его умнее).
"""

# import timeit
from random import randint

MIN_VALUE = -100
MAX_VALUE = 99
array = [randint(MIN_VALUE, MAX_VALUE) for _ in range(10)]
print(f'Исходный массив: {array}')


def bubble_sort(a):
    spam_length = len(a)
    for n in range(spam_length - 1):
        for i in range(spam_length - n - 1):
            if a[i] < a[i + 1]:
                a[i], a[i + 1] = a[i + 1], a[i]
    return a


print(f'Отсортированный массив: {bubble_sort(array)}')

# size = 1
# while size != 1000:
#     size *= 10
#     array = [randint(-100, 99) for _ in range(size)]
#     print(timeit.timeit('bubble_sort(array)', number=1000, globals=globals()))

"""
0.017293699999999995
1.1274526
119.8524888
"""
