from constants import CUSTOMER_LIST
from inventory import Inventory
from guitar import Guitar, GuitarSpec


def find_guitar(search_spec):
    inventory = Inventory()
    inventory_guitars = inventory.search_guitar(search_spec)
    if inventory_guitars:
        print('Found matching guitars')
        for guitar in inventory_guitars:
            guitar_spec = guitar.spec
            print('Guitar: ', guitar_spec.builder, guitar_spec.model,
                  guitar_spec.type, guitar_spec.back_wood,
                  guitar_spec.top_wood, guitar_spec.num_strings,
                  'string for price', guitar.price)
    else:
        print('No guitar found')


if __name__ == '__main__':
    for spec in CUSTOMER_LIST:
        builder, model, type, back_wood, top_wood, num_strings = spec
        search_spec = GuitarSpec(builder, model, type, back_wood, top_wood, num_strings)
        find_guitar(search_spec)
