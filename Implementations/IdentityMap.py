from IMap import *

class IdentityMap(IMap):
    """ A mapping function that represents the identity function: its 'map' method simply returns the given argument. """

    def __init__(self):
        pass

    def map(self, Value):
        """ Maps the item to its target representation. """
        return Value