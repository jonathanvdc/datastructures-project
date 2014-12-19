from CommandLineDialog import *

class QuitDialog(CommandLineDialog):
    """ A dialog that quits immediately. """

    def __init__(self, Callback):
        CommandLineDialog.__init__(self, "quit")

        self.quitCallback = Callback

    def RunDialog(self):
        """ Calls the quit callback. """

        return self.quitCallback()