"""
Написать программу сложения и умножения двух положительных целых шестнадцатеричных чисел.
При этом каждое число представляется как коллекция, элементы которой — цифры числа.
Например, пользователь ввёл A2 и C4F. Нужно сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].
"""

from collections import deque

BASE = 16
BASE_10 = 10
hex_dict = dict(zip([str(i) for i in range(10)] + ['A', 'B', 'C', 'D', 'E', 'F'], [i for i in range(16)]))
hex_dict_inv = {value: key for key, value in hex_dict.items()}


def hex_sum(x, y):
    answer = deque()
    memory = 0
    y.extendleft('0' * (len(x) - len(y)))
    for i in range(len(y) - 1, -1, -1):
        spam_sum = hex_dict[x[i]] + hex_dict[y[i]] + memory
        if spam_sum > BASE:
            answer.appendleft(hex_dict_inv[spam_sum - BASE])
            memory = 1
        else:
            answer.appendleft(hex_dict_inv[spam_sum])
            memory = 0
    if memory == 1:
        answer.appendleft('1')
    return answer


a = input('Введите первое число: ')
b = input('Введите второе число: ')
if len(a) < len(b):
    c, d = deque(b), deque(a)
else:
    c, d = deque(a), deque(b)
print(f'Сумма чисел {list(a)} и {list(b)} равна {list(hex_sum(c, d))}')


# Если считать в шестнадцатеричной системе, то только сложением, как вариант - сделать через десятичную.
def hex_mult(x, y):
    answer_mult = deque()
    x_10 = 0
    for i in x:
        x_10 = x_10 * BASE + hex_dict[i]
    y_10 = 0
    for i in y:
        y_10 = y_10 * BASE + hex_dict[i]
    spam_mult = x_10 * y_10
    while spam_mult > 0:
        answer_mult.appendleft(hex_dict_inv[spam_mult % BASE])
        spam_mult //= BASE
    return answer_mult


# a = input('Введите первое число: ')
# b = input('Введите второе число: ')
c, d = deque(b), deque(a)
print(f'Произведение чисел {list(a)} и {list(b)} равно {list(hex_mult(c, d))}')
