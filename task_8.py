"""
Матрица 5x4 заполняется вводом с клавиатуры кроме последних элементов строк.
Программа должна вычислять сумму введенных элементов каждой строки
и записывать ее в последнюю ячейку строки. В конце следует вывести полученную матрицу.
"""

SIZE = 5
MIN_ITEM = 0
MAX_ITEM = 20
# вводим каждую строку матрицы на отдельной строчке, элементы разделяем пробелом
array = [list(map(int, input().split(' '))) for _ in range(SIZE)]
length = len(array[0])
for i in range(length + 1):
    s = 0
    for j in range(length):
        s += array[i][j]
    array[i].append(s)

for i in array:
    print(' '.join(list(map(str, i))))

print()
# вывод без использования join
for i in array:
    for j in i:
        print(j, end=' ')
    print()
