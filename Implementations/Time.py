class Time:
    """ Represents the time of day. """

    def __init__(self, Hour, Minute, Second = None):
        """ Creates a new time based on an hour, minute and second. """
        if Second is None:
            self.total_seconds = 0
            self.total_seconds = Hour * 3600 + Minute * 60
            return
        self.total_seconds = 0
        self.total_seconds = Hour * 3600 + Minute * 60 + Second

    def __str__(self):
        """ Gets the time's string representation. """
        if self.second == 0:
            return self.hour + ":" + self.minute
        else:
            return self.hour + ":" + self.minute + ":" + self.second

    @property
    def second(self):
        """ Gets the second of this time instance. """
        return self.total_seconds % 60

    @property
    def hour(self):
        """ Gets the hour of this time instance. """
        return self.total_seconds // 3600

    @property
    def minute(self):
        """ Gets the minute of this time instance. """
        return (self.total_seconds % 3600) // 60