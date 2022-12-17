#Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z (расшифровка этого выражения not (x[0] or x[1] or x[2] = not x[0] and not x[1] and not x[2]) для всех значений предикат.

# VARIANT 1

for x in [True, False]:
    for y in [True, False]:
        for z in [True,False]:
            print(x, 'AND', y, 'OR', z, '=', x and y or z)

# VARIANT 2

# x = False
# y = True
# z = False
# if not (x or y or z) == (not x and not y and not z) :
#     print(True)
# else:
#     print(False)