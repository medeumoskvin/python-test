# Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел.
# У пользователя необходимо запрашивать новый элемент рейтинга.
# Если в рейтинге существуют элементы с одинаковыми значениями,
# то новый элемент с тем же значением должен разместиться после них.

def permutation(a, value):
    max_value = max(a)
    if value > max_value:
        a.insert(0, value)
    elif value in a:
        a.insert(a.index(value), value)
    else:
        a.append(value)

num = int(input('введите свое число! '))
my_list = [7, 6,  5, 4, 3, 3, 2]
print(my_list)
permutation(my_list, num)
print(my_list)