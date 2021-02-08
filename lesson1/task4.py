a = int(input('введите ваше число !'))
max = a % 10
a = a // 10
while a > 0:
    if a % 10 > max:
        max = a % 10
    a = a//10
print('максимальное число ваше =',max)