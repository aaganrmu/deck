from display import display
import os
from collections import deque
import threading


PIPE_NAME = '/home/pi/git/deck/oled'

class display_pipe(display):
    def __init__(self):
        if not os.path.exists(PIPE_NAME):
            os.mkfifo(PIPE_NAME)
        self.pipewatcher = Pipewatcher()
        self.pipewatcher.daemon = True
        self.pipewatcher.start()

    def get_text(self):
        items = self.pipewatcher.text.copy()
        return(items)

    def stop(self):
        self.pipewatcher.stop()

class Pipewatcher(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.text = deque(maxlen=6)
        self._running = True

    def run(self):
        while self._running:
            pipe = open(PIPE_NAME, 'r')
            raw_text = pipe.read()
            text = raw_text.splitlines()
            for line in text:
                self.text.append(line)
            pipe.close()

    def stop(self):
        self._running = False
