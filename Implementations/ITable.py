from IReadOnlyCollection import *

class ITable(IReadOnlyCollection):
    """ Describes a slightly modified version of the table ADT. """

    def insert(self, Item):
        """ Inserts an item into the table. """
        raise NotImplementedError("Method 'ITable.insert' was not implemented.")

    def remove(self, Key):
        """ Removes a key from the table. """
        raise NotImplementedError("Method 'ITable.remove' was not implemented.")

    def contains_key(self, Key):
        """ Finds out if the table contains the specified key. """
        raise NotImplementedError("Method 'ITable.contains_key' was not implemented.")

    def to_list(self):
        """ Gets the table's items as a read-only list. """
        raise NotImplementedError("Method 'ITable.to_list' was not implemented.")

    def __getitem__(self, Key):
        """ Retrieves the item in the table with the specified key. """
        raise NotImplementedError("Method 'ITable.__getitem__' was not implemented.")