from typing import Any, Dict
from src.BaseProduct import BaseProduct
from src.mixin import Mixin


class Product(Mixin, BaseProduct):
    """Класс содержит название продукта, описание, цена и количество"""

    def __init__(self, name: str, description: str, price: float, quantity: int) -> None:
        super().__init__(name, description, price, quantity)

    def hand_over(self):
        return f"Продукт: {self.name}, Описание: {self.description}, Цена: {self.price}, Количество: {self.quantity}"


    @classmethod
    def new_product(cls, product_data: Dict[str, Any]) -> "Product":
        """Создает новый продукт из словаря"""
        return cls(
            name=product_data["name"],
            description=product_data["description"],
            price=product_data["price"],
            quantity=product_data["quantity"],
        )


    def __str__(self) -> str:
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other: "Product") -> float:
        if type(self) is not type(other):
            raise TypeError("Нельзя складывать товары из разных классов")
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
