from ITable import *

class SwapTable(ITable):
    """ A wrapper table that allows for the underlying table to be 'swapped'. """

    def __init__(self, table):
        """ Creates a new instance of a swap table. """
        self.table = None
        self.table = table

    def swap(self, Table):
        """ Changes the underlying table implementation to the provided table. """
        for item in self:
            Table.insert(item)
        self.table = Table

    def insert(self, Value):
        """ Inserts an item into the table. """
        return self.table.insert(Value)

    def contains_key(self, Key):
        """ Finds out if the table contains the specified key. """
        return self.table.contains_key(Key)

    def remove(self, Key):
        """ Removes a key from the table. """
        return self.table.remove(Key)

    def __iter__(self):
        """ Creates an iterator that iterates over every element in the collection. """
        return self.table.__iter__()

    def to_list(self):
        """ Gets the table's items as a read-only list. """
        return self.table.to_list()

    @property
    def key_map(self):
        """ Gets the table's record-to-key map. """
        return self.table.key_map

    def __getitem__(self, Key):
        """ Retrieves the item in the table with the specified key. """
        return self.table[Key]

    @property
    def count(self):
        """ Gets the number of elements in the collection. """
        return self.table.count