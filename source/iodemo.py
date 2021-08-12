import threading
import ezgpio
import time


def thread(led_pin, button_pin):
    led = ezgpio.output(led_pin)
    button = ezgpio.input(button_pin)
    watching_thread = threading.Thread(target=watcher, args=(led, button,), daemon=True)
    return watching_thread


def watcher(led, button):

    while True:
        state = button.wait_for_state_change()
        led.state = state
        if state:
            print("now on")
        else:
            print("now off")