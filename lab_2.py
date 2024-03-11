import random


def lab2_1():
    password = input("Введите пароль: ")
    password_again = input("Повторите пароль: ")

    if password == password_again:
        print("Пароль принят")
    else:
        print("Пароль не принят. Попробуйте еще раз.")


def lab2_2():
    place_number = None

    while not place_number:
        place_number = input("Место: ")

    if int(place_number) in range(37, 55):
        print("Место боковое")
        return

    if int(place_number) % 2 == 0:
        print("Место верхнее")
        return
    else:
        print("Место нижнее")


def lab2_3():
    month = None

    try:
        while not month:
            month = input("Введите год: ")

        if (int(month) % 4 == 0 and int(month) % 100 != 0) or int(month) % 400 == 0:
            print(f"Год {month} високосный.")
        else:
            print(f"Год {month} не високосный.")
    except ValueError:
        print("Кажется ввели не число...")


def lab2_4():
    COLORS = ("красный", "синий", "желтый")

    color1 = random.randrange(0, 3)
    color2 = random.randrange(0, 3)

    if color1 == color2:
        print(COLORS[color1])
        return

    if (color1 == 0 or color2 == 0) and (color1 == 1 or color2 == 1):
        print("Фиолетовый")
    elif (color1 == 0 or color2 == 0) and (color1 == 2 or color2 == 2):
        print("Оранжевый")
    elif (color1 == 1 or color2 == 1) and (color1 == 2 or color2 == 2):
        print("Зеленый")
    else:
        print("Не умею такое смешивать...")
