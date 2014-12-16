class ITree:
    """ Describes a generic search tree. This is a generalization of a binary search tree that is also applicable to 2-3 trees, 2-3-4 trees, black-red trees and AVL trees. """

    def insert(self, Item):
        """ Inserts an item in the search tree. """
        raise NotImplementedError("Method 'ITree.insert' was not implemented.")

    def retrieve(self, Key):
        """ Retrieves the item with the specified key. """
        raise NotImplementedError("Method 'ITree.retrieve' was not implemented.")

    def remove(self, Key):
        """ Removes the item with the specified key from the search tree. """
        raise NotImplementedError("Method 'ITree.remove' was not implemented.")

    def traverse_inorder(self):
        """ Performs inorder traversal on the binary search tree and writes its items to a new list. """
        raise NotImplementedError("Method 'ITree.traverse_inorder' was not implemented.")

    def __iter__(self):
        """ Creates an iterator that iterates over every element in the tree. """
        raise NotImplementedError("Method 'ITree.__iter__' was not implemented.")

    @property
    def key_map(self):
        """ Gets the function that maps the search tree's records to their search keys. """
        raise NotImplementedError("Getter of property 'ITree.key_map' was not implemented.")

    @property
    def count(self):
        """ Counts the number of items in the search tree. """
        raise NotImplementedError("Getter of property 'ITree.count' was not implemented.")

    @property
    def is_empty(self):
        """ Gets a boolean value that indicates if the tree is empty. """
        raise NotImplementedError("Getter of property 'ITree.is_empty' was not implemented.")