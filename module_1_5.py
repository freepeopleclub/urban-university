# 2. Задайте переменные разных типов данных:
#   - Создайте переменную immutable_var и присвойте ей кортеж из нескольких элементов разных типов данных.
#   - Выполните операции вывода кортежа immutable_var на экран.
#
# 3. Изменение значений переменных:
#   - Попытайтесь изменить элементы кортежа immutable_var. Объясните, почему нельзя изменить значения элементов кортежа.
#
# 4. Создание изменяемых структур данных:
#   - Создайте переменную mutable_list и присвойте ей список из нескольких элементов.
#   - Измените элементы списка mutable_list.
#   - Выведите на экран измененный список mutable_list.
immutable_var = 1, 2, 3, 5, 'true'
print(immutable_var)
print(immutable_var, type(immutable_var))
#
immutable_var[2] = 10  # TypeError: 'tuple' object does not support item assignment
#
mutable_list = [1, 33, "false", "Ошибка вывода"]
print(mutable_list)
print(mutable_list, type(mutable_list))
mutable_list[2] = "True"
print(mutable_list)