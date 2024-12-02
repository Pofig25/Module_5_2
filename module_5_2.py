class House:                                            # Создайте класс House.
    def __init__(self, name, number_of_floors):         # Вунтри класса House определите метод __init__, в который передадите название и кол-во этажей.
        self.name = name                                # Внутри метода __init__ создайте атрибуты объекта self.name
        self.number_of_floors =  number_of_floors       # и self.number_of_floors, присвойте им переданные значения.

    def go_to(self, new_floor):                         # Создайте метод go_to с параметром new_floor
        for i in range(1, new_floor + 1):               # и напишите логику внутри него на основе описания задачи
            if 1 <= new_floor <= self.number_of_floors:
                print(i)
            else:
                print('Такого этажа не существует')
                break

    def __len__(self):
        return (self.number_of_floors)

    def __str__(self):
        return (f'Название: {self.name}, кол-во этажей: {self.number_of_floors}')
                                                        # Создайте объект класса House с произвольным названием и количеством этажей.
h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)
# h1.go_to(5)                                             # h1.go_to(5)
# h2.go_to(10)                                            # h2.go_to(10)
# __str__
print(h1)
print(h2)
# __len__
print(len(h1))
print(len(h2))

'''
Необходимо дополнить класс House следующими специальными методами:
__len__(self) - должен возвращать кол-во этажей здания self.number_of_floors.
__str__(self) - должен возвращать строку: "Название: <название>, кол-во этажей: <этажи>".

Пример выполняемого кода:
h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)

# __str__
print(h1)
print(h2)

# __len__
print(len(h1))
print(len(h2))

Вывод на консоль:
Название: ЖК Эльбрус, кол-во этажей: 10
Название: ЖК Акация, кол-во этажей: 20
10
20
'''