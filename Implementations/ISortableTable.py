from ITable import *

class ISortableTable(ITable):
    """ Describes a sortable table. """

    def sort(self, Sorter):
        """ Sorts the table's contents in ascending order based on the the provided comparer. """
        raise NotImplementedError("Method 'ISortableTable.sort' was not implemented.")