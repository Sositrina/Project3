import pytest
from src.lawngrass import LawnGrass
from src.product import Product


def test_lawngrass_initialization() -> None:
    """Тест инициализации объекта LawnGrass"""
    lawn_grass = LawnGrass(
        name="Grass",
        description="Газонная трава",
        price=1500.0,
        quantity=20,
        country="Россия",
        germination_period=7,
        color="Зеленый"
    )

    # Проверка значений атрибутов
    assert lawn_grass.name == "Grass"
    assert lawn_grass.description == "Газонная трава"
    assert lawn_grass.price == 1500.0
    assert lawn_grass.quantity == 20
    assert lawn_grass.country == "Россия"
    assert lawn_grass.germination_period == 7
    assert lawn_grass.color == "Зеленый"


def test_lawngrass_inheritance() -> None:
    """Тест на наследование от Product"""
    lawn_grass = LawnGrass(
        name="Grass",
        description="Газонная трава",
        price=1500.0,
        quantity=20,
        country="Россия",
        germination_period=7,
        color="Зеленый"
    )

    assert isinstance(lawn_grass, Product)
    assert isinstance(lawn_grass, LawnGrass)


def test_lawngrass_str() -> None:
    """Тест строки представления объекта LawnGrass"""
    lawn_grass = LawnGrass(
        name="Grass",
        description="Газонная трава",
        price=1500.0,
        quantity=20,
        country="Россия",
        germination_period=7,
        color="Зеленый"
    )

    assert str(lawn_grass) == "Grass, 1500.0 руб. Остаток: 20 шт."


def test_lawngrass_addition() -> None:
    """Тест сложения двух объектов LawnGrass"""
    lawn_grass1 = LawnGrass(
        name="Grass",
        description="Газонная трава",
        price=1500.0,
        quantity=10,
        country="Россия",
        germination_period=7,
        color="Зеленый"
    )

    lawn_grass2 = LawnGrass(
        name="Luxury Grass",
        description="Газонная трава другая",
        price=2000.0,
        quantity=5,
        country="Германия",
        germination_period=10,
        color="Светло-зеленый"
    )

    assert lawn_grass1 + lawn_grass2 == (1500.0 * 10 + 2000.0 * 5)