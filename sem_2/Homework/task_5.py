# 5. Реализуйте алгоритм перемешивания списка. (рандомно поменять местами элементы списка между собой)

from random import randint

N = [1,2,3,4,5]
print(N)
for i in range(0,len(N)):
    ind = randint(0,len(N)-1)
    N[i], N[ind] = N[ind], N[i]
print(N)