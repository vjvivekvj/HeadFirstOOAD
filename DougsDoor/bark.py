
class Bark:
    def __init__(self, sound):
        self.sound = sound

    def equals(self, bark):
        if self.sound == bark.sound:
            return True
        else:
            return False

    def __str__(self):
        return self.sound
