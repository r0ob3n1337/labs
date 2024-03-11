"""Работа с файлами"""

import os
import random
from PIL import Image, ImageFilter


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
            with Image.open(os.path.join(source_path_dir, image_name)) as image:
                img_name, img_ext = os.path.splitext(image_name)
                filtered_image = image.convert("RGB").filter(
                    random.choice(applied_filters)
                )
                filtered_image.save(
                    os.path.join(output_path_dir, f"{img_name}_filtered.{img_ext}")
                )
    except OSError:
        print("[ОШИБКА] Проблемы с файлами.")


def lab_9_2():
    pass


def lab_9_3():
    pass


lab_9_1()
