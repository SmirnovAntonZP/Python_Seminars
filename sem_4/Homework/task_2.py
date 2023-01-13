#Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N

N = int(input('Введите натуральное число '))
multiplier = []
while N < 0:
    print('Это не натуральное число')
    N = int(input('Введите натуральное число '))
x = 2
while x * x <= N:
    if N % x == 0:
        multiplier.append(x)
        N//=x
    else:
        x+=1
if N >  1:
    multiplier.append(N)
print(multiplier)