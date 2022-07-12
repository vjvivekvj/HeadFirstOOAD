
class BarkRecognizer:
    def __init__(self, door):
        self.door = door

    def recognize(self, bark):
        print('Bark recognizer heard a', bark)
        for allowed_bark in self.door.get_allowed_barks():
            if allowed_bark.equals(bark):
                self.door.open()
                return
        print('Dog not allowed')
        return

