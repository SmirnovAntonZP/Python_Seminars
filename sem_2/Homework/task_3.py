# 3. Задайте список из n чисел последовательности (1+1/n)**n и выведите на экран их сумму.

n = int(input('Введите чиcло: '))
numbers = []
i = 1
while i <= n:                                   #заполняем список числами
    numbers.append((1+1/i)**i)
    i+=1
print(f'Список последовательности {numbers}')
sum = 0
for item in numbers:
    sum += item
print(f'Сумма последовательности {sum}')