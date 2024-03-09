from random import randint
from typing import List, Any
from PIL import Image, ImageDraw, ImageOps, ImageEnhance


def get_uniq_random_int(length: int, max_value: int) -> List[int]:
    """Возвращает массив уникальных рандомных чисел"""
    numbers = []
    while len(numbers) < length:
        n = randint(0, max_value)
        if n not in numbers:
            numbers.append(n)
    return numbers


def get_occurence_count(source_list: List[Any], target: Any) -> int:
    """Количество вхождений target в список"""
    occurences = 0

    if target not in source_list:
        return 0

    for elem in source_list:
        if elem == target:
            occurences += 1

    return occurences


def get_countries_capitals():
    """Получить словарь стран и их столиц"""
    return {
        "Russia": "Moscow",
        "USA": "Washington",
        "China": "Beijing",
        "India": "New Delhi",
        "Germany": "Berlin",
        "France": "Paris",
        "Japan": "Tokyo",
        "Brazil": "Brasilia",
        "Canada": "Ottawa",
        "Australia": "Canberra",
    }


def get_chars_rates():
    """Получить значение баллов для каждой буквы"""
    return {
        1: ["а", "в", "е", "и", "н", "о", "р", "с", "т"],
        2: ["д", "к", "л", "м", "п", "у"],
        3: ["б", "г", "ё", "ь", "я"],
        4: ["й", "ы"],
        5: ["ж", "з", "х", "ц", "ч"],
        8: ["ш", "э", "ю"],
        10: ["ф", "щ", "ъ"],
    }


def get_students_and_languages():
    """Получить студентов и известные им языки"""
    return {
        "Иван Петров": ["русский", "английский", "китайский"],
        "Анна Сидорова": ["русский", "английский", "немецкий"],
        "Петр Иванов": ["японский", "английский", "французский"],
        "Мария Кузнецова": ["русский", "китайский"],
        "Алексей Смирнов": ["русский"],
        "Елена Попова": ["русский", "английский"],
        "Сергей Федоров": ["китайский", "английский", "русский"],
        "Ольга Васильева": ["русский", "немецкий", "французский"],
        "Максим Лебедев": ["русский", "английский", "испанский"],
        "Екатерина Козлова": ["русский", "английский"],
    }


def add_watermark_to_image(image: Image.Image):
    """Добавить водяной знак на картинку"""
    try:
        with Image.open("boo.png") as watermark:
            resized_watermark = watermark.resize(
                size=(int(image.width / 5), int(image.height / 5))
            )
            resized_watermark = resized_watermark.convert("RGBA")
            result = image.paste(resized_watermark)
            return result
    except OSError:
        print("[ОШИБКА] Проблемы с изображением.")
