import cProfile
import timeit
import random

"""
1). Проанализировать скорость и сложность одного любого алгоритма из разработанных
в рамках домашнего задания первых трех уроков.
Примечание. Идеальным решением будет:
● выбрать хорошую задачу, которую имеет смысл оценивать (укажите в комментарии какую задачу вы взяли),
● написать 3 варианта кода (один у вас уже есть),
● проанализировать 3 варианта и выбрать оптимальный,
● результаты анализа вставить в виде комментариев в файл с кодом
(не забудьте указать, для каких N вы проводили замеры),
● написать общий вывод: какой из трёх вариантов лучше и почему.
"""

"""
Матрица 5x4 заполняется вводом с клавиатуры кроме последних элементов строк.
Программа должна вычислять сумму введенных элементов каждой строки
и записывать ее в последнюю ячейку строки. В конце следует вывести полученную матрицу.
"""


# 1-ый способ
def func_1(array, length):
    for i in range(length):
        s = 0
        for j in range(length - 1):
            s += array[i][j]
        array[i].append(s)
    return array


s1 = 30
arr1 = [[random.randint(0, s1) for j in range(s1 - 1)] for i in range(s1)]
print(func_1(arr1, s1))

# получение данных о времени выполнения
# with open('2.txt', 'w') as f:
#     size = 10
#     while size <= 500:
#         arr = [[random.randint(0, size) for j in range(size - 1)] for i in range(size)]
#         time_it = str(timeit.timeit("func_1(arr, size)", number=100, globals=globals()))
#         f.write(f'{str(size)} {time_it}' '\n')
#         size += 10

"""
10 0.002124799999999996
100 0.23100569999999998
200 0.7791848000000003
300 1.7355360000000033
400 3.3450732000000016
500 5.686817599999998
"""


# 2-й способ (использование sum)
def func_2(array, length):
    for i in range(length):
        array[i].append(sum(array[i]))
    return array


s1 = 30
arr2 = [[random.randint(0, s1) for j in range(s1 - 1)] for i in range(s1)]
print(func_1(arr2, s1))

# получение данных о времени выполнения
# with open('2.txt', 'w') as f:
#     size = 10
#     while size <= 500:
#         arr = [[random.randint(0, size) for j in range(size - 1)] for i in range(size)]
#         time_it = str(timeit.timeit("func_2(arr, size)", number=100, globals=globals()))
#         f.write(f'{str(size)} {time_it}' '\n')
#         size += 10

"""
10 0.0032042000000000043
100 0.050797800000000004
200 0.12583770000000016
300 0.23289440000000017
400 0.38091010000000125
500 0.5675202000000006
"""


# 3-й способ (enumerate)
def func_3(array, size):
    for i, item in enumerate(array):
        array[i][size - 1] = sum(item)
    return array


s3 = 30
arr3 = [[random.randint(0, s3) if j < s3 - 1 else 0 for j in range(s3)] for i in range(s3)]
print(func_3(arr3, s3))

# получение данных о времени выполнения
# with open('2.txt', 'w') as f:
#     size = 10
#     while size <= 500:
#         arr = [[random.randint(0, size) if j < size - 1 else 0 for j in range(size)] for i in range(size)]
#         time_it = str(timeit.timeit("func_3(arr,size)", number=100, globals=globals()))
#         f.write(f'{str(size)} {time_it}' '\n')
#         size += 10

"""
10 0.0005425999999999903
100 0.025565100000000007
200 0.10002789999999995
300 0.13007219999999986
400 0.27316690000000143
500 0.3592733000000017
"""

size = 500
arr = [[random.randint(0, size) if j < size - 1 else 0 for j in range(size)] for i in range(size)]
cProfile.run('func_1(arr, size)')
"""
504 function calls in 0.049 seconds
Ordered by: standard name
ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.049    0.049 <string>:1(<module>)
        1    0.049    0.049    0.049    0.049 task_1.py:25(func_1)
        1    0.000    0.000    0.049    0.049 {built-in method builtins.exec}
      500    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
"""

cProfile.run('func_2(arr, size)')
"""
1004 function calls in 0.004 seconds
Ordered by: standard name
ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.004    0.004 <string>:1(<module>)
        1    0.000    0.000    0.004    0.004 task_1.py:58(func_2)
        1    0.000    0.000    0.004    0.004 {built-in method builtins.exec}
      500    0.004    0.000    0.004    0.000 {built-in method builtins.sum}
      500    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
"""

cProfile.run('func_3(arr, size)')
"""
504 function calls in 0.004 seconds
Ordered by: standard name
ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.003    0.003 <string>:1(<module>)
        1    0.000    0.000    0.003    0.003 task_1.py:88(func_3)
        1    0.000    0.000    0.004    0.004 {built-in method builtins.exec}
      500    0.003    0.000    0.003    0.000 {built-in method builtins.sum}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
"""

"""
Ассимптотика всех программ - квадратичная, так как работа проводится с матрицей. 
Резкое уменьшение времени дало использование встроенной функции sum (как я поняла, написанная на С).
В третьем способе я сначала применила только enumerate, но сокращение времени практически не было, тогда я попробовала 
при создании матрицы сразу добавлять последнюю ячейку, содержащую ноль, что дало выигрыш при выполнении функции, 
но создание самой матрицы будет выполняться чуть дольше. Соответственно, можно еще посмотреть, что будет приоритетнее.
"""
