import sys
from operator import add, sub, mul, truediv
from typing import Union, Optional

from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton

from lab_14.ui import Ui_MainWindow


NUMBERS_BUTTONS = [f"btn_{num}" for num in range(10)]

OPERATIONS = {
    "+": add,
    "-": sub,
    "/": truediv,
    "*": mul,
}


class Calculator(QMainWindow):
    """Калькулятор"""

    def __init__(self):
        super(Calculator, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.a_nums = []
        self.b_nums = []
        self.operation = None
        self.total = None

        self.connect_numbers_buttons()
        self.connect_clear_buttons()
        self.connect_dot_button()
        self.connect_math_operations()
        self.connect_calculate_button()

    def connect_numbers_buttons(self) -> None:
        """Обработка на клавиши-цифры"""
        self.ui.btn_0.clicked.connect(lambda: self.press_number("0"))
        self.ui.btn_1.clicked.connect(lambda: self.press_number("1"))
        self.ui.btn_2.clicked.connect(lambda: self.press_number("2"))
        self.ui.btn_3.clicked.connect(lambda: self.press_number("3"))
        self.ui.btn_4.clicked.connect(lambda: self.press_number("4"))
        self.ui.btn_5.clicked.connect(lambda: self.press_number("5"))
        self.ui.btn_6.clicked.connect(lambda: self.press_number("6"))
        self.ui.btn_7.clicked.connect(lambda: self.press_number("7"))
        self.ui.btn_8.clicked.connect(lambda: self.press_number("8"))
        self.ui.btn_9.clicked.connect(lambda: self.press_number("9"))

    def connect_clear_buttons(self) -> None:
        """Обработка кликов на кнопки очистки поля и результатов"""
        self.ui.btn_c.clicked.connect(self.clear_input)
        self.ui.btn_ce.clicked.connect(self.clear_all)

    def connect_dot_button(self) -> None:
        """Обработка клика по кнопке точки"""
        self.ui.btn_dot.clicked.connect(self.add_dot)

    def connect_calculate_button(self) -> None:
        """Обработка клика по кнопке равно"""
        self.ui.btn_calc.clicked.connect(self.calculate)

    def connect_math_operations(self) -> None:
        """Обработка клика по кнпокам математических операций"""
        self.ui.btn_plus.clicked.connect(lambda: self.press_operation("+"))
        self.ui.btn_minus.clicked.connect(lambda: self.press_operation("-"))
        self.ui.btn_divide.clicked.connect(lambda: self.press_operation("/"))
        self.ui.btn_mult.clicked.connect(lambda: self.press_operation("*"))

    def clear_temp_vars(self) -> None:
        self.a_nums = []
        self.b_nums = []
        self.operation = None
        self.total = None

    def clear_all(self) -> None:
        """Очистка поля и результатов"""
        self.ui.lbl_result.clear()
        self.ui.input.setText("0")
        self.clear_temp_vars()

    def clear_input(self) -> None:
        """Очистка поля"""
        self.ui.input.setText("0")

    def press_number(self, number: str) -> None:
        """Добавляем цифру в инпут при нажатии на кнопку"""
        if self.operation:
            self.b_nums.append(number)
            self.ui.input.setText("".join(self.b_nums))
        else:
            self.a_nums.append(number)
            self.ui.input.setText("".join(self.a_nums))

    def add_dot(self) -> None:
        """Добавляем точку в инпут при нажатии на кнопку, если ее еще нет"""
        if "." not in self.ui.input.text():
            self.ui.input.setText(self.ui.input.text() + ".")

    def press_operation(self, operation: str):
        """Запись математической операции в лейбл"""

        if self.total:
            self.a_nums = self.total.split()

        self.operation = operation
        self.ui.lbl_result.setText("".join(self.a_nums) + f" {operation}")
        self.ui.input.setText("0")

    def remove_extra_zeros(self, num: Union[float, int, str]) -> str:
        """Очистка лишни нулей"""
        n = str(float(num))
        return n.replace(".0", "") if n.endswith(".0") else n

    def get_right_side_nums(self) -> Union[int, float]:
        """Берем значение из инпута с введенными"""
        if not self.a_nums:
            return 0

        nums = "".join(self.a_nums)
        return float(nums) if "." in nums else int(nums)

    def get_left_side_nums(self) -> Union[float, int, None]:
        """Если текст есть в лейбле операций, то берем оттуда число ДО знака"""
        if not self.b_nums:
            return 0

        nums = "".join(self.b_nums)
        return float(nums) if "." in nums else int(nums)

    def get_operation(self) -> Optional[str]:
        """Если текст есть в лейбле операций, то берем оттуда знак операции"""
        if self.operation:
            return self.operation

    def clear_operation(self):
        """Очистка операции"""
        self.operation = None

    def calculate(self) -> Optional[str]:
        """Основная функция калькуляции"""
        if self.ui.input.text():
            try:
                result = self.remove_extra_zeros(
                    str(
                        OPERATIONS[self.get_operation()](
                            self.get_right_side_nums(), self.get_left_side_nums()
                        )
                    )
                )
                self.ui.lbl_result.setText(
                    f"{self.get_right_side_nums()} {self.get_operation()} {self.get_left_side_nums()} = {result}"
                )

                self.total = result
                self.ui.input.setText(result)
                self.clear_operation()
                self.a_nums = []
                self.b_nums = []

                return result
            except KeyError:
                self.ui.lbl_result.setText("")
                self.ui.input.setText("0")
            except ZeroDivisionError:
                self.ui.lbl_result.setText("Деление на ноль")
                self.ui.input.setText("0")
                self.clear_all()


if __name__ == "__main__":
    app = QApplication([])

    window = Calculator()
    window.show()

    sys.exit(app.exec())
