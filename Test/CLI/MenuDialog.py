from CommandLineDialog import *
from OptionDialog import *

class MenuDialog(OptionDialog):
    """ A dialog that allows the user to select from a menu of dialogs. """

    def __init__(self, Name, Intro, OptionTable = None):
        OptionDialog.__init__(self, Name, Intro, OptionTable)

    def RunDialog(self, Parent):
        """ Starts the dialog with the user. """
        CommandLineDialog.RunDialog(self, Parent)

        result = super().RunDialog(self)
        # The result is itself a dialog, so let's run that
        result.RunDialog(self)