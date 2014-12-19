from CommandLineDialog import *
from OptionDialog import *
from MenuDialog import *
import DialogHelpers
import Project

class NewShowtimeDialog(CommandLineDialog):
    """ A dialog that creates and registers a new showtime. """

    def __init__(self, Theater):
        CommandLineDialog.__init__(self, "new showtime")

        self.theater = Theater

    def RunDialog(self):
        """ Runs the dialog to create a new user. """

        selectedMovie = DialogHelpers.SelectMovie(self.theater, "Which movie will play at the showtime?")
        selectedAuditorium = DialogHelpers.SelectAuditorium(self.theater, "In which auditorium will the showtime take place?")
        selectedStartTime = DialogHelpers.SelectStartTime(self.theater, selectedAuditorium)
        
        return self.theater.schedule_showtime(selectedAuditorium, selectedMovie, selectedStartTime)

