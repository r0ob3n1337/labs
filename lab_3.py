import random


def lab_3_1():
    n = input("Сколько слов вводим? ")

    if n is None or int(n) <= 0:
        print("1 и более слов...")
        return

    words = []
    while len(words) < int(n):
        word = input("Введите слово: ")
        words.append(word)

    print(" ".join(words))


def lab_3_2():
    words = []
    is_repeat = True

    print("Программа будет принимать слова до тех пор, пока не напишите слово stop.")

    while is_repeat:
        w = input("Введите слово: ")
        if w == "stop":
            is_repeat = False
        else:
            words.append(w)

    print(f'Написанные вами слова: {" ".join(words)}')


def lab_3_3():
    is_repeat = True

    print("Проверка слов на редкость! Играем, пока не напишите слово stop.")

    while is_repeat:
        word = input("Слово: ")
        if word == "stop":
            is_repeat = False
        elif "ф" in word:
            print("Вот это реально редкое слово!")
        else:
            print("Эх... Обычное слово...")
    print("Конец игры...")


def lab_3_4():
    correct_answers = 0
    wrong_answers = 0

    while wrong_answers < 3:
        num1 = random.randint(1, 10)
        num2 = random.randint(1, 10)
        answer = int(input(f"{num1} + {num2} = "))

        if answer == num1 + num2:
            print("Правильно!")
            correct_answers += 1
        else:
            print("Ошибка!")
            wrong_answers += 1

    print(f"Конец игры. Правильных ответов: {correct_answers}")
