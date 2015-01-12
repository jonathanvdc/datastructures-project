from ArrayList import *
from ISortableTable import *

class SortedTable(ISortableTable):
    """ A sortable table implementation that provides access to sorted objects which are sorted lazily. """

    def __init__(self, Table, Sorter):
        """ Creates a lazily sorted table with the specified table as backing storage, and the specified list sorter for sorting functionality. """
        self.table = None
        self.sorted_list = None
        self.sorter_value = None
        self.table = Table
        self.sorter = Sorter

    def sort_table(self):
        if self.sorted_list is None:
            targetList = ArrayList()
            for item in self.table:
                targetList.add(item)
            self.sorted_list = self.sorter.sort(targetList)

    def sort(self, Sorter):
        """ 'Sorts' the sorted table with the specified list sorter. The actual sorting process is deferred until __iter__ or ToList are called, however. """
        self.sorter = Sorter
        self.sorted_list = None

    def insert(self, Item):
        """ Inserts an item into the table. """
        self.sorted_list = None
        return self.table.insert(Item)

    def remove(self, Key):
        """ Removes a key from the table. """
        self.sorted_list = None
        return self.table.remove(Key)

    def contains_key(self, Key):
        """ Finds out if the table contains the specified key. """
        return self.table.contains_key(Key)

    def to_list(self):
        """ Gets the table's items as a read-only list. """
        self.sort_table()
        return self.sorted_list

    def __iter__(self):
        """ Creates an iterator that iterates over every element in the collection. """
        return self.to_list().__iter__()

    @property
    def sorter(self):
        """ Gets the sorted table's list sorter. """
        return self.sorter_value

    @sorter.setter
    def sorter(self, value):
        """ Sets the sorted table's list sorter. """
        self.sorter_value = value

    @property
    def key_map(self):
        """ Gets the table's record-to-key map. """
        return self.table.key_map

    @property
    def count(self):
        """ Gets the number of elements in the collection. """
        return self.table.count

    def __getitem__(self, Key):
        """ Retrieves the item in the table with the specified key. """
        return self.table[Key]