
import RPi.GPIO as GPIO
import lib.ezgpio as ezgpio
import time

LED_PIN = 12
BUTTON_PIN = 16

GPIO.setmode(GPIO.BOARD)

led = ezgpio.output(LED_PIN)
button = ezgpio.input(BUTTON_PIN)

while True:
    state = button.wait_for_state_change()
    led.state = state
    if state:
        print("now on")
    else:
        print("now off")