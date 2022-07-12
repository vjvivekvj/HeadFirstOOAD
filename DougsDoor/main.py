from bark import Bark
from remote import Remote
from constants import ALLOWED_BARKS
from bark_recognizer import BarkRecognizer
from door import Door
from time import sleep


def run_simulator():
    door = Door()
    for bark_string in ALLOWED_BARKS:
        bark = Bark(bark_string)
        door.add_allowed_bark(bark)
    recognizer = BarkRecognizer(door)
    remote = Remote(door)
    # Simulate the hardware hearing a bark
    print('Fido Barks')
    recognizer.recognize(Bark('rowlf'))
    print('Fido went outside')
    sleep(8)
    print('Fido\'s done')
    print('but he is stuck outside')
    # simulate some other dog barking
    other_dogs_bark = Bark('bhau')
    recognizer.recognize(other_dogs_bark)
    sleep(5)
    print('Fido barks again')
    recognizer.recognize(Bark('woof'))
    print('Fido is back again')


if __name__ == '__main__':
    run_simulator()
