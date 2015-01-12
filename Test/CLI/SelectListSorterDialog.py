from CommandLineDialog import *
from OptionDialog import *
import Project

class SelectListSorterDialog(CommandLineDialog):
    """ A dialog that acquires a list sorter. """

    def __init__(self, Name, ExtraCriteria = []):
        CommandLineDialog.__init__(self, Name)

        self.extraCriteria = ExtraCriteria

    @property
    def options(self):
        """ Gets a table of key-value pairs that represents the various options. """

        table = Project.ListTable(Project.DefaultRecordMap(), Project.ArrayList())
        table.insert(Project.KeyValuePair("quicksort", lambda map: Project.Quicksort(Project.MapComparer(map))))
        table.insert(Project.KeyValuePair("treesort - binary tree", lambda map: Project.SortedListSort(Project.TreeSortedList(Project.BinarySearchTree(map)))))
        table.insert(Project.KeyValuePair("treesort - 2-3-4 tree", lambda map: Project.SortedListSort(Project.TreeSortedList(Project.TwoThreeFourSearchTree(map)))))
        table.insert(Project.KeyValuePair("insertion sort - linked list", lambda map: Project.SortedListSort(Project.SortedList(map, Project.LinkedList()))))
        table.insert(Project.KeyValuePair("insertion sort - array list", lambda map: Project.SortedListSort(Project.SortedList(map, Project.ArrayList()))))

        return table

    @property
    def criteria_options(self):
        """ Gets a table of key-value pairs that represents the various sorting criteria. """

        table = Project.TreeTable(Project.TwoThreeFourSearchTree(Project.DefaultRecordMap()))
        table.insert(Project.KeyValuePair("key", Project.DefaultRecordMap()))
        for (key, value) in self.extraCriteria:
            table.insert(Project.KeyValuePair(key, value))

        return table

    def RunDialog(self, Parent):
        CommandLineDialog.RunDialog(self, Parent)
        
        comparer = OptionDialog("", "Based on which criteria would you like to sort?", self.criteria_options).RunDialog(self).value
        sorter = OptionDialog("", "Which algorithm would you like to use?", self.options).RunDialog(self).value(comparer)
        return sorter