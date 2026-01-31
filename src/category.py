from src.product import Product

from typing import List


class Category:
    """
        Класс, представляющий категорию товаров в магазине.

        Атрибуты:
            name (str): Название категории
            description (str): Описание категории
            products (list): Список товаров в категории
            category_count (int): Счетчик количества созданных категорий (классовый атрибут)
            product_count (int): Счетчик общего количества товаров во всех категориях (классовый атрибут)
        """
    name: str
    description: str
    category_count: int = 0
    product_count: int = 0

    def __init__(self, name: str, description: str, products: list) -> None:
        """
        Инициализирует экземпляр категории товаров.
        name (str): Название категории
        description (str): Описание категории
        products (list): Список товаров, принадлежащих категории
        Автоматически увеличивает счетчик категорий и обновляет счетчик товаров
        """
        self.name = name
        self.description = description
        self.__products = products
        Category.category_count += 1
        Category.product_count += len(products)


    def add_product(self, product4: Product) -> None:
        """Добавляет продукты в категорию и добавляет количество продуктов"""
        self.__products.append(product4)
        Category.product_count += 1

    @property
    def products(self) -> List[str]:
        """Выводит список товаров в виде строк"""
        return [str(product) for product in self.__products]

    def __str__(self) -> str:
        total_quantity = 0
        for product in self.__products:
            total_quantity += product.quantity
        return f"{self.name}, количество продуктов: {total_quantity} шт."


if __name__ == "__main__":
    product1 = Product("Samsung Galaxy S23 Ultra",
                       "256GB, Серый цвет, 200MP камера",
                       180000.0,
                       5)

    product2 = Product("Iphone 15",
                       "512GB, Gray space",
                       210000.0,
                       8)

    product3 = Product("Xiaomi Redmi Note 11",
                       "1024GB, Синий",
                       31000.0,
                       14)

    print(product1.name)
    print(product1.description)
    print(product1.price)
    print(product1.quantity)

    print(product2.name)
    print(product2.description)
    print(product2.price)
    print(product2.quantity)

    print(product3.name)
    print(product3.description)
    print(product3.price)
    print(product3.quantity)

    category1 = Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации,"
        "но и получения дополнительных функций для удобства жизни",
        [product1, product2, product3],
    )

    print(category1.name == "Смартфоны")
    print(category1.description)
    print(len(category1.products))
    print(category1.category_count)
    print(category1.product_count)

    product4 = Product('55" QLED 4K', "Фоновая подсветка", 123000.0, 7)
    category2 = Category(
        "Телевизоры",
        "Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и помощником",
        [product4],
    )

    print(category2.name)
    print(category2.description)
    print(len(category2.products))
    print(category2.products)

    print(Category.category_count)
    print(Category.product_count)

    print(category1.products)
    product4 = Product("55\" QLED 4K", "Фоновая подсветка", 123000.0, 7)
    category1.add_product(product4)
    print(category1.products)
    print(category1.product_count)
    print(category1)
    print(category2)
    print(category1.products)

