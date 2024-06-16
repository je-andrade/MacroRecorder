import tkinter as tk
import tksvg
import customtkinter
from Macro import Macro


class MainWindow:
    def __init__(self, name, width, height):
        self.macro = Macro()

    def render(self):
        pass


if __name__ == "__main__":
    main_window = MainWindow("macro recorder", 800, 600)
    main_window.render()
