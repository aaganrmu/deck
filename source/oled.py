import threading
from datetime import datetime
import subprocess
import time

mac = True


def setup():
    watching_thread = threading.Thread(target=watcher, args=(), daemon=True)
    return watching_thread


def run_in_shell(cmd):
    result_bytes = subprocess.check_output(cmd, shell=True)
    result_string = result_bytes.decode('utf-8')
    return result_string


def draw_screen(items):
    for item in items:
        print(item)


def stat_cpu():
    if mac:
        raw_cpu = run_in_shell('top -l 2 | grep -E "^CPU"')
        return(raw_cpu)
    else:
        raw_cpu = run_in_shell("top -bn1 | grep load | awk '{printf \"CPU Load: %.2f\", $(NF-2)}'")
        return(raw_cpu)


def stat_time():
    timestring = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    return timestring


def stat_disk():
    if mac:
        raw_disk = "disk 10% full maybe"
    else:
        raw_disk = run_in_shell("df -h | awk '$NF==\"/\"{printf \"Disk: %d/%dGB %s\", $3,$2,$5}'")
    return raw_disk


def stat_ip():
    if mac:
        raw_ip = "1.1.1.1"
    else:
        raw_ip = run_in_shell("hostname -I | cut -d\' \' -f1")
    return raw_ip


def watcher():
    while True:
        items = [
                 stat_cpu(),
                 stat_disk(),
                 stat_ip(),
                 stat_time()
                 ]
        draw_screen(items)
        time.sleep(1)
