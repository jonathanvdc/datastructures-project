from CommandLineDialog import *

class CollectionDialog(CommandLineDialog):
    """ A class for dialogs that provide a collection of information. """

    def __init__(self, Name, Intro, Collection):
        CommandLineDialog.__init__(self, Name)
        self.intro = Intro
        self.collection = Collection

    def RunDialog(self):
        """ Displays the list of items. """

        print(self.intro)
        for item in self.collection:
            print(str(item))
        print("========================")