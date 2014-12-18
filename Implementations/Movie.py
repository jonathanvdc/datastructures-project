from IRecord import *

class Movie(IRecord):
    """ Describes a movie. """

    def __init__(self, Id, Title, Rating):
        """ Creates a new movie instance for the given parameters. """
        self.title_value = None
        self.id_value = 0
        self.rating_value = 0.0
        self.id = Id
        self.title = Title
        self.rating = Rating

    def __str__(self):
        return self.id + ": " + self.title + " (Rated " + self.rating + ")"

    def __repr__(self):
        return self.id + ": " + self

    @property
    def title(self):
        """ Gets the movie's title. """
        return self.title_value

    @title.setter
    def title(self, value):
        """ Sets the movie's title. """
        self.title_value = value

    @property
    def id(self):
        """ Gets the movie's identifier. """
        return self.id_value

    @id.setter
    def id(self, value):
        """ Sets the movie's identifier. """
        self.id_value = value

    @property
    def rating(self):
        """ Gets the movie's rating. """
        return self.rating_value

    @rating.setter
    def rating(self, value):
        """ Sets the movie's rating. """
        self.rating_value = value

    @property
    def key(self):
        """ Gets the record's search key. """
        return self.id