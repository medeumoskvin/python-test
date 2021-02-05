# 5. Программа запрашивает у пользователя строку чисел, разделенных пробелом.
# При нажатии Enter должна выводиться сумма чисел.
# Пользователь может продолжить ввод чисел, разделенных пробелом и снова нажать Enter.
# Сумма вновь введенных чисел будет добавляться к уже подсчитанной сумме.
# Но если вместо числа вводится специальный символ, выполнение программы завершается.
# Если специальный символ введен после нескольких чисел,
# то вначале нужно добавить сумму этих чисел к полученной ранее сумме
# и после этого завершить программу.


def exe_5():
    res = 0
    while True:
        numbers = input('Введите список номеров, или * для выхода: ').split()
        for i in numbers:
            try:
                if i == '*':
                    print(f'Сумма равна {res}. Выход!')
                    return
                else:
                    res += int(i)
            except ValueError:
                print('Введите номер или *')
        print(f'Сумма {res}')
exe_5()