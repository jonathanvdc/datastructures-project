from CommandLineDialog import *
from OptionDialog import *
from MenuDialog import *

class SetTimeDialog(CommandLineDialog):
	""" A dialog that modifies the theaters internal time. """

	def __init__(self, name):
		CommandLineDialog.__init__(self, name)

	def RunDialog(self):
		""" Runs the dialog to modify the theaters internal time. """
		
		global date_time_override
		print("The current date is: " + str(get_now().date))
		newDate = self.ReadDate("Please input a new date.")
		newTime = self.ReadTime("Please input a new time.")
		override_now(Project.DateTime(newDate, newTime))
		print(date_time_override)
		print("The date has been set to: " + str(get_now().date))