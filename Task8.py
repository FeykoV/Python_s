n = int(input('Длина шоколадки - '))
m = int(input('Ширина шоколадки - '))
k = int(input('Сколько долек отломить? - '))
if (k > n * m) or ((k % n > 0) and (k % m > 0)):
    print("No")
else:
    print("Yes")