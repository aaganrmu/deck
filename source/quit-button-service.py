import lib.ezgpio as ezgpio
import subprocess
import time

QUIT_PIN=31

button = ezgpio.input(QUIT_PIN)
shutting_down = False
while True:
    if button.wait_for_state_change() and not shutting_down:
        shutting_down = True
        subprocess.check_output("sudo shutdown +0", shell=True)
