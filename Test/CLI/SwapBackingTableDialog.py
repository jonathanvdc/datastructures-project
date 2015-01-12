from CommandLineDialog import *
from OptionDialog import *
from TypeBucketFactory import *
import DialogHelpers
import Project

class SwapBackingTableDialog(CommandLineDialog):
    """ A dialog that swaps the backing storage of a swap table. """

    def __init__(self, Name, Target):
        CommandLineDialog.__init__(self, Name)

        self.target = Target

    @property
    def key_map(self):
        return self.target.key_map

    def RunDialog(self, Parent):
        CommandLineDialog.RunDialog(self, Parent)

        result = OptionDialog("", "To which kind of table would you like to switch?", DialogHelpers.GetTableDelegates()).RunDialog(self)
        self.target.swap(result.value(self.key_map))
        self.Write("Table backing storage switched.")
        return self.target