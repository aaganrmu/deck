import threading
import ezgpio
import subprocess
import time


def thread(pin):
    button = ezgpio.input(pin)
    watching_thread = threading.Thread(target=watcher, args=(button,), daemon=True)
    return watching_thread


def watcher(button):
    shutting_down = False
    while True:
        time.sleep(0.2)
        if button.state and not shutting_down:
            shutting_down = True
            subprocess.check_output("sudo shutdown +0", shell=True)
