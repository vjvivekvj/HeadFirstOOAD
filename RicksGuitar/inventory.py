from guitar import Guitar, GuitarSpec
from constants import INVENTORY_LIST


class Inventory:
    def __init__(self):
        self.guitars = []
        for guitar_property in INVENTORY_LIST:
            serial_number, price, builder, model, type, back_wood, top_wood, num_strings = guitar_property
            self.add_guitar(serial_number, price, builder, model, type, back_wood, top_wood, num_strings)

    def add_guitar(self, serial_number, price, builder, model, type, back_wood, top_wood, num_strings):
        guitar_spec = GuitarSpec(builder, model, type, back_wood, top_wood, num_strings)
        guitar = Guitar(serial_number, price, guitar_spec)
        self.guitars.append(guitar)

    def get_guitar(self, serial_number):
        for guitar in self.guitars:
            if guitar.serial_number == serial_number:
                return guitar
        return None

    def search_guitar(self, search_spec):
        matching_guitars = []
        # delegate this job to Guitar spec, match function
        for guitar in self.guitars:
            guitar_spec = guitar.spec
            if guitar_spec.matches(search_spec):
                matching_guitars.append(guitar)
        return matching_guitars

