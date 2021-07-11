import RPi.GPIO as GPIO
from time import sleep
import ezgpio

import subprocess

GPIO.setmode(GPIO.BOARD)

led_pin = 12
button_pin = 16
quit_button_pin = 18




led = ezgpio.output(led_pin)
button = ezgpio.input(button_pin)
quit_button = ezgpio.input(quit_button_pin)
shutting_down = False
timer = 0.003
previous_state = False
try:
    while True:
        current_state = button.state
        if current_state != previous_state:
            led.state = current_state
            previous_state = current_state
            if current_state:
                print("now on")
            else:
                print("now off")
        if quit_button.state and not shutting_down:
            shutting_down = True
            subprocess.check_output("sudo shutdown +0", shell=True)

finally:
    GPIO.cleanup()



