from time import sleep


class Door:
    def __init__(self):
        self.door_open = False
        self.allowed_barks = []

    def open(self, auto_close=True):
        self.door_open = True
        if auto_close:
            sleep(5)
            self.close()

    def close(self):
        self.door_open = False

    def is_open(self):
        return self.door_open

    def add_allowed_bark(self, bark):
        self.allowed_barks.append(bark)

    def get_allowed_barks(self):
        return self.allowed_barks
