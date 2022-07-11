

class GuitarSpec:
    def __init__(self, builder, model, type, back_wood, top_wood, num_strings):
        self.builder = builder
        self.model = model
        self.type = type
        self.back_wood = back_wood
        self.top_wood = top_wood
        self.num_strings = num_strings

    def matches(self, customer_spec):
        if customer_spec.builder != self.builder:
            return False
        model = customer_spec.model
        if model and model != '' and model != self.model:
            return False
        if customer_spec.type != self.type:
            return False
        if customer_spec.back_wood != self.back_wood:
            return False
        if customer_spec.top_wood != self.top_wood:
            return False
        if customer_spec.num_strings != self.num_strings:
            return False
        return True


class Guitar:
    def __init__(self, serial_number, price, guitar_spec):
        self.serial_number = serial_number
        self.price = price
        self.spec = guitar_spec



