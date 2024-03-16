"""Работа с файлами"""

import os
import random
import csv
from PIL import Image, ImageFilter


# For lab-9-2
VALID_IMAGE_EXTS = ("jpg", "jpeg", "png")


def lab_9_1():
    """Получить список всех файлов в папке"""
    source_path_dir = os.path.join(os.getcwd(), "lab_7")
    output_path_dir = os.path.join(os.getcwd(), "lab_9")

    if not os.path.exists(output_path_dir):
        os.makedirs(output_path_dir)

    source_images_name = [
        f for f in os.listdir(source_path_dir) if not f.endswith("_filtered.jpg")
    ]

    applied_filters = [
        ImageFilter.CONTOUR,
        ImageFilter.SMOOTH,
        ImageFilter.SHARPEN,
        ImageFilter.EMBOSS,
        ImageFilter.EDGE_ENHANCE,
    ]

    try:
        for image_name in source_images_name:
            img_name, img_ext = os.path.splitext(image_name)
            if img_ext in VALID_IMAGE_EXTS:
                with Image.open(os.path.join(source_path_dir, image_name)) as image:
                    filtered_image = image.convert("RGB").filter(
                        random.choice(applied_filters)
                    )
                    filtered_image.save(
                        os.path.join(output_path_dir, f"{img_name}_filtered.{img_ext}")
                    )
    except OSError:
        print("[ОШИБКА] Проблемы с файлами.")


def lab_9_3():
    """Вывести содержимое CSV файла. Подсчитать итоговую стоимость."""
    try:
        total_price = 0

        with open("lab_9_3_mock.csv", encoding="UTF-8") as f:
            reader = csv.reader(f)
            next(reader)

            print("Нужно купить:")
            for item, count, price in reader:
                total_price += int(price) * int(count)
                print(f"[ ] {item} - {count} шт. за {price} руб.")
            print(f"Итого: {total_price} руб.")
    except OSError:
        print("[ОШИБКА] Проблемы с файламом CSV.")


lab_9_3()
