"""
Массив размером 2m + 1, где m — натуральное число, заполнен случайным образом. Найдите в массиве медиану.
Медианой называется элемент ряда, делящий его на две равные части: в одной находятся элементы,
которые не меньше медианы, в другой — не больше медианы.
"""
import timeit
from random import choice, randint  # , random


def left_right(a, n):
    spam = choice(a)

    less = []
    for i in a:
        if i < spam:
            less.append(i)
    if len(less) > n:
        return left_right(less, n)
    n -= len(less)

    eqv = a.count(spam)
    if eqv > n:
        return spam
    n -= eqv

    more = []
    for i in a:
        if i > spam:
            more.append(i)
    return left_right(more, n)


def median(a):
    left_right(a, (len(a) + 1) // 2)
    right = left_right(a, (len(a) - 1) // 2)
    return right


MIN_VALUE = -100
MAX_VALUE = 99
M = 5
array = [randint(MIN_VALUE, MAX_VALUE) for _ in range(M * 2 + 1)]
# array = [random() * MAX_VALUE + MIN_VALUE for _ in range(2 * M + 1)] если массив вещественный
print(f'Исходный массив: {array}')
print(f'Отсортированный массив (для удобной проверки): {sorted(array)}')
print(f'Медиана: {median(array)}')

M = 1
while M != 1000:
    M *= 10
    array = [randint(MIN_VALUE, MAX_VALUE) for _ in range(M * 2 + 1)]
    print(timeit.timeit('median(array)', number=1000, globals=globals()))

"""
0.03678910000000002
0.3118098
2.8237444
"""
