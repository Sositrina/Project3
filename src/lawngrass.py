from src.product import Product


class LawnGrass(Product):
    """
        Класс, представляющий газонную траву как товар.

        Наследуется от класса Product и расширяет его дополнительными атрибутами.

        Атрибуты:
            name (str): Название продукта
            description (str): Описание продукта
            price (float): Цена за единицу
            quantity (int): Количество в наличии
            country (str): Страна-производитель
            germination_period (float): Срок прорастания (в днях)
            color (str): Цвет травы
        """
    def __init__(
        self,
        name: str,
        description: str,
        price: float,
        quantity: int,
        country: str,
        germination_period: float,
        color: str,
    ) -> None:
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color

    def hand_over(self):
        return f"{self.name}, {self.description}, {self.price}, {self.quantity}"
