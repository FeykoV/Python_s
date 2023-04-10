n = int(input('Введите номер билета = '))
sum1 = 0
sum2 = 0
while n > 999:
    x = n % 10
    sum1 += x
    n //= 10
while n > 0:
    x = n % 10
    sum2 += x
    n //= 10
if sum1 == sum2:
    print("Ура, ваш билет счастливый!")
else:
    print("Билет не счастливый")