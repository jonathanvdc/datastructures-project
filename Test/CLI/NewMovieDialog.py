from CommandLineDialog import *
from OptionDialog import *
from MenuDialog import *

class NewMovieDialog(CommandLineDialog):
    """ A dialog that creates and registers a new movie. """

    def __init__(self, Callback):
        CommandLineDialog.__init__(self, "new movie")

        self.finishCallback = Callback

    def RunDialog(self, Parent):
        """ Runs the dialog to create a new user. """
        CommandLineDialog.RunDialog(self, Parent)

        title = self.ReadNoBlankString("What is the movie's title?")
        rating = self.ReadRangeFloat(0.0, 5.0, "How is the movie rated?")

        return self.finishCallback(title, rating)