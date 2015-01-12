from IStringOutputStream import *

class OutputType:
    """ A context manager class for stream output types. Example usage:
            with OutputType.Info(stream):
                <statements>
    """

    def __init__(self, Type, OutputStream):
        self.type = Type
        self.ostream = OutputStream

    def Push(self):
        """ Pushes the output type on the output stream's stack. """
        self.ostream.PushOutputType(self.type)

    def Pop(self):
        """ Pushes the output type from the output stream's stack. """
        self.ostream.PopOutputType()

    def __enter__(self):
        """ Pushes the output type on the output stream's stack. """
        self.Push()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        """ Pushes the output type from the output stream's stack. """
        self.Pop()

    # Common output types:
    # The application presents some kind of result or info
    Info = lambda ostream: OutputType("info", ostream)
    # The application asks the input stream for input, but tries to communicate its query first
    Query = lambda ostream: OutputType("query", ostream)
    # The application reports an error
    Error = lambda ostream: OutputType("error", ostream)