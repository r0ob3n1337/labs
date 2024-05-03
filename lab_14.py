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
    def __init__(self):
        super(Calculator, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.a = None
        self.b = None
        self.total = None

        self.input = self.ui.input
        self.result = self.ui.lbl_result
        self.input_max_len = self.input.maxLength()

        self.connect_numbers_buttons()
        self.connect_clear_buttons()
        self.connect_dot_button()
        self.connect_math_operations()
        self.connect_calculate_button()

    def connect_numbers_buttons(self) -> None:
        """Обработка на клавиши-цифры"""
        self.ui.btn_0.clicked.connect(lambda: self.add_number("0"))
        self.ui.btn_1.clicked.connect(lambda: self.add_number("1"))
        self.ui.btn_2.clicked.connect(lambda: self.add_number("2"))
        self.ui.btn_3.clicked.connect(lambda: self.add_number("3"))
        self.ui.btn_4.clicked.connect(lambda: self.add_number("4"))
        self.ui.btn_5.clicked.connect(lambda: self.add_number("5"))
        self.ui.btn_6.clicked.connect(lambda: self.add_number("6"))
        self.ui.btn_7.clicked.connect(lambda: self.add_number("7"))
        self.ui.btn_8.clicked.connect(lambda: self.add_number("8"))
        self.ui.btn_9.clicked.connect(lambda: self.add_number("9"))

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
        self.ui.btn_plus.clicked.connect(lambda: self.add_temp_operation("+"))
        self.ui.btn_minus.clicked.connect(lambda: self.add_temp_operation("-"))
        self.ui.btn_divide.clicked.connect(lambda: self.add_temp_operation("/"))
        self.ui.btn_mult.clicked.connect(lambda: self.add_temp_operation("*"))

    def clear_all(self) -> None:
        """Очистка поля и результатов"""
        self.result.clear()
        self.input.setText("0")

    def clear_input(self) -> None:
        """Очистка поля"""
        self.input.setText("0")

    def add_number(self, btn_text: str) -> None:
        """Добавляем цифру в инпут при нажатии на кнопку"""
        if self.input.text() == "0":
            self.input.setText(btn_text)
        else:
            self.input.setText(self.input.text() + btn_text)

    def add_dot(self) -> None:
        """Добавляем точку в инпут при нажатии на кнопку, если ее еще нет"""
        if "." not in self.input.text():
            self.input.setText(self.input.text() + ".")

    def add_temp_operation(self, operation: str):
        """Запись математической операции в лейбл"""
        if not self.ui.lbl_result.text():
            self.ui.lbl_result.setText(self.ui.input.text() + f" {operation}")
            self.ui.input.setText("0")

    def remove_extra_zeros(self, num: Union[float, int, str]) -> str:
        n = str(float(num))
        return n.replace(".0", "") if n.endswith(".0") else n

    def get_num(self) -> Union[int, float]:
        """Берем значение из инпута с введенными"""
        input_text = self.ui.input.text().strip(".")
        return float(input_text) if "." in input_text else int(input_text)

    def get_temp_num(self) -> Union[float, int, None]:
        """Если текст есть в лейбле операций, то берем оттуда число ДО знака"""
        if self.ui.lbl_result.text():
            temp = self.ui.lbl_result.text().strip(".").split()[0]
            return float(temp) if "." in temp else int(temp)

    def get_math_operation_symbol(self) -> Optional[str]:
        """Если текст есть в лейбле операций, то берем оттуда знак операции"""
        if self.ui.lbl_result.text():
            return self.ui.lbl_result.text().strip(".").split()[-1]

    def calculate(self) -> Optional[str]:
        """Основная функция калькуляции"""
        if self.ui.input.text():
            result = self.remove_extra_zeros(
                str(
                    OPERATIONS[self.get_math_operation_symbol()](
                        self.get_temp_num(), self.get_num()
                    )
                )
            )
            self.ui.lbl_result.setText(
                f"{self.get_temp_num()} {self.get_math_operation_symbol()} {self.get_num()} = {result}"
            )
            self.ui.input.setText(result)
            return result


if __name__ == "__main__":
    app = QApplication([])

    window = Calculator()
    window.show()

    sys.exit(app.exec())
