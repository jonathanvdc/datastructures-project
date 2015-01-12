from CommandLineDialog import *
from OptionDialog import *
from MenuDialog import *

class SetTimeDialog(CommandLineDialog):
	""" A dialog that modifies the theaters internal time. """

	def __init__(self, name):
		CommandLineDialog.__init__(self, name)

	def RunDialog(self, Parent):
		""" Runs the dialog to modify the theaters internal time. """
		CommandLineDialog.RunDialog(self, Parent)

		self.Write("The current date is: " + str(get_now().date))
		newDate = self.ReadDate("Please input a new date:")
		newTime = self.ReadTime("Please input a new time:")
		override_now(Project.DateTime(newDate, newTime))
		self.Write("The date/time has been set to: " + str(get_now()))