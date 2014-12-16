from TwoThreeFourTree import *
from ITree import *
from ArrayList import *

class TwoThreeFourSearchTree(ITree):
    """ A wrapper class that exposes 'TwoThreeFourTree' functionality through an ITree interface. """

    def __init__(self, KeyMap):
        """ Creates a new 'TwoThreeFourSearchTree' instance based on an empty 'TwoThreeFourTree' """
        self.tree = TwoThreeFourTree()
        self.key_map_value = KeyMap

    @property
    def key_map(self):
        """ Gets the function that maps the search tree's records to their search keys. """
        return self.key_map_value

    @property
    def count(self):
        """ Counts the number of elements in the search tree. """
        if self.tree.root == None:
            return 0
        else:
            return self.tree.root.count()

    def is_empty(self):
        """ Gets a boolean value that indicates if the tree is empty. """
        return self.tree.root == None

    def insert(self, Item):
        """ Inserts an item into the search tree. """
        return self.tree.InsertItem(self.key_map.map(Item), Item)

    def remove(self, Key):
        """ Removes the item with the specified key from the search tree. """
        return self.tree.RemoveItem(Key)

    def retrieve(self, Key):
        """ Retrieves the item with the specified key. """
        return self.tree.RetrieveItem(Key)

    def __iter__(self):
        """ Creates an iterator that iterates over every element in the tree. """
        if self.tree.root == None:
            return iter([])
        else:
            return self.tree.root.IterateInorder()

    def traverse_inorder(self):
        """ Performs inorder traversal on the binary search tree and writes its items to a new list. """
        result = ArrayList()
        for item in self:
            result.add(item)
        return result