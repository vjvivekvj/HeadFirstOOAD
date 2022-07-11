import enum


class Type(enum.Enum):
    ACOUSTIC = "acoustic"
    ELECTRIC = "electric"
    BASS = "bass"

    def __str__(self):
        return self.value


class Builder(enum.Enum):
    FENDER = "fender"
    MARTIN = "martin"
    GIBSON = "gibson"
    COLLINGS = "collins"
    OLSON = "olson"
    RYAN = "ryan"
    PRS = "PRS"
    ANY = "any"

    def __str__(self):
        return self.value


class Wood(enum.Enum):
    INDIAN_ROSEWOOD = "indian rosewood"
    BRAZILIAN_ROSEWOOD = "brazilian rosewood"
    MAHOGANY = "mahogany"
    MAPLE = "maple"
    COCOBOLO = "cocobolo"
    CEDAR = "cedar"
    ADIRONDACK = "adirondack"
    ALDER = "alder"
    SITKA = "sitka"

    def __str__(self):
        return self.value
