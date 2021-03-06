############
# Part 1   #
############


class MelonType(object):
    """A species of melon at a melon farm."""

    def __init__(self, code, first_harvest, color, is_seedless, is_bestseller, 
                 name):
        """Initialize a melon."""

        self.pairings = []

        # Fill in the rest
        self.code = code
        self.first_harvest = first_harvest
        self.color = color
        self.is_seedless = is_seedless
        self.is_bestseller = is_bestseller
        self.name = name

    def add_pairing(self, pairing):
        """Add a food pairing to the instance's pairings list."""

        # Fill in the rest
        self.pairings.extend(pairing)

    def update_code(self, new_code):
        """Replace the reporting code with the new_code."""

        # Fill in the rest
        self.code = new_code

def make_melon_types():
    """Returns a list of current melon types."""

    all_melon_types = []

    # Fill in the rest
    musk = MelonType('musk', 1998, 'green', True, True, 'Muskmelon')
    casaba = MelonType('cas', 2003, 'orange', False, False, 'Casaba')
    crenshaw = MelonType('cren', 1996, 'green', False, False, 'Crenshaw')
    yellow_watermelon = MelonType('yw', 2013, 'yellow', False, True, 
                                  'Yellow Watermelon')
    
    musk.add_pairing(["mint"])
    casaba.add_pairing(["strawberries","mint"])
    crenshaw.add_pairing(["prosciutto"])
    yellow_watermelon.add_pairing(["ice cream"])

    all_melon_types.extend([musk, casaba, crenshaw, yellow_watermelon])

    return all_melon_types

def print_pairing_info(melon_types):
    """Prints information about each melon type's pairings."""
    for melon_type in melon_types:
        print("{} pairs well with {}.".format(melon_type.name,
              " ,".join(melon_type.pairings)))
    # Fill in the rest

def make_melon_type_lookup(melon_types):
    """Takes a list of MelonTypes and returns a dictionary of melon type by code."""

    # Fill in the rest
    melon_type_lookup = {}

    for melon_type in melon_types:
        melon_type_lookup[melon_type.code] = melon_type
    
    return melon_type_lookup

############
# Part 2   #
############

class Melon(object):
    """A melon in a melon harvest.""

    # Fill in the rest
    # Needs __init__ and is_sellable methods"""

    def __init__(type):
        pass


def make_melons(melon_types):
    """Returns a list of Melon objects."""
    # Fill in the rest


def get_sellability_report(melons):
    """Given a list of melon object, prints whether each one is sellable."""

    # Fill in the rest 


melons = make_melon_types()

print_pairing_info(melons)

melon_dict = make_melon_type_lookup(melons)

print(melon_dict)