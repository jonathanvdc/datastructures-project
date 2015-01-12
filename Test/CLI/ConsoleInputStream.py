from StringInputStream import *

class ConsoleInputStream(StringInputStream):
    """ A StringInputStream implementation for console input. """

    def Read(self):
        return input("> ")
