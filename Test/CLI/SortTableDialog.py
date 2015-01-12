from CommandLineDialog import *
from OptionDialog import *
from SelectListSorterDialog import *
import Project

class SortTableDialog(CommandLineDialog):
    """ A dialog that performs a one-time sort on a sortable table. """

    def __init__(self, Name, Target, ExtraCriteria = []):
        CommandLineDialog.__init__(self, Name)

        self.target = Target
        self.select_dialog = SelectListSorterDialog("", ExtraCriteria)

    def RunDialog(self, Parent):
        CommandLineDialog.RunDialog(self, Parent)
        
        sorter = self.select_dialog.RunDialog(self)
        self.target.sort(sorter)
        self.Write("Table sorted.")
        return self.target