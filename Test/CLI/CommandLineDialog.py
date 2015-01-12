import Project
import IOStreams
import datetime

date_time_override = None

def override_now(date):
	global date_time_override
	date_time_override = date

def get_now():
	if date_time_override is None:
		currentTime = datetime.datetime.now()
		return Project.DateTime(Project.Date(currentTime.day, currentTime.month, currentTime.year), Project.Time(currentTime.hour, currentTime.minute, currentTime.second))
	else:
		return date_time_override

class CommandLineDialog(Project.IRecord):
    """ A base class for command-line dialogs. """

    def __init__(self, Name, InputStream = None, OutputStream = None):
        self.name_value = Name
        self.istream = InputStream
        self.ostream = OutputStream

    @property
    def name(self):
        """ Gets the command-line dialog's name. """
        return self.name_value

    @property
    def key(self):
        """ Gets the key of the command-line dialog as a record."""
        return self.name

    def CreateOutputType(self, Delegate):
        """ Creates an output type for the command-line dialog by calling the given function with the dialog's output stream as argument. """
        return Delegate(self.ostream)

    @property
    def Query(self):
        """ Creates a query output type for this command-line dialog. """ 
        return self.CreateOutputType(IOStreams.OutputType.Query)

    @property
    def Error(self):
        """ Creates an error output type for this command-line dialog. """ 
        return self.CreateOutputType(IOStreams.OutputType.Error)

    def Write(self, Value):
        """ Writes a line of text to the output stream. """
        self.ostream.Write(Value)

    def WriteQuery(self, Value):
        """ Writes a line of text with output type 'query' to the output stream. """
        with self.Query:
            self.ostream.Write(Value)

    def WriteError(self, Value):
        """ Writes a line of text with output type 'error' to the output stream. """
        with self.Error:
            self.ostream.Write(Value)

    def PersistRead(self, ReadDelegate, Text, Predicate = lambda x: x is None):
        """ Reads input from the command line until a suitable answer is found. """
        result = ReadDelegate()
        while not Predicate(result):
            self.WriteError(Text)
            result = ReadDelegate()
        return result

    def TryReadInteger(self):
        """ Tries to read a integer from the command line. """
        try:
            return int(self.ReadString())
        except:
            return None

    def TryReadIndex(self):
        """ Tries to read an integer index from the command line. """
        val = self.ReadString().strip()
        if val[0] == '#':
            try:
                return int(val[1:])
            except:
                return None
        else:
            try:
                return int(val)
            except:
                return None

    def TryReadFloat(self):
        """ Tries to read a floating-point number from the command line. """
        try:
            return float(self.ReadString())
        except:
            return None

    def TryReadBoolean(self):
        """ Tries to read a boolean value from the command line. """
        val = self.ReadString().strip().lower()
        if val == "y" or val == "yes":
            return True
        elif val == "n" or val == "no":
            return False
        else:
            return None

    def TryReadDate(self):
        """ Tries to read a date from the command line. """
        splitVals = self.ReadString().replace(" ", "").split('/')
        today = get_now().date
        try:
            dayData = [today.day, today.month, today.year]
            for i, item in enumerate(splitVals):
                dayData[i] = int(item)
                if i < 2:
                    if dayData[i] < 1:
                        return None
                    elif i == 1 and dayData[i] > 12:
                        return None
                    elif i == 0 and dayData[i] > 31:
                        return None
            return Project.Date(dayData[0], dayData[1], dayData[2])
        except:
            return None

    def TryReadTime(self):
        """ Tries to read a time from the command line. """
        splitVals = self.ReadString().replace(" ", "").split(':')
        if len(splitVals) < 2 or len(splitVals) > 3:
            return None
        try:
            tData = [None] * 3
            for i, item in enumerate(splitVals):
                tData[i] = int(item)
                if tData[i] < 0:
                    return None
                elif i == 0 and tData[i] > 24:
                    return None
                elif i > 0 and tData[i] > 60:
                    return None
            result = Project.Time(tData[0], tData[1], tData[2])
            if result > Project.Time(24, 0, 0):
                return None
            else:
                return result
        except:
            return None

    def ReadInteger(self, 
                    Text = None, 
                    Predicate = lambda x: x is not None, 
                    FailText = "The given input was not an integer. Please input an integer."):
        """ Reads an integer from the command line. """
        if Text is not None:
            self.WriteQuery(Text)
        return self.PersistRead(self.TryReadInteger, FailText, Predicate)

    def ReadIndex(self, 
                    Text = None, 
                    Predicate = lambda x: x is not None, 
                    FailText = "The given input was not an integer index. Please input an integer index."):
        """ Reads an integer index from the command line. """
        if Text is not None:
            self.WriteQuery(Text)
        return self.PersistRead(self.TryReadIndex, FailText, Predicate)

    def ReadFloat(self, 
                  Text = None, 
                  Predicate = lambda x: x is not None, 
                  FailText = "The given input could not be parsed as a floating-point number. Please input a float."):
        """ Reads a floating-point number from the command line. """
        if Text is not None:
            self.WriteQuery(Text)
        return self.PersistRead(self.TryReadFloat, FailText, Predicate)

    def ReadBoolean(self, 
                  Text = None, 
                  Predicate = lambda x: x is not None, 
                  FailText = "The given input could not be parsed as a boolean number. Please input either 'yes' or 'no'."):
        """ Reads a boolean value from the command line. """
        if Text is not None:
            self.WriteQuery(Text)
        return self.PersistRead(self.TryReadBoolean, FailText, Predicate)

    def ReadTime(self, 
                  Text = None, 
                  Predicate = lambda x: x is not None, 
                  FailText = "The given input could not be parsed as a time. Please format times as 'hh:mm:ss' or 'hh:mm'."):
        """ Reads a time value from the command line. """
        if Text is not None:
            self.WriteQuery(Text)
        return self.PersistRead(self.TryReadTime, FailText, Predicate)

    def ReadDate(self, 
                  Text = None, 
                  Predicate = lambda x: x is not None, 
                  FailText = "The given input could not be parsed as a date. Please format dates as 'dd/mm/yyyy'."):
        """ Reads a date value from the command line. """
        if Text is not None:
            self.WriteQuery(Text)
        return self.PersistRead(self.TryReadDate, FailText, Predicate)

    def ReadRangeFloat(self, Min, Max, Text = None):
        """ Reads a floating-point number within a specified range from the command line. """
        return self.ReadFloat(Text, lambda x: x is not None and x >= Min and x <= Max, "The given input could not be parsed as a floating-point between " + str(Min) + " and " + str(Max) + ". Please input a correct float.")

    def ReadString(self, Text = None):
        """ Reads a string from the command line. """
        if Text is not None:
            self.WriteQuery(Text)
        return self.istream.Read()

    def ReadNoBlankString(self, Text = None):
        """ Reads a non-empty string that is not blank from the command line. """
        if Text is not None:
            self.WriteQuery(Text)
        return self.PersistRead(self.ReadString, "The given string was empty or blank. Please input a non-empty string that is not blank.", lambda x: x is not None and x != "" and not x.isspace())

    def ReadFutureDate(self, Text = None):
        """ Reads a future date. """
        if Text is None:
            totalText = None
        else:
            totalText = Text + " (current date: " + str(get_now().date) + ")"
        return self.ReadDate(totalText, 
                             lambda x: x is not None and x >= get_now().date, 
                             "The given input could not be parsed as a future date. Please format dates as 'dd/mm/yyyy'.")

    def RunDialog(self, Parent):
        """ Starts the command-line dialog with the user. """
        
        self.istream = Parent.istream
        self.ostream = Parent.ostream
