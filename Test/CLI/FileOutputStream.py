from IStringOutputStream import *
from StringOutputStreamBase import *
import Project

class FileOutputStream(StringOutputStreamBase):
    """ An output stream that writes its output to a file. """

    def __init__(self, File):
        """ Creates a new file ouput stream from the given file name. """
        StringOutputStreamBase.__init__(self)
        self.file = open(File, 'w')

    def close(self):
        """ Closes the output stream and the underlying file handle. """
        self.file.close()
        self.file = None

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.close()

    def Write(self, Text):
        """ Writes a line of input to the file. """
        if self.output_type != "query": # Printing queries is not useful
            self.file.write(Text + '\n')

