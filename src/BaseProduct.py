from abc import ABC, abstractmethod

class BaseProduct(ABC):
    """Абстрактный класс, который содержит название продукта, описание, цена, количество,геттер и сеттер"""

    name: str
    description: str
    quantity: int

    def __init__(self, name: str, description: str, price: float, quantity: int) -> None:
        self.name = name  # название продукта
        self.description = description  # описание
        self.__price = price  # цена
        self.quantity = quantity  # количество в наличии


    @abstractmethod
    def hand_over(self):
        """Общая функциональность"""
        pass

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