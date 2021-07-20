import RPi.GPIO as GPIO


class input:
    def __init__(self, pin):
        self._pin = pin
        GPIO.setup(self._pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

    @property
    def state(self):
        return GPIO.input(self._pin) == 0


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
