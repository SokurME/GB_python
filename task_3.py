"""По введенным пользователем координатам двух точек вывести уравнение прямой вида y = kx + b,
проходящей через эти точки."""

x1=float(input('Введите абсциссу первой точки '))
y1=float(input('Введите ординату первой точки '))
x2=float(input('Введите абсциссу второй точки '))
y2=float(input('Введите ординату второй точки '))
if x1==x2:
    print(f'Уравнение прямой имеет вид 0 = x - {x1:.2f}')
else:
    k=(y2-y1)/(x2-x1)
    b=y1-k*x1
    print(f'Уравнение прямой имеет вид y = {k:.2f}x + {b:.2f}')