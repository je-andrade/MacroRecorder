import customtkinter as ctk
import CTkMenuBar as ctkm
import tksvg
from Macro import Macro


class App:
    def __init__(self, name, width, height):
        self.macro = Macro()

        self.root = ctk.CTk()
        self.root.title(name)
        self.root.geometry(f"{width}x{height}")
        self.root.resizable(True, True)
        self.root.minsize(width, height)
        self.root.configure(background="#181919")
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)

        self.menu = ctkm.CTkMenuBar(self.root)
        self.menu.add_cascade("File")
        self.menu.add_cascade("Edit")
        self.menu.add_cascade("View")
        self.menu.add_cascade("Tools")
        self.menu.add_cascade("Help")

    def render(self):
        self.root.mainloop()

    def on_closing(self):
        self.root.destroy()


if __name__ == "__main__":
    app = App("MACRO RECORDER", 400, 300)
    app.render()