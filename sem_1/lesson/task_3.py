# Напишите программу, которая на вход принимает 5 чисел и находит максимальное из них.

# # VAR 1
# list = []
# for i in range(0, 5): # for i in range(5):
#     list.append(int(input('vvedite chislo')))
# print(max(list))

# VAR 2

list = []
i = 0
while i < 5:
    j = int(input("Введите число: "))
    list.append(j)
    i += 1
print(list)

maxNumber = list[0]
i = 1
while i < len(list):
    if list[i] > maxNumber:
        maxNumber = list[i]
    i += 1
print(maxNumber)

# VAR 3

# list =[23,34,46,45,32]
# maxNumber = list[0]
# i=1
# while i<len(list):
#     if list[i] > maxNumber:
#         maxNumber = list[i]
#     i += 1
# print(maxNumber)

# VAR 4

# def max_number(list_number):
#     return max(list_number)
# print(max_number([2, 4, 23, 76, 45]))

# VAR 5

# def max_number2(list_number):
#     result = 0
#     for x in list_number:
#         if x > result:
#             result = x
#     return result

# print(max_number([54, 34, 87, 45, 3]))
