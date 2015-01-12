from IndirectTable import *

class SwapTable(IndirectTable):
    """ A wrapper table that allows for the underlying table to be 'swapped'. """

    def __init__(self, table):
        """ Creates a new instance of a swap table. """
        self.table = None
        IndirectTable.__init__(self)
        self.table = table

    def get_table(self):
        """ Gets the indirect table's underlying table. """
        return self.table

    def swap(self, Table):
        """ Changes the underlying table implementation to the provided table. """
        for item in self:
            Table.insert(item)
        self.table = Table