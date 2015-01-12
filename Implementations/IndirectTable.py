from ITable import *

class IndirectTable(ITable):
    """ A wrapper class for tables that forwards function calls to another table. """

    def __init__(self):
        pass

    def get_table(self):
        """ Gets the indirect table's underlying table. """
        raise NotImplementedError("Method 'IndirectTable.get_table' was not implemented.")

    def insert(self, Value):
        """ Inserts an item into the table. """
        return self.get_table().insert(Value)

    def contains_key(self, Key):
        """ Finds out if the table contains the specified key. """
        return self.get_table().contains_key(Key)

    def remove(self, Key):
        """ Removes a key from the table. """
        return self.get_table().remove(Key)

    def __iter__(self):
        """ Creates an iterator that iterates over every element in the collection. """
        return self.get_table().__iter__()

    def to_list(self):
        """ Gets the table's items as a read-only list. """
        return self.get_table().to_list()

    @property
    def key_map(self):
        """ Gets the table's record-to-key map. """
        return self.get_table().key_map

    def __getitem__(self, Key):
        """ Retrieves the item in the table with the specified key. """
        return self.get_table()[Key]

    @property
    def count(self):
        """ Gets the number of elements in the collection. """
        return self.get_table().count