from datetime import datetime

class Log:
    def __init__(self) -> None:
        dt = datetime.now()

        self.day = dt.day
        self.month = dt.month
        self.year = dt.year
        self.hour = dt.hour
        self.minute = dt.minute
        self.second = dt.second

    def __repr__(self) -> str:
        return f"'{ self.day }'," + \
            f"'{ self.month }'," + \
            f"'{ self.year }'," + \
            f"'{ self.hour }'," + \
            f"'{ self.minute }'," + \
            f"'{ self.second }'"

    def store(self, filename: str) -> None:
        with open(filename, "a") as file:
            file.write(f"{ self }\n")