from abc import ABC
from abc import abstractmethod

from os import makedirs
from os.path import dirname

class Logger(ABC):
    def __init__(self, filename: str) -> None:
        self.filename = filename

        makedirs(dirname(self.filename), exist_ok = True)

    @abstractmethod
    def listen(self) -> None:
        raise NotImplementedError()