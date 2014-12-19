from CommandLineDialog import *
import DialogHelpers

class DeleteTimeslotDialog(CommandLineDialog):
    """ A dialog that allows for a timeslot to be deleted. """

    def __init__(self, Theater):
        CommandLineDialog.__init__(self, "delete timeslot")
        self.theater = Theater

    def RunDialog(self):
        slot = DialogHelpers.SelectTimeslot(self.theater.timeslots, "Which timeslot would you like to delete?")
        if slot is None:
            print("Could not delete timeslot.")
            return
        
        for i, item in enumerate(self.theater.timeslots):
            if item == slot:
                self.theater.timeslots.remove_at(i)
                print("Timeslot removed.")
                return

        print("Timeslot could not be deleted.")