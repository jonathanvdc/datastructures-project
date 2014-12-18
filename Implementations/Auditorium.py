from IRecord import *

class Auditorium(IRecord):
    """ Describes an auditorium. """

    def __init__(self, Index, NumberOfSeats):
        """ Creates a new auditorium instance for the provided index and number of seats. """
        self.index_value = 0
        self.number_of_seats_value = 0
        self.index = Index
        self.number_of_seats = NumberOfSeats

    def __str__(self):
        """ Gets the auditorium's string representation. """
        return "Auditorium " + self.index + " (" + self.number_of_seats + " seats)"

    @property
    def index(self):
        """ Gets the auditorium's index, or room number. """
        return self.index_value

    @index.setter
    def index(self, value):
        """ Sets the auditorium's index, or room number. """
        self.index_value = value

    @property
    def number_of_seats(self):
        """ Gets the number of seats in the auditorium. """
        return self.number_of_seats_value

    @number_of_seats.setter
    def number_of_seats(self, value):
        """ Sets the number of seats in the auditorium. """
        self.number_of_seats_value = value

    @property
    def key(self):
        """ Gets the record's search key. """
        return self.index