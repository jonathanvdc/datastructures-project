from ListNode import *
from IList import *

class LinkedList(IList):
    """ Describes a linked list. """

    def __init__(self):
        """ Creates an empty linked list. """
        self.head_value = None

    def to_array(self):
        """ Gets an array representation of this linked list. """
        arr = [None] * self.count
        node = self.head
        i = 0
        while i < len(arr):
            arr[i] = node.value
            node = node.successor
            i += 1
        return arr

    def __iter__(self):
        """ Creates an iterator that iterates over every element in the collection. """
        node = self.head
        while node is not None:
            yield node.value
            node = node.successor

    def node_at(self, Index):
        """ Gets the list node at the specified index. """
        if Index < 0:
            return None
        node = self.head
        i = 0
        while node is not None and i < Index:
            node = node.successor
            i += 1
        return node

    def item_at(self, Index):
        """ Gets the item in the linked list at the given index. """
        return self.node_at(Index).value

    def add(self, Item):
        """ Adds an item to the end of the linked list. """
        if self.head is None:
            self.head = ListNode(Item)
        else:
            self.tail.insert_after(Item)

    def remove_at(self, Index):
        """ Removes the item in the linked list at the specified index. """
        if Index >= 0 and Index < self.count:
            if Index == 0:
                self.head = self.head.successor
            else:
                predecessor = self.node_at(Index - 1)
                predecessor.successor = predecessor.successor.successor
            return True
        else:
            return False

    def insert(self, Index, Item):
        """ Inserts an item in the list at the specified position. """
        if Index == 0:
            oldHead = self.head
            self.head = ListNode(Item)
            if oldHead is not None:
                self.head.successor = oldHead
            return True
        node = self.node_at(Index - 1)
        if node is None:
            return False
        else:
            node.insert_after(Item)
            return True

    @property
    def count(self):
        """ Gets the number of elements in the collection. """
        node = self.head
        i = 0
        while node is not None:
            node = node.successor
            i += 1
        return i

    @property
    def head(self):
        """ Gets the linked list's head node. """
        return self.head_value

    @head.setter
    def head(self, value):
        """ Sets the linked list's head node. """
        self.head_value = value

    @property
    def tail(self):
        """ Gets the linked list's tail node. """
        if self.head is None:
            return None
        else:
            return self.head.tail

    def __getitem__(self, Index):
        """ Gets the item in the linked list at the given index. """
        return self.item_at(Index)

    def __setitem__(self, Index, value):
        """ Sets the item in the linked list at the given index. """
        self.node_at(Index).value = value