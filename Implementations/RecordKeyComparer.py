from IComparer import *

class RecordKeyComparer(IComparer):
    """ A comparer that compares records based on their keys. """

    def __init__(self):
        """ Creates a new record key comparer. """
        pass

    def compare(self, Item, Other):
        """ Compares two items and returns an integer describing their relationship to each other. """
        if Item.key < Other.key:
            return -1
        elif Item.key > Other.key:
            return 1
        else:
            return 0