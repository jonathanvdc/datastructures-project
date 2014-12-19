from Auditorium import *
from Showtime import *
from User import *
from Movie import *
from SwapList import *
from ArrayList import *
from SortedSwapList import *
from TreeSortedList import *
from BinarySearchTree import *
from MovieRatingMap import *
from ListTable import *
from DefaultRecordMap import *
from ReservationManager import *
from Time import *

class Theater:
    """ Represents a movie theater. """

    def __init__(self, Name):
        """ Creates a new movie theater instance. """
        self.showtime_index = 0
        self.movie_index = 0
        self.auditors = SwapList(ArrayList())
        self.slots = SwapList(ArrayList())
        self.allmovies = SortedSwapList(TreeSortedList(BinarySearchTree(MovieRatingMap())))
        self.scheduled_showtimes = ListTable(DefaultRecordMap(), ArrayList())
        self.registered_users = SwapList(ArrayList())
        self.name = Name
        self.reservations = ReservationManager()
        self.slots.add(Time(14, 30))
        self.slots.add(Time(17, 0))
        self.slots.add(Time(20, 0))
        self.slots.add(Time(22, 30))

    def find_movie(self, Title):
        """ Tries to find a movie based on its complete title. """
        for item in self.movies:
            if item.title == Title:
                return item
        return None

    def is_timeslot(self, Value):
        """ Gets a boolean value that indicates if the provided time corresponds to a timeslot. """
        for item in self.timeslots:
            if Value == item:
                return True
        return False

    def showtime_planned(self, Location, StartTime):
        """ Gets a boolean value that indicates whether a showtime has been planned or not at the specified time in the specified auditorium. """
        for item in self.showtimes:
            if item.location == Location and item.start_time == StartTime:
                return True
        return False

    def build_auditorium(self, NumberOfSeats):
        """ Builds and returns a new auditorium with the specified number of seats. """
        auditor = Auditorium(self.auditors.count, NumberOfSeats)
        self.auditors.add(auditor)
        return auditor

    def schedule_showtime(self, Location, MoviePlaying, StartTime):
        """ Schedules a new showtime at this theater, based on the provided arguments. """
        if (not self.is_timeslot(StartTime.time_of_day)) or (not self.movies.contains(MoviePlaying)) or self.showtime_planned(Location, StartTime):
            return None
        show = Showtime(self.showtime_index, Location, MoviePlaying, StartTime)
        self.showtime_index += 1
        self.scheduled_showtimes.insert(show)
        return show

    def register_customer(self, FirstName, LastName, EmailAddress):
        """ Registers a new customer and returns a User instance that describes them. """
        customer = User(self.registered_users.count, FirstName, LastName, EmailAddress)
        self.registered_users.add(customer)
        return customer

    def register_movie(self, Title, Rating):
        """ Creates a new movie from the given arguments and adds it to the list of playing movies. """
        result = Movie(self.movie_index, Title, Rating)
        self.movies.add(result)
        self.movie_index += 1
        return result

    @property
    def movies(self):
        """ Gets the list of all movies known to the movie theater. """
        return self.allmovies

    @property
    def timeslots(self):
        """ Gets the list of all available timeslots for this movie theater. """
        return self.slots

    @property
    def showtimes(self):
        """ Gets a table containing scheduled showtimes. The showtimes are contained in a table that uses the showtimes' IDs as search keys. """
        return self.scheduled_showtimes

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
    def registered_customers(self):
        """ Gets a read-only view of all customers registered with this theater. """
        return self.registered_users