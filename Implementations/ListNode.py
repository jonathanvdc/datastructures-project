from ListNode import *

class ListNode:
    """ Describes a node in a linked list. """

    def __init__(self, Value):
        """ Creates a new linked list node instance from the specified value. """
        self.successor_value = None
        self.value = Value

    def insert_after(self, Value):
        """ Inserts a node containing the provided value after this node. """
        nextVal = ListNode(Value)
        nextVal.successor = self.successor
        self.successor = nextVal

    @property
    def value(self):
        """ Gets the value contained in the list node. """
        return self.value_value

    @value.setter
    def value(self, value):
        """ Sets the value contained in the list node. """
        self.value_value = value

    @property
    def successor(self):
        """ Gets the list node's successor node. """
        return self.successor_value

    @successor.setter
    def successor(self, value):
        """ Sets the list node's successor node. """
        self.successor_value = value

    @property
    def tail(self):
        """ Gets the "tail" node of this linked chain. """
        if self.successor is None:
            return self
        else:
            return self.successor.tail