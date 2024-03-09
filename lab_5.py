import random
from utils import get_uniq_random_int, get_occurence_count


def lab_5_1():
    """Угадай одно из 5 чисел: которые я загадал"""
    from_limit = 0
    to_limit = 20

    try:
        print(f"Какое число я загадал от {from_limit} до {to_limit}?")
        answer = input("Ваш ответ: ")
        random_numbers = [random.randint(from_limit, to_limit) for _ in range(5)]

        print("Я загадывал: ", ", ".join(map(str, random_numbers)))
        if int(answer) in random_numbers:
            print("Поздравляю, Вы угадали число!")
            return True
        print("Нет такого числа")
        return False
    except ValueError:
        print("[ОШИБКА] Возможно вы ввели не число... Попробуйте еще раз.")
        return False


def lab_5_2():
    """Количество повторяющихся значений в списке"""
    my_list = [random.randint(0, 10) for _ in range(10)]
    numbers_count = {}

    for i in my_list:
        if i in numbers_count:
            numbers_count[i] += 1
        else:
            numbers_count[i] = 1

    print("Список значений: ", ", ".join(map(str, my_list)))

    for k, v in numbers_count.items():
        if v > 1:
            print(f'Значение "{k}" встретилось {v} раз(-а)!')


def lab_5_3():
    """Бездельник считает сколько ему дней работать!"""
    week_days = (
        "понедельник",
        "вторник",
        "среда",
        "четверг",
        "пятница",
        "суббота",
        "воскресенье",
    )

    days_off_num = input("Сколько выходных на неделе хотите: ")

    try:
        if int(days_off_num) == 7:
            print("А работать кто будет? :)")
        elif int(days_off_num) == 0:
            print("Ого, без выходных!")
        else:
            weekends = week_days[-int(days_off_num) :]
            lost_week_days = week_days[: -int(days_off_num)]
            print("Ваши выходные дни: ", ", ".join(weekends))
            print("Но поработать нужно в эти дни: ", ", ".join(lost_week_days))
    except ValueError:
        print("[ОШИБКА] Кажется ввели неверное значение. Попробуйте число")
    except IndexError:
        print("[ОШИБКА] Значение должно быть от 0 до 7")


def lab_5_4():
    """Команда из игроков двух групп. Подробный вывод"""
    group_1 = [
        "Иванов",
        "Смирнов",
        "Кузнецов",
        "Васильев",
        "Петров",
        "Михайлов",
        "Попов",
        "Соколов",
        "Козлов",
        "Новиков",
    ]
    group_2 = [
        "Морозов",
        "Волков",
        "Семёнов",
        "Соловьёв",
        "Фёдоров",
        "Лебедев",
        "Григорьев",
        "Зайцев",
        "Николаев",
        "Макаров",
    ]

    group_1_players = tuple(
        group_1[i] for i in get_uniq_random_int(5, len(group_1) - 1)
    )
    group_2_players = tuple(
        group_2[i] for i in get_uniq_random_int(5, len(group_2) - 1)
    )

    total_team = group_1_players + group_2_players

    print("Игроки из 1-й группы:", ", ".join(group_1_players))
    print("Игроки из 2-й группы:", ", ".join(group_2_players))
    print("Наша общая команда:", ", ".join(total_team))
    print(f"Играет {len(total_team)} игроков.")
    print("В алфавитном порядке:", ", ".join(sorted(total_team)))

    occurence_target = "Иванов"
    occurence_count = get_occurence_count(sorted(total_team), "Иванов")
    print(f"{occurence_target} встречался в списке игроков {occurence_count} раз!")


lab_5_4()
