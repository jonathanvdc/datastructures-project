from IRecord import *

class User(IRecord):
    """ Describes a registered customer at a movie theater. """

    def __init__(self, Id, FirstName, LastName, EmailAddress):
        """ Creates a new instance of a user with the provided information. """
        self.id_value = 0
        self.first_name_value = None
        self.last_name_value = None
        self.email_address_value = None
        self.id = Id
        self.first_name = FirstName
        self.last_name = LastName
        self.email_address = EmailAddress

    def __str__(self):
        """ Gets the user's data as a string. """
        return "User #" + str(self.id) + ": " + self.name + " (" + self.email_address + ")"

    def __eq__(self, Other):
        """ Tests user equality. """
        if Other is None:
            return False
        else:
            return self.id == Other.id

    def __hash__(self):
        """ Calculates a user's hash code. """
        return self.id

    def __ne__(self, Other):
        return not self == Other

    @property
    def id(self):
        """ Gets the user's unique identifier. """
        return self.id_value

    @id.setter
    def id(self, value):
        """ Sets the user's unique identifier. """
        self.id_value = value

    @property
    def first_name(self):
        """ Gets the user's first name. """
        return self.first_name_value

    @first_name.setter
    def first_name(self, value):
        """ Sets the user's first name. """
        self.first_name_value = value

    @property
    def last_name(self):
        """ Gets the user's last name. """
        return self.last_name_value

    @last_name.setter
    def last_name(self, value):
        """ Sets the user's last name. """
        self.last_name_value = value

    @property
    def email_address(self):
        """ Gets the user's email address. """
        return self.email_address_value

    @email_address.setter
    def email_address(self, value):
        """ Sets the user's email address. """
        self.email_address_value = value

    @property
    def name(self):
        """ Gets the user's full name. """
        return self.first_name + " " + self.last_name

    @property
    def key(self):
        """ Gets the record's search key. """
        return self.id