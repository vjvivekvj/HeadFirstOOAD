from choices import Builder, Wood, Type

INVENTORY_LIST = [
    ('A', 10, Builder.FENDER, 'STRAT', Type.ACOUSTIC, Wood.ALDER, Wood.SITKA, 6),
    ('B', 20, Builder.GIBSON, 'STRAT', Type.ELECTRIC, Wood.SITKA, Wood.CEDAR, 6),
    ('C', 13, Builder.MARTIN, 'STRAT', Type.ACOUSTIC, Wood.ALDER, Wood.CEDAR, 12),
    ('D', 15, Builder.RYAN, 'STRAT', Type.ELECTRIC, Wood.MAPLE, Wood.MAPLE, 12)
]

CUSTOMER_LIST = [
    (Builder.FENDER, 'STRAT', Type.ACOUSTIC, Wood.ALDER, Wood.SITKA, 6),
    (Builder.GIBSON, 'STRAT', Type.ELECTRIC, Wood.SITKA, Wood.CEDAR, 6),
    (Builder.MARTIN, 'STRAT', Type.ELECTRIC, Wood.CEDAR, Wood.MAPLE, 12),
    (Builder.RYAN, 'STRAT', Type.ELECTRIC, Wood.MAPLE, Wood.MAPLE, 12)
]
