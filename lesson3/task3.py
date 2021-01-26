# Реализовать функцию my_func(), которая принимает три позиционных аргумента,
# и возвращает сумму наибольших двух аргументов.


def my_func(a, b, c):
    z = [a, b, c]
    z.remove(min(a, b, c))
    return sum(z)

def my_func_1():
    print(my_func(4, 1, 9))
my_func_1()