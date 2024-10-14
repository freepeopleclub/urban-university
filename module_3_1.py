# Задача "Счётчик вызовов":
#
# Вам необходимо написать 3 функции:
# 1. Функция count_calls подсчитывающая вызовы остальных функций.
# 2. Функция string_info принимает аргумент - строку и возвращает кортеж из: длины этой строки, строку в верхнем регистре, строку в нижнем регистре.
# 3. Функция is_contains принимает два аргумента: строку и список, и возвращает True, если строка находится в этом списке, False - если отсутствует. Регистром строки при проверке пренебречь: UrbaN ~ URBAN.
#
# Пункты задачи:
# 1. Создать переменную calls = 0 вне функций.
# 2. Создать функцию count_calls и изменять в ней значение переменной calls. Эта функция должна вызываться в остальных двух функциях.
# 3. Создать функцию string_info с параметром string и реализовать логику работы по описанию.
# 4. Создать функцию is_contains с двумя параметрами string и list_to_search, реализовать логику работы по описанию.
# 5. Вызвать соответствующие функции string_info и is_contains произвольное кол-во раз с произвольными данными.
# 6. Вывести значение переменной calls на экран(в консоль).
#
from module_1_3 import test_2

calls = 0 # Создать переменную calls
#
def count_calls():
    global calls
    calls = calls + 1

def string_info(string):
    count_calls()
    t = (len(string), string.upper(), string.lower()) # из строки делаем кортеж из: длины этой строки, строку в верхнем регистре, строку в нижнем регистре.
    print(t)

def is_contains(string, list_to_search):
    count_calls()
    flag_ = 0 # создаём переменную для проверки совпадения строки и списка. Если совпадение есть - добавляем единицу
    for i in range(0, len(list_to_search)): # перебираем список столько раз, сколько в нём элементов
        if string.upper() == list_to_search[i].upper():
            flag_ = flag_ + 1
    if flag_ >= 1:
        print(True)
    else:
        print(False)

string_info("Привет Мир")
string_info("Создать функцию is_contains с двумя параметрами string и list_to_search")
string_info('Armageddon')

is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])
is_contains('Urban', ['ban', 'BaNaN', 'TUrban'])

print('Количество вызовов функций: ', calls)