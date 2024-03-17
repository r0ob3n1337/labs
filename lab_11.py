"""ООП"""


class Restaurant:
    """Класс ресторана"""

    def __init__(self, name: str, cuisin_type: str, rate: float) -> None:
        self.name = name
        self.cuisin_type = cuisin_type
        self.rate = rate

    def describe_restaurant(self):
        """Вывести название ресторана и тип кухни"""
        print(
            f"Название: {self.name} | Кухня: {self.cuisin_type} | Рейтинг: {self.rate}"
        )

    def open_restaurant(self):
        """Вывести состояние, открыт ли ресторан"""
        print("Ресторан открыт!")

    def update_rate(self, new_rate: float):
        """Установить рейтинг заведения"""
        self.rate = new_rate
        print(f"Рейтинг {self.name} обновлен!")


def lab_11_1():
    """Создание экземпляра класса ресторана"""
    rest1 = Restaurant("Вкусно - и точка!", "фастфуд", 4.30)
    print(rest1.name)
    print(rest1.cuisin_type)
    rest1.describe_restaurant()
    rest1.open_restaurant()


def lab_11_2():
    """Создание нескольких экземпляров ресторана"""
    rest1 = Restaurant("Вкусно - и точка!", "фастфуд", 4.35)
    rest2 = Restaurant("Хочупури", "грузинская", 5.0)
    rest3 = Restaurant("У Рубэна", "армянская", 4.25)

    rest1.describe_restaurant()
    rest2.describe_restaurant()
    rest3.describe_restaurant()

    # lab_11_3
    rest1.update_rate(4.52)
    rest1.describe_restaurant()


lab_11_2()
