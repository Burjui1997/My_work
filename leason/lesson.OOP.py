# class NesteDroll:
#     def __init__(self, color, size, material):
#         self.color = color
#         self.size = size
#         self.material = material
#
#     def get_color(self):
#         return self.color
#
#
#
#
# droll = NesteDroll("красный", 12, "дерево")
# print(droll.color, droll.size, droll.material)
# print(droll.get_color())
#
# """Давай разберёмся.
#
# ### Как работает этот код:
#
# 1. **Классы `SmallMatryoshka`, `MediumMatryoshka`, `BigMatryoshka`**:
#    Эти классы представляют собой разные типы матрешек: маленькие, средние и большие. Структура наследования указывает
#     на то, что `MediumMatryoshka` наследует `SmallMatryoshka`, а `BigMatryoshka` наследует `MediumMatryoshka`.
#
# 2. **Атрибут класса `counter`**:
#    Это переменная на уровне класса, которая используется для подсчета количества созданных экземпляров
#    каждого типа матрешек. Когда мы создаем новую матрешку, `counter` увеличивается на 1.
#
# 3. **Метод `__init__`**:
#    Это специальный метод, который автоматически вызывается при создании нового экземпляра класса
#     (то есть при инициализации). В этом методе происходит увеличение счетчика `counter` и присвоение уникального ID матрешке.
#
# 4. **Метод `super().__init__()`**:
#    Этот метод вызывает конструктор родительского класса. Это значит, что при создании
#    `MediumMatryoshka`, например, сначала будет создана `SmallMatryoshka`, и затем `MediumMatryoshka`.
#
# ### Что такое метод класса:
#
# В Python существует три основных типа методов:
#
# 1. **Обычные методы (instance methods)**:
#    Это наиболее часто используемый тип метода. Они принимают параметр `self`,
#     который ссылается на экземпляр класса, и обычно используются для работы с атрибутами экземпляра.
#
# 2. **Статические методы (`@staticmethod`)**:
#    Это методы, которые относятся к классу, но не могут изменять состояние
#    класса или его экземпляра. Они определяются с помощью декоратора `@staticmethod`
#    и не принимают ни `self`, ни `cls` в качестве первого параметра.
#
# 3. **Методы класса (`@classmethod`)**:
#    Они принимают параметр `cls`, который ссылается на сам класс, а не на его экземпляр.
#     Это позволяет им работать с атрибутами класса, а не с атрибутами экземпляра.
#     В нашем коде метод `total_made` является методом класса. Он возвращает значение счетчика для соответствующего класса.
#
# В отличие от обычных методов, методы класса не требуют создания экземпляра класса для вызова.
#  Вы можете вызывать их напрямую из класса, как это делается в строке:
# ```python
# print(f"Всего маленьких матрешек: {SmallMatryoshka.total_made()}")
# ```
#
# Декоратор `@classmethod` перед методом указывает, что данный метод является методом класса.
# """
#
#
# class SmallMatryoshka:
#     counter = 0  # общий счетчик для всех маленьких матрешек
#
#     def __init__(self):
#         SmallMatryoshka.counter += 1
#         self.id = SmallMatryoshka.counter  # уникальный ID матрешки
#         print(f"Создана маленькая матрешка с ID {self.id}!"
#               f"Всего маленьких матрешек: {SmallMatryoshka.counter}!")
#
#     @classmethod
#     def total_made(cls):
#         return cls.counter
#
#
# class MediumMatryoshka(SmallMatryoshka):
#     counter = 0  # общий счетчик для всех средних матрешек
#
#     def __init__(self):
#         super().__init__()
#         MediumMatryoshka.counter += 1
#         self.id = MediumMatryoshka.counter
#         print(f"Создана средняя матрешка с ID {self.id}!"
#               f"Всего средних матрешек: {MediumMatryoshka.counter}!")
#
#     @classmethod
#     def total_made(cls):
#         return cls.counter
#
#
# class BigMatryoshka(MediumMatryoshka):
#     counter = 0  # общий счетчик для всех больших матрешек
#
#     def __init__(self):
#         super().__init__()
#         BigMatryoshka.counter += 1
#         self.id = BigMatryoshka.counter
#         print(f"Создана большая матрешка с ID {self.id}!"
#               f"Всего больших матрешек: {BigMatryoshka.counter}!")
#
#     @classmethod
#     def total_made(cls):
#         return cls.counter
#
#
# # Тестирование
# big_m = BigMatryoshka()
# big_m2 = BigMatryoshka()
# big_m3 = BigMatryoshka()
#
# medium_m = MediumMatryoshka()
# print("-----")
# print(f"Всего маленьких матрешек: {SmallMatryoshka.total_made()}")
# print(f"Всего средних матрешек: {MediumMatryoshka.total_made()}")
# print(f"Всего больших матрешек: {BigMatryoshka.total_made()}")

# class Pizza:
#     def __init__(self,name: str, weight: float, price: float):
#         self.name = name
#         self.weight = weight
#         self.price = price
#
#     def __eq__(self, other):
#         if not isinstance(other,Pizza):
#             raise ValueError("Сравнивать можно только объекты класса Pizza")
#         return self.name == other.name and self.weight == other.weight
#
#     def __gt__(self, other):
#         if not isinstance(other,Pizza):
#             raise ValueError("Сравнивать можно только обьекты класса Pizza")
#         return self.name >= other.name
#
#     def __le__(self, other):
#         if not isinstance(other,Pizza):
#             raise ValueError("")
#         return self.name <= other.name
#
#     def __lt__(self, other):
#         if not isinstance(other,Pizza):
#             raise ValueError("")
#         return self.name < other.name
#
#     def __ge__(self, other):
#         if not isinstance(other,Pizza):
#             raise ValueError("")
#         return self.name > other.name
#
#     def __repr__(self):
#         return f'Название: {self.name} , Размер:{self.weight}, Цена: {self.price}'
#
#
# pizza_1 = Pizza('Маргарита', 1000, 200)
# pizza_2 = Pizza('Маргарита', 1000, 200)
#
# print(pizza_1 == pizza_2)

from functools import total_ordering
@total_ordering

# class Pizza:
#
#     def __init__(self, size: float):
#         self.size = size
#
#     def __str__(self):
#         return f' Пицаа размером : {self.size}'
#
#     def __repr__(self):
#         return f'Pizza: {self.size}'

class Girya:

    def __init__(self, name: str, weight: float):
        self.name = name
        self.weight = weight

    def __eq__(self, other):
        return self.name == other.name and self.weight == other.weight

    def __lt__(self, other):
        return self.name < other.name and self.weight < other.weight

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

girya_1 = Girya('Золото', 16)
girya_2 = Girya('Чугун', 24)
girya_3 = Girya('Серебро', 25)
girya  = [girya_1, girya_2, girya_3]

print(girya.sort(key=lambda x: x.is_equel_name(girya)))
print(girya_1 == girya_2)
print(girya_1 > girya_2)
print(girya_1 < girya_2)
print(girya_1 != girya_2)
print(girya_1 <= girya_2)
print(girya_1 >= girya_2)