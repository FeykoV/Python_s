# Задача 32: Определить индексы элементов массива (списка), 
# значения которых принадлежат заданному диапазону 
# (т.е. не меньше заданного минимума и не больше заданного максимума)


n = int(input("Введите количество элементов массива: "))
from random import randint
array = [randint(0, 20) for i in range(n)] 
print(array)


min = int(input("Введите минимальное значение: "))
max = int(input("Введите максимальное значение: "))

for i in range(n):
    if array[i]>=min and array[i]<=max:
        print(i, end=" ")