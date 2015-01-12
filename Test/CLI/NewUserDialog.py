from CommandLineDialog import *
from OptionDialog import *
from MenuDialog import *

class NewUserDialog(CommandLineDialog):
    """ A dialog that creates and registers a new user. """

    def __init__(self, Callback):
        CommandLineDialog.__init__(self, "new user")

        self.finishCallback = Callback

    def RunDialog(self, Parent):
        """ Runs the dialog to create a new user. """
        CommandLineDialog.RunDialog(self, Parent)

        firstName = self.ReadNoBlankString("Please enter your first name.")
        lastName = self.ReadNoBlankString("How about your last name?")
        email = self.ReadNoBlankString("What is your e-mail address.")

        return self.finishCallback(firstName, lastName, email)