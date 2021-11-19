"""
Пользователь вводит данные о количестве предприятий, их наименования и прибыль за 4 квартал (т.е. 4 числа)
для каждого предприятия. Программа должна определить среднюю прибыль (за год для всех предприятий)
и отдельно вывести наименования предприятий, чья прибыль выше среднего и ниже среднего.
"""
from collections import namedtuple

QUARTERS = 4
sum_profit = 0
profit = ['pr_1', 'pr_2', 'pr_3', 'pr_4']
Firm = namedtuple('Firm', 'name, profit, sum_pr')
firms = []
count_of_firms = int(input('Введите количество предприятий '))
for i in range(1, count_of_firms + 1):
    f = Firm(input(f'Введите наименование {i} предприятия '),
             [int(input(f'Введите прибыль за {i} квартал ')) for i in range(1, QUARTERS + 1)], 0)
    f = f._replace(sum_pr=sum(f.profit))
    firms.append(f)
for f in firms:
    sum_profit += sum(f.profit)
avg_profit = sum_profit / count_of_firms
print(f'Средняя прибыль предприятий за {QUARTERS} квартала: {avg_profit}')
print('Список предприятий, чья прибыль выше средней:')
for f in firms:
    if f.sum_pr > avg_profit:
        print(f.name)
print('Список предприятий, чья прибыль ниже средней:')
for f in firms:
    if f.sum_pr < avg_profit:
        print(f.name)
