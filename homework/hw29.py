from abc import ABC, abstractmethod


# Абстрактный класс для фабрики ингредиентов
class IngredientFactory(ABC):
    @abstractmethod
    def create_cheese(self, cheese_type: str) -> str:
        pass

    @abstractmethod
    def create_sauce(self, cheese_type: str) -> str:
        pass


# Конкретная фабрика для ингредиентов пиццы Додо
class DodoIngredientFactory(IngredientFactory):
    def create_cheese(self, cheese_type):
        if cheese_type == "Цедер":
            return "Цедер"
        elif cheese_type == "Моцарелла":
            return "Моцарелла"
        else:
            return "Неизвестный сыр"

    def create_sauce(self, sauce_type: str) -> str:
        if sauce_type == "Томатная":
            return "Tоматный"
        elif sauce_type == "Песто":
            return "Песто"
        else:
            return "Неизвестный соус"


# Фабрика для управления размерами пиццы
class SizeFactory:
    def create_size(self, size):
        return f"{size} Пицца"


# Строитель для сборки пиццы
class PizzaBuilder:
    def __init__(self, ingredient_factory: IngredientFactory, size_factory: SizeFactory, pizza_type: str):
        self.ingredient_factory = ingredient_factory
        self.size_factory = size_factory
        self.pizza_type = pizza_type
        self.size = None

    def set_size(self, size):
        self.size = self.size_factory.create_size(size)

    def build(self, cheese_type, sauce_type):
        cheese = self.ingredient_factory.create_cheese(cheese_type)
        sauce = self.ingredient_factory.create_sauce(sauce_type)
        return f"{self.size} с {cheese} сыром и {sauce} соусом"


# Функция для создания заказа пиццы
def main():
    size = input('Введите размер: ')
    pizza_type = input('Введите пиццу :')
    cheese_type = input('Введите название сыра: ')
    sauce_type = input('Введите название соуса: ')
    ingredient_factory = DodoIngredientFactory()
    size_factory = SizeFactory()
    pizza_builder = PizzaBuilder(ingredient_factory, size_factory, pizza_type)
    pizza_builder.set_size(size)
    order_description = pizza_builder.build(cheese_type, sauce_type)
    print(f"Ваша пицца: {order_description}")


if __name__ == "__main__":
    main()
