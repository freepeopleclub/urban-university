# Задача "Рекурсивное умножение цифр":
# Напиши функцию get_multiplied_digits, которая принимает аргумент целое число number и подсчитывает произведение цифр этого числа.
#
# Пункты задачи:
# 1. Напишите функцию get_multiplied_digits и параметр number в ней.
# 2. Создайте переменную str_number и запишите строковое представление(str) числа number в неё.
# 3. Основной задачей будет отделение первой цифры в числе: создайте переменную first и запишите в неё первый символ
#       из str_number в числовом представлении(int).
# 4. Возвращайте значение first * get_multiplied_digits(int(str_number[1:])). Таким образом вы умножите первую цифру
#       числа на результат работы этой же функции с числом, но уже без первой цифры.
# 5. 4 пункт можно выполнить только тогда, когда длина str_number больше 1, т.к. в противном случае не получиться взять
#       срез str_number[1:].
# 6. Если же длина str_number не больше 1, тогда вернуть оставшуюся цифру first.
# Стек вызовов будет выглядеть следующим образом:
# get_multiplied_digits(40203) -> 4 * get_multiplied_digits(203) -> 4 * 2 * get_multiplied_digits(3) -> 4 * 2 * 3
#
def get_multiplied_digits(number):
    str_number = str(number)
    n = len(str_number)  # Выясняю, сколько символов в строке str_number
    k = n - 1
    first = int(str_number[0])
    for i in range(1, n):
        if int(str_number[(n - k)]) != 0:
            first = first * int(str_number[(n - k)])
            k = k - 1
        else:
            k = k - 1
    print(first)

get_multiplied_digits(40203)