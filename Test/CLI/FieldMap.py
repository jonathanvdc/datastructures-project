import Project

class FieldMap(Project.IMap):
    """ Maps an object to its named field. """
    # The technique this class uses exists only in dynamic languages, which is why it was added to the 'CLI' folder,
    # rather than the 'Implementations' folder.

    def __init__(self, Name):
        """ Creates a new field map. """
        self.name = Name

    def map(self, Item):
        """ Maps the object to its field. """
        return getattr(Item, self.name)