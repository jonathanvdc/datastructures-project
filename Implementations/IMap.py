class IMap:
    """ Describes a map, an object that maps source values to their target representation. It is essentially a pure mathematical function. """

    def map(self, Item):
        """ Maps the item to its target representation. """
        raise NotImplementedError("Method 'IMap.map' was not implemented.")