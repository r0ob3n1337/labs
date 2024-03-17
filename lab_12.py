"""Продолжение ООП"""

import tkinter as tk
from classes import IceCreamStand


def lab_12_1():
    """Создать экземпляр магазинчика мороженого и вывести список видов мороженого"""
    ice1 = IceCreamStand(
        "Супер Лед!",
        "мороженое",
        4.78,
        ["ванильное", "шоколадное", "клубничное"],
        "ТРЦ Мега",
        9,
        18,
    )
    ice1.get_flavors()


def lab_12_2():
    """Интерфейс управления магазинчиком"""
    ice1 = IceCreamStand(
        "Супер Лед!",
        "мороженое",
        4.78,
        ["ванильное", "шоколадное", "клубничное"],
        "ТРЦ Мега",
        9,
        18,
    )

    app = tk.Tk()
    app.title("Управление магазином мороженого")
    app.geometry("500x200")
    for c in range(3):
        app.columnconfigure(index=c, weight=4)
        app.rowconfigure(index=c, weight=4)

    # Left side
    info_frame = tk.Frame(app)
    info_frame.pack(side="left", padx=4, pady=4, fill="both", expand=True)

    name_label = tk.Label(info_frame, text=ice1.name, font=("Consolas", 24, "bold"))
    name_label.pack(side="top", anchor="nw")

    rate_label = tk.Label(
        info_frame, text=f"Рейтинг: {ice1.rate}", font=("Consolas", 10), bg="orange"
    )
    rate_label.pack(side="top", anchor="nw")

    work_time_label = tk.Label(
        info_frame,
        text=f"Время работы: {ice1.work_start_at}-{ice1.work_end_at}",
        font=("Consolas", 14),
    )
    work_time_label.pack(side="bottom", anchor="sw")
    location_label = tk.Label(
        info_frame,
        text=f"Место: {ice1.location}",
        font=("Consolas", 14),
    )
    location_label.pack(side="bottom", anchor="sw")

    # Right side
    flavors_frame = tk.Frame(app)
    flavors_frame.pack(side="right", padx=4)

    flavors_list = tk.Listbox(flavors_frame)
    for i, fl in enumerate(ice1.flavors):
        flavors_list.insert(i, fl)
    flavors_list.pack(side="top")

    add_btn = tk.Button(flavors_frame, text="+", bg="#55FF55", borderwidth=0)
    add_btn.pack(side="left", fill="x", expand=True)

    remove_btn = tk.Button(flavors_frame, text="-", bg="#FF5555", borderwidth=0)
    remove_btn.pack(side="right", fill="x", expand=True)

    app.mainloop()


lab_12_2()
