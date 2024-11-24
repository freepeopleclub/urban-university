# Задача "Нужно больше этажей":
# Для решения этой задачи будем пользоваться решением к предыдущей задаче "Специальные методы класса".
#
# Необходимо дополнить класс House следующими специальными методами:
#     __eq__(self, other) - должен возвращать True, если количество этажей одинаковое у self и у other.
#     Методы __lt__(<), __le__(<=), __gt__(>), __ge__(>=), __ne__(!=) должны присутствовать в классе и возвращать
#     результаты сравнения по соответствующим операторам. Как и в методе __eq__ в сравнении участвует кол-во этажей.
#     __add__(self, value) - увеличивает кол-во этажей на переданное значение value, возвращает сам объект self.
#     __radd__(self, value), __iadd__(self, value) - работают так же как и __add__ (возвращают результат его вызова).
#
# Остальные методы арифметических операторов, где self - x, other - y:
# Следует заметить, что other может быть не только числом, но и вообще любым объектом другого класса.
# Для более точной логики работы методов __eq__, __add__  и других методов сравнения и арифметики перед выполняемыми
# действиями лучше убедиться в принадлежности к типу при помощи функции isinstance:
# isinstance(other, int) - other указывает на объект типа int.
# isinstance(other, House) - other указывает на объект типа House.
class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def __eq__(self, other):
        return self.number_of_floors == other.number_of_floors
    def __lt__(self, other):
        return self.number_of_floors < other.number_of_floors
    def __le__(self, other):
        return self.number_of_floors <= other.number_of_floors
    def __gt__(self, other):
        return self.number_of_floors > other.number_of_floors
    def __ge__(self, other):
        return self.number_of_floors >= other.number_of_floors
    def __ne__(self, other):
        return self.number_of_floors != other.number_of_floors

    def __add__(self, value):
        self.number_of_floors = self.number_of_floors + value
        return self
    def __radd__(self, value):
        self.number_of_floors = self.number_of_floors + value
        return self
    def __iadd__(self, value):
        self.number_of_floors += value.number_of_floors
        return self

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
gk_2 = House("ЖК Горизонт", 35)
gk_3 = House("ЖК Алые паруса", 150)

print()
print(f'Количество этажей "{gk_1.name}" равно "{gk_2.name}". Это {gk_1 == gk_2}')
print(f'Количество этажей "{gk_1.name}" меньше, или равно "{gk_2.name}". Это {gk_1 <= gk_2}')
print(f'Количество этажей "{gk_1.name}" больше "{gk_2.name}". Это {gk_1 > gk_2}')
print(f'Количество этажей "{gk_1.name}" больше, или равно "{gk_2.name}". Это {gk_1 >= gk_2}')
print(f'Количество этажей "{gk_1.name}" не равно "{gk_2.name}". Это {gk_1 != gk_2}')
print()
gk_1 = gk_1 + 10
gk_2 = gk_2 + 55

print(f'Теперь в "{gk_1.name}" {gk_1.number_of_floors} этажей')
print(f'Теперь в "{gk_2.name}" {gk_2.number_of_floors} этажей')
gk_1 = gk_1 + 13
print(f'Теперь в "{gk_1.name}" {gk_1.number_of_floors} этажей')
gk_3 = gk_3 + 33
print(f'Теперь в "{gk_3.name}" {gk_3.number_of_floors} этажей')
gk_3 = gk_3 + 14
print(f'Теперь в "{gk_3.name}" {gk_3.number_of_floors} этажей')
