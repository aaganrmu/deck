#used for easy buttons.
#assumes buttons connects to ground

import RPi.GPIO as GPIO
import time

BOUNCE_TIME = 50
WAIT_FOR_STATE_CHANGE_DELAY = 50

class input:
    def __init__(self, 
                 pin, 
                 bounce_time = BOUNCE_TIME,
                 wait_for_state_change_delay = WAIT_FOR_STATE_CHANGE_DELAY
                 ):
        self._pin = pin
        GPIO.setup(self._pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        self.bounce_time = bounce_time
        self.wait_for_state_change_delay = wait_for_state_change_delay
    @property
    def state(self):
        return GPIO.input(self._pin) == 0

    def wait_for_state_change(self):
        GPIO.wait_for_edge(self._pin, 
            GPIO.BOTH, 
            bouncetime=self.bounce_time)
        time.sleep(self.wait_for_state_change_delay/1000)
        return self.state


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

