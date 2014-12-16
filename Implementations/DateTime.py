class DateTime:
    """ Describes a date and time: a date and the time of day. """

    def __init__(self, Date, TimeOfDay):
        """ Creates a new date-time instance based on the date and time provided. """
        self.date_value = None
        self.time_of_day_value = None
        self.date = Date
        self.time_of_day = TimeOfDay

    def __str__(self):
        """ Gets the time's string representation. """
        return self.date + " " + self.time_of_day

    @property
    def date(self):
        """ Gets this timestamp's date. """
        return self.date_value

    @date.setter
    def date(self, value):
        """ Sets this timestamp's date. """
        self.date_value = value

    @property
    def time_of_day(self):
        """ Gets this timestamp's time of day. """
        return self.time_of_day_value

    @time_of_day.setter
    def time_of_day(self, value):
        """ Sets this timestamp's time of day. """
        self.time_of_day_value = value