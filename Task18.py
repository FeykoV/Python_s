# Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X.
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X 

# *Пример:*

# 5
#     1 2 3 4 5
#     6
#     -> 5

n = int(input("Введите число N "))
from random import randint
A = [randint(0, 20) for i in range(n)]
print(A)
x = int(input("Введите число X "))
result = False
k = 1
for j in range(n):
    for i in range(n):
        if A[i] == x-k or A[i] == x+k:
            print(A[i])
            result = True
            break
    if result:
        break        
    else:
        k +=1
