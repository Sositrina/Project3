from src.category import Category
from src.lawngrass import LawnGrass
from src.product import Product
from src.smartphone import Smartphone

if __name__ == "__main__":
    # Создание продуктов класса Product
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)

    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)

    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

    product4 = Product('55" QLED 4K', "Фоновая подсветка", 123000.0, 7)
    for p in [product1, product2, product3, product4]:
        print(p)

    # Создание продуктов из классов наследников
    phone1 = Smartphone("Пусто", "Пусто", 0, 0, "Пусто", "Пусто", "Пусто", "Пусто")

    phone2 = Smartphone("Пусто", "Пусто", 0, 0, "Пусто", "Пусто", "Пусто", "Пусто")

    grass = LawnGrass("Пусто", "Пусто", 0, 0, "Пусто", 0, "Пусто")

    for p in [phone1, phone2, grass]:
        print(p)

    # Сложение одинаковых классов
    print(f"{phone1.name} + {phone2.name} =", phone1 + phone2)

    # Сложение разных классов
    try:
        result = phone1 + grass
    except TypeError as e:
        print("Ошибка:", e)

    # Создание категорий
    category1 = Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации," "но и получения дополнительных функций для удобства жизни",
        [product1, product2, product3],
    )

    category2 = Category(
        "Телевизоры",
        "Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и помощником",
        [product4],
    )

    print(category1)
    print(category2)
