class IStringOutputStream:
    """ A stream that outputs textual data. """

    def Write(self, Text):
        """ Writes a line of text to the output stream. """
        raise NotImplementedError("Method 'IStringOutputStream.Write' was not implemented.")

    def PushOutputType(self, Type):
        """ Sets the stream's output type to the specified type. """
        raise NotImplementedError("Method 'IStringOutputStream.PushOutputType' was not implemented.")

    def PopOutputType(self):
        """ Reverts the stream's output type to the previous type """
        raise NotImplementedError("Method 'IStringOutputStream.PopOutputType' was not implemented.")