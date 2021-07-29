import threading
import ezgpio


def setup(led_pin, button_pin):
    led = ezgpio.output(led_pin)
    button = ezgpio.input(button_pin)
    watching_thread = threading.Thread(target=watcher, args=(led, button,), daemon=True)
    return watching_thread


def watcher(led, button):
    previous_state = False
    while True:
        current_state = button.state
        if current_state != previous_state:
            led.state = current_state
            previous_state = current_state
            if current_state:
                print("now on")
            else:
                print("now off")
