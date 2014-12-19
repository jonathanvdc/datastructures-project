from IRecord import *

class KeyValuePair(IRecord):
    """ A pair record that contains a key and a value. """

    def __init__(self, Key, Value):
        """ Creates a new instance of a key-value pair based on the given key and value. """
        self.key = Key
        self.value = Value

    @property
    def key(self):
        """ Gets the key-value pair's key. """
        return self.key_value

    @key.setter
    def key(self, value):
        """ Sets the key-value pair's key. """
        self.key_value = value

    @property
    def value(self):
        """ Gets the key-value pair's value. """
        return self.value_value

    @value.setter
    def value(self, value):
        """ Sets the key-value pair's value. """
        self.value_value = value