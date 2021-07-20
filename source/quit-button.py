import threading
import ezgpio
import subprocess


def start(pin):
    button = ezgpio.input(pin)
    watching_thread = threading.Thread(target=watcher, args=(button,), daemon=True)
    watching_thread.start()


def watcher(button):
    shutting_down = False
    while True:
        if button.state and not shutting_down:
            shutting_down = True
            subprocess.check_output("sudo shutdown +0", shell=True)
