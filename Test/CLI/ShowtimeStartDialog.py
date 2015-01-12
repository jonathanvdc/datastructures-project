from CommandLineDialog import *
from OptionDialog import *
from MenuDialog import *
from ShowtimeManager import *
import Project

class ShowtimeStartDialog(CommandLineDialog):
    """ A dialog that selects the start time for a showtime. """

    def __init__(self, Theater, Auditorium):
        CommandLineDialog.__init__(self, "select showtime start")

        self.theater = Theater
        self.auditorium = Auditorium

    def ShowtimeScheduled(self, StartTime):
        """ Returns a boolean value that indicates whether a showtime has been scheduled for this auditorium for the specified time. """

        for item in FilterShowtimes(self.theater):
            if item.location == self.auditorium and item.start_time == StartTime:
                return True
        return False

    def IsValidTimeslot(self, Timeslot):
        """ Returns a boolean value that indicates if the given timeslot is a viable candidate. """
        return Timeslot > get_now() and (not self.ShowtimeScheduled(Timeslot))

    def ReadStartDate(self):
        """ Reads the start date of the showtime. """
        return self.ReadFutureDate("For what date would you like to schedule the showtime?")

    def CreateTimeslotTable(self, StartDate):
        """ Creates a new table that maps all available timeslots to themselves for showtimes that start at the specified date. """

        # Linear open-addressed hash table with time -> time map
        timeslotTable = Project.OpenHashtable(Project.IdentityMap(), Project.PowerSequenceMap(1))
        for item in [Project.DateTime(StartDate, slot) for slot in self.theater.timeslots]:
            if self.IsValidTimeslot(item):
                timeslotTable.insert(item.time_of_day)

        return timeslotTable

    def RunDialog(self, Parent):
        """ Runs the dialog to select the start time for a showtime. """
        CommandLineDialog.RunDialog(self, Parent)

        date = self.ReadStartDate()
        # Linear open-addressed hash table with time -> time map
        timeslotTable = self.CreateTimeslotTable(date)

        while timeslotTable.count == 0:
            self.Write("The selected date did not have any open timeslots. Please select another date.")
            date = self.ReadStartDate()
            timeslotTable = self.CreateTimeslotTable(date)

        selectTimeslotDialog = OptionDialog("select timeslot", "Which timeslot would you like to schedule the showtime for?", timeslotTable)
        # Reads times as keys
        selectTimeslotDialog.ReadOptionKey = selectTimeslotDialog.ReadTime
        time = selectTimeslotDialog.RunDialog(self)

        return Project.DateTime(date, time)