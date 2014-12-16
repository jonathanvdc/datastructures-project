from IMap import *

class DefaultRecordMap(IMap):
    """ A mapping function that simply passes along the search key provided by the record. """

    def __init__(self):
        pass

    def map(self, Record):
        """ Maps the item to its target representation. """
        return Record.key