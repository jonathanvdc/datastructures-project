from CommandLineDialog import *
from OptionDialog import *
import Project

class SwapBackingSortedListDialog(CommandLineDialog):
    """ A dialog that swaps the backing storage of a sorted list. """

    def __init__(self, Name, Target):
        CommandLineDialog.__init__(self, Name)

        self.target = Target

    @property
    def key_map(self):
        return self.target.key_map

    @property
    def options(self):
        """ Gets a table of key-value pairs that represents the various options. """

        table = Project.ListTable(Project.DefaultRecordMap(), Project.LinkedList())
        table.insert(Project.KeyValuePair("binary tree sorted list", Project.TreeSortedList(Project.BinarySearchTree(self.key_map))))
        table.insert(Project.KeyValuePair("2-3-4 tree sorted list", Project.TreeSortedList(Project.TwoThreeFourSearchTree(self.key_map))))

        return table

    def RunDialog(self):
        
        result = OptionDialog("", "To which kind of sorted list would you like to switch?", self.options).RunDialog()
        self.target.swap(result.value)
        print("Sorted list backing storage switched.")
        return self.target