class IListSorter:
    """ Describes a sorting algorithm that is to be applied on lists. The way and order in which the items are sorted is left to individual implementations. """

    def sort(self, Items):
        """ Sorts the items in the given list.  Whether the results are stored in-place or a new list is created is an implementation detail. """
        raise NotImplementedError("Method 'IListSorter.sort' was not implemented.")