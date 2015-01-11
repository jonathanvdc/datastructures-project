from ISortableTable import *

class ListTable(ISortableTable):
    """ An implementation of a table that uses a list as backing storage. """

    def __init__(self, KeyMap, List):
        """ Creates a new list table instance. """
        self.list = None
        self.key_map_value = None
        self.key_map = KeyMap
        self.list = List

    def contains_key(self, Key):
        """ Finds out if the table contains the specified key. """
        for item in self.list:
            if self.key_map.map(item) == Key:
                return True
        return False

    def remove(self, Key):
        """ Removes a key from the table. """
        i = 0
        while i < self.list.count:
            if self.key_map.map(self.list[i]) == Key:
                self.list.remove_at(i)
                return True
            i += 1
        return False

    def insert(self, Item):
        """ Inserts an item into the table. """
        if self.contains_key(self.key_map.map(Item)):
            return False
        else:
            self.list.add(Item)
            return True

    def __iter__(self):
        """ Creates an iterator that iterates over every element in the collection. """
        return self.list.__iter__()

    def to_list(self):
        """ Gets the table's items as a read-only list. """
        return self.list

    def sort(self, Sorter):
        """ Sorts the list based on the given item comparer. """
        self.list = Sorter.sort(self.list)

    @property
    def key_map(self):
        """ Gets the value-to-key mapping function of this list table. """
        return self.key_map_value

    @key_map.setter
    def key_map(self, value):
        """ Sets the value-to-key mapping function of this list table. """
        self.key_map_value = value

    def __getitem__(self, Key):
        """ Retrieves the item in the table with the specified key. """
        for item in self.list:
            if self.key_map.map(item) == Key:
                return item
        return None

    @property
    def count(self):
        """ Gets the number of elements in the collection. """
        return self.list.count