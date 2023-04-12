import threading
from lib.sh1106 import sh1106
from smbus import SMBus
from PIL import ImageFont
from signal import signal, SIGTERM
import time
from enum import Enum

PADDING = 0
LINEHEIGHT = 9


class Mode(Enum):
    TEXT = 1
    IMAGE = 2


class Oled(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        i2cbus = SMBus(1)
        self._display = sh1106(i2cbus)
        self._mode = Mode.TEXT
        self._text = []
        self_image = None
        self._running = True
        self._shutting_down = False
        signal(SIGTERM, self._shutdown)

    def run(self):
        self._display.onoff(1)
        while self._running:
            self.update_screen()
        if self._shutting_down:
            self._text = [' ', ' ', '    shutting down']
            self._mode = Mode.TEXT
            self.update_screen()
            time.sleep(1.5)
        self._display.onoff(0)

    def stop(self):
        self._running = False

    def _shutdown(self, signal, frame):
        self._shutting_down = True
        self.stop()

    def update_screen(self):
        if self._mode == Mode.TEXT:
            self.draw_text()
        elif self._mode == Mode.CANVAS:
            self.draw_image()

    @property
    def text(self):
        return self._text

    @text.setter
    def text(self, text):
        if not self._shutting_down:
            self._text = text
            self._mode = Mode.TEXT

    @property
    def canvas(self):
        return self._display.canvas

    @canvas.setter
    def canvas(self, canvas):
        if not self._shutting_down:
            self._display.canvas = canvas
            self._mode = Mode.CANVAS

    def draw_text(self):
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
        for line in self._text:
            canvas.text((x, y), line, font=font, fill=255)
            y += LINEHEIGHT

        # display result
        self._display.display()
