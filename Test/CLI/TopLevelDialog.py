from CommandLineDialog import *

class TopLevelDialog(CommandLineDialog):
    """ A dialog that provides an input and output stream for other dialogs. """

    def __init__(self, InputStream, OutputStream):
        CommandLineDialog.__init__(self, "", InputStream, OutputStream)

    def RunChild(self, Child):
        return Child.RunDialog(self)