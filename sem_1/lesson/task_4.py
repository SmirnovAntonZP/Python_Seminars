# Напишите программу, которая будет на вход принимать число N и выводить числа от -N до N

#Var 1

# N = int(input('Vvedite chislo N '))
# b = N * -1
# if N >= 0:
#     while b <= N:
#         print(b, end=' ')
#         b+=1
# else:
#     while b >= N:
#         print(N, end=' ')
#         N+=1

#VAR 2

a=int(input('vvedite chislo'))
for i in range (-a, a+1):
    print (i, end=" ")