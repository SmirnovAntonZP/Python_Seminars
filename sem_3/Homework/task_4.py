#Напишите программу, которая будет преобразовывать десятичное число в двоичное.

N = int(input("введите число: "))
double = []
while True:
    double.append(N%2)
    N = N//2
    if N//2 == 0 and N != 1:
        break
double.reverse()
print(double)