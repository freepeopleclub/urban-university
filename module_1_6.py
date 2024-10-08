# 2. Работа со словарями:
#   - Создайте переменную my_dict и присвойте ей словарь из нескольких пар ключ-значение.
# Например: Имя(str)-Год рождения(int).
#   - Выведите на экран словарь my_dict.
#   - Выведите на экран одно значение по существующему ключу, одно по отсутствующему из словаря my_dict без ошибки.
#   - Добавьте ещё две произвольные пары того же формата в словарь my_dict.
#  - Удалите одну из пар в словаре по существующему ключу из словаря my_dict и выведите значение из этой пары на экран.
#   - Выведите на экран словарь my_dict.
#
my_dict = {"Василий": 2002, "Гаврила": 1902, "Дядя Фёдор": 1972}
print(my_dict)
print(my_dict["Гаврила"])
print(my_dict.get("Лёва"))
my_dict.update({"Маша": 2021, "Саша": 1917, "Гена": 1999})
print(my_dict)
my_dict.pop("Гаврила")
print(my_dict)
# 3. Работа с множествами:
#   - Создайте переменную my_set и присвойте ей множество, состоящее из разных типов данных с повторяющимися значениями.
#   - Выведите на экран множество my_set (должны отобразиться только уникальные значения).
#   - Добавьте 2 произвольных элемента в множество my_set, которых ещё нет.
#   - Удалите один любой элемент из множества my_set.
#   - Выведите на экран измененное множество my_set.
my_set = {"Гаврила", "37", "1", 37, 15, 3, True, False, "Гаврила", False}
print(my_set)
my_set.add(38)
my_set.add("Добавляю строчный элемент")
print(my_set)
my_set.discard(False)
print(my_set)