from IMap import *

class PowerSequenceMap(IMap):
    """ Describes a mapping function that maps an integer to a probe sequence of the specified order. """

    def __init__(self, Power):
        """ Creates a new instance of a power sequence map based on the power to which the offsets will be exponentiated. """
        self.power_value = 0
        self.power = Power

    def map(self, Value):
        """ Maps the starting point of a sequence to a power sequence with offsets exponentiated to the value exposed by the 'Power' property. """
        index = 0
        while True:
            offset = index
            i = 1
            while i < self.power:
                offset *= index
                i += 1
            yield Value + offset
            index += 1

    @property
    def power(self):
        """ Gets the power to which the offsets will be exponentiated. """
        return self.power_value

    @power.setter
    def power(self, value):
        """ Sets the power to which the offsets will be exponentiated. """
        self.power_value = value