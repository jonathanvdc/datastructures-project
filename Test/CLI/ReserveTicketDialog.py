from CommandLineDialog import *
from OptionDialog import *
import DialogHelpers
import Project

class ReserveTicketDialog(CommandLineDialog):
    """ A dialog that reserves tickets for a showtime. """

    def __init__(self, Theater):
        CommandLineDialog.__init__(self, "reserve tickets")
        self.theater = Theater

    def GetAvailableShowtimes(self):
        """ Gets all available showtimes. """

        now = get_now()

        # Quadratic open-addressed hashtable with default Record -> Key map
        table = Project.OpenHashtable(Project.DefaultRecordMap(), Project.PowerSequenceMap(2))
        for item in self.theater.showtimes:
            if item.start_time > now and item.number_of_free_seats > 0:
                table.insert(item)

        return table

    def RunDialog(self):
        """ Runs the ticket reservation dialog. """

        if self.theater.registered_customers.count == 0:
            print("Sorry, no customers have been registered yet.")
            return None

        user = DialogHelpers.SelectCustomer(self.theater, "Who are you?")

        showtimes = self.GetAvailableShowtimes()
        if showtimes.count == 0:
            print("No showtimes have been scheduled yet. Tickets cannot be reserved.")
            return None

        showtimeDialog = OptionDialog("select showtime", "Please select a showtime", showtimes, True)
        showtimeDialog.ReadOptionKey = showtimeDialog.ReadIndex
        selectedShowtime = showtimeDialog.RunDialog()

        numberOfSeats = self.ReadInteger("How many seats would you like to reserve?", lambda x: x is not None and x > 0, "The given input was not a positive integer, please input an integer greater than or equal to one.")
        
        freeSeatsCount = selectedShowtime.number_of_free_seats
        while numberOfSeats > freeSeatsCount:
            numberOfSeats = self.ReadInteger("Sorry, there are only " + str(freeSeatsCount) + " seats left. Please pick a smaller number of seats.", lambda x: x is not None and x > 0, "The given input was not a positive integer, please input an integer greater than or equal to one.")

        # Queues the reservation
        result = self.theater.reservations.queue_reservation(Project.ReservationRequest(user, selectedShowtime, numberOfSeats, get_now()))
        # And processes the reservations right away
        # Otherwise, a blissfully ignorant user might reserve more tickets than the number of remaining tickets,
        # as the showtime's free seat counter has not been updated yet
        print("Your reservation:")
        for item in self.theater.reservations.process_reservations():
            print(str(item))