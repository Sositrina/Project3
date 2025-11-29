class Product:
    """Класс содержит название продукта, описание, цена и количество"""

    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name: str, description: str, price: float, quantity: int) -> None:
        self.name = name  # название продукта
        self.description = description  # описание
        self.price = price  # цена
        self.quantity = quantity  # количество в наличии
