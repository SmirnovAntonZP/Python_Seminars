# Напишите программу, которая принимает на вход число N и выдаёт последовательность из N членов.
# *Пример:*
#
# - Для N = 5: 1, -3, 9, -27, 81

x = int(input('Vvedite naturalnoe chislo: '))
for i in range(x):
    print((-3)**i, end=' ')