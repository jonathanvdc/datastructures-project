from StringOutputStream import *

class ConsoleOutputStream(StringOutputStream):
    """ A console string output stream. """

    def __init__(self):
        pass

    def Write(self, Text):
        return print(str(Text))

