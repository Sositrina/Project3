from unittest.mock import patch, mock_open
from src.utils import read_json, create_objects_from_json
from src.category import Category

def test_read_json():
    fake_data = [{"name": "TestCat", "description": "Desc", "products": []}]
    m = mock_open()
    with patch("builtins.open", m), patch("json.load", return_value=fake_data):
        result = read_json("fake_path.json")

    assert result == fake_data
    m.assert_called_once()

def test_create_objects_from_json():
    fake_data = [
        {
            "name": "Смартфоны",
            "description": "Описание",
            "products": [
                {"name": "iPhone", "description": "Телефон", "price": 1000.0, "quantity": 5}
            ]
        }
    ]
    result = create_objects_from_json(fake_data)

    assert isinstance(result, list)
    assert isinstance(result[0], Category)
    assert isinstance(result[0].products[0], str)
    assert "iPhone" in result[0].products[0]
    assert "1000.0 руб." in result[0].products[0]