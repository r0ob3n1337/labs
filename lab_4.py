def lab_4_1(a: int) -> bool:
    """Делится ли число на 3 без остатка"""
    print(a != 0 and a % 3 == 0)


def lab_4_2():
    """Деление числа 100 на введенное число"""

    try:
        n = int(input("Введите число: "))
        print(f"100 / {n} = {100/n%.0}")
    except ValueError:
        print("[ОШИБКА] Нужно вводить число!")
    except ZeroDivisionError:
        print("[Ошибка] Деление на ноль!")
