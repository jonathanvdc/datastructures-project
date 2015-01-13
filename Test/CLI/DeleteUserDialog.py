from CommandLineDialog import *
import DialogHelpers

class DeleteUserDialog(CommandLineDialog):
    """ A dialog that allows for a timeslot to be deleted. """

    def __init__(self, Theater):
        CommandLineDialog.__init__(self, "delete user")
        self.theater = Theater

    def RunDialog(self, Parent):
        CommandLineDialog.RunDialog(self, Parent)

        user = DialogHelpers.SelectCustomer(self, self.theater, "Which user would you like to delete?")
        if user is None:
            self.WriteError("Could not delete user.")
            return
        
        for i, item in enumerate(self.theater.registered_customers):
            if item == user:
                self.theater.registered_customers.remove_at(i)
                self.Write("User removed.")
                return

        self.WriteError("User could not be deleted.")