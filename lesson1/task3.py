n = int(input('введите ваше число ! '))
res = str(n)
res1 = res + res
res2 = res + res + res
result = n + int(res1) + int(res2)
print('результат =',result,'!', 'введеное число равнаяется =',result - int(res1) - int(res2),'!')


