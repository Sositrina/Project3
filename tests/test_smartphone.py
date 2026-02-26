import pytest
from src.smartphone import Smartphone
from src.product import Product


def test_smartphone_initialization() -> None:
    """Тест инициализации объекта Smartphone"""
    smartphone = Smartphone(
        name="iPhone 15",
        description="512GB, Серый цвет",
        price=210000.0,
        quantity=8,
        efficiency="Высокая",
        model="15",
        memory="512GB",
        color="Серый"
    )

    assert smartphone.name == "iPhone 15"
    assert smartphone.description == "512GB, Серый цвет"
    assert smartphone.price == 210000.0
    assert smartphone.quantity == 8
    assert smartphone.efficiency == "Высокая"
    assert smartphone.model == "15"
    assert smartphone.memory == "512GB"
    assert smartphone.color == "Серый"


def test_smartphone_inheritance() -> None:
    """Тест на наследование от Product"""
    smartphone = Smartphone(
        name="iPhone 15",
        description="512GB, Серый цвет",
        price=210000.0,
        quantity=8,
        efficiency="Высокая",
        model="15",
        memory="512GB",
        color="Серый"
    )

    assert isinstance(smartphone, Product)
    assert isinstance(smartphone, Smartphone)


def test_smartphone_str() -> None:
    """Тест строки представления объекта Smartphone"""
    smartphone = Smartphone(
        name="iPhone 15",
        description="512GB, Серый цвет",
        price=210000.0,
        quantity=8,
        efficiency="Высокая",
        model="15",
        memory="512GB",
        color="Серый"
    )

    assert str(smartphone) == "iPhone 15, 210000.0 руб. Остаток: 8 шт."


def test_smartphone_addition() -> None:
    """Тест сложения двух объектов Smartphone"""
    smartphone1 = Smartphone(
        name="iPhone 15",
        description="512GB, Серый цвет",
        price=210000.0,
        quantity=5,
        efficiency="Высокая",
        model="15",
        memory="512GB",
        color="Серый"
    )

    smartphone2 = Smartphone(
        name="Samsung Galaxy S23 Ultra",
        description="256GB, Серый цвет",
        price=180000.0,
        quantity=3,
        efficiency="Очень высокая",
        model="S23",
        memory="256GB",
        color="Черный"
    )

    assert smartphone1 + smartphone2 == (210000.0 * 5 + 180000.0 * 3)  # цена * количество