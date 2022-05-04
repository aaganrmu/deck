import subprocess
import threading
from lib.sh1106 import sh1106
from smbus import SMBus
from PIL import Image, ImageDraw, ImageFont
import time

PADDING = 0
LINEHEIGHT = 9

def draw_screen(oled, items):
    canvas = oled.canvas

    #clear screen
    width = oled.width
    height = oled.height
    rectangle = (0, 0, width, height)
    canvas.rectangle(rectangle, outline=0, fill=0)

    #draw text
    font = ImageFont.load_default()
    x = PADDING
    y = PADDING
    for item in items:
        canvas.text((x, y), item, font=font, fill=255)
        y += LINEHEIGHT

    #display result

    oled.display()


class oled_manager(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        i2cbus = SMBus(1)
        self.display = sh1106(i2cbus)
        self.items = []
        self.running = True
    def run(self):
        print('starting oled thread')
        while self.running:
            draw_screen(self.display, self.items)
