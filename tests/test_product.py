from src.product import Product


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
