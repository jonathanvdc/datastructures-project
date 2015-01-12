from CommandLineDialog import *
import ShowtimeManager
import DialogHelpers
import Project

class RedeemTicketDialog(CommandLineDialog):
    """ A dialog that allows a user to redeem a ticket at a showtime. """

    def __init__(self, Theater):
        CommandLineDialog.__init__(self, "redeem ticket")

        self.theater = Theater

    def GetReservedShowtimes(self, Customer):
        """ Gets a collection of all showtimes a ticket has been reserved for by the given customer. """
        result = Project.LinkedList()
        # We know we're working with a linked list, whose contract specifically grants us access to its nodes.
        # We're using the linked list's public API. This code may be less portable, but this is a performance optimization.
        # This method has O(n) performance, using only the methods exposed by IList<Showtime> would yield O(n^2) performance for linked lists, which is undesirable.
        tailNode = None
        for item in ShowtimeManager.FilterShowtimes(self.theater):
            if item.has_ticket(Customer) and ShowtimeManager.CanEnter(item):
                if tailNode is None:
                    result.add(item)
                    tailNode = result.tail
                else:
                    tailNode.insert_after(item)
                    tailNode = tailNode.successor
        return result

    def RunDialog(self, Parent):
        """ Runs the dialog to redeem a user's ticket. """
        CommandLineDialog.RunDialog(self, Parent)

        user = DialogHelpers.SelectCustomer(self, self.theater, "Whose ticket would you like to redeem?")
        if user is None:
            self.Write("Could not redeem ticket.")
            return
        reserved = self.GetReservedShowtimes(user)
        if reserved.count == 0:
            self.Write("You do not have any outstanding tickets for showtimes that begin in the next " + str(ShowtimeManager.overdue_time) + ".")
            return

        showtime = DialogHelpers.SelectShowtime(self, reserved)

        showtime.redeem_ticket(self.theater, user)
        self.Write("One ticket has been redeemed")