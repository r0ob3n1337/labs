import tkinter as tk


class AddItemButton(tk.Button):
    """Класс компонента кнопки добавления айтема в листбокс"""

    def __init__(self, parent: tk.Frame, root: tk.Tk, add_to: tk.Listbox):
        super().__init__(
            parent,
            text="+",
            bg="#55FF55",
            borderwidth=0,
            command=self.open_modal,
        )
        self.root = root
        self.listbox = add_to

    def add_item_to_listbox(self, value: str):
        """Добавление значения в листбокс"""
        self.listbox.insert(self.listbox.size(), value)

    def open_modal(self):
        """Открытие модалки"""
        modal = tk.Toplevel(self.root, padx=8, pady=8)
        modal.title("Добавить вкус")
        modal.geometry("350x150")

        name_label = tk.Label(
            modal, text="Название вкуса", font=("Consolas", 16, "bold")
        )
        name_label.pack(side="top", anchor="n")

        name_value = tk.Text(modal, height=1)
        name_value.pack(side="top", fill="x", anchor="n")

        add_btn = tk.Button(
            modal,
            text="Add",
            command=lambda: self.add_item_to_listbox(
                value=name_value.get("1.0", "end")
            ),
        )
        add_btn.pack(side="top", fill="x", anchor="n")
