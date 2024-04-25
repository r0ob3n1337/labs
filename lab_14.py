import sys

from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton

from lab_14.ui import Ui_MainWindow


NUMBERS_BUTTONS = [f"btn_{num}" for num in range(10)]


class Calculator(QMainWindow):
    def __init__(self):
        super(Calculator, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.input = self.ui.input
        self.result = self.ui.lbl_result
        self.input_max_len = self.input.maxLength()

        self.connect_numbers_buttons()
        self.connect_clear_buttons()
        self.connect_dot_button()

    def connect_numbers_buttons(self) -> None:
        """Инициализируем метод нажатия на кнопку для каждой кнопки"""
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
        """Инициализация методов очистки поля и результатов"""
        self.ui.btn_c.clicked.connect(lambda: self.clear_input())
        self.ui.btn_ce.clicked.connect(lambda: self.clear_all())

    def connect_dot_button(self) -> None:
        """Инициализация метода для точки"""
        self.ui.btn_dot.clicked.connect(lambda: self.add_dot())

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


if __name__ == "__main__":
    app = QApplication([])

    window = Calculator()
    window.show()

    sys.exit(app.exec())
