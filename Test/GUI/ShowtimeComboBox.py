import tkinter
import tkinter.ttk
import tkinter.messagebox
import Project

class ShowtimeComboBox(tkinter.ttk.Combobox):
    """ A ComboBox that allows the user to pick a showtime. """

    def __init__(self, master, Theater):
        """ Creates a new instance of a showtime combo box. """

        tkinter.ttk.Combobox.__init__(self, master)
        self.theater = Theater
        self["values"] = []
        self.showtimeIds = Project.ArrayList()
        for i, showtime in enumerate(Theater.showtimes):
            self["values"].append(str(showtime))
            showtimeIds.add(showtime.id)
        if len(self["values"]) > 0:
            self.current(0)

    def getSelectedShowtime(self):
        """ Gets the selected showtime. Returns 'None' if no showtime was selected. """

        cur = self.current()
        if cur < 0:
            return None
        else:
            return self.theater.showtimes(self.showtimeIds[cur])