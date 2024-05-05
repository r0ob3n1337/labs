"""ООП"""

from classes.restaurant import Restaurant


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
