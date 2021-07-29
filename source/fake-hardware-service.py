# import RPi.GPIO as GPIO
# import iodemo
# import quitbutton
import oled

# GPIO.setmode(GPIO.BOARD)
threads = []

# quit_button_pin = 18
# threads += quitbutton.setup(quit_button_pin)

# led_pin = 12
# button_pin = 16
# threads += iodemo.setup(led_pin, button_pin)

threads += oled.setup()

for thread in threads:
    thread.start()

for thread in threads:
    thread.join()
