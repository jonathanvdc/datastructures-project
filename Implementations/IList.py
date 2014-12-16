from IReadOnlyList import *
from ICollection import *

class IList(IReadOnlyList, ICollection):
    """ Describes a generic list. """

    def insert(self, Index, Item):
        """ Inserts an item in the list at the specified position. """
        raise NotImplementedError("Method 'IList.insert' was not implemented.")

    def remove_at(self, Index):
        """ Removes the element at the specified index from the list. """
        raise NotImplementedError("Method 'IList.remove_at' was not implemented.")

    def __getitem__(self, Index):
        """ Gets the item at the specified position in the list. """
        raise NotImplementedError("Method 'IList.__getitem__' was not implemented.")

    def __setitem__(self, Index, value):
        """ Sets the item at the specified position in the list. """
        raise NotImplementedError("Method 'IList.__setitem__' was not implemented.")