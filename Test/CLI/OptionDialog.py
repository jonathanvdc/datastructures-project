from CommandLineDialog import *
import Project

class OptionDialog(CommandLineDialog):
    """ A command-line dialog that offers a finite series of options. """

    def __init__(self, Name, Intro, OptionTable = None, ShowValues = False):
        """ Creates a new instance of an option dialog from a name, an intro,
        a table of options and a boolean value that specifies whether the values or keys of the option table are printed. """

        CommandLineDialog.__init__(self, Name)

        self.intro = Intro
        self.ReadOptionKey = self.ReadString
        self.showValues = ShowValues
        if OptionTable is None:
            self.optionTable = Project.TreeTable(Project.BinarySearchTree(Project.DefaultRecordMap()))
        else:
            self.optionTable = OptionTable

    def add_option(self, Option):
        """ Adds an option to the dialog. """
        return self.optionTable.insert(Option)

    @property
    def options(self):
        """ Gets a collection of all available options. """
        if self.showValues:
            return self.optionTable
        else:
            return [self.optionTable.key_map.map(item) for item in self.optionTable]

    def get_value(self, Key):
        """ Gets the value associated with the provided key, if any. """

        return self.optionTable[Key]

    def RunDialog(self, Parent):
        """ Starts the dialog with the user. """
        CommandLineDialog.RunDialog(self, Parent)

        self.Write(self.intro)
        if self.showValues:
            self.Write("options (please enter an item's key, not its whole value):")
        else:
            self.Write("options:")
        for item in self.options:
            self.Write(" - " + str(item))
        val = self.get_value(self.ReadOptionKey())
        while val is None:
            self.Write("The provided input could not be matched exactly to a valid option. Please try again.")
            val = self.get_value(self.ReadOptionKey())
        return val