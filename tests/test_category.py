from src.category import Category


def test_category(first_category: Category) -> None:
    assert first_category.name == "Смартфоны"
    assert (
        first_category.description
        == "Смартфоны, как средство не только коммуникации,но и получения дополнительных функций для удобства жизни"
    )
    assert len(first_category.products) == 3
    assert Category.category_count == 1
