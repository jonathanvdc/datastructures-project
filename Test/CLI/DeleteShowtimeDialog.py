from CommandLineDialog import *
import DialogHelpers

class DeleteShowtimeDialog(CommandLineDialog):
    """ A dialog that allows for a timeslot to be deleted. """

    def __init__(self, Theater):
        CommandLineDialog.__init__(self, "delete showtime")
        self.theater = Theater

    def RunDialog(self, Parent):
        CommandLineDialog.RunDialog(self, Parent)

        showtime = DialogHelpers.SelectShowtime(self, self.theater.showtimes)
        if showtime is None:
            return
        
        if self.theater.showtimes.remove(showtime.id):
            self.Write("Showtime successfully deleted.")
            return
		
        self.Write("Could not delete showtime.")