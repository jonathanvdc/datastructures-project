from IStringOutputStream import *

class ConsoleOutputStream(IStringOutputStream):
    """ A console string output stream. """

    def __init__(self):
        pass

    def Write(self, Text):
        print(str(Text))

    def __enter__(self):
        pass

    def __exit__(self, exc_type, exc_value, traceback):
        pass

    def PopOutputType(self):
        """ Does nothing. Output types are not used in console output. """
        pass

    def PushOutputType(self, Type):
        """ Does nothing. Output types are not used in console output. """
        pass