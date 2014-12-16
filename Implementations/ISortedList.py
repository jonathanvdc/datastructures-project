from ICollection import *

class ISortedList(ICollection):
    """ Describes a modified version of the Sorted List ADT. """

    def remove(self, Item):
        """ Removes an item from the list. """
        raise NotImplementedError("Method 'ISortedList.remove' was not implemented.")

    def contains(self, Item):
        """ Finds out if the sorted list contains the given item. """
        raise NotImplementedError("Method 'ISortedList.contains' was not implemented.")

    def to_list(self):
        """ Returns a read-only list that represents this list's contents, for easy enumeration. """
        raise NotImplementedError("Method 'ISortedList.to_list' was not implemented.")

    @property
    def is_empty(self):
        """ Gets a boolean value that indicates if the sorted list is empty. """
        raise NotImplementedError("Getter of property 'ISortedList.is_empty' was not implemented.")