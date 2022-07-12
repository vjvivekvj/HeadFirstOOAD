from door import Door


class Remote:
    def __init__(self, door):
        self.door = door

    def press_button(self):
        if self.door.is_open():
            self.door.close()
        else:
            self.door.open()

