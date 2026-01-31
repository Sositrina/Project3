from typing import Dict, Any


class Product:
    """Класс содержит название продукта, описание, цена и количество"""

    name: str
    description: str
    #price: float
    quantity: int

    def __init__(self, name: str, description: str, price: float, quantity: int) -> None:
        self.name = name  # название продукта
        self.description = description  # описание
        self.__price = price  # цена
        self.quantity = quantity  # количество в наличии

    @classmethod
    def new_product(cls, product_data: Dict[str, Any]) -> "Product":
        """Создает новый продукт из словаря"""
        return cls(
            name=product_data["name"],
            description=product_data["description"],
            price=product_data["price"],
            quantity=product_data["quantity"],
        )

    @property
    def price(self) -> float:
        """Геттер для цены"""
        return self.__price

    @price.setter
    def price(self, value: float) -> None:
        """Сеттер для цены"""
        if value <= 0:
            print("Цена не должна быть нулевая или отрицательная")
        else:
            self.__price = value

    def __str__(self) -> str:
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other: "Product") -> float:
        return self.price * self.quantity + other.price * other.quantity


if __name__ == "__main__":
    new_product = Product.new_product(
        {
            "name": "Samsung Galaxy S23 Ultra",
            "description": "256GB, Серый цвет, 200MP камера",
            "price": 180000.0,
            "quantity": 5,
        }
    )
    print(new_product.name)
    print(new_product.description)
    print(new_product.price)
    print(new_product.quantity)

    new_product.price = 800
    print(new_product.price)

    new_product.price = -100
    print(new_product.price)
    new_product.price = 0
    print(new_product.price)
    print(new_product)

    a = Product("Товар A", "Описание", 100, 10)
    b = Product("Товар B", "Описание", 200, 2)

    print(a + b)