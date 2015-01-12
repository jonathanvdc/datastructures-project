from IStringOutputStream import *
from OutputType import *
import Project

class StringOutputStreamBase(IStringOutputStream):
    """ A base type for string output streams that use a stack to remember their output types. """

    def __init__(self):
        """ Creates a new file ouput stream from the given file name. """
        self.type_stack = Project.Stack(Project.ArrayList())
        OutputType.Info(self).Push()

    @property
    def output_type(self):
        """ Gets the output stream's output type. """
        return self.type_stack.top

    def PushOutputType(self, Type):
        """ Sets the stream's output type to the specified type. """
        return self.type_stack.push(Type)

    def PopOutputType(self):
        """ Reverts the stream's output type to the previous type """
        self.type_stack.pop()