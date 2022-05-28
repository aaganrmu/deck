from display import display
import os
from collections import deque

PIPE_NAME = 'oled'

class display_pipe(display):
    def __init__(self):
        if not os.path.exists(PIPE_NAME):
            os.mkfifo(PIPE_NAME)
        self._text = deque(maxlen=6)
        self.i = 0


    
        pipe = open(PIPE_NAME, 'r')
        self._text.append(pipe.read())


    def get_text(self):
        items = self._text.copy()
        return(items)
