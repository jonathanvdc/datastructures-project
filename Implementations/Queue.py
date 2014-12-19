from ArrayList import *
from IReadOnlyCollection import *

class Queue(IReadOnlyCollection):
    """ Represents a generic queue. """

    def __init__(self, dataContainer = None):
        """ Creates a new queue instance that uses the specified list to store its data. """
        if dataContainer is None:
            self.data_container = ArrayList()
            return
        self.data_container = dataContainer

    def enqueue(self, Item):
        """ Adds an item to the queue. """
        self.data_container.add(Item)

    def dequeue(self):
        """ Dequeues an item and returns it. """
        if self.is_empty:
            return None
        value = self.data_container[0]
        self.data_container.remove_at(0)
        return value

    def __iter__(self):
        """ Creates an iterator that iterates over every element in the collection. """
        return self.data_container.__iter__()

    @property
    def is_empty(self):
        """ Gets a boolean value that indicates whether the queue is empty or not. """
        return self.count == 0

    @property
    def count(self):
        """ Gets the number of items on the queue. """
        return self.data_container.count

    @property
    def front(self):
        """ Peeks at the item at the top of the queue, without removing it. """
        if self.is_empty:
            return None
        else:
            return self.data_container[0]