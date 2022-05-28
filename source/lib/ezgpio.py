#used for easy buttons.
#assumes buttons connects to ground

import RPi.GPIO as GPIO
import time

BOUNCE_TIME = 50
DELAY = 50

class input:
    def __init__(self,
                 pin,
                 bounce_time = BOUNCE_TIME,
                 delay = DELAY
                 ):
        self._pin = pin
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(self._pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        self.bounce_time = bounce_time
        self.delay = delay/1000
        self._callback_enabled = False
        self.callbacks = []
    @property
    def state(self):
        return GPIO.input(self._pin) == 0

    @property
    def pin(self):
        return self._pin

    def wait_for_state_change(self):
        start_state = self.state
        while self.state == start_state:
            GPIO.wait_for_edge(self._pin,
                               GPIO.BOTH,
                               bouncetime=self.bounce_time
                               )
            time.sleep(self.delay)
        return self.state

    def add_callback(self, function):
        if not self._callback_enabled:
            self._callback_enabled = True
            GPIO.add_event_detect(self._pin,
                                  GPIO.FALLING,
                                  callback=self._callback,
                                  bouncetime=self.bounce_time
                                  )
        self.callbacks.append(function)

    def _callback(self, channel):
        if self.state:
            for callback in self.callbacks:
                callback()


class output:
    def __init__(self, pin):
        self._pin = pin
        self._state = False
        GPIO.setup(self._pin, GPIO.OUT)
        GPIO.output(self._pin, GPIO.LOW)

    @property
    def state(self):
        return self._state

    @state.setter
    def state(self, state):
        self._state = state
        if self._state:
            GPIO.output(self._pin, GPIO.HIGH)
        else:
            GPIO.output(self._pin, GPIO.LOW)

