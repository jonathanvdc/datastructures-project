from CommandLineDialog import *
import DialogHelpers

class DeleteMovieDialog(CommandLineDialog):
    """ A dialog that allows for a timeslot to be deleted. """

    def __init__(self, Theater):
        CommandLineDialog.__init__(self, "delete movie")
        self.theater = Theater

    def RunDialog(self, Parent):
        CommandLineDialog.RunDialog(self, Parent)

        movie = DialogHelpers.SelectMovie(self, self.theater, "Which movie would you like to delete?")
        if movie is None:
            self.WriteError("Could not delete movie.")
            return
        
        if self.theater.movies.remove(movie):
            self.Write("Movie successfully deleted.")
        else:
            self.WriteError("Movie could not be deleted.")