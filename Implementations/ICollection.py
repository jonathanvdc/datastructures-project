from IReadOnlyCollection import *

class ICollection(IReadOnlyCollection):
    """ Describes a generic collection that allows items to be added. """

    def add(self, Item):
        """ Adds an item to the collection. """
        raise NotImplementedError("Method 'ICollection.add' was not implemented.")