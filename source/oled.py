import threading
from datetime import datetime
import subprocess
import time
from lib_sh1106 import sh1106
from smbus import SMBus
from PIL import Image, ImageDraw, ImageFont

PADDING = 2
LINEHEIGHT = 8

def thread():
    watching_thread = threading.Thread(target=watcher, args=(), daemon=True)
    return watching_thread


def run_in_shell(cmd):
    result_bytes = subprocess.check_output(cmd, shell=True)
    result_string = result_bytes.decode('utf-8')
    return result_string


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

def stat_cpu():
    raw_cpu = run_in_shell("top -bn1 | grep load | awk '{printf \"CPU Load: %.2f\", $(NF-2)}'")
    return(raw_cpu)


def stat_time():
    timestring = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    return timestring


def stat_disk():
    raw_disk = run_in_shell("df -h | awk '$NF==\"/\"{printf \"Disk: %d/%dGB %s\", $3,$2,$5}'")
    return raw_disk


def stat_ip():
    raw_ip = run_in_shell("hostname -I | cut -d\' \' -f1")
    return raw_ip





def watcher():
    i2cbus = SMBus(1)
    oled = sh1106(i2cbus)
    while True:
        items = [
                 stat_cpu(),
                 stat_disk(),
                 stat_ip(),
                 stat_time()
                 ]
        draw_screen(oled, items)

        time.sleep(1)
