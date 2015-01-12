from CommandLineDialog import *
from CollectionDialog import *

class LazyCollectionDialog(CommandLineDialog):
    """ A class for dialogs that lazily provide a collection of information. """

    def __init__(self, Name, Intro, Func):
        """ Creates a new instance of a lazy collection dialog from the given name, intro and collection-yielding function. """
        CommandLineDialog.__init__(self, Name)
        self.intro = Intro
        self.func = Func

    def RunDialog(self, Parent):
        """ Displays the list of items. """
        CommandLineDialog.RunDialog(self, Parent)

        dialog = CollectionDialog("", self.intro, self.func())
        return dialog.RunDialog(self)