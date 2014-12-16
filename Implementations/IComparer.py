class IComparer:
    """ Describes a generic comparer: a class containing pure function that compares two objects of the same types, and returns an integer value describing their relationship to each other. """

    def compare(self, Item, Other):
        """ Compares two items and returns an integer describing their relationship to each other. """
        raise NotImplementedError("Method 'IComparer.compare' was not implemented.")