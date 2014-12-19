from ITable import *

class TreeTable(ITable):
    """ A search tree implementation of a table. """

    def __init__(self, tree):
        """ Creates a new tree implementation of a table, using the provided tree as backing storage. """
        self.tree = tree

    def insert(self, Item):
        """ Inserts an item into the table. """
        if not self.contains_key(self.key_map.map(Item)):
            self.tree.insert(Item)
            return True
        else:
            return False

    def contains_key(self, Key):
        """ Finds out if the table contains the specified key. """
        return self[Key] is not None

    def remove(self, Key):
        """ Removes a key from the table. """
        return self.tree.remove(Key)

    def to_list(self):
        """ Gets the table's items as a read-only list. """
        return self.tree.traverse_inorder()

    def __iter__(self):
        """ Creates an iterator that iterates over every element in the collection. """
        return self.tree.__iter__()

    def __getitem__(self, Key):
        """ Retrieves the item in the table with the specified key. """
        return self.tree.retrieve(Key)

    @property
    def key_map(self):
        """ Gets the mapping function that maps list items to their search keys. """
        return self.tree.key_map

    @property
    def count(self):
        """ Gets the number of elements in the collection. """
        return self.tree.count

    @property
    def is_empty(self):
        """ Gets a boolean value that indicates whether the table is empty or not. """
        return self.tree.is_empty