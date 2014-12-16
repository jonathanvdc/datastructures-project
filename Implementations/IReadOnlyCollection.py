class IReadOnlyCollection:
    """ Describes a generic read-only collection of items. """

    def __iter__(self):
        """ Creates an iterator that iterates over every element in the collection. """
        raise NotImplementedError("Method 'IReadOnlyCollection.__iter__' was not implemented.")

    @property
    def count(self):
        """ Gets the number of elements in the collection. """
        raise NotImplementedError("Getter of property 'IReadOnlyCollection.count' was not implemented.")