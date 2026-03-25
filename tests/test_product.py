import pytest

from src.category import Category
from src.lawngrass import LawnGrass
from src.product import Product
from src.smartphone import Smartphone


def test_product(first_product: Product) -> None:
    assert first_product.name == "Samsung Galaxy S23 Ultra"
    assert first_product.description == "256GB, Серый цвет, 200MP камера"
    assert first_product.price == 180000.0
    assert first_product.quantity == 5


def test_simple_new_product() -> None:
    data = {"name": "Test", "description": "Desc", "price": 100, "quantity": 1}
    product = Product.new_product(data)
    assert isinstance(product, Product)
    assert product.name == "Test"
    assert product.price == 100


def test_simple_price_setter() -> None:
    """Тесты для сеттера"""
    product = Product("Test", "Test", 100, 1)
    product.price = 200
    assert product.price == 200
    product.price = -50
    assert product.price == 200


def test_new_product_with_different_data() -> None:
    """Тест с разными данными"""
    data1 = {"name": "Product1", "description": "Desc1", "price": 99.99, "quantity": 10}
    product1 = Product.new_product(data1)
    assert product1.price == 99.99
    assert product1.quantity == 10

    data2 = {"name": "Product2", "description": "Desc2", "price": 50.0, "quantity": 0}
    product2 = Product.new_product(data2)
    assert product2.quantity == 0


def test_product_str() -> None:
    product = Product("Тест", "Описание", 80, 15)
    assert str(product) == "Тест, 80 руб. Остаток: 15 шт."


def test_product_add() -> None:
    a = Product("A", "Описание", 100, 10)
    b = Product("B", "Описание", 200, 2)
    assert a + b == 1400


def test_category_str() -> None:
    p1 = Product("A", "Описание", 100, 5)
    p2 = Product("B", "Описание", 200, 3)
    category = Category("Тестовая", "Описание", [p1, p2])
    assert str(category) == "Тестовая, количество продуктов: 8 шт."


def test_add_same_class_product() -> None:
    a = Product("A", "Описание", 100, 2)
    b = Product("B", "Описание", 200, 3)
    assert a + b == 100 * 2 + 200 * 3


def test_add_different_classes_raises_type_error() -> None:
    """Проверка ошибки при сложении разных классов"""
    phone = Smartphone("iPhone", "Новый", 50000, 5, "Высокая", "15", "128GB", "Черный")
    grass = LawnGrass("Газон", "Семена", 1000, 10, "Россия", 7, "Зеленый")

    with pytest.raises(TypeError) as e:
        phone + grass


def test_mixin_repr(capsys):
    """Проверка работы миксина"""
    product = Product("Продукт", "Описание", 100, 5)

    captured = capsys.readouterr()
    assert "Product(Продукт, Описание, 100, 5)" in captured.out

    assert repr(product) == "Product(Продукт, Описание, 100, 5)"
