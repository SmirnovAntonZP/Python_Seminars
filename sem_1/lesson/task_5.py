# Напишите программу, которая будет принимать на вход дробь и показывать первую цифру дробной части числа.

x = float(input('Vvedite drobnoe chislo'))
c=int((x-int(x))*10)
if c == 0:
    print('No')
print(c)