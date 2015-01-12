from IStringInputStream import *

class FileInputStream(IStringInputStream):
    """ An input stream that uses a file to provide input. """

    def __init__(self, File):
        """ Creates a new file input stream from the given file name. """
        self.file = open(File)

    def close(self):
        """ Closes the input stream and the underlying file handle. """
        self.file.close()
        self.file = None

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.close()

    def Read(self):
        """ Reads a line of input from the file. """
        return self.file.readline().strip()