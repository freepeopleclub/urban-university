# Задача "Магические здания":
# Для решения этой задачи будем пользоваться решением к предыдущей задаче "Атрибуты и методы объекта".
#
# Необходимо дополнить класс House следующими специальными методами:
# 1. __len__(self) - должен возвращать кол-во этажей здания self.number_of_floors.
# 2. __str__(self) - должен возвращать строку: "Название: <название>, кол-во этажей: <этажи>".

class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self):
        if new_floor > self.number_of_floors or new_floor < 1:
            print("Такого этажа не существует")
        else:
            print(f"Лифт отправляется на {new_floor} этаж")

    def __len__(self):
        print(self.number_of_floors)

    def __str__(self):
        print(f'Название: {self.name}, кол-во этажей: {self.number_of_floors}')

gk_1 = House("ЖК Эльбрус", 25)
gk_2 = House("ЖК Горизонт", 33)
gk_3 = House("ЖК Алые паруса", 150)

gk_1.__str__()
gk_2.__str__()
gk_3.__str__()

gk_1.__len__()
gk_2.__len__()
gk_3.__len__()