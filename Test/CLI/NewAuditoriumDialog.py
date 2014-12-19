from CommandLineDialog import *

class NewAuditoriumDialog(CommandLineDialog):
    """ A dialog that supports the creation of a new auditorium. """

    def __init__(self, Theater):
        CommandLineDialog.__init__(self, "new auditorium")
        self.theater = Theater
        
    def RunDialog(self):
        numberOfSeats = self.ReadInteger("How many seats should the auditorium have?", lambda x: x is not None and x > 0, "The given input is not a positive integer. Please input a positive integer.")
        aud = self.theater.build_auditorium(numberOfSeats)
        print(str(aud) + " has been created")
        return aud