"""Работа с JSON"""

import json
import os

from typing import Optional
from dataclasses import dataclass, asdict


JSON_PATH = os.path.join(os.getcwd(), "lab_10", "mock.json")


@dataclass
class Product:
    """Типизация словаря продукта"""

    name: str
    price: int
    weight: int
    available: Optional[bool]


def print_product_info(product: Product):
    """Форматированный вывод информации о продукте"""
    print("Название:", product.name)
    print("Цена:", product.price, "руб.")
    print("Вес:", product.weight, "гр.")
    print("В наличии" if product.available else "Нет в наличии!")
    print("-----")


# For 10.2
def add_new_item(data):
    """Добавить новый продукт"""
    new_item_info = input("Введите через запятую значения: название,цена,вес:\n")
    try:
        new_name, new_price, new_weight = new_item_info.split(",")
        new_item = Product(
            name=new_name,
            price=int(new_price),
            weight=int(new_weight),
            available=True,
        )
        data["products"].append(asdict(new_item))

        with open(JSON_PATH, "w", encoding="utf-8") as f:
            f.write(json.dumps(data, indent=2, ensure_ascii=False))
    except ValueError:
        print("[ОШИБКА] Неверный ввод.")


def lab_10_1():
    """Получение и вывод JSON содержимого"""
    try:
        with open(JSON_PATH, "r", encoding="utf-8") as f:
            data = json.load(f)
            products: list[dict] = data["products"]
            for p in products:
                product = Product(**p)
                print_product_info(product)

        need_add_new = input("Добавить новые товары? [y/n]: ")
        if need_add_new == "y":
            add_new_item(data)

    except OSError:
        print("[ОШИБКА] Проблемы с файламом JSON.")


lab_10_1()
