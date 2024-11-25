# Задача "История строительства":
#
# Для решения этой задачи будем пользоваться решением к предыдущей задаче "Перегрузка операторов".
# В классе House создайте атрибут houses_history = [], который будет хранить названия созданных объектов.
# Правильней вписывать здание в историю сразу при создании объекта, тем более можно удобно обращаться к атрибутам класса используя ссылку на сам класс - cls.
# Дополните метод __new__ так, чтобы:
#     Название объекта добавлялось в список cls.houses_history.
#     Название строения можно взять из args по индексу.
# Также переопределите метод __del__(self) в котором будет выводиться строка:
# "<название> снесён, но он останется в истории"
# Создайте несколько объектов класса House и проверьте работу методов __del__ и __new__, а также значение атрибута houses_history.

class House:
#    houses_history = []  # Создаём атрибут houses_history - как список

#    def __new__(cls, name, number_of_floors):
#        cls.houses_history.append(name)

    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def __del__(self):
        print(f'{self.name}, снесён, но он останется в истории')

gk_1 = House("ЖК Эльбрус", 25)
# print(House.houses_history)

gk_2 = House("ЖК Горизонт", 35)
# print(House.houses_history)

gk_3 = House("ЖК Алые паруса", 150)
# print(House.houses_history)

del gk_2
# print(House.houses_history)


