"""
Collect data from wearable devices.
"""
import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW


class wearablecollection(toga.App):

    def startup(self):
            main_box = toga.Box(style=Pack(direction=COLUMN))

            name_label = toga.Label(
                'Your name: ',
                style=Pack(padding=(0, 5))
            )
            self.name_input = toga.TextInput(style=Pack(flex=1))

            name_box = toga.Box(style=Pack(direction=ROW, padding=5))
            name_box.add(name_label)
            name_box.add(self.name_input)

            button = toga.Button(
                'Submit',
                on_press=self.user_input,
                style=Pack(padding=5)
            )

            main_box.add(name_box)
            main_box.add(button)

            self.main_window = toga.MainWindow(title=self.formal_name)
            self.main_window.content = main_box
            self.main_window.show()

    def user_input(self, widget):
        print("Input:", self.name_input.value)


def main():
    return wearablecollection()
