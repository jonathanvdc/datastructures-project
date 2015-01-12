from IStringInputStream import *

class ConsoleInputStream(IStringInputStream):
    """ A StringInputStream implementation for console input. """

    def Read(self):
        return input("> ")
