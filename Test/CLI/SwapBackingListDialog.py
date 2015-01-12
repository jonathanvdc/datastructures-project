from CommandLineDialog import *
from OptionDialog import *
import Project

class SwapBackingListDialog(CommandLineDialog):
    """ A dialog that swaps the backing list of a swap list. """

    def __init__(self, Name, Target):
        CommandLineDialog.__init__(self, Name)

        self.target = Target

    @property
    def options(self):
        """ Gets a table of key-value pairs that represents the various options. """

        table = Project.ListTable(Project.DefaultRecordMap(), Project.LinkedList())
        table.insert(Project.KeyValuePair("array list", Project.ArrayList()))
        table.insert(Project.KeyValuePair("linked list", Project.LinkedList()))

        return table

    def RunDialog(self, Parent):
        CommandLineDialog.RunDialog(self, Parent)
        
        result = OptionDialog("", "To which kind of list would you like to switch?", self.options).RunDialog(self)
        self.target.swap(result.value)
        self.Write("List backing storage switched.")
        return self.target