from CommandLineDialog import *
from OptionDialog import *
import Project

class SortTableDialog(CommandLineDialog):
    """ A dialog that performs a one-time sort on a sortable table. """

    def __init__(self, Name, Target, ExtraCriteria = []):
        CommandLineDialog.__init__(self, Name)

        self.target = Target
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

    def RunDialog(self):
        
        comparer = OptionDialog("", "Based on which criteria would you like to sort?", self.criteria_options).RunDialog().value
        sorter = OptionDialog("", "Which algorithm would you like to use?", self.options).RunDialog().value(comparer)
        self.target.sort(sorter)
        print("Table sorted.")
        return self.target