from CommandLineDialog import *

class QuitDialog(CommandLineDialog):
    """ A dialog that quits immediately. """

    def __init__(self, Callback):
        CommandLineDialog.__init__(self, "quit")

        self.quitCallback = Callback

    def RunDialog(self, Parent):
        """ Calls the quit callback. """
        CommandLineDialog.RunDialog(self, Parent)

        return self.quitCallback()