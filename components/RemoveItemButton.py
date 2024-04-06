import tkinter as tk
from tkinter import messagebox


class RemoveItemButton(tk.Button):
    """Класс компонента кнопки удаления айтема из листбокса"""

    def __init__(self, parent: tk.Frame, listbox: tk.Listbox):
        super().__init__(
            parent,
            text="-",
            bg="#FF5555",
            borderwidth=0,
            command=self.remove_item,
        )
        self.listbox = listbox

    def remove_item(self):
        """Удаление выбранного элемента из листбокса"""
        values = self.listbox.curselection()

        try:
            self.listbox.delete(values[0])
        except IndexError:
            messagebox.showwarning("Внимание", "Сначала нужно выбрать вид")
