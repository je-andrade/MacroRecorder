import customtkinter as ctk
import CTkMenuBar as ctkm
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

        self.menu = ctkm.CTkMenuBar(master=self.root)
            
        self.CreateMenuBarDropdown(self.menu.add_cascade("File"),{
            "New File": lambda: print("New File"),
            "Open File": lambda: print("Open File"),
            "Save": lambda: print("Save"),
            "Save as": lambda: print("Save as"),
            "separator": "",
            "Exit": self.on_closing,
        })
        
        self.CreateMenuBarDropdown(self.menu.add_cascade("Settings"),{
            "preferences": lambda: print("preferences")
        })
        
        self.CreateMenuBarDropdown(self.menu.add_cascade("Help"),{
            "About": lambda: print("About")
        })

    def CreateMenuBarDropdown(self, cascade, options:dict):
        dropdown = ctkm.CustomDropdownMenu(cascade)
        for key, value in options.items():
            if key != "separator":
                dropdown.add_option(option=key, command=value)
            else:
                dropdown.add_separator()

    def render(self):
        self.root.mainloop()

    def on_closing(self):
        self.root.destroy()


if __name__ == "__main__":
    app = App("MACRO RECORDER", 400, 300)
    app.render()