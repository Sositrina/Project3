from src.smartphone import  Smartphone
from src.lawngrass import   LawnGrass

if __name__ == "__main__":

    phone1 = Smartphone("iPhone 15", "Новый", 50000, 5,
                        "Высокая", "15", "128GB", "Черный")

    phone2 = Smartphone("Samsung", "Новый", 40000, 3,
                        "Высокая", "S23", "256GB", "Белый")

    grass = LawnGrass("Газон", "Семена", 1000, 10,
                      "Россия", 7, "Зеленый")

    print(phone1 + phone2)
    print(phone1 + grass) # ошибка
