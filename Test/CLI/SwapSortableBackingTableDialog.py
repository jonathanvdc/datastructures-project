from CommandLineDialog import *
from OptionDialog import *
from SelectListSorterDialog import *
import DialogHelpers
import Project

class SortableTableFactory(Project.IRecord):
    """ Describes a factory for sortable tables. """

    def __init__(self, Name, RequiresSorter, Func):
        self.name = Name
        self.requires_sorter = RequiresSorter
        self.func = Func
            
    @property
    def key(self):
        return self.name

    def create(self, Map, Sorter):
        """ Creates the sortable table. """
        if self.requires_sorter:
            return self.func(Map, Sorter)
        else:
            return self.func(Map)

class SwapSortableBackingTableDialog(CommandLineDialog):
    """ A dialog that swaps the backing storage of a sortable swap table. """

    def __init__(self, Name, Target, ExtraCriteria = []):
        CommandLineDialog.__init__(self, Name)
        
        self.target = Target
        self.sort_dialog = SelectListSorterDialog("", ExtraCriteria)

    @property
    def options(self):
        """ Gets a table that contains possible sortable table descriptions. """
        table = Project.TreeTable(Project.TwoThreeFourSearchTree(Project.DefaultRecordMap()))
        table.insert(SortableTableFactory("sortable array list", False, lambda map: Project.ListTable(map, Project.ArrayList())))
        table.insert(SortableTableFactory("sortable linked list", False, lambda map: Project.ListTable(map, Project.LinkedList())))

        for item in DialogHelpers.GetTableDelegates():
            table.insert(SortableTableFactory("sorted " + item.key, True, lambda map, sorter: Project.SortedTable(item.value(map), sorter)))

        return table

    def RunDialog(self, Parent):
        """ Displays the sortable backing table dialog. """
        CommandLineDialog.RunDialog(self, Parent)

        tableFactory = OptionDialog("", "To which kind of sortable table would you like to switch?", self.options).RunDialog(self)
        if tableFactory.requires_sorter:
            sorter = self.sort_dialog.RunDialog(self)
        else:
            sorter = None

        result = tableFactory.create(self.target.key_map, sorter)
        self.Write("Sortable table backing storage switched.")
        self.target.swap(result)

        