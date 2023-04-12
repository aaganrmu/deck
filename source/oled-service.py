import oled_manager
from display_stats import display_stats
from display_pipe import display_pipe

import lib.ezgpio as ezgpio

SWITCH_PIN = 13
MENU_PIN = 37


class UI:
    def __init__(self, modes):
        self.modes = modes
        self.mode_index = 0
        self.switch = ezgpio.input(SWITCH_PIN)
        self.menu_button = ezgpio.input(MENU_PIN, bounce_time=50)
        self.menu_button.add_callback(self.change_mode)

    def start(self):
        try:
            while True:
                self.update_screen()
        except KeyboardInterrupt:
            return

    def update_screen(self):
        oled = oled_manager.Oled()
        oled.start()
        try:
            while self.switch.state:
                oled.text = self.modes[self.mode_index].get_text()
        except KeyboardInterrupt:
            for mode in self.modes:
                mode.stop()
            oled.stop()
            raise KeyboardInterrupt
        oled.stop()
        self.switch.wait_for_state_change()

    def change_mode(self):
        self.mode_index += 1
        if self.mode_index >= len(self.modes):
            self.mode_index = 0


def main():
#    modes = [display_timers(), display_stats(), display_pipe()]
    modes = [display_stats(), display_pipe()]
    oled_ui = UI(modes)
    oled_ui.start()


if __name__ == "__main__":
    main()
