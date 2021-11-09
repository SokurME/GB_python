"""
Определить, какое число в массиве встречается чаще всего.
"""

import random

SIZE = 20
MIN_ITEM = 0
MAX_ITEM = 20
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)

max_count = 1
max_el = array[0]
length = len(array)
for i in range(length - 1):
    spam_count = 1
    for j in range(i + 1, length):
        if array[i] == array[j]:
            spam_count += 1
            if spam_count > max_count:
                max_count = spam_count
                max_el = array[i]
print(f'Число {max_el} встречается чаще всего ({max_count} раз(а))')

# если элементы встречаются одинаковое количество раз, то выводится первое число
