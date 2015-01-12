from IStringInputStream import *

class ConsoleInputStream(IStringInputStream):
    """ A StringInputStream implementation for console input. """

    def __enter__(self):
        pass

    def __exit__(self, exc_type, exc_value, traceback):
        pass

    def Read(self):
        return input("> ")
