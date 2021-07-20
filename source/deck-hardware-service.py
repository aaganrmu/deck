import RPi.GPIO as GPIO
import ezgpio
import quitbutton

GPIO.setmode(GPIO.BOARD)

led_pin = 12
button_pin = 16
quit_button_pin = 18

quitbutton.start(quit_button_pin)


led = ezgpio.output(led_pin)
button = ezgpio.input(button_pin)
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


finally:
    GPIO.cleanup()
