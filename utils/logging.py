import time


class Logging:
    def __init__(self, filename):
        self.filename = filename

    def log(self, msg):
        with open(self.filename, "a") as f:
            f.write(f"{time.ctime()}: {msg}\n")
