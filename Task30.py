# Задача 30:  Заполните массив элементами арифметической прогрессии.
# Её первый элемент, разность и количество элементов нужно ввести с клавиатуры.
# Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.

a = int(input("Введите первый элемент массива: "))
d = int(input("Введите разность между членами арифметической прогрессии: "))
n = int(input("Введите количество членов арифметической прогрессии: "))

b = (a + (n-1) * d) + 1
for i in range(a,b,d):
    print(i, end=" ")