from Auditorium import *
from Showtime import *
from User import *
from SwapList import *
from ArrayList import *
from SortedSwapList import *
from TreeSortedList import *
from BinarySearchTree import *
from MovieRatingMap import *
from ReservationManager import *
from Time import *

class Theater:
    """ Represents a movie theater. """

    def __init__(self, Name):
        """ Creates a new movie theater instance. """
        self.auditors = SwapList(ArrayList())
        self.slots = SwapList(ArrayList())
        self.allmovies = SortedSwapList(TreeSortedList(BinarySearchTree(MovieRatingMap())))
        self.showtime_index = 0
        self.scheduled_showtimes = None
        self.registered_users = SwapList(ArrayList())
        self.name_value = None
        self.reservations_value = None
        self.name = Name
        self.reservations = ReservationManager()
        self.slots.add(Time(14, 30))
        self.slots.add(Time(17, 0))
        self.slots.add(Time(20, 0))
        self.slots.add(Time(22, 30))

    def build_auditorium(self, NumberOfSeats):
        """ Builds and returns a new auditorium with the specified number of seats. """
        auditor = Auditorium(self.auditors.count, NumberOfSeats)
        self.auditors.add(auditor)
        return auditor

    def schedule_showtime(self, Location, MoviePlaying, StartTime):
        """ Schedules a new showtime at this theater, based on the provided arguments. """
        show = Showtime(self.showtime_index, Location, MoviePlaying, StartTime)
        self.showtime_index += 1
        self.scheduled_showtimes.insert(show)
        return show

    def register_customer(self, FirstName, LastName, EmailAddress):
        """ Registers a new customer and returns a User instance that describes them. """
        customer = User(self.registered_users.count, FirstName, LastName, EmailAddress)
        self.registered_users.add(customer)
        return customer

    @property
    def name(self):
        """ Gets the movie theater's name. """
        return self.name_value

    @name.setter
    def name(self, value):
        """ Sets the movie theater's name. """
        self.name_value = value

    @property
    def reservations(self):
        """ Gets the reservation manager instance. """
        return self.reservations_value

    @reservations.setter
    def reservations(self, value):
        """ Sets the reservation manager instance. """
        self.reservations_value = value

    @property
    def auditoria(self):
        """ Gets a read-only list of all auditoria in this movie theater. """
        return self.auditors

    @property
    def timeslots(self):
        """ Gets the list of all available timeslots for this movie theater. """
        return self.slots

    @property
    def movies(self):
        """ Gets the list of all movies known to the movie theater. """
        return self.allmovies

    @property
    def showtimes(self):
        """ Gets a table containing scheduled showtimes. The showtimes are contained in a table that uses the showtimes' IDs as search keys. """
        return self.scheduled_showtimes

    @property
    def registered_customers(self):
        """ Gets a read-only view of all customers registered with this theater. """
        return self.registered_users