from random import randint
from typing import List, Any


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
