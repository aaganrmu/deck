from datetime import datetime
import subprocess
import time
from lib.sh1106 import sh1106
from smbus import SMBus
from PIL import Image, ImageDraw, ImageFont

PADDING = 0
LINEHEIGHT = 9
BAR_STEPS = 10


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


def make_bar_nice (name, value, maximum = 1):
    ratio = value/maximum
    bar_full = int(ratio*BAR_STEPS)
    bar_empty = BAR_STEPS - bar_full
    bar_string = "[" + "="*bar_full + " "*bar_empty + "]"
    percentage_string = str(int(100 * ratio)) + "%"
    full_string = f'{name: <5}{bar_string} {percentage_string: >3}'
    return full_string


def stat_time():
    timestring = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    return timestring


def stat_cpu():
    raw_idle = run_in_shell("top -bn1 | grep Cpu | awk '{print $(NF-9)}'")
    idle_percent = float(raw_idle)
    usage = 1-idle_percent/100
    cpu_string = make_bar_nice("CPU", usage)
    return(cpu_string)


def stat_mem():
    raw_mem = run_in_shell("top -bn1 | grep 'MiB Mem' | awk '{print $(NF-3), $(NF-7)}'")
    values = raw_mem.split()
    mem_usage = float(values[0])
    mem_max = float(values[1])
    mem_string = make_bar_nice("MEM", mem_usage, mem_max)
    return(mem_string)


def stat_disk():
    raw_disk = run_in_shell("df -h | grep root | awk '{print $(NF-3), $(NF-2)}'")
    values = raw_disk.split()
    disk_usage = float(values[0][:-1])
    disk_max = float(values[1][:-1])
    disk_string = make_bar_nice("DISK", disk_usage, disk_max)
    return disk_string


def stat_ip():
    raw_ip = run_in_shell("hostname -I | cut -d\' \' -f1")
    ip_string = f'IP   {raw_ip}'
    return ip_string

def stat_temp():
    raw_temp = run_in_shell("vcgencmd measure_temp")
    temp = raw_temp[5:5+4]
    raw_throttled = run_in_shell("vcgencmd get_throttled")
    throttled = raw_throttled[12:12+1]
    if (throttled == '0'):
        throttled_description = 'ok'
    else:
        throttled_description = 'throttling'
    temp_string = f'Temp {temp}°C ({throttled_description})'
    return temp_string



i2cbus = SMBus(1)
oled = sh1106(i2cbus)
while True:
    items = [
             stat_time(),
             stat_cpu(),
             stat_mem(),
             stat_disk(),
             stat_ip(),
             stat_temp()
             ]
    draw_screen(oled, items)
