"""
2). Написать два алгоритма нахождения i-го по счёту простого числа.
Функция нахождения простого числа должна принимать на вход натуральное и возвращать соответствующее простое число.
Проанализировать скорость и сложность алгоритмов.
Первый — с помощью алгоритма «Решето Эратосфена».
Примечание. Алгоритм «Решето Эратосфена» разбирался на одном из прошлых уроков.
Используйте этот код и попробуйте его улучшить/оптимизировать под задачу.
Второй — без использования «Решета Эратосфена».
"""

import cProfile
import timeit


def prime(n):
    if n % 2 == 0:
        return False
    j = 3
    while n % j != 0 and j * j <= n:
        j += 2
    return j * j > n


def prime_num(num):
    spam_num = 1
    _i = 3
    while spam_num != num:
        if prime(_i):
            spam_num += 1
        _i += 1
    return _i - 1


# получение данных о времени выполнения
# with open('1.txt', 'w') as f:
#     i = 1
#     while i < 4097:
#         time_it = str(timeit.timeit("prime_num(i)", number=100, globals=globals()))
#         f.write(f'{str(i)} {time_it}' '\n')
#         i *= 2

"""
номер   время выполнения        
1       2.839999999999787e-05
2       0.00010980000000000018
4       0.0003779999999999964
8       0.0011380000000000001
16      0.005060300000000004
32      0.018485300000000003
64      0.0319098
128     0.0902059
256     0.2044312
512     0.6894585
1024    1.5068934
2048    4.3736413999999995
4096    12.167337100000001
"""

cProfile.run('prime_num(1000)')
# 7921 function calls in 0.019 seconds
# Ordered by: standard name
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.019    0.019 <string>:1(<module>)
#      7917    0.015    0.000    0.015    0.000 task_2.py:15(prime)
#         1    0.004    0.004    0.019    0.019 task_2.py:24(prime_num)
#         1    0.000    0.000    0.019    0.019 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

cProfile.run('prime_num(5000)')
# 48613 function calls in 0.230 seconds
# Ordered by: standard name
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.230    0.230 <string>:1(<module>)
#     48609    0.205    0.000    0.205    0.000 task_2.py:15(prime)
#         1    0.025    0.025    0.230    0.230 task_2.py:24(prime_num)
#         1    0.000    0.000    0.230    0.230 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

"""
Решение задачи с помощью решета Эратосфена
"""


def sieve_1(num):
    _arr = (4, 25, 168, 1229, 9592, 78498, 664579)
    i = 0
    while num > _arr[i]:
        i += 1
    k = 10 ** (i + 1)
    sieve = [i for i in range(k)]
    sieve[1] = 0

    for i in range(2, k):
        if sieve[i] != 0:
            j = i + i
            while j < k:
                sieve[j] = 0
                j += i
    res = [i for i in sieve if i != 0]
    return res[num - 1]


# получение данных о времени выполнения
# with open('1.txt', 'w') as f:
#     i = 1
#     while i < 4097:
#         time_it = str(timeit.timeit("sieve_1(i)", number=100, globals=globals()))
#         f.write(f'{str(i)} {time_it}' '\n')
#         i *= 2

"""
номер   время выполнения 
1       0.0005040000000000044
2       0.0004930999999999686
4       0.000489200000000023
8       0.004079200000000005
16      0.007685900000000023
32      0.07648100000000002
64      0.09247349999999999
128     0.06924889999999995
256     1.1855912
512     1.0505011000000002
1024    0.7153042999999997
2048    8.3805333
4096    8.418694700000001

При таких входных данных сложно оценить линейность функции, так как время зависит от диапазона (список _arr), 
в который попадает номер элемента
"""

# я решила взять для замера времени середину каждого диапазона
# print(2, timeit.timeit("sieve_1(2)", number=100, globals=globals()))  # 0.000530899999997558
# print(14, timeit.timeit("sieve_1(14)", number=100, globals=globals()))  # 0.00706830000000024
# print(96, timeit.timeit("sieve_1(96)", number=100, globals=globals()))  # 0.0536840999999981
# print(698, timeit.timeit("sieve_1(698)", number=100, globals=globals()))  # 1.28864869999999
# print(5410, timeit.timeit("sieve_1(5410)", number=100, globals=globals()))  # 9.79103489999999

cProfile.run('sieve_1(1000)')
# 6 function calls in 0.010 seconds
# Ordered by: standard name
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.010    0.010 <string>:1(<module>)
#         1    0.008    0.008    0.010    0.010 task_2.py:84(sieve_1)
#         1    0.000    0.000    0.000    0.000 task_2.py:90(<listcomp>)
#         1    0.001    0.001    0.001    0.001 task_2.py:99(<listcomp>)
#         1    0.000    0.000    0.010    0.010 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

cProfile.run('sieve_1(5000)')
# 6 function calls in 0.094 seconds
# Ordered by: standard name
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.001    0.001    0.093    0.093 <string>:1(<module>)
#         1    0.082    0.082    0.093    0.093 task_2.py:84(sieve_1)
#         1    0.005    0.005    0.005    0.005 task_2.py:90(<listcomp>)
#         1    0.006    0.006    0.006    0.006 task_2.py:99(<listcomp>)
#         1    0.000    0.000    0.094    0.094 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


print(timeit.timeit("prime_num(50000)", number=100, globals=globals()))  # 699.0595625
print(timeit.timeit("sieve_1(50000)", number=100, globals=globals()))  # 101.67404579999993

"""
Вывод: оба алгоритма имеют линейную асимптотику (для значений до 4000-5000, дальше не проверяла).   
Но скорость выполнения методом решета Эратосфена намного быстрее для больших значений (это видно на диаграмме 2). 
Например, для номера 5000 скорость выше в 2,44 раза, а для номера 50000 - в 6,9 раза. 
Большое количество вызовов функции prime() в первом примере необходимо.
"""
