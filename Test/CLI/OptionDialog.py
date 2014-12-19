from CommandLineDialog import *
import Project

class OptionDialog(CommandLineDialog):
    """ A command-line dialog that offers a series of options. """

    def __init__(self, Name, Intro, OptionTable = None):
        CommandLineDialog.__init__(self, Name)

        self.intro = Intro
        if OptionTable is None:
            self.optionTable = Project.Hashtable(Project.DefaultRecordMap(), Project.BinaryTreeTableFactory())
        else:
            self.optionTable = OptionTable

    def add_option(self, Option):
        """ Adds an option to the dialog. """
        return self.optionTable.insert(Option)

    @property
    def options(self):
        """ Gets a list of all available options. """

        return [self.optionTable.key_map.map(item) for item in self.optionTable]

    def get_value(self, Key):
        """ Gets the value associated with the provided key, if any. """

        return self.optionTable[Key]

    def RunDialog(self):
        """ Starts the dialog with the user. """

        print(self.intro)
        print("options:")
        for item in self.options:
            print(" - " + item)
        val = self.get_value(self.ReadString())
        while val is None:
            print("The provided input did not match exactly to a valid option. Try again.")
            val = self.get_value(self.ReadString())
        return val