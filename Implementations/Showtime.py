from Ticket import *
from Reservation import *
from Stack import *
from IRecord import *

class Showtime(IRecord):
    """ Describes a showtime at the movie theater. """

    def __init__(self, Id, Location, MoviePlaying, StartTime):
        """ Creates a new instance of a showtime. """
        self.id_value = 0
        self.location_value = None
        self.movie_playing_value = None
        self.start_time_value = None
        self.tickets = Stack()
        self.id = Id
        self.location = Location
        self.movie_playing = MoviePlaying
        self.start_time = StartTime

    def __str__(self):
        """ Gets the showtime's string representation. """
        return "Showtime #" + str(self.id) + " of " + str(self.movie_playing) + ", " + str(self.location) + ", at " + str(self.timeslot) + ", " + str(self.number_of_free_seats) + " free seats"

    def make_reservation(self, Id, Request):
        """ Reserves a ticket for this showtime. """
        if Request.number_of_seats > self.number_of_free_seats:
            return None
        else:
            i = 0
            while i < Request.number_of_seats:
                self.tickets.push(Ticket(Request.customer))
                i += 1
            return Reservation(Id, Request.customer, self, Request.timestamp, Request.number_of_seats)

    def has_ticket(self, Customer):
        """ Gets a boolean value that indicates whether the provided customer has a ticket for this showtime. """
        for item in self.tickets:
            if item.customer == Customer:
                return True
        return False

    def redeem_ticket(self, Theater, Customer):
        """ Have one person redeem their ticket and enter the showtime.  Note that a user who reserved more than one ticket must enter the showtime multiple times, once per ticket. """
        if self.has_ticket(Customer):
            tempStorage = Stack()
            while not self.tickets.is_empty:
                item = self.tickets.pop()
                if item.customer == Customer:
                    break
                else:
                    tempStorage.push(item)
            while not tempStorage.is_empty:
                self.tickets.push(tempStorage.pop())
            if self.tickets.is_empty:
                Theater.showtimes.remove(self.id)

    @property
    def id(self):
        """ Gets the showtime's unique identifier. """
        return self.id_value

    @id.setter
    def id(self, value):
        """ Sets the showtime's unique identifier. """
        self.id_value = value

    @property
    def location(self):
        """ Gets the auditorium where the showtime will take place. """
        return self.location_value

    @location.setter
    def location(self, value):
        """ Sets the auditorium where the showtime will take place. """
        self.location_value = value

    @property
    def movie_playing(self):
        """ Gets the movie that will play at the showtime. """
        return self.movie_playing_value

    @movie_playing.setter
    def movie_playing(self, value):
        """ Sets the movie that will play at the showtime. """
        self.movie_playing_value = value

    @property
    def start_time(self):
        """ Gets the date and time for which this showtime is scheduled. """
        return self.start_time_value

    @start_time.setter
    def start_time(self, value):
        """ Sets the date and time for which this showtime is scheduled. """
        self.start_time_value = value

    @property
    def timeslot(self):
        """ Gets the movie's starting time. """
        return self.start_time.time_of_day

    @property
    def number_of_free_seats(self):
        """ Gets the number of remaining free seats for this showtime. """
        return self.location.number_of_seats - self.tickets.count

    @property
    def date(self):
        """ Gets the date assigned to the showtime. """
        return self.start_time.date

    @property
    def auditorium_index(self):
        """ Gets the index of the auditorium where the showtime will take place. """
        return self.location.index

    @property
    def movie_id(self):
        """ Gets the identifier of the movie that's playing at the showtime instance. """
        return self.movie_playing.id

    @property
    def key(self):
        """ Gets the record's search key. """
        return self.id