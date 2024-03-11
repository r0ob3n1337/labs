import re


def lab_4_1(a: int):
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


def lab_4_3() -> bool:
    """Магическая ли дата?"""
    date = input("Введите дату по формату дд.мм.гггг: ")
    date_pattern = r"^(0[1-9]|[12][0-9]|3[01])\.(0[1-9]|1[012])\.\d{4}$"

    if re.match(date_pattern, date):
        [day, month, year] = date.split(".")
        return int(day) * int(month) == int(year[-2:])
    else:
        print("[ОШИБКА] Неверный формат входной даты.")
        return False


def lab_4_4() -> bool:
    """Счастливый ли билет"""
    ticket_number = input("Введите номер билетика: ")
    ticket_number_length = len(ticket_number)

    if ticket_number_length < 2 or ticket_number_length % 2 > 0:
        print("Количество символов в номере должно быть четным.")
        return False

    [left_numbers, right_numbers] = ticket_number[:: int(len(ticket_number) / 2)]
    left_sum = sum(int(i) for i in list(left_numbers))
    right_sum = sum(int(i) for i in list(right_numbers))

    return left_sum == right_sum


print(lab_4_4())
