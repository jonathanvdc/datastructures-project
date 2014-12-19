from IMap import *

class MovieTitleMap(IMap):
    """ A mapping function that maps a movie to its title. """

    def __init__(self):
        """ Creates a new movie-title map. """
        pass

    def map(self, Item):
        """ Maps the item to its target representation. """
        return Item.title