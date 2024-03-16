"""Обработка изображений Часть 2"""

import sys
from PIL import Image, ImageDraw, ImageFont


def lab_8_1():
    """Кроп. Обрезка части картинки"""
    try:
        with Image.open("./lab_8/test_image.png") as source:
            text_crop_box = (0, 0, 700, 272)
            crop_text = source.crop(text_crop_box)

            dogs_crop_box = (0, 188, 375, 465)
            crop_dogs = source.crop(dogs_crop_box)

            crop_text.save("./lab_8/text.png", "png")
            crop_dogs.save("./lab_8/dogs.png", "png")
    except OSError:
        print("[ОШИБКА] Возникли проблемы с доступом к картинке.")


def lab_8_2():
    """Получить картинку к празднику"""
    holidays = {
        "всемирный день интроверта": "./lab_8/introvert.png",
        "день соломинки для коктейлей": "./lab_8/solominka.png",
        "день рождения резиновых калош": "./lab_8/kaloshi.png",
        "день кошки в японии": "./lab_8/cats.png",
        "международный день оптимиста": "./lab_8/optimist.png",
    }

    print("Покажем картинку для праздника!")
    print("Нам известны следующие праздники:")
    for h in holidays:
        print(f" - {h}")

    try:
        holiday = input("Для какого праздника вы ищите картинку: ")

        if holiday.lower() in holidays:
            with Image.open(holidays[holiday]) as img:
                print("Вот ваша картинка!")
                img.show(holiday)
                sys.exit()
    except ValueError:
        print("[ОШИБКА] Такого праздника мы не знаем...")


def lab_8_3():
    """Добавить текст на открытку"""
    try:
        name = input("Кого поздравляем (введите имя): ")

        with Image.open("./lab_8/test_image.png") as source:
            txt = Image.new("RGBA", source.size, (255, 255, 255, 0))
            draw = ImageDraw.Draw(txt)
            fnt = ImageFont.truetype("arial.ttf", 60, encoding="UTF-8")

            draw.rectangle((0, 0, source.width, 120), fill=(255, 0, 0))
            draw.text(
                (100, 30),
                f"{name}, поздравляем!",
                font=fnt,
                fill=(255, 255, 255),
                stroke_width=6,
                stroke_fill=(125, 125, 255),
            )

            result = Image.alpha_composite(source, txt)
            result.show()
    except OSError:
        print("[ОШИБКА] Возникли проблемы с доступом к картинке или шрифту.")


lab_8_3()
