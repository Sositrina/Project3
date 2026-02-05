import pytest

from src.category import Category
from src.product import Product


def test_category(first_category: Category) -> None:
    assert first_category.name == "Смартфоны"
    assert (
        first_category.description
        == "Смартфоны, как средство не только коммуникации,но и получения дополнительных функций для удобства жизни"
    )
    assert len(first_category.products) == 3
    assert Category.category_count == 1


@pytest.fixture
def sample_product() -> Product:
    return Product("Test Product", "Test Description", 1000, 10)


def test_add_product(first_category: Category, sample_product: Product) -> None:
    """Добавление товара в категорию"""
    initial_count = len(first_category.products)
    first_category.add_product(sample_product)
    assert len(first_category.products) == initial_count + 1


def test_product_count_increases(first_category: Category, sample_product: Product) -> None:
    """Проверяте увеличение счетчика"""
    initial_total = Category.product_count
    first_category.add_product(sample_product)
    assert Category.product_count == initial_total + 1


def test_products_returns_list(first_category: Category) -> None:
    """Проверяет, что возвращается список"""
    assert isinstance(first_category.products, list)


def test_products_format(first_category: Category) -> None:
    """Проверяет формат строк в списке"""
    for product_str in first_category.products:
        assert "руб." in product_str
        assert "Остаток:" in product_str
        assert "шт." in product_str


def test_category_name_and_description() -> None:
    """Тест name и description"""
    category = Category("Телевизоры", "4K телевизоры с HDR", [])
    assert isinstance(category.name, str)
    assert isinstance(category.description, str)

    assert category.name == "Телевизоры"
    assert category.description == "4K телевизоры с HDR"


def test_category_static_fields() -> None:
    """Тест полей класса Category"""
    initial_category_count = Category.category_count
    initial_product_count = Category.product_count

    category = Category("Тестовая", "Описание", [])

    assert Category.category_count == initial_category_count + 1

    product = Product("Тест", "Тест", 100, 1)
    category.add_product(product)

    assert Category.product_count == initial_product_count + 1


def test_add_one_product() -> None:
    """Тест добавления товара"""
    cat = Category("Одна", "Одна категория", [])
    prod = Product("Один", "Один товар", 500, 2)

    cat.add_product(prod)
    assert len(cat.products) == 1
    assert "Один" in cat.products[0]
    assert "500" in cat.products[0]


def test_category_with_single_product() -> None:
    """Тест с одним продуктом при создании"""
    product = Product("Монитор", "27 дюймов", 15000, 5)
    category = Category("Мониторы", "Компьютерные мониторы", [product])

    assert len(category.products) == 1
    assert "Монитор" in category.products[0]
    assert "15000" in category.products[0]
