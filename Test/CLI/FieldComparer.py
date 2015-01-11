import Project

class FieldComparer(Project.IComparer):
    """ Compares the values in the named fields of two objects. """
    # The technique this class uses exists only in dynamic languages, which is why it was added to the 'CLI' folder,
    # rather than the 'Implementations' folder.

    def __init__(self, Name, Comparer):
        """ Creates a new field comparer. """
        self.name = Name
        self.comparer = Comparer

    def compare(self, Item, Other):
        """ Compares two items and returns an integer describing their relationship to each other. """

        val1 = getattr(Item, self.name)
        val2 = getattr(Other, self.name)

        return self.comparer.compare(val1, val2)