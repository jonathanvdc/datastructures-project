from CommandLineDialog import *
import Project

overdue_time = Project.Time(1, 00)

def SetOverdueTime(Time):
    """ Sets the overdue timeout to the given value. """
    global overdue_time
    overdue_time = Time

def IsOverdue(Theater, Showtime):
    """ Finds out if a showtime in a theater is overdue and returns the result as a boolean. """
    now = get_now()
    for item in Theater.showtimes:
        if Showtime.date < now.date or (item.timeslot > Showtime.timeslot and item.timeslot - now.time_of_day < overdue_time and item.location.key == Showtime.location.key): # A showtime is considered overdue if it was scheduled to be screened yesterday or an earlier date, or if another showtime will begin shortly in the same auditorium
            return True
    return False

def CanEnter(Showtime):
    """ Returns a boolean value that indicates whether customers can enter the given showtime already. """
    now = get_now()
    return Showtime.date == now.date and Showtime.timeslot - now.time_of_day < overdue_time # A user can enter a showtime if said showtime is today, and the 

def FilterShowtimes(Theater):
    """ Filters the theater's showtimes, removing showtimes that are overdue, and returns the result. """

    showtimeList = Project.ArrayList([item for item in Theater.showtimes])

    for item in showtimeList:
        if IsOverdue(Theater, item):
            Theater.showtimes.remove(item.key)

    return Theater.showtimes