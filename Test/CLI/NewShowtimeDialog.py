from CommandLineDialog import *
from OptionDialog import *
from MenuDialog import *
import Project

class NewShowtimeDialog(CommandLineDialog):
    """ A dialog that creates and registers a new showtime. """

    def __init__(self, Theater):
        CommandLineDialog.__init__(self, "new showtime")

        self.theater = Theater

    def RunDialog(self):
        """ Runs the dialog to create a new user. """

        table = Project.Hashtable(Project.MovieTitleMap(), Project.BinaryTreeTableFactory())
        for item in self.theater.movies:
            table.insert(item)
        selectMovieDialog = OptionDialog("select movie", "Which movie will play at the showtime?", table)
        selectedMovie = selectMovieDialog.RunDialog()

