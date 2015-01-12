from CommandLineDialog import *
from CollectionDialog import *

class NewTimeslotDialog(CommandLineDialog):
    """ A dialog for the creation of a new timeslot. """

    def __init__(self, Theater, Threshold = Project.Time(0, 30)):
        CommandLineDialog.__init__(self, "new timeslot")

        self.theater = Theater
        self.threshold = Threshold

    def GetMinDistance(self, Time):
        """ Gets the minimal distance from the given time to any other timeslot in the theater. """
        return min([Time - item if Time > item else item - Time for item in self.theater.timeslots])


    def RunDialog(self, Parent):
        """ Schedules a new timeslot through input procured via the command line. """
        
        time = self.ReadTime("When would you like to schedule a new timeslot?")

        while self.GetMinDistance(time) < self.threshold:
            self.Write("The timeslot may not be closer to another timeslot than " + str(self.threshold))
            CollectionDialog("view timeslots", "List of current timeslots:", self.theater.timeslots).RunDialog(self)
            time = self.ReadTime("When would you like to schedule a new timeslot?")

        self.theater.timeslots.add(time)
        return time