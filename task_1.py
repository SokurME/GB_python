# Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.

a = int(input('Введите трехзначное число '))
s = 0
p = 1
s += a % 10
p *= a % 10
a //= 10
s += a % 10
p *= a % 10
a //= 10
s += a % 10
p *= a % 10
print(f'Сумма цифр {s}')
print(f'Произведение цифр {p}')
