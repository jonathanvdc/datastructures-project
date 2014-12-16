class Date:
    """ Represents a simple date. """

    def __init__(self, Day, Month, Year):
        """ Creates a new date from a day, month and year. """
        self.day_value = 0
        self.month_value = 0
        self.year_value = 0
        self.day = Day
        self.month = Month
        self.year = Year

    def __str__(self):
        """ Gets this date's string representation. """
        return self.day + "/" + self.month + "/" + self.year

    @property
    def day(self):
        """ Gets the day of this date. """
        return self.day_value

    @day.setter
    def day(self, value):
        """ Sets the day of this date. """
        self.day_value = value

    @property
    def month(self):
        """ Gets the month of this date. """
        return self.month_value

    @month.setter
    def month(self, value):
        """ Sets the month of this date. """
        self.month_value = value

    @property
    def year(self):
        """ Gets the year of this date. """
        return self.year_value

    @year.setter
    def year(self, value):
        """ Sets the year of this date. """
        self.year_value = value