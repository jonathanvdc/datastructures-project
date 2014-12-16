from IReadOnlyCollection import *

class IReadOnlyList(IReadOnlyCollection):
    """ Describes a generic read-only, zero-based list. """

    def __getitem__(self, Index):
        """ Gets the item at the specified position in the list. """
        raise NotImplementedError("Method 'IReadOnlyList.__getitem__' was not implemented.")