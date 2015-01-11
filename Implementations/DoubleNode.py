from DoubleNode import *

class DoubleNode:
    """ A node that points to two other nodes. It is used as a node in a doubly linked list. """

    def __init__(self, Value):
        """ Creates a new doubly linked node containing the given value. """
        self.value_value = None
        self.successor_value = None
        self.predecessor_value = None
        self.value = Value

    def set_predecessor(self, Node):
        """ Sets this node's predecessor to the given node, and sets the given node's successor to this node, if 'Node' is not 'None'. """
        self.predecessor = Node
        Node.successor = self

    def set_successor(self, Node):
        """ Sets this node's successor to the given node, and sets the given node's predecessor to this node, if 'Node' is not 'None'. """
        self.successor = Node
        Node.predecessor = self

    def insert_after(self, Value):
        """ Inserts a node containing the provided value after this node. """
        nextVal = DoubleNode(Value)
        nextVal.set_successor(self.successor)
        nextVal.set_predecessor(self)

    def insert_before(self, Value):
        """ Inserts an item containing the provided node right before this node. """
        prevVal = DoubleNode(Value)
        prevVal.set_predecessor(self.predecessor)
        prevVal.set_successor(self)

    def remove(self):
        """ Removes this node from the linked chain. """
        if self.predecessor is not None:
            self.predecessor.set_successor(self.successor)
        elif self.successor is not None:
            self.successor.set_predecessor(None)

    @property
    def predecessor(self):
        """ Gets the node's predecessor, if any. """
        return self.predecessor_value

    @predecessor.setter
    def predecessor(self, value):
        """ Sets the node's predecessor, if any. """
        self.predecessor_value = value

    @property
    def successor(self):
        """ Gets the node's successor, if any. """
        return self.successor_value

    @successor.setter
    def successor(self, value):
        """ Sets the node's successor, if any. """
        self.successor_value = value

    @property
    def value(self):
        """ Gets the node's value. """
        return self.value_value

    @value.setter
    def value(self, value):
        """ Sets the node's value. """
        self.value_value = value

    @property
    def tail(self):
        """ Gets the "tail" node of this linked chain. """
        if self.successor is None:
            return self
        else:
            return self.successor.tail