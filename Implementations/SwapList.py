from IReadOnlySwapList import *
from IList import *

class SwapList(IReadOnlySwapList, IList):
    """ A basic implementation of a swap list. """

    def __init__(self, backingList):
        """ Creates a new swap list. """
        self.backing_list = None
        self.backing_list = backingList

    def swap(self, Container):
        """ Swaps the swap list's backing storage with the provided list. """
        while Container.count > 0:
            Container.remove_at(0)
        count = self.backing_list.count
        i = 0
        while i < count:
            Container.add(self.backing_list[i])
            i += 1
        self.backing_list = Container

    def add(self, Item):
        """ Adds an item to the collection. """
        self.backing_list.add(Item)

    def insert(self, Index, Item):
        """ Inserts an item in the list at the specified position. """
        return self.backing_list.insert(Index, Item)

    def remove_at(self, Index):
        """ Removes the element at the specified index from the list. """
        return self.backing_list.remove_at(Index)

    def __iter__(self):
        """ Creates an iterator that iterates over every element in the collection. """
        return self.backing_list.__iter__()

    @property
    def count(self):
        """ Gets the number of elements in the collection. """
        return self.backing_list.count

    def __getitem__(self, Index):
        """ Gets the item at the specified position in the list. """
        return self.backing_list[Index]

    def __setitem__(self, Index, value):
        """ Sets the item at the specified position in the list. """
        self.backing_list[Index] = value