import tkinter
import tkinter.ttk
import tkinter.messagebox
import Project
from MovieComboBox import *
from ShowtimeComboBox import *
from NumberEntry import *

def isEmptyOrWhitespace(Value):
    """ Gets a boolean value that indicates if the given string is empty or whitespace. """
    return Value == "" or Value.isspace()

def showWindow(FrameType, Arg):
    """ Creates a new frame with the given argument and displays a new window that contains said frame. """

    window = tkinter.Tk()
    userFrame = FrameType(Arg, window)
    window.mainloop()