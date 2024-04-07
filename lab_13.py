from utils import get_weather_by_city

import tkinter as tk

from classes.weather_response import Location, Current


def get_formatted_info(weather: tuple[Location, Current]):
    """Форматирование данных погоды в строку"""
    (location, current) = weather

    return (
        f"Город: {location.name} | {current.condition.text}\n"
        f"{int(current.temp_c)}°C (ощущается как {int(current.feelslike_c)}°C)\n"
        f"Видимость: {current.vis_km} км\n"
        f"Широта: {location.lat} | Долгота: {location.lon}\n"
    )


def lab_13():
    """Узнать погоду для конкретного города"""
    root = tk.Tk()
    root.title("Погода в городе")
    root.geometry("350x200")
    root.configure(padx=16, pady=8)

    label = tk.Label(
        root, text="Введите город на английском\n[Moscow, Saint Petersburg]", pady=4
    )
    label.pack(fill="x")

    entry = tk.Entry(root)
    entry.insert(0, "Saint Petersburg")
    entry.pack(fill="x", pady=4)

    button = tk.Button(
        root,
        text="Показать",
        padx=12,
        pady=4,
        command=lambda: info_label.configure(
            text=get_formatted_info(get_weather_by_city(entry.get()))
        ),
    )
    button.pack(fill="x")

    info_label = tk.Label(root, text="", justify="left")
    info_label.pack(fill="x")

    root.mainloop()


lab_13()
