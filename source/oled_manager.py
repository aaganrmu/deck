import threading
from lib.sh1106 import sh1106
from smbus import SMBus
from PIL import ImageFont
from signal import signal, SIGTERM
import time

PADDING = 0
LINEHEIGHT = 9


class Oled(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        i2cbus = SMBus(1)
        self._display = sh1106(i2cbus)
        self.items = []
        self._running = True
        self._shutting_down = False
        signal(SIGTERM, self._shutdown)

    def run(self):
        while self._running:
            self.draw_text(self.items)
        if self._shutting_down:
            self.draw_text([' ', ' ', '    Shutting down'])
            time.sleep(1.5)
        self.draw_text([])

    def stop(self):
        self._running = False

    def _shutdown(self, signal, frame):
        self._shutting_down = True
        self.stop()

    def draw_text(self, items):
        canvas = self._display.canvas

        # clear screen
        width = self._display.width
        height = self._display.height
        rectangle = (0, 0, width, height)
        canvas.rectangle(rectangle, outline=0, fill=0)

        # draw text
        font = ImageFont.load_default()
        x = PADDING
        y = PADDING
        for item in items:
            canvas.text((x, y), item, font=font, fill=255)
            y += LINEHEIGHT

        # display result

        self._display.display()
