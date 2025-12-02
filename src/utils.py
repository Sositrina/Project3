import json
import os
from typing import Any, Dict, List

from src.category import Category
from src.product import Product


def read_json(path: str) -> List[Dict[str, Any]]:
    """Принимает путь к файлу и возвращает данные в словаре"""
    full_patch = os.path.abspath(path)
    with open(full_patch, "r", encoding="UTF-8") as file:
        data: List[Dict[str, Any]] = json.load(file)
    return data


def create_objects_from_json(data: List[Dict[str, Any]]) ->  List[Category]:
    """Принимает json файл и возвращает список"""
    products = []
    for product in data:
        categorys = []
        for category in product["products"]:
            categorys.append(Product(**category))
            product["products"] = categorys
            products.append(Category(**product))
    return products


if __name__ == "__main__":
    raw_data = read_json("../data/products.json")
    products_data = create_objects_from_json(raw_data)

    print(products_data[0].name)
    print(products_data[0].products)
