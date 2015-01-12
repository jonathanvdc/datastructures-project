from CommandLineDialog import *
from OptionDialog import *
from TypeBucketFactory import *
import Project

class SwapBackingSortedListDialog(CommandLineDialog):
    """ A dialog that swaps the backing storage of a sorted list. """

    def __init__(self, Name, Target, KeyMapOptions = []):
        CommandLineDialog.__init__(self, Name)

        self.target = Target
        self.map_options = KeyMapOptions

    @property
    def key_map(self):
        return self.target.key_map

    @property
    def key_map_options(self):
        """ Gets a table containing record -> key maps that can be selected to sort the sorted list. """

        table = Project.Hashtable(Project.DefaultRecordMap(), TypeBucketFactory(lambda map: Project.ListTable(map, Project.LinkedList())))

        for k, v in self.map_options:
            table.insert(Project.KeyValuePair(k, v))

        if table.count == 0:
            table.insert(Project.KeyValuePair("current map", self.key_map))

        return table

    @property
    def options(self):
        """ Gets a table of key-value pairs that represents the various options. """

        table = Project.ListTable(Project.DefaultRecordMap(), Project.LinkedList())
        table.insert(Project.KeyValuePair("binary tree", lambda map: Project.TreeSortedList(Project.BinarySearchTree(map))))
        table.insert(Project.KeyValuePair("2-3-4 tree", lambda map: Project.TreeSortedList(Project.TwoThreeFourSearchTree(map))))
        table.insert(Project.KeyValuePair("sorted array list", lambda map: Project.SortedList(map, Project.ArrayList())))
        table.insert(Project.KeyValuePair("sorted linked list", lambda map: Project.SortedList(map, Project.LinkedList())))

        return table

    def RunDialog(self, Parent):
        """ Displays the dialog. """
        CommandLineDialog.RunDialog(self, Parent)

        km_options = self.key_map_options
        if km_options.count > 1:
            map = OptionDialog("", "Which mapping funtion would you like to use to sort the list with?", self.key_map_options).RunDialog(self).value
        else:
            map = self.key_map

        result = OptionDialog("", "To which kind of sorted list would you like to switch?", self.options).RunDialog(self)
        self.target.swap(result.value(map))
        self.Write("Sorted list backing storage switched.")
        return self.target