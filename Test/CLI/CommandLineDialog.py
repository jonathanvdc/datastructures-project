import Project

class CommandLineDialog(Project.IRecord):
    """ A base class for command-line dialogs. """

    def __init__(self, Name):
        self.name_value = Name

    @property
    def name(self):
        """ Gets the command-line dialog's name. """
        return self.name_value

    @property
    def key(self):
        """ Gets the key of the command-line dialog as a record."""
        return self.name

    def PersistRead(self, ReadDelegate, Text, Predicate = lambda x: x is None):
        """ Reads input from the command line until a suitable answer is found. """
        result = ReadDelegate()
        while not Predicate(result):
            print(Text)
            result = ReadDelegate()
        return result

    def TryReadInteger(self):
        """ Tries to read a integer from the command line. """
        try:
            return int(input())
        except:
            return None

    def TryReadFloat(self):
        """ Tries to read a floating-point number from the command line. """
        try:
            return float(input())
        except:
            return None

    def TryReadBoolean(self):
        """ Tries to read a boolean value from the command line. """
        val = input().strip().lower()
        if val == "y" or val == "yes":
            return True
        elif val == "n" or val == "no":
            return False
        else:
            return None

    def ReadInteger(self, 
                    Text = None, 
                    Predicate = lambda x: x is not None, 
                    FailText = "The given input was not an integer. Please input an integer."):
        """ Reads an integer from the command line. """
        if Text is not None:
            print(Text)
        return self.PersistRead(self.TryReadInteger, FailText, Predicate)

    def ReadFloat(self, 
                  Text = None, 
                  Predicate = lambda x: x is not None, 
                  FailText = "The given input could not be parsed as a floating-point number. Please input a float."):
        """ Reads a floating-point number from the command line. """
        if Text is not None:
            print(Text)
        return self.PersistRead(self.TryReadFloat, FailText, Predicate)

    def ReadBoolean(self, 
                  Text = None, 
                  Predicate = lambda x: x is not None, 
                  FailText = "The given input could not be parsed as a boolean number. Please input either 'yes' or 'no'."):
        """ Reads a boolean value from the command line. """
        if Text is not None:
            print(Text)
        return self.PersistRead(self.TryReadBoolean, FailText, Predicate)

    def ReadRangeFloat(self, Min, Max, Text = None):
        """ Reads a floating-point number within a specified range from the command line. """
        return self.ReadFloat(Text, lambda x: x is not None and x >= Min and x <= Max, "The given input could not be parsed as a floating-point between " + str(Min) + " and " + str(Max) + ". Please input a correct float.")

    def ReadString(self, Text = None):
        """ Reads a string from the command line. """
        if Text is not None:
            print(Text)
        return input()

    def ReadNoBlankString(self, Text = None):
        """ Reads a non-empty string that is not blank from the command line. """
        if Text is not None:
            print(Text)
        return self.PersistRead(self.ReadString, "The given string was empty or blank. Please input a non-empty string that is not blank.", lambda x: x is not None and x != "" and not x.isspace())

    def RunDialog(self):
        """ Starts the command-line dialog with the user. """
        
        raise NotImplementedError("Method 'CommandLineDialog.StartDialog' was not implemented.")