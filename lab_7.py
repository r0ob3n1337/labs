"""Обработка изображений"""

from PIL import Image, ImageFilter
from utils import add_watermark_to_image


TEST_IMAGE_NAME = "./lab_7/test_image.jpg"


def lab_7_1():
    """Получение информации об изображении"""
    try:
        with Image.open(TEST_IMAGE_NAME) as image:
            image.show("Test image from lab-7-1")
            print(f"Формат изображения: {image.format}")
            print(f"Размер картинки: {image.width}x{image.height} пикселей")
            print(f"Цветовая модель: {image.mode}")
    except OSError:
        print("[ОШИБКА] Проблемы с изображением.")


def lab_7_2():
    """Создание миниатюрной версии изображения"""
    try:
        with Image.open(TEST_IMAGE_NAME) as image:
            image.thumbnail((int(image.width / 3), int(image.height / 3)))
            image.save("./lab_7/image_thumbnail.jpg")
    except OSError:
        print("[ОШИБКА] Проблемы с изображением.")


def lab_7_3():
    """Применить фильтры для изображений"""
    applied_filters = [
        ImageFilter.CONTOUR,
        ImageFilter.SMOOTH,
        ImageFilter.SHARPEN,
        ImageFilter.EMBOSS,
        ImageFilter.EDGE_ENHANCE,
    ]

    try:
        for index, image_filter in enumerate(applied_filters):
            with Image.open(f"./lab_7/{index + 1}.jpg") as image:
                filtered_image = image.filter(image_filter)
                filtered_image.save(f"./lab_7/{index+1}_filtered.jpg")
    except OSError:
        print("[ОШИБКА] Проблемы с изображением.")


def lab_7_4():
    """Добавить водяной знак на изображение"""
    try:
        with Image.open(TEST_IMAGE_NAME) as image:
            image_with_watermark = add_watermark_to_image(image)
            if image_with_watermark is not None:
                image_with_watermark.save("./lab_7/image_with_watermark.png")
    except OSError:
        print("[ОШИБКА] Проблемы с изображением.")


lab_7_4()
