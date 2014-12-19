from CommandLineDialog import *
from OptionDialog import *
import Project
import TwoThreeFourSearchTree as Project

class SwapBackingTableDialog(CommandLineDialog):
    """ A dialog that swaps the backing list of a swap list. """

    def __init__(self, Name, Target):
        CommandLineDialog.__init__(self, Name)

        self.target = Target

    @property
    def key_map(self):
        return self.target.key_map

    @property
    def options(self):
        """ Gets a table of key-value pairs that represents the various """

        table = Project.OpenHashtable(Project.DefaultRecordMap(), Project.PowerSequenceMap(1))
        table.insert(Project.KeyValuePair("list table - array", Project.ListTable(self.key_map, Project.ArrayList())))
        table.insert(Project.KeyValuePair("list table - linked list", Project.ListTable(self.key_map, Project.LinkedList())))
        table.insert(Project.KeyValuePair("binary tree table", Project.TreeTable(Project.BinarySearchTree(self.key_map))))
        table.insert(Project.KeyValuePair("2-3-4 tree table", Project.TreeTable(Project.TwoThreeFourSearchTree(self.key_map))))
        table.insert(Project.KeyValuePair("separate chaining hashtable - binary tree", Project.Hashtable(self.key_map, Project.BinaryTreeTableFactory())))
        table.insert(Project.KeyValuePair("linear open addressing hashtable", Project.OpenHashtable(self.key_map, Project.PowerSequenceMap(1))))
        table.insert(Project.KeyValuePair("quadratic open addressing hashtable", Project.OpenHashtable(self.key_map, Project.PowerSequenceMap(2))))


        return table

    def RunDialog(self):
        
        result = OptionDialog("", "To which kind of table would you like to switch?", self.options).RunDialog()
        self.target.swap(result.value)
        print("Table backing storage switched.")
        return self.target