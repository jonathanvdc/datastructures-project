import tkinter

class NumberEntry(tkinter.Entry):
    """ An entry field that supports only numeric input. """

    def __init__(self, master, IntegerInput, cnf = {}, **kw):
        tkinter.Entry.__init__(self, master, cnf, **kw)
        self.integerInput = IntegerInput

    @property
    def is_empty(self):
        """ Gets a boolean value that indicates if the number entry box is empty. """
        return self.get() == None or self.get() == ""

    def getValue(self):
        """ Gets the number this number entry widget represents. """
        try:
            if self.integerInput:
                return int(self.get())
            else:
                return float(self.get())
        except:
            return None

    @property
    def isValid(self):
        """ Gets a boolean value that indicates whether the input in the number entry box is valid. """
        return self.getValue() is not None