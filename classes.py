"""Классы"""


class Restaurant:
    """Класс ресторана"""

    def __init__(self, name: str, cuisin_type: str, rate: float) -> None:
        self.name = name
        self.cuisin_type = cuisin_type
        self.rate = rate

    def describe_restaurant(self):
        """Вывести название ресторана и тип кухни"""
        print(
            f"Название: {self.name} | Кухня: {self.cuisin_type} | Рейтинг: {self.rate}"
        )

    def open_restaurant(self):
        """Вывести состояние, открыт ли ресторан"""
        print("Ресторан открыт!")

    def update_rate(self, new_rate: float):
        """Установить рейтинг заведения"""
        self.rate = new_rate
        print(f"Рейтинг {self.name} обновлен!")


# lab 12-1
# lab 12-2
class IceCreamStand(Restaurant):
    """Магазин мороженого"""

    def __init__(
        self,
        name: str,
        cuisin_type: str,
        rate: float,
        flavors: list[str],
        location: str,
        work_start_at: int,
        work_end_at: int,
    ) -> None:
        super().__init__(name, cuisin_type, rate)
        self.flavors = flavors
        self.location = location
        self.work_start_at = work_start_at
        self.work_end_at = work_end_at

    def get_flavors(self):
        """Вывести сорты мороженого"""
        print("Сорты мороженого:", ", ".join(self.flavors))

    def is_exist_flavor(self, name):
        """Есть ли такой вкус"""
        return name in self.flavors

    def add_flavor(self, fl: str):
        """Добавить вкус в продажу"""
        if self.is_exist_flavor(fl):
            print("Такой вкус уже есть в продаже")
        else:
            self.flavors.append(fl)
            print(f'Вкус "{fl}" добавлен в продажу')

    def remove_flavor(self, fl: str):
        """Удалить вкус из продаж"""
        if self.is_exist_flavor(fl):
            self.flavors.remove(fl)
            print(f'Вкус "{fl}" убран из продажи')
        else:
            print(f"Такого вида мороженого нет у магазина {self.name}.")
            print("У нас есть:", ", ".join(self.flavors))
