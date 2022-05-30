from tkinter import *
import math

root = Tk()
blank_space = " "
root.title (50 * blank_space + "VS Code Calculation")
root.resizable(width = False, height = FALSE)
root.geometry ("438x573+460+40")

coverFrame = Frame (root, bd = 20, pady=2, relief = RIDGE)
coverFrame.grid()

coverMainFrame = Frame (coverFrame, bd = 20, pady=2, bg = 'cadetblue', relief = RIDGE)
coverMainFrame.grid()

MainFrame = Frame (root, bd = 20, pady=2, relief = RIDGE)
MainFrame.grid()

root.mainloop()