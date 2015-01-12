from IStringOutputStream import *

class ConsoleOutputStream(IStringOutputStream):
    """ A console string output stream. """

    def __init__(self):
        pass

    def Write(self, Text):
        return print(str(Text))

