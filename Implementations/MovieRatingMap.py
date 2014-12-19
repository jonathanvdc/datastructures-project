from IMap import *

class MovieRatingMap(IMap):
    """ A mapping function that maps a movie to its rating. """

    def __init__(self):
        """ Creates a new movie-rating map. """
        pass

    def map(self, Item):
        """ Maps the item to its target representation. """
        return Item.rating