from src.product import Product


class Smartphone(Product):
    """
        Класс, представляющий смартфон как товар.

        Наследуется от класса Product и расширяет его дополнительными атрибутами.

        Атрибуты:
            name (str): Название продукта
            description (str): Описание продукта
            price (float): Цена за единицу
            quantity (int): Количество в наличии
            efficiency (str): Производительность устройства
            model (str): Модель смартфона
            memory (str): Объем встроенной памяти
            color (str): Цвет устройства
        """
    def __init__(
        self,
        name: str,
        description: str,
        price: float,
        quantity: int,
        efficiency: str,
        model: str,
        memory: str,
        color: str,
    ) -> None:
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color
