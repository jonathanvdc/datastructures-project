import tkinter
import tkinter.ttk
import tkinter.messagebox
import Project

class MovieComboBox(tkinter.ttk.Combobox):
    """ A ComboBox that allows the user to pick a movie. """

    def __init__(self, master, Theater):
        """ Creates a new instance of a movie combo box. """

        tkinter.ttk.Combobox.__init__(self, master)
        self.theater = Theater
        self["values"] = []
        for movie in Theater.movies:
            self["values"].append(movie.title)
        if len(self["values"]) > 0:
            self.current(0)

    def getSelectedMovie(self):
        """ Gets the selected movie. Returns 'None' if no movie was selected. """

        cur = self.current()
        if cur < 0:
            return None
        else:
            return self.theater.find_movie(self["values"][cur])