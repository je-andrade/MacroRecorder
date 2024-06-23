from time import sleep
import pyautogui
import keyboard
import mouse


class Macro:
    def __init__(self):
        self.instructions = []
        self.index = 0
        self.end = 0

        self.stop = False
        self.no_input_timer = 0

    def add_wait(self, time_seconds: int):
        self.instructions.append({"type": "wait", "time": time_seconds})
        print(f"wait {time_seconds}")

    def add_click(self, x: int, y: int, mouse_btn: str):
        self.instructions.append(
            {"type": "click", "x": x, "y": y, "mouse_btn": mouse_btn})

    def add_key_press(self, key: str):
        self.instructions.append({"type": "key_press", "key": key})

    def add_key_release(self, key: str):
        self.instructions.append({"type": "key_release", "key": key})

    def add_goto(self, index: int):
        self.instructions.append({"type": "goto", "index": index})

    def key_release_all(self):
        """
        Releases all keys currently held down.

        This function iterates over a list of all possible keys and releases each one using pyautogui.keyUp().
        This is useful when you want to ensure that no keys are left held down after executing a macro.

        Parameters:
        None

        Returns:
        None
        """

        key_list = ['\t', '\n', '\r', ' ', '!', '"', '#', '$', '%', '&', "'", '(',
                    ')', '*', '+', ',', '-', '.', '/', '0', '1', '2', '3', '4', '5', '6', '7',
                    '8', '9', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`',
                    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
                    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '{', '|', '}', '~',
                    'accept', 'add', 'alt', 'altleft', 'altright', 'apps', 'backspace',
                    'browserback', 'browserfavorites', 'browserforward', 'browserhome',
                    'browserrefresh', 'browsersearch', 'browserstop', 'capslock', 'clear',
                    'convert', 'ctrl', 'ctrlleft', 'ctrlright', 'decimal', 'del', 'delete',
                    'divide', 'down', 'end', 'enter', 'esc', 'escape', 'execute', 'f1', 'f10',
                    'f11', 'f12', 'f13', 'f14', 'f15', 'f16', 'f17', 'f18', 'f19', 'f2', 'f20',
                    'f21', 'f22', 'f23', 'f24', 'f3', 'f4', 'f5', 'f6', 'f7', 'f8', 'f9',
                    'final', 'fn', 'hanguel', 'hangul', 'hanja', 'help', 'home', 'insert', 'junja',
                    'kana', 'kanji', 'launchapp1', 'launchapp2', 'launchmail',
                    'launchmediaselect', 'left', 'modechange', 'multiply', 'nexttrack',
                    'nonconvert', 'num0', 'num1', 'num2', 'num3', 'num4', 'num5', 'num6',
                    'num7', 'num8', 'num9', 'numlock', 'pagedown', 'pageup', 'pause', 'pgdn',
                    'pgup', 'playpause', 'prevtrack', 'print', 'printscreen', 'prntscrn',
                    'prtsc', 'prtscr', 'return', 'right', 'scrolllock', 'select', 'separator',
                    'shift', 'shiftleft', 'shiftright', 'sleep', 'space', 'stop', 'subtract', 'tab',
                    'up', 'volumedown', 'volumemute', 'volumeup', 'win', 'winleft', 'winright', 'yen',
                    'command', 'option', 'optionleft', 'optionright']

        for key in key_list:
            pyautogui.keyUp(key)

    def run(self):
        while self.index < len(self.instructions):
            print(f"index:{self.index}")

            if self.instructions[self.index]["type"] == "wait":
                sleep(self.instructions[self.index]["time"])
                self.index += 1

            elif self.instructions[self.index]["type"] == "click":
                pyautogui.click(
                    x=self.instructions[self.index]["x"],
                    y=self.instructions[self.index]["y"],
                    button=self.instructions[self.index]["mouse_btn"])
                self.index += 1

            elif self.instructions[self.index]["type"] == "key_press":
                pyautogui.keyDown(self.instructions[self.index]["key"])
                self.index += 1

            elif self.instructions[self.index]["type"] == "key_release":
                pyautogui.keyUp(self.instructions[self.index]["key"])
                self.index += 1

            elif self.instructions[self.index]["type"] == "goto":
                self.index = self.instructions[self.index]["index"]

        self.key_release_all()

    def save(self, path: str, file_name: str) -> bool:
        try:
            with open(path + file_name + ".macro", "w") as file:
                file.write(str(self.instructions))
                return True
        except:
            return False

    def load(self, file_path: str) -> bool:
        try:
            with open(file_path, "r") as file:
                self.instructions = eval(file.read())
                return True
        except:
            return False

    def record_instructions(self, append: bool = False):
        if append == False:
            self.clear_instructions()

    def clear_instructions(self):
        self.instructions = []
        self.index = 0
        self.end = 0

        print("instructions cleared")


if __name__ == "__main__":
    macro = Macro()
    macro.add_wait(1)
    macro.add_click(100, 100, "left")
    macro.add_key_press("a")
    macro.add_key_release("a")
    macro.add_key_press("b")
    macro.add_key_release("b")
    macro.add_key_press("c")
    macro.add_key_release("c")
    macro.add_key_press("d")
    macro.add_key_release("d")
    macro.add_key_press("e")
    macro.add_key_release("e")
    macro.add_key_press("f")
    macro.add_key_release("f")
    macro.add_key_press("g")
    macro.add_key_release("g")
    macro.add_goto(0)

    macro.run()
