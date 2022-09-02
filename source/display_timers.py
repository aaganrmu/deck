from display import display
from datetime import datetime
import subprocess
import time

BAR_STEPS = 10


class display_stats(display):

    class timer():
        def text()
            return("test")

    def make_bar_nice (self, name, value, maximum = 1):
        ratio = value/maximum
        bar_full = int(ratio*BAR_STEPS)
        bar_empty = BAR_STEPS - bar_full
        bar_string = "[" + "="*bar_full + " "*bar_empty + "]"
        percentage_string = str(int(100 * ratio)) + "%"
        full_string = f'{name: <5}{bar_string} {percentage_string: >3}'
        return full_string


    def stat_time(self):
        timestring = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
        return timestring




    def get_text(self):
        items = ["timers:"]
        for timer in self.timers:
            items.append(timer.text())
        return(items)
